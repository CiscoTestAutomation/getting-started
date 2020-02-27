.. _write-trigger:

Write a trigger
===============
This topic describes how to write your own triggers when you want to extend the |library| functionality to meet your network automation requirements.

.. note:: The *Get Started with pyATS* guide, `Run a test case <https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/quickstart/runtestcase.html#run-a-test-case>`_ section explains the concepts that you need to know before you begin to write a trigger.

Triggers, verifications, and test cases
---------------------------------------

.. include:: ../definitions/def_trigger.rst
   :start-line: 3

You can think of a trigger and its associated :term:`verifications <verification>` as a reusable |pyATS| test case. In |pyATS|, you embed triggers within your test script. With the |library|, you import and run the trigger as a Python library. Triggers make it easy to change the order of your test cases without having to write a new script.

Purpose of triggers
^^^^^^^^^^^^^^^^^^^
Triggers provide a way to:

* Make tests independent of specific devices, topologies, and hostnames.
* Remove dependencies on one, specific configuration.
* Reuse a test in combination with other tests.
* Grow the |library| "pool" of triggers to make future automation easier!
* Make the logs readable, so that you can easily understand why tests fail. We do this by:

  * Dividing the test into separate, specific actions.
  * Logging the right information at the right level of detail. |br| |br|

How triggers and verifications work
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The |library| components work together so that you can:

* Pick and choose the test cases (triggers and verifications) that you need.
* Use the |library| infrastructure (``gRun``) to create a dynamic test suite.

.. tip::  Nothing is hard-coded, everything is reusable, and the flow is exactly as you determine.

To run triggers using the ``harness``, you need at least three files, as described in the following table.

.. csv-table:: Files required to run triggers
    :header: "File type", "Format", "Description"
    :widths: 25 25 50

    "Trigger", "Python (.py)", "Defines the trigger class or classes."
    "Trigger datafile", "YAML (.yaml)", "Lists the triggers and arguments to pass to each trigger."
    "Job file", "Python (.py)", "Imports ``gRun`` functionality from the ``harness`` package. Points to a specific datafile and identifies which triggers and (optional) verifications to run."

The following diagram shows how the triggers, datafiles, and job files interact when you use the |library| harness to run test cases.

.. image:: ../images/harness_run_job.png

Example of a trigger file
-------------------------

Structure of a trigger
^^^^^^^^^^^^^^^^^^^^^^
In the following example, you can see the structure of the trigger. This trigger shuts and unshuts BGP on the :monospace:`uut` device defined in the testbed YAML file. Note that:

#. A trigger is a Python class. 
#. One Python file can have more than one trigger class.
#. Triggers inherit from the base :monospace:`Trigger` class, which contains common setup and cleanup tasks and checks. These tasks help you to identify any unexpected changes to testbed devices that are not under test. For more information about common setup and cleanup, see the topic `Automated testing process <https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/quickstart/runtestcase.html#automated-testing-process>`_ in the *Get Started with pyATS* guide. 
#. Trigger setup steps typically check for any prerequisites and configure the device to meet the required pre-test conditions.
#. For each trigger, if a step marked as :monospace:`@aetest.setup` fails, the steps marked as :monospace:`aetest.test` do not run.
#. The |library| triggers typically have a

   * test step, to change a device configuration or operational state, and
   * a recovery step, to restore the pre-test conditions.

#. Within a step, you can call any of `our pre-built API functions <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/apis>`_. These are clearly-named, reusable actions that can save you time and effort. For more information, see the topic `Functions <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/apis/index.html?highlight=apis#functions>`_.

Have a look at the following example, and then we'll explain it step-by-step in the section :ref:`write-simple-trigger`.

.. code-block:: python

    # Python imports
    import time
    
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

Run the example trigger
^^^^^^^^^^^^^^^^^^^^^^^
Complete the following steps to see the trigger in action on a mock device.

#. In your virtual environment, create a directory with the name :monospace:`testcases`::

    mkdir testcases

#. :download:`Download the attached zip file <trigger.zip>`, and then extract the files to the :monospace:`testcases` directory. |br| |br|

#. Change to the :monospace:`testcases` directory::

    cd testcases

#. Because this example uses a mock device, you must set the Python path and source the trigger example.

   * For Bash::
    
       export PYTHONPATH=$VIRTUAL_ENV
       source trigger_example.sh

   * For C shell::

       setenv PYTHONPATH $VIRTUAL_ENV
       source trigger_example.csh

