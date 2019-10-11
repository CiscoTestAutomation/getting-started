
# Python
import sys
import time
import logging

# Enable logger
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')
log = logging.getLogger(__name__)

# Import pyATS and the pyATS Library
from genie.testbed import load
from ats.log.utils import banner


# ----------------
# Load the testbed
# ----------------
log.info(banner("Loading testbed"))
testbed = load('testbed.yaml')
log.info("\nPASS: Successfully loaded testbed '{}'\n".format(testbed.name))


# --------------------------
# Connect to device nx-osv-1
# --------------------------
log.info(banner("Connect to device 'nx-osv-1'"))
device = testbed.devices['nx-osv-1']
device.connect(via='cli')
log.info("\nPASS: Successfully connected to device 'nx-osv-1'\n")


# ---------------------------------------
# Execute parser to check interface state
# ---------------------------------------
log.info(banner("Executing parser to verify interface state before unshutting..."))
pre_output = device.parse("show interface Ethernet2/1 brief")

# Verify interface is down before unshutting
pre_status = pre_output['interface']['ethernet']['Ethernet2/1']['status']

if pre_status == 'down':
    log.info("\nPASS: Interface Ethernet2/1 status is 'down' as expected\n")
else:
    log.error("\nFAIL: Interface Ethernet2/1 status is not 'down' as expected\n")
    exit()


# -------------------------------------------------
# Unshut the interface by configuring "no shutdown"
# -------------------------------------------------
log.info(banner("Unshutting interface by configuring 'no shutdown'..."))
device.configure("interface Ethernet2/1\n"
                 " no shutdown")
log.info("\nPASS: Successfully unshut interface Ethernet2/1\n")


# -----
# Sleep
# -----
log.info("\nSleeping 15 seconds for configuration to take effect...\n")
time.sleep(15)


# ---------------------------------------
# Execute parser to check interface state
# ---------------------------------------
log.info(banner("Executing parser to verify interface state after unshutting..."))
post_output = device.parse("show interface Ethernet2/1 brief")

# Verify interface is up after unshutting
post_status = post_output['interface']['ethernet']['Ethernet2/1']['status']
if post_status == 'up':
    log.info("\nPASS: Interface Ethernet2/1 status is 'up' as expected\n")
else:
    log.error("\nPASS: Interface Ethernet2/1 status is not 'up' as expected\n")


log.info(banner("End of Script"))

