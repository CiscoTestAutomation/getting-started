
# Python
import logging

# pyATS
from ats import aetest

log = logging.getLogger(__name__)


def my_callable_verification(self, *args, **kwargs):
    output = {}
    output['var1'] = self.parameters['uut'].parse('show interface brief')
    output['var2'] = self.parameters['uut'].parse('show version')
    return output


class SampleTrigger(aetest.Testcase):

    @aetest.setup
    def setup_step(self, uut, testbed):
        log.info("setup_step")
        pass

    @aetest.test
    def actual_step(self, uut, testbed):
        log.info("actual_step")
        pass

    @aetest.cleanup
    def cleanup_step(self, uut, testbed):
        log.info("cleanup_step")
        pass