#. Run the job::

    pyats run job example_job.py --testbed-file testbed.yaml --devices uut

   .. note:: If you're a DevNet user and you want to receive an email with the results, add the argument ``--mailto yourname@company.domain``.

   *Result*: The harness runs the trigger specified in :monospace:`example_job.py`, using arguments from :monospace:`trigger_datafile.yaml`, and defined by :monospace:`shutnoshut.py`.

   Your terminal shows the step-by-step actions and the following detailed list of results:

   .. image:: /images/trigger_results.png
      :width: 75% 

Write your own trigger
----------------------

.. _write-simple-trigger:

Write a simple trigger
^^^^^^^^^^^^^^^^^^^^^^
The following steps describe how you can write a simple trigger using the :monospace:`ShutNoShutBgp` trigger example as a guide.

#. Open a text editor and start a new :monospace:`.py` file. |br| |br|

#. Import the functionality that you need from Python, |pyATS|, and the |library|, and set up logging. For a description of the more commonly used functionality that you might want to import, see the topic `Useful Libraries <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#useful-libraries>`_:

   .. code-block:: python

    # Python imports
    import time
    import logging
    
    # pyATS import
    from pyats import aetest
    from genie.harness.base import Trigger

    log = logging.getLogger()

   .. note:: You don't need to import the ``genie.testbed`` ``load`` function, because you don't have to specify a testbed file in your trigger. Instead, you specify the testbed file when you run the job file, and the |library| ``Harness`` pulls all of the data together, including arguments from the datafile. This makes your trigger reusable.

#. Define the :monospace:`ShutNoShutBgp` trigger class and inherit from the standard :monospace:`Trigger` class:

   .. code-block:: python

    class ShutNoShutBgp(Trigger):

#. Define the setup steps to:

    * Parse the show command output.
    * Check that BGP is configured on the device.
    * Check the current operational state.
    * Store the initial parsed output to compare later.

   .. code-block:: python

    @aetest.setup
    def prerequisites(self, uut):

        output = uut.parse('show bgp process vrf all')

        if not 'bgp_tag' in output:
            self.skipped("No Bgp is configured for "\
                        "device '{d}'".format(d=uut.name))

        if 'bgp_protocol_state' not in output or\
        output['bgp_protocol_state'] != 'running':
            self.skipped("Bgp is not operational on "
                        "device '{d}'".format(d=uut.name))

        self.bgp_id = output['bgp_tag']

   .. note:: If a setup step fails, the trigger stops.

#. Define the first test step (:monospace:`shut`):

   .. code-block:: python

        @aetest.test
        def shut(self, uut):
            '''Shut bgp'''
            uut.configure('''\
    router bgp {id}
    shutdown'''.format(id=self.bgp_id))


#. Define steps for the second test (:monospace:`verify`):

    * Parse the show command output.
    * Check that BGP is configured on the device.
    * Check the current operational state.

   .. code-block:: python

    @aetest.test
    def verify(self, uut):
        '''Verify if the shut worked'''
        
        output = uut.parse('show bgp process vrf all')

        if output['bgp_tag'] != self.bgp_id:
            self.failed("Bgp id {bgp_id} no longer shows in the "
                        "output, this is "
                        "unexpected!".format(bgp_id=self.bgp_id))

        if output['bgp_protocol_state'] != 'shutdown':
            self.failed("Shut on Bgp {bgp_id} did not work as it is not "
                        "shutdown".format(bgp_id=self.bgp_id))

#. Define steps for the third test (:monospace:`unshut`):

   .. code-block:: python

        @aetest.test
        def shut(self, uut):
            '''Shut bgp'''
            uut.configure('''\
    router bgp {id}
    no shutdown'''.format(id=self.bgp_id))

#. Define steps for the fourth test (:monospace:`verify_recover`):

    * Parse the show command output.
    * Check that BGP is configured on the device.
    * Check the current operational state.

   .. code-block:: python

    @aetest.test
    def verify_recover(self, uut, wait_time=20):
        '''Figure out if bgp is configured and up'''

        output = uut.parse('show bgp process vrf all')

        if output['bgp_tag'] != self.bgp_id:
            self.failed("Bgp id {bgp_id} no longer shows in the "
                        "output, this is "
                        "unexpected!".format(bgp_id=self.bgp_id))

        if output['bgp_protocol_state'] != 'running':
            self.failed("Reconfigure of Bgp {bgp_id} did not work as it is not "
                        "running".format(bgp_id=self.bgp_id))

