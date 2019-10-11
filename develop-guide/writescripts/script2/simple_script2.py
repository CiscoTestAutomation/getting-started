
# Python
import sys
import time
import pprint
import logging

# Enable logger
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')
log = logging.getLogger(__name__)

# Import pyATS and the pyATS Library
from genie.testbed import load
from ats.log.utils import banner
from genie.utils.diff import Diff
from genie.libs.sdk.apis.iosxe.bgp.get import get_bgp_session_count


# ----------------
# Load the testbed
# ----------------
log.info(banner("Loading testbed"))
testbed = load('testbed.yaml')
log.info("\nPASS: Successfully loaded testbed '{}'\n".format(testbed.name))


# -----------------------
# Connect to all devices
# -----------------------
log.info(banner("Connect to all devices..."))

dev_xe = testbed.devices['csr1000v-1']
dev_xe.connect(via='cli')

dev_nx = testbed.devices['nx-osv-1']
dev_nx.connect(via='cli')

# Log result to user
log.info("\nPASS: Successfully connected to all devices\n")


# -------------------------------------------------
# Get number of established BGP neighbors on device
# -------------------------------------------------
log.info(banner("Get number of established BGP neighbors on device '{}'".\
                format(dev_xe.name)))

orig_bgp_estab_nbrs = dev_xe.api.get_bgp_session_count(in_state='established')
log.info("\nPASS: Total number of established BGP neighbors is {}\n".\
         format(orig_bgp_estab_nbrs))


# ------------------------------------------------------
# Learn feature 'BGP' for XE device before config change
# ------------------------------------------------------
log.info(banner("Learn feature 'BGP' for XE device '{}' before config change".\
                format(dev_xe.name)))

pre_bgp_ops = dev_xe.learn("bgp")
log.info("\nPASS: Successfully learnt feature 'bgp' for XE device '{}' before config change\n".\
         format(dev_xe.name))
log.info(pprint.pprint(pre_bgp_ops.info))


# ------------------------------------
# Shutdown 'BGP' neighbor on XE device
# ------------------------------------
log.info(banner("Shutdown 'BGP' neighbor on XE device '{}'".format(dev_xe.name)))

dev_xe.configure("router bgp 65000\n"
                 " neighbor 10.2.2.2 shutdown")
log.info("\nPASS: Successfully shutdown BGP neighbor on XE device '{}'\n".\
         format(dev_xe.name))


# -----
# Sleep
# -----
log.info("\nSleeping 10 seconds for configuration to take effect...\n")
time.sleep(10)


# -----------------------------------------------------
# Learn feature 'BGP' for XE device after config change
# -----------------------------------------------------
log.info(banner("Learn feature 'BGP' for XE device '{}' after config change".\
                format(dev_xe.name)))

post_bgp_ops1 = dev_xe.learn("bgp")
log.info("\nPASS: Successfully learnt feature 'bgp' for XE device '{}' after config change\n".\
         format(dev_xe.name))


# --------------------------------
# Use Genie Diff to compare states
# --------------------------------
log.info(banner("Use Genie Diff to verify BGP neighbor is shutdown on XE device '{}'".\
                format(dev_xe.name)))

bgp_diff = Diff(pre_bgp_ops.info, post_bgp_ops1.info)
bgp_diff.findDiff()
log.info("Genie Diffs observed, BGP neighbor is shutdown/missing:\n\n" + str(bgp_diff) + "\n")


# -----------------------------------
# Restore 'BGP' neighbor on XE device
# -----------------------------------
log.info(banner("Restore 'BGP' neighbor on XE device '{}'".format(dev_xe.name)))

dev_xe.configure("router bgp 65000\n"
                 " no neighbor 10.2.2.2 shutdown")
log.info("\nPASS: Successfully restored BGP neighbor on XE device '{}'\n".\
         format(dev_xe.name))


# -----
# Sleep
# -----
log.info("\nSleeping 10 seconds for configuration to take effect...\n")
time.sleep(10)


# --------------------------------------------------------
# Learn feature 'BGP' for XE device after restoring config
# --------------------------------------------------------
log.info(banner("Learn feature 'BGP' for XE device '{}' after restoring config".\
                format(dev_xe.name)))

post_bgp_ops2 = dev_xe.learn("bgp")
log.info("\nPASS: Successfully learnt feature 'bgp' for XE device '{}' after restoring config\n".\
         format(dev_xe.name))


# --------------------------------
# Use Genie Diff to compare states
# --------------------------------
log.info(banner("Use Genie Diff to verify BGP operational state has minimal differences on XE device '{}'".\
                format(dev_xe.name)))

bgp_diff = Diff(pre_bgp_ops.info, post_bgp_ops2.info)
bgp_diff.findDiff()
log.info("Genie Diffs observed:\n" + str(bgp_diff) + "\n")


# -------------------------------------------------------
# Verify number of established BGP neighbors on XE device
# -------------------------------------------------------
log.info(banner("Verify number of established BGP neighbors on XE device '{}'".\
                format(dev_xe.name)))

curr_bgp_estab_nbrs = dev_xe.api.get_bgp_session_count(in_state='established')

if curr_bgp_estab_nbrs == orig_bgp_estab_nbrs:
    log.info("\nPASS: Total number of established BGP neighbors is {}\n".\
             format(curr_bgp_estab_nbrs))
else:
    log.error("\FAIL: Total number of established BGP neighbors is {}\n".\
             format(curr_bgp_estab_nbrs))


# -------------------------------------------------------
# Check interface status for all interfaces on XE device
# -------------------------------------------------------
log.info(banner("Check interface status for all interfaces on XE device '{}'".\
                format(dev_xe.name)))

intf_output = dev_xe.parse('show ip interface brief')

for interface in intf_output['interface']:
    status = intf_output['interface'][interface]['status']
    if status == 'up':
        log.info("\nPASS: Interface {intf} status is: '{s}'".format(intf=interface, s=status))
    elif status == 'down':
        log.error("\nFAIL: Interface {intf} status is: '{s}'".format(intf=interface, s=status))


log.info(banner("End of Script"))
