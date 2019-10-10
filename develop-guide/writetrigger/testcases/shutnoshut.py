
# Python imports
import time
import logging

# pyATS import
from pyats import aetest
from genie.harness.base import Trigger

# Set up logging
log = logging.getLogger()

# Define the trigger class and steps
# This class inherits from the Trigger class
class ShutNoShutBgp(Trigger):
    '''Shut and unshut bgp'''

    # Setup steps
    @aetest.setup
    def prerequisites(self, uut):
        '''Check whether bgp is configured and running'''

        # Parse the BGP output on uut
        output = uut.parse('show bgp process vrf all')

        # Check for a bgp_id
        if not 'bgp_tag' in output:
            self.skipped("No Bgp is configured for "\
                        "device '{d}'".format(d=uut.name))

        # Check that BGP is running
        if 'bgp_protocol_state' not in output or\
        output['bgp_protocol_state'] != 'running':
            self.skipped("Bgp is not operational on "
                        "device '{d}'".format(d=uut.name))

        # Store the initial parsed output
        self.bgp_id = output['bgp_tag']

    # Test steps

    # Shut BGP on uut
    @aetest.test
    def shut(self, uut):
        '''Shut bgp'''
        uut.configure('''\
router bgp {id}
shutdown'''.format(id=self.bgp_id))

    # Verify the new configuration
    @aetest.test
    def verify(self, uut):
        '''Verify if the shut worked'''
        # Parse the BGP output on uut
        output = uut.parse('show bgp process vrf all')

        # Check that the bgp_id still shows in the output
        if output['bgp_tag'] != self.bgp_id:
            self.failed("Bgp id {bgp_id} no longer shows in the "
                        "output, this is "
                        "unexpected!".format(bgp_id=self.bgp_id))

        # Check that BGP is shut down
        if output['bgp_protocol_state'] != 'shutdown':
            self.failed("Shut on Bgp {bgp_id} did not work as it is not "
                        "shutdown".format(bgp_id=self.bgp_id))

    # Recover the initial config, unshut BGP on uut
    @aetest.test
    def unshut(self, uut):
        '''Unshut bgp'''
        uut.configure('''\
router bgp {id}
no shutdown'''.format(id=self.bgp_id))

    # Verify the recovered configuration
    @aetest.test
    def verify_recover(self, uut, wait_time=20):
        '''Figure out if bgp is configured and up'''

        # Parse the BGP output on uut
        output = uut.parse('show bgp process vrf all')

        # Check that the bgp_id still shows in the output
        if output['bgp_tag'] != self.bgp_id:
            self.failed("Bgp id {bgp_id} no longer shows in the "
                        "output, this is "
                        "unexpected!".format(bgp_id=self.bgp_id))

        # Check that BGP is running
        if output['bgp_protocol_state'] != 'running':
            self.failed("Reconfigure of Bgp {bgp_id} did not work as it is not "
                        "running".format(bgp_id=self.bgp_id))