#. Save your file as :monospace:`shutnoshut.py` .

Create a new trigger datafile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When you write your own trigger, you must also create a YAML trigger datafile. The following example shows the trigger datafile for the simple trigger described in the previous sections::

 TriggerShutNoShutBgp:
    source:
      class: path.shutnoshut.ShutNoShutBgp
    devices: ['uut']

where:

* :monospace:`TriggerShutNoShutBgp` is the name of the trigger that you call in the job file.
* :monospace:`path` is the location of your trigger file.
* :monospace:`shutnoshut` is the name of your trigger file.
* :monospace:`ShutNoShutBgp` is the trigger class.

.. tip:: If you use the standard |library| triggers, you don't have to provide a trigger datafile. The system uses the default datafile stored in your virtual environment at ``/genie_yamls/<uut_os>/trigger_datafile_<uut_os>.yaml``. The default trigger datafile specifies the device :monospace:`uut`, which you define in your :term:`testbed yaml file`.

Create a new job file
^^^^^^^^^^^^^^^^^^^^^
The Python job file specifies the trigger datafile and triggers to run:

.. code-block:: python

  import os

   from genie.harness.main import gRun

   def main():
       test_path = os.path.dirname(os.path.abspath(__file__))

       gRun(trigger_uids=('TriggerShutNoShutBgp'),
           trigger_datafile='new_trigger_datafile.yaml')

To run the job file:

.. code-block:: python

  pyats run job example_job.py --testbed-file testbed.yaml --devices uut

Example of a trigger with verifications
---------------------------------------
A trigger verifies the expected results. For example, a trigger can check that BGP is down after you take the action to shut it down.

You can use :term:`verifications <verification>` to check for *unexpected* results, such as changes to the feature that you didn't initiate. When you add a verification to your test case, it runs before and after every trigger. This enables you to compare the device’s operational state before and after the trigger (change to a device) and to verify that nothing unexpected happened.

.. note:: To see a list of all available verifications, go to https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/verifications.

#. To add verifications, simply add the verification class to your job file:

   .. code-block::

    import os

    from genie.harness.main import gRun

    def main():
        test_path = os.path.dirname(os.path.abspath(__file__))

        gRun(verification_uids=('Verify_BgpProcessVrfAll.uut'),
            trigger_uids=('TriggerShutNoShutBgp'),
            trigger_datafile='new_trigger_datafile.yaml')
   
   In this example, :monospace:`Verify_BgpProcessVrfAll` is a standard verification that parses output for the show command ``show bgp process vrf all``. 

   .. note:: You don't have to specify a verification datafile when you use a standard verification. The |library| harness uses a default datafile that works with all standard triggers and verifications.

#. If you write your own verification, you must create a verification datafile:

   .. code-block:: python

    Verify_Bgp:
        cmd:
            class: show_bgp.ShowBgpAll
            pkg: genie.libs.parser
        context: cli
        source:
            class: genie.harness.base.Template
        devices: ['uut']
        iteration:
        attempt: 5
        interval: 10
        exclude:
        - if_handle
        - keepalives
        - last_reset
        - reset_reason
        - foreign_port
        - local_port
        - msg_rcvd
        - msg_sent
        - up_down
        - bgp_table_version
        - routing_table_version
        - tbl_ver
        - table_version
        - memory_usage
        - updates
        - mss
        - total
        - total_bytes
        - up_time
        - bgp_negotiated_keepalive_timers
        - hold_time
        - keepalive_interval
        - sent
        - received
        - status_codes
        - holdtime
        - router_id
        - connections_dropped
        - connections_established
        - advertised
        - prefixes
        - routes
        - state_pfxrcd

   The :monospace:`exclude` block defines keys that are unrelated to your test case. Excluded keys typically have dynamic values, and you don't use them in your test cases. |br| |br|

#. Add the verification datafile and verification class to the job file:

   .. code-block:: python

    import os

    from genie.harness.main import gRun

    def main():
        test_path = os.path.dirname(os.path.abspath(__file__))

        gRun(verification_uids=('Verify_Bgp.uut'),
            trigger_uids=('TriggerShutNoShutBgp'),
            verification_datafile='new_verification_datafile.yaml'
            trigger_datafile='new_trigger_datafile.yaml')

   In this example, :monospace:`Verify_Bgp` is the name of the verification class that you defined in the verification datafile. |br| |br|

#. To run the job::

    pyats run job job.py --testbed-file tb.yaml

   where :monospace:`tb.yaml` is your testbed file.

Quick Trigger
-------------

The *Quick Trigger* is a YAML-driven template that makes it easy for you to run
a test case without having to know any programming. The quick trigger ---
called *Blitz* because it's lightning fast --- does the following actions:

* Configure a device.
* Parse the device output to verify if the device state is as expected.
* Unconfig or modify the initial configuration.
* Parse the output to recheck the operational state.
* Yang integration
* <It is fully customizable, new actions can be added>

Designed for quick development, the quick trigger verifies key-value pairs and
uses parsing for full flexibility across OS and platforms. As with any
pyATS Library trigger, other triggers can inherit from the `Blitz` class. Go
ahead and build on top of it!

To use the quick trigger template, add the YAML content to the
`trigger_datafile.yaml`  as shown in the following example for BGP on a router.
The yaml is commented out explaining what each section does

.. code-block:: YAML

  # Name of the testcase
  TestBgpShutdown:
      # Location of the blitz trigger
      source:
        pkg: genie.libs.sdk
        class: triggers.blitz.blitz.Blitz

      # Devices to run on - Default is uut
      devices: ['uut']
  
      # Field containing all the Testcase sections
      test_sections:
  
        # Section name - Can be any name, it will show as the first section of
        # the testcase
          - apply_configuration:
              # List of actions
              - configure:
                  device: R3_nx
                  command: |
                    router bgp 65000
                    shutdown
              - sleep:
                  sleep_time: 5
  
          # Second section name
          - verify_configuration:
              # Action #1
              # Send show command to the device and verify if part 
              # of a string is in the output or not
              - execute:
                  device: R3_nx
                  command: show bgp process vrf all
                  include:
                      # Verify Shutdown is within the show run output
                    - 'Shutdown'
                  exclude:
                      # Verify Running is not within the show run output
                    - 'Running'
              # Action #2
              # Send show command and use our available parsers to make sure
              # the bgp protocol state is shutdown
              - parse:
                  device: R3_nx
                  # All action supports banner field to add to the log
                  banner: Verify bgp process is shutdown
                  command: show bgp process vrf all
                  include:
                    - get_values('shutdown')
                  exclude:
                    - not_contains('bgp_protocol_state')
          - Revert_configuration:
              # Configure action, which accepts command as an argument
              - configure:
                  device: R3_nx
                  banner: Un-Shutting down bgp 65000
                  command: |
                    router bgp 65000
                    no shutdown
          - verify_revert:
              # Send show command and verify if part of a string is in the output or not
              - execute:
                  device: R3_nx
                  command: show bgp process vrf all
                  include:
                      # Verify Running is within the show run output
                      - 'Running'
                  exclude:
                      # Verify Shutdown is not within the show run output
                      - 'Shutdown'
              # Send show command and use our available parsers to make sure
              # it is the bgp protocol state which is running
              - parse:
                  device: R3_nx
                  command: show bgp process vrf all
                  output:
                      - "[bgp_protocol_state][running]"
        ...

Actions
^^^^^^^

Here is the list of all available actions. These actions are to be placed at
this level:

.. code-block:: YAML

    # Name of the testcase
    Testcase1:

        # Location of the blitz trigger
        # Leave this as is for most use cases
        source:
            pkg: genie.libs.sdk
            class: triggers.blitz.blitz.Blitz

        # Field containing all the sections
        test_sections:

            # Section name - Can be any name, it will show as the first section
            # of the testcase
            - apply_configuration:
                - ">>>> <ACTION> <<<<"
                - ">>>> <ACTION> <<<<"
                - ">>>> <ACTION> <<<<"

            - section_two:
                - ">>>> <ACTION> <<<<"
                - ">>>> <ACTION> <<<<"
        ...

Below you can find the list of all available actions

Execute
_______

The `Execute` action is used to send a command to the device. Keyword `include`
and `exclude` are to be used to verify if specific string exists or do not
exists in the output. Both keys are optional. 

.. code-block:: YAML

    - execute: # ACTION
        # (Either device hostname or device alias)
        device: R1 
        # Send show version to the device
        command: show version
        # Can have as many items under include or exclude that you want
        include:
            - '12.9.1'
            - 'CSR1000V'
            # Regular expression can also be provided
            - '\d+'
        exclude:
            - 'Should not be in the output'
        ...

Parse
_____

The `parse` action use pyATS `Parsers
<https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers>`_.
The parsers return structure data in a dictionary format. It allows to verify
if certain key have an expected output, where `execute` verify that it is
somewhere in the output, irrelevant of the structure.

.. code-block:: YAML

    - parse: # ACTION
        device: R2
        command: show version

        # Can have as many items under include or exclude that you want
        include:
            # Using Dq (the new dictionary querying tool), you can verify whether 
            # a specific Keyword exists within your parsed output
            - raw("[version][version]")
            - contains("version").value_operator('mem_size' '>=', 1217420)
              # Make sure the memory is greater than 1217420
        exclude:
            - get_values('platform')
              # The output: [VIRTUAL XE]
        ...

The following operations are supported `"{=, >=, <=, >, <, !=}"`

Configure
_________

The `configure` action is used to configure the device.

.. code-block:: YAML

    - configure: # ACTION
        device: device_name
        command: |
            router bgp 65000
            shutdown

Api
___

The `api` action use pyATS `api
<https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/apis>`_.

You can use include/exclude(same as parse and execute) to verify, whether
a variable exists in an api output.

Api's that has 'dictionary' output can be queried in the same manner as parse.

.. code-block:: YAML

    # validating non-numerical reuslts
    - api: # ACTION
        continue: True
        function: get_interface_mtu_size
        arguments:
            interface: GigabitEthernet1
        include:
            - contains('max')
            - get_values('range')
        exclude:
            - contains('min-max')
        ...

Other Api's (with integer or string outputs), can be verified as same as in 
the example below.  

.. code-block:: YAML

    # validating numerical reuslts
    - api: # ACTION
        continue: True
        function: get_interface_mtu_size
        arguments:
            interface: GigabitEthernet1
        include:
            - <= 2000
        ...

The follow operation is supported `"{=, >=, <=, >, <, !=}"`

TGN 
____

The 'tgn' action now allows you to call traffic generator(tgn) apis as well

.. code-block:: YAML

    - api: # ACTION
        continue: True
        function: get_traffic_stream_objects
        ...

Sleep
_____

The `sleep` action is used to pause the execution for a specified amount of time.

.. code-block:: YAML

    - sleep: # ACTION
        # Sleep for 5 seconds
        sleep_time: 5
        ...

Learn
_____

The `learn` action is used to learn a feature on a specific device, returning a
OS agnostic structure.  You also can validate the outcome of this action
similar to api action and parse action.

.. code-block:: YAML

    - learn:
        device: R1
        feature: bgp
        include:
            - raw("[info][instance][default][vrf][default][cluster_id]")
        ...

Print
______

Print action allows you to print any vairable into the console.

.. code-block:: YAML

    - print:
        continue: True
        print_item1: "%VARIABLES{parse_output}"
        print_item2: "%VARIABLES{configure_output}"
        ...

Yang
____

Documentation in development

configure_replace
_________________

The `configure_replace` action is used to replace the running-config. Just
provide the location of the saved configuration.

.. code-block:: YAML

    - configure_replace:
        device: my_device
        config: bootflash:/golden_config

        # Iteration and interval is used for a retry mechanism
        iteration: <int> #optional, default is 2
        interval: <int> #optional, default is 30

save_config_snapshot
____________________

The `save_config_snapshot` action is used to save a snapshot of the current
device configuration. The config can later be used with the
`restore_config_snapshot` action.

.. code-block:: YAML

    - save_config_snapshot:
        device: my_device

restore_config_snapshot
_______________________

The `restore_config_snapshot` action is used to restore a snapshot taken
from the `save_config_snapshot` action. If you want to re-use the same
snapshot you can specify to not delete it (shown below).

.. code-block:: YAML

    - restore_config_snapshot:
        device: my_device
        delete_snapshot: False #optional, default is True

run_genie_sdk
_____________

The `run_genie_sdk` action is used to run other triggers from within
blitz.

.. note::

    You must extend the main trigger_datafile for any of those triggers
    to be accessible. Put this at the top of your trigger_datafile:
    `extends: '%ENV{VIRTUAL_ENV}/genie_yamls/trigger_datafile.yaml'`

.. code-block:: YAML

    - run_genie_sdk:
        <trigger_name>:
            <any trigger arguments>

        # An example of running TriggerSleep
        TriggerSleep:
            devices: [my_device]
Saving and loading variable using 'Markup'
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using this specific markup, users can apply different filters on actions' outputs
and save them into a variable and later load it in another action inside 
the YAML data-file, whether.

.. code-block:: YAML

    # Looking for the parse_output variable in the action execute
    - apply_configuration:    
          - parse:
              continue: True
              command: show version
              device: PE2
              save: 
                - variable_name: parse_output
                  filter: contains('version').get_values('type_of_disk', index=1)
                - variable_name: another_parser_output
                  filter: get_values('mem_size')
                - variable_name: an_another_parser_output
                # You can save the entire output of an action
                # without applying a filter 
          - execute:
              continue: True
              device: PE1
              command: show version
              max_time: 1
              check_interval: 1
              reply:
                - pattern: r'.*Protocol +\[ip\]:.*
                  action: 'sendline(1.1.1.1)'
              include:
                - "w"
                - "%VARIABLES{parse_output}"

    # Using the api output as part of the command that would be configured on device PE1
    # The api output would be casted to string
    - apply_configuration:    
          - api:
              continue: True
              device: PE1
              function: get_interface_mtu_size
              save:
                - variable_name: api_output
              arguments:
                interface: GigabitEthernet1
          - configure:
              device: PE1
              command: |
                router bgp '%VARIABLES{api_output}'
        ...

Both filter and include/exclude features are using a dictionary querying tool called `Dq
<https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#dq>`_.

Quick Trigger parallel
^^^^^^^^^^^^^^^^^^^^^^

All actions can be executed in parallel and can also execute actions on multiple
devices in parallel.

.. code-block:: YAML

    # Name of the testcase
    Testcase1:

        # Location of the blitz trigger
        source:
            pkg: genie.libs.sdk
            class: triggers.blitz.blitz.Blitz

        # Field containing all the sections
        test_sections:

            # This section shows an example of executing actions
            # When defining the action you can set the device that execute the action
            
            # section
            - apply_configuration:
                - configure:
                    device: PE1
                    command: |
                      router bgp 65000
                - api: 
                    continue: True
                    device: PE1
                    function: get_interface_mtu_config_range
                    arguments:
                      device: PE1
                      interface: GigabitEthernet1


            # This section shows an example of multiple actions that are running in parallel. 
            # Different devices can execute these actions on parallel.
            
            # section
            - verify_configuration
                - parallel:
                    - api:
                        continue: True
                        device: PE1
                        function: get_interface_mtu_size
                        arguments:
                          interface: GigabitEthernet1
                    - parse:
                        command: show version
                        device: PE2
                        include: 
                          - contains("version_short")
                    - learn:
                        continue: True
                        device: PE1
                        feature: bgp
                        include:
                          - contains("info")

            # This section shows an example of executing actions parallel and non parallel at the same time
            # Actions 'execute' and 'sleep' are being executed on a sequential manner 
            # While 'api' and 'parse' are executed at the same time
            
            # section
            - apply_configuration:
                - execute:
                    continue: True
                    device: PE1
                    command: show version
                - parallel:
                    - api:
                        continue: True
                        device: PE1
                        function: get_interface_mtu_config_range
                        arguments:
                          device: P2
                          interface: GigabitEthernet1
                    - parse:
                        command: show bgp process vrf all
                        device: P1
                - sleep:
                    sleep_time: 5
        ...

Please note that you cannot save a variable in parallel and immideately use it in another action 
that is being executed in parallel.

Trigger timeout/interval ratio adjustments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each action performs verification to make sure it has performed as expected.
These timeouts can be modified with a ratio from the testbed datafile.

.. code-block:: YAML

    # Name of the testcase
    Testcase1:

        source:
            pkg: genie.libs.sdk
            class: triggers.blitz.blitz.Blitz

        # Field containing all the sections
        test_sections:

            # Section name - Can be any name, it will show as the first section
            # of the testcase
                - apply_configuration:
                    - execute:
                        continue: True
                        command: show version
                        include:
                          - 'w'
                        max_time: 5
                        check_interval: 1 
        ...

.. code-block:: YAML

  devices:
    PE2:
      connections:
        ssh:
          ip: 10.255.1.17
          protocol: ssh
      credentials:
        default:
          password: cisco
          username: cisco
        enable:
          password: cisco
      custom:
        max_time_ratio: '0.5'
        check_interval_ratio: 0.5
      os: iosxe
      type: CSR1000v

Now the max_time and will half'd. 
