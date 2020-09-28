.. _write-blitz:

Quick Trigger (Blitz)
---------------------

The *Blitz* also known as *Quick Trigger* is a YAML-driven template that makes it easy for you to run
a test case without having to know any knowledge of programming. The *Quick Trigger* ---
called *Blitz* because it's lightning fast --- does the following actions:

* Configure a device.
* Parse the device output to verify if the device state is as expected.
* Unconfig or modify the initial configuration.
* Parse the output to check the operational state.
* Learn a feature and verify the result of the action
* Calling different apis and use their outputs on other actions and other devices
* Yang integration
* It is fully customizable and new actions can be added
* Many more features that will be discussed thoroughly in the upcoming sections

Designed for quick development, the quick trigger verifies *key-value* pairs and
uses parsing for full flexibility across OS and platforms. As with any
pyATS Library trigger, other triggers can inherit from the ``Blitz`` class. Go
ahead and build on top of it!

To use the quick trigger template, add the `YAML` content to a
:monospace:`trigger_datafile.yaml` as shown in the following example for `BGP` on a router.
The yaml is commented out explaining what each section does. See example below.

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
                    - not_contains('running')
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

Actions
^^^^^^^

Here is the list of all available actions. These actions are to be placed at
this level:

.. code-block:: YAML

    # Name of the testcase
    Testcase1:

        # Leave this as is for most use cases
        source:
            pkg: genie.libs.sdk
            class: triggers.blitz.blitz.Blitz

        # Field containing all the sections
        test_sections:

            # Section name - Can be any name, it will show as the first section
            # of the testcase
            - section_one:
                - ">>>> <ACTION> <<<<"
                - ">>>> <ACTION> <<<<"
                - ">>>> <ACTION> <<<<"

            - section_two:
                - ">>>> <ACTION> <<<<"
                - ">>>> <ACTION> <<<<"
        ...

Below you can find the list of all available actions

execute
_______

The ``execute`` action is used to send a command to the device. Keywords `include`
and `exclude` are to be used to verify if specific string exists or do not
exists in the output. You also, have the option to check if a specific
``regex`` exists within the output of the action.

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


Both include and exclude keywords are optional to use.

configure
_________

The `configure` action is used to configure the device.

.. code-block:: YAML

    - configure: # ACTION
        device: device_name
        command: |
            router bgp 65000
            shutdown

.. note::

    You can apply additional arguments to commands ``execute`` and ``configure``.
    List of arguments for the execute command can be found at this (`link
    <http://wwwin-pyats.cisco.com/cisco-shared/unicon/latest/user_guide/services/generic_services.html#execute>`_.), 
    and all the arguments for the configure command can be found at this (`link
    <http://wwwin-pyats.cisco.com/cisco-shared/unicon/latest/user_guide/services/generic_services.html#configure>`_.).
    Example can be seen below.

.. code-block:: YAML

    # A timeout of 10 second is applied to each action,
    # Now if the device is not configured within 10 seconds, the step will fail.
    - configure:
        command: feature bgp
        device: PE1
        timeout: 10
    - execute:
        command: show version
        device: PE1
        timeout: 10

parse
_____

The ``parse`` action use pyATS `Parsers
<https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers>`_.
The parsers return structured data in a dictionary format. It allows to verify
if certain key have an expected output, where `execute` verify that it is
somewhere in the output, irrelevant of the structure. You can use the keywords 
`include` and `exclude` to *query* the output of your parser. You can learn, how 
to use `include/exclude` keywords in a parse action by reading through 
this `section
<#querying-actions-output>`_.

.. code-block:: YAML

    - parse: # ACTION
        device: R2
        command: show version

        # Can have as many items under include or exclude that you want
        include:
            - raw("[version][version]")
            - contains("version").value_operator('mem_size' '>=', 1217420)
              # Make sure the memory is greater than 1217420

        ...

api
___

The ``api`` action use pyATS `Api
<https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/apis>`_.

You can use `include/exclude` to query the results of the apis that their outputs are ``dictionary``.
See `section
<#querying-actions-output>`_.

.. code-block:: YAML

        - api: # ACTION
            function: get_interface_mtu_config_range
            arguments:
                interface: GigabitEthernet1
            include:

                - contains('max')
                - get_values('range')
            exclude:
                - contains('min-max')
        ...

The output of the apis that are numerical or string can be also verified using the `include/exclude` keywords.
See `section
<#verification-of-non-dictionary-outputs>`_.

tgn 
____

The ``tgn`` action now allows you to call `traffic generator` (tgn) apis in addition to the 
other existing apis.

.. code-block:: YAML

    - tgn: # ACTION
        function: get_traffic_stream_objects
        ...

rest
____

The ``rest`` action allows to make rest call to any endpoint on a device. Rest uses http method to 
transfer data. Five http protocols are supported, `get`, `post`, `put`, `patch` and `delete`.

You can find additional information on rest, using this `tutorial
<http://wwwin-pyats.cisco.com/cisco-shared/rest/connector/latest/user_guide/services/index.html>`_.

.. code-block:: YAML

    test_sections:
        - plain_actions:
            - rest:
                method: get
                dn:  '/api/mo/sys/intf/phys-[eth1/1].json'
                device: N93_3
            - rest:
                method: delete
                device: N93_3
                dn: '/api/mo/sys/bgp/inst.json'
            - rest:
                method: put
                dn:  '/api/mo/sys/bgp/inst/dom-default/af-ipv4-mvpn.json'
                device: N93_3
                payload: {
                    "intf-items": {
                      "phys-items": {
                        "PhysIf-list": [
                          {
                            "adminSt": "down",
                            "id": "eth1/2",
                            "userCfgdFlags": "admin_layer,admin_state"
                          }
                        ]
                      }
                    }
                  }
            - rest:
                method: post
                dn:  'api/mo/sys/bgp/inst.json'
                device: N93_3
                payload: {
                  "bgpInst": {
                    "attributes": {
                      "isolate": "disabled",
                      "adminSt": "enabled",
                      "fabricSoo": "unknown:unknown:0:0",
                      "ctrl": "fastExtFallover",
                      "medDampIntvl": "0",
                      "affGrpActv": "0",
                      "disPolBatch": "disabled",
                      "flushRoutes": "disabled"
                     }
                  }
                }
            - rest:
                method: patch
                dn:  '/api/mo/sys/bgp/inst/dom-default/af-ipv4-mvpn.json'
                device: N93_3
                payload: {
                    "intf-items": {
                      "phys-items": {
                        "PhysIf-list": [
                          {
                            "adminSt": "down",
                            "id": "eth1/2",
                            "userCfgdFlags": "admin_layer,admin_state"
                          }
                        ]
                      }
                    }
                  }

sleep
_____

The ``sleep`` action is used to pause the execution for a specified amount of time.

.. code-block:: YAML

    - sleep: # ACTION
        # Sleep for 5 seconds
        sleep_time: 5
        ...

learn
_____

The ``learn`` action is used to learn a feature on a specific device, returning an
OS agnostic structure.  You also can query the outcome of this action
similar to api action and parse action.

.. code-block:: YAML

    - learn:
        device: R1
        feature: bgp
        include:
            - raw("[info][instance][default][vrf][default][cluster_id]")
        ...

print
______

``print`` action allows you to print messages, variables and actions output into the console. 

.. code-block:: YAML

    - print:
        print_item1: "%VARIABLES{parse_output}"
        print_item2: "%VARIABLES{configure_output}"
        ...

yang
____

The :ref:`yang action` action is designed to work with differing underlying protocols, but, at the
time of this writing, only NETCONF and gNMI are supported.  Changing the connection and
protocol determines the message format.

Example of configuration using NETCONF (with automated verification of edit-config on device)

.. code-block:: YAML

    - yang:
        device: uut2
        connection: netconf
        operation: edit-config
        protocol: netconf
        datastore: candidate
        banner: YANG EDIT-CONFIG MESSAGE
        content:
          namespace:
            ios-l2vpn: http://cisco.com/ns/yang/Cisco-IOS-XE-l2vpn
          nodes:
          - value: 10.10.10.2
            xpath: /native/l2vpn-config/ios-l2vpn:l2vpn/ios-l2vpn:router-id
            edit-op: merge

bash_console
_________________

Using this action, now you can run various bash command on the device. You can save output of each command, and apply include/exclude
verification on the output of each command. Below example shows how to use bash_console action.

.. code-block:: YAML

    - verify_config:
          - bash_console:
              device: csr1000v-1
              target: standby
              timeout: 45
              save:
                - variable_name: second_cmd
                  filter: contains('ls')
                - variable_name: everything
              commands:
                - pwd
                - ls
                - |
                  cd ~
                  echo A string of text
              include: 
                  - contains('ls')

configure_replace
_________________

The ``configure_replace`` action is used to replace the running-config. Users only needs 
to provide the location of the saved configuration.

.. code-block:: YAML

    - configure_replace:
        device: my_device
        config: bootflash:/golden_config

        # Iteration and interval is used for a retry mechanism
        iteration: <int> #optional, default is 2
        interval: <int> #optional, default is 30

save_config_snapshot
____________________

The ``save_config_snapshot`` action is used to save a snapshot of the current
device configuration. The config can later be used with the
``restore_config_snapshot`` action.

.. code-block:: YAML

    - save_config_snapshot:
        device: my_device

restore_config_snapshot
_______________________

The ``restore_config_snapshot`` action is used to restore a snapshot taken
from the ``save_config_snapshot`` action. If you want to re-use the same
snapshot you can specify to not delete it. See `example` below.

.. code-block:: YAML

    - restore_config_snapshot:
        device: my_device
        delete_snapshot: False #optional, default is True

run_genie_sdk
_____________

The ``run_genie_sdk`` action is used to run other triggers from within
``Blitz``. All you have to do is to mention the trigger name and its arguments
in your ``Blitz`` datafile. 

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

diff
_____

Allow to diff two variables (Dictionary or Ops object).

By default it will just print the difference, but can also fail the section
if they are different with the argument `fail_different=True`.

``command`` or ``feature`` to diff will gather pre-defined exclude list from 
the parser or Ops.

``mode`` can be specified only what you want to check. ``mode`` has ``add``, 
``remote`` and ``modified``. By default, it will show all the differences, 
for the case ``add``, will show only added difference.

.. code-block:: YAML

        - snapshot_pre_configuration:
           - parse:
               device: R3_nx
               command: show interface
               save:
                 - variable_name: pre_snapshot_nxos

        - configure_interface:
            # List of actions
            - configure:
                device: R3_nx
                command: |
                  interface Ethernet1/56
                  no switchport
                  ip address 10.5.5.5 255.255.255.0
                  no shutdown

            - parse:
                device: R3_nx
                command: show interface
                save:
                  - variable_name: post_snapshot_nxos

            - diff:
                pre: "%VARIABLES{pre_snapshot_nxos}"
                post: "%VARIABLES{post_snapshot_nxos}"
                device: R3_nx
                command: show interface
                mode: modified

Example with ``feature``.

.. code-block:: YAML

            - diff:
                pre: "%VARIABLES{pre_interface_ops}"
                post: "%VARIABLES{post_interface_ops}"
                device: R3_nx
                feature: interface
                mode: add

.. note::

    Please find more detail for ``diff`` from below document.
    `Diff <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#diff>`_

compare 
_____________

Action ``compare`` allows you to verify the values of the saved variables. Below example shows how you can actually use this action.

.. code-block:: YAML

    # assume you already saved values in the variable bios, os, date_created and bootflash
    - compare:
        items:
        - "'%VARIABLES{os}' == 'NX-OS' and '%VARIABLES{date_created}' == '10/22/2019 10:00:00 [10/22/2019 16:57:31]'"
        - " %VARIABLES{bootflash} >= 290000 or '%VARIABLES{bios}' == '07.33'"


.. note::

    The starting message of a Step can be modified by specifying a custom message like the example below. This can be applied
    to all the actions supported in Blitz.

.. code-block:: YAML

    - execute:
        command: show version
        device: PE1
        custom_start_step_message: This is a test to see if a custom_start_step_message would be applied
        timeout: 100

as shown in the image you can see how in the logs the starting message is customized.

.. image:: ../images/custom_step_msg.png
   :width: 200%

Negative testing
^^^^^^^^^^^^^^^^

You can get a Passed result for an action that is expected to fail by setting the key; ``expected_failure: True``.
Actions, [``configure``, ``execute``, ``parse``, ``learn``, ``api``, ``rest``, ``bash_console``] support this feature.

.. code-block:: YAML

    # The command doesnt exist so action should error out but since it was anticipated that the command wouldn't work.
    The results would finally be shown as passed.
    - execute:
        command: banana
        device: PE1
        expected_failure: True
        timeout: 100


Failing actions and sections upon failure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default blitz actions and sections continue to work even after a failure. However, users can manually adjust their
testscripts so the script stop upon failure. Below example shows how to achieve that.

.. code-block:: YAML

    - test_sections:
        - apply_configuration:    
            - continue: False
            - configure:
                command: router bgp 6500
                device: PE2
        - confirm_actions:
            - execute:
                continue: False
                command: show interface
                device: PE2
            - execute:
                command: show module
                device: P2

In the section apply_configuration in action level ``- continue: False`` is set, so if the result of the section is
a failure the script stops the run of the rest of the sections in the testscript.

In the section confirm_actions, in the first action ``execute`` a keyword ``continue`` is added with value ``False``.
That would send the signal that upon failure of an action the rest of the actions in that section should not be running.

Querying actions' output
^^^^^^^^^^^^^^^^^^^^^^^^

As it was mentioned when introducing different actions, users can query
the action outputs that are dictionary using a tool called Dq. You can find the complete
tutorial of Dq by following this `link
<https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#dq>`_.

Actions ``parse``, ``learn`` and ``api`` are benefiting from this feature the most, as they are
the one that are most likely to have a dictionary output. You can query a dictionary using Dq
and see whether the result of a query is included or excluded in our output.

Below you can see an `example` of using include and exclude on the parsed output of the 
command ``show version``.

.. code-block:: YAML

    - apply_configuration:    
              - parse:
                  command: show version
                  device: PE2
                  include:

                    # we want to se if the result of this query
                    # is not a empty dictionary
                    - contains('WebUI[\S\s]+', regex=True)
                  exclude:

                    # The output of the query is 'VIRTUAL XE'
                    # but we hope that the key 'platform' has no value
                    # or does not exist within the dictionary by using
                    # the exclude keyword
                    - get_values('platform')

Below you can see an `example` of calling the :monospace:`get_interface_mtu_config_range` api
within the :monospace:`trigger_datafile` and checking if certain query results are included or excluded in the output.

.. code-block:: YAML

    - apply_configuration:    
        - api: #
            function: get_interface_mtu_config_range
            arguments:
                interface: GigabitEthernet1
            include:
                
                # Check if the output of this query is not an empty dictionary
                - contains('max')

                # Check if the key 'range' has the value of <1200, 1800>
                - contains_key_value('range', <1200, 1800>)
            exclude:

                # Check if the output of these queries are actually an empty dictionary
                - contains('min-max')

.. note::

    There is no need to use Dq to validate if a dictionary output is equal to an expected dictionary.
    See below example.

.. code-block:: YAML

    # Description: This would check whether the output of the parser is equal to the specified dictionary.
    # No Dq query is needed to perform such validation.

    - parse:
        device: 'N93_3'
        command: 'show module'
        save: 
            - variable_name: banana
              filter: contains('lc')
        include:
            -  {'slot': {'lc': {'2': {'40G Ethernet Expansion Module': {'ports': '12',
                'model': 'N9K-M12PQ',
                'status': 'ok',
                'software': 'NA',
                'hardware': '1.2',
                'slot/world_wide_name': 'GEM',
                'mac_address': '88-1d-fc-71-de-38 to 88-1d-fc-71-de-43',
                'serial_number': 'SAL1928K4EG',
                'online_diag_status': 'Pass'}}},
                'rp': {'1': {'1/10G SFP+ Ethernet Module': {'ports': '48',
                   'model': 'N9K-C9396PX',
                   'status': 'active',
                   'software': '9.3(3)IDI9(0.509)',
                   'hardware': '2.2',
                    'slot/world_wide_name': 'NA',
                    'mac_address': '84-b8-02-f0-83-90 to 84-b8-02-f0-83-c7',
                   'serial_number': 'SAL1914CNL6',
                   'online_diag_status': 'Pass'}}}}}
            - contains('lc')
            - get_values('rp')

Verification of non dictionary outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At this moment, it is only action `api` that supports this feature, as it is the only
action that have ``integer``, ``float`` and ``string`` outputs.

In below `example` , we want to verify that the numerical output of :monospace:`get_interface_mtu_size` is 
smaller or equal 2000

.. code-block:: YAML

    # code_block_5

    - api: # ACTION
        function: get_interface_mtu_size
        arguments:
            interface: GigabitEthernet1
        include:
            - <= 2000
        ...

For numerical outputs we support all the common mathematical operations ``{=, >=, <=, >, <, !=}``.

You also can check whether a value is within a certain range. Below 
is an `example` of this feature. We want to see if the action output is 
greater than 1200 and smaller or equal 1500.

.. code-block:: YAML

    - api: # ACTION
        function: get_interface_mtu_size
        arguments:
            interface: GigabitEthernet1
        include:
            - ">1200  && <=1500"


If you use the keyword include without specifying any operation the default operation would be 
set to ``==`` and by using keyword exclude the operation would be set to ``!=``. 
Below you can see an `example` of this.

.. code-block:: YAML

    - api: # ACTION
        function: get_interface_mtu_size
        arguments:
            interface: GigabitEthernet1
        include:
            - 1500
        exclude:
            - 9999

Replying to the prompt dialogue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When executing or configuring commands on some devices, it is possible that you receive 
a prompt message that needs to be replied. In ``Blitz``, you can handle these prompt messages 
automatically by using the keyword `reply` in your action. In order to reply a message, 
you need to know the regex pattern of the message that would show up in the console.

Below you can see an `example` of the action ``execute`` handling a prompt message.

.. code-block:: YAML

    # Looking for the parse_output variable in the action execute
    - apply_configuration:    
        - execute:
            device: PE1
            command: write erase
            reply:
            - pattern: .*Do you wish to proceed anyway\? \(y/n\)\s*\[n\]
              action: sendline(y)
              loop_continue: True
              continue_timer: False

Filter, Save and Load variables 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Another very useful feature that BLITZ has, is the ability to save actions output or a variation of the output. You can save values to a variable name and later use that variable in other actions. There are different ways to save values to a variable:

* Save the entire output of an action to a variable name.

* Save a part of the output of an action to a variable name.

Below you can find examples of how to save the entire output to a variable name.

.. code-block:: YAML

    # Description: Saving the entire output of an execute action into a variable
    # The type of output is string

    - Execute:
        device:  '%{testbed.devices.uut.alias}'
        command: show platform
        save:
          - variable_name: execute_output

.. code-block:: YAML

    # Description: Saving the entire output of an execute action into a variable
    # The type of output is dictionary/JSON data.

    - parse:
        device:  '%{testbed.devices.uut.alias}'
        command: show platform
        save:
          - variable_name: execute_output

For actions that has outputs with ``JSON`` datatype It is possible to apply a filter (`Dq
<https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#dq>`_ queries)
and save a part of dictionary into a variable

.. code-block:: YAML

    # Description: Applying a dq query and save the outcome into the variable parse_output.
    # Later on checking if that value exist in action execute output.
    # Dq query only works on outputs that are dictionary

    - apply_configuration:
          - parse:
              command: show module
              device: PE2
              save:
                - variable_name: parse_output
                  filter: contains('ok').get_values('lc', index=2)
                  # The output is '4'
          - execute:
              device: PE1
              command: show version
              include:
                - "w"
                # check if '4' exists within the result of this action
                - "%VARIABLES{parse_output}"

For actions that has string outputs you can apply a regex filter. If regex matches the output, the grouped value, 
that has a variable name specified like ``(?P<variable_name>)``, will be stored into that variable_name.

Below you can see the example of regex filter

.. code-block:: YAML

    # first saving values from execute action output
    # later on printing those values

    - execute:
        device: N93_3
        command: show version
        save:
        - filter: BIOS:\s+version\s+(?P<bios>[0-9A-Za-z()./]+).*                        # bios version is 07.33
          regex: true
        - filter: bootflash:\s+(?P<bootflash>[0-9A-Za-z()./]+)\s+(?P<measure>\w+).*     # bootflash is  51496280 and measure is KB
          regex: true
    - print:
        bios:
          value: "The bios version is %VARIABLES{bios}"
        bootflash:
          value: "The bootflash is %VARIABLES{bootflash} and %VARIABLES{measure}"

.. note::

    The name of the device that the action is being executed on will be saved automatically upon
    execution of the action and stay usable till the end of that action lifecycle. You can use that 
    name as a variable using ``%VARIABLES{device.name}`` for various purposes in your action. Task id and 
    transcript name also can be accessed by using ``%VARIABLES{task.ud}``, ``%VARIABLES{transcript.name}.``

.. note::

    The result of a section (whether it is passed, failed etc.) will be saved automatically into a variable 
    same as the section name. You can use that name using ``%VARIABLES{<section_name>}``. Also in your YAML file,
    it is possible to have accesc the section's uid simply by using ``%VARIABLES{section.uid}``.

.. note::

    Job file related values, such as job file path or job file name can be accessed by using ``%VARIABLES{runtime.job.file}`` 
    and ``%VARIABLES{runtime.job.name}``. Any other job file related value can be accessed in similar fashion ``%VARIABLES{runtime.job.<value>``


The following `example` is showing how to use our specific markup language
to load the saved variable in another action. In this example we save the output
of the :monospace:`get_interface_mtu_size` api and later use it within the command
of the action ``configure``.

.. code-block:: YAML

    - apply_configuration:    
          - api:
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

Another example of how to use our markup language is provided below. In this example the output of the ``learn``
action is saved on variable  :monospace:`main_learn_output`. Also, a filter is applied on this output and is saved
in variable  :monospace:`filtered_learn_output`. We later check the inclusion of the :monospace:`filtered_learn_output` 
in action ``execute`` output and print the   :monospace:`main_learn_output` into the console.

.. code-block:: YAML

    - apply_configuration:    

          - learn:
              device: PE1
              feature: bgp
              save:
                - variable_name: main_learn_output
                - variable_name: filtered_learn_output
                    filter: raw("[info][instance][default][vrf][default][cluster_id]")
          - execute:
              device: PE1
              command: show version
              include:
                - "w"
                - "%VARIABLES{filtered_learn_output}"
          - print:
              print_item1: "%VARIABLES{main_learn_output}"

.. note::

    Both filter and include/exclude features are using our dictionary querying tool `Dq
    <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#dq>`_.


Quick Trigger parallel
^^^^^^^^^^^^^^^^^^^^^^

Up to this point of this tutorial, we were mainly talking about how to operate with ``Blitz`` and execute
different actions in a sequential manner. This means that upon running the :monospace:`trigger_datafile`
actions are getting executed one after the other and each action should completely finish its job before 
another action starts. In some testcases executing actions sequentially could be quite time consuming. 

In this section we will discuss how to execute multiple actions in parallel and at the same time. Running actions 
in parallel allows you to execute numerous actions all together, which make the execution of a  :monospace:`trigger_datafile`
way more faster.

You can run multiple actions concurrently by defining your actions after the keyword `parallel` within 
your :monospace:`trigger_datafile`. Below you can see an example of multiple actions that are running in parallel.
In below example actions ``api`` and ``learn`` are executed on device ``PE1`` and ``parse`` is executed on device ``PE2``
and all at the same time.

.. code-block:: YAML

            - verify_configuration
                - parallel:
                    - api:
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
                        device: PE1
                        feature: bgp
                        include:
                          - contains("info")
        ... 

While you can execute actions in parallel to make the execution of a :monospace:`trigger_datafile` faster, 
you can still run some other actions in the same sequential manner. In below example action ``execute`` 
gets executed first and then two actions ``api`` and ``parse`` start their work in parallel, and finally
the action ``sleep`` start its work for 5 seconds.

.. code-block:: YAML

            # Actions 'execute' and 'sleep' are being executed on a sequential manner 
            # While 'api' and 'parse' are executed at the same time
            - apply_configuration:
                - execute:
                    device: PE1
                    command: show version
                - parallel:
                    - api:
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

Please note that you cannot save a variable in parallel and immediately use it in another action 
that is being executed in the same parallel block. However, you still can save a variable in an action 
that being executed in a parallel block, and use it outside that parallel block later. If you want to use a 
variable in an action that is being executed in parallel, you need to save that variable beforehand in an 
action outside of that parallel block.

In below `example` value ``min`` and ``max`` are saved from the output of the :monospace:`get_interface_mtu_config_range`
api action and later is being used in :monospace:`get_interface_mtu_size` api that is going to be executed in parallel
along with a ``configure`` action. Within the same parallel block the output of the action ``configure`` is being saved
to be used later in other actions.

.. code-block:: YAML

    test_sections:
        - apply_configuration:

            - api:
                device: PE2
                function: get_interface_mtu_config_range
                save:
                - variable_name: min
                  filter: contains('min')
                - variable_name: max
                  filter: contains('max')
            - parallel:
                - api:
                    device: PE1
                    function: get_interface_mtu_size
                    arguments:
                      interface: GigabitEthernet1
                    include:
                      - ">= %VARIABLES{min} && <= %VARIABLES{max} "
                - configure:
                    device: PE1
                    save: 
                      - variable_name: another_configure_output
                    command: |
                        router bgp 65000
            - execute:
                  device: PE1
                  command: show interface
                  include:
                    - "%VARIABLES{another_configure_output}"
 

Trigger timeout/interval ratio adjustments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each action performs verification to make sure it has performed as expected.
These timeouts can be modified with a ratio from the testbed datafile.
This feature is supported by actions ``api``, ``execute``, ``parse``, ``learn`` and ``rest``.

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

Running conditional statements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is possible to run (or not run) a set of actions with regards to a conditional statement. 
This can be achieved by running actions below the keyword run_condition. 
To run actions with a conditional statement, BLITZ expects:

* An if statement with boolean value (True or False statement).

* A function that can be the result of all the actions under run_condition if the boolean condition is equal True.

* A set of actions (e.g parse, execute etc.) that would be specified under keyword ``actions``.

The function can be one from this list ``[passed, failed, aborted, skipped, blocked, errored, passx]``. 
The function will be applied only if the if statement is equal True, otherwise actions will be running normally.

To better understand the use of this feature lets look at the following example.

.. code-block:: YAML

    - run_condition:
        
        if: "2000 == 2000"  # if statement boolean value True
        function: failed    # function that would be applied to actions
        
        actions:            # All the actions that are under this keyword will be conditioned and the results of them will be set as failed
          - api:            # output as Failed

              description: get the api value and verify the output
              device: "%{testbed.devices.PE1.alias}"
              function: get_interface_mtu_size
              save:
                - variable_name: nbc
              arguments:
                interface: GigabitEthernet1
              include:
                - ">= 1400 && <= 1600"
          - sleep:         # output as Failed
              sleep_time: 1
    
    - run_condition:
        
        if: "2000 != 2000"  # if statement boolean value False
        function: passed    # function that would be applied to actions
        
        actions:
          - api:            # will call the api

              description: get the api value and verify the output
              device: "%{testbed.devices.PE1.alias}"
              function: get_interface_mtu_size
              save:
                - variable_name: nbc
              arguments:
                interface: GigabitEthernet1
              include:
                - ">= 1400 && <= 1600"
          - sleep:         # will sleep for a sec
              sleep_time: 1

Using the run_condition, users can evaluate various conditional statements before running their actions. 
Examples are provided below for these conditional statements.

.. code-block:: YAML

    # Description: You can check whether a section that has previously ran has a `passed`
    # results and run your actions if that sections functioned properly.

    test:
        source:
            pkg: genie.libs.sdk
            class: triggers.blitz.blitz.Blitz
        devices: ['uut']
        test_sections:
            - plain_actions:                                      # the section.results is == passed
                - sleep:
                    sleep_time: 10
            - apply_config:
                - run_condition:
                       if: "%VARIABLES{plain_actions} == failed"  # if section plain_actions has failed, fail all the actions below
                       function: failed                           # The section plain_actions has passed so all the actions below will con't running
                       actions:
                         - execute:
                             command: show version
                             device: uut
                         - sleep:
                             sleep_time: 1


.. code-block:: YAML

    # Description: You can check whether if an action that has previously ran has `passed`
    # and run your actions if that action functioned properly.

    # To be able to reference an action, you need to define an action alias for that action

    test:
        source:
            pkg: genie.libs.sdk
            class: triggers.blitz.blitz.Blitz
        devices: ['uut']
        test_sections:
            - apply_config:
                - execute:                                          # execute result is a failure because parser does not include in execute output
                    alias: execute_alias
                    command: show vrf
                    device: uut
                    include:
                        - parser
                - run_condition:
                       if: "%VARIABLES{parser_alias} == failed"     # if action execute_alias has failed fail all the actions below
                       function: skipped                            # The action execute_alias failed so all the actions below will be skipped
                       actions:
                         - parse:
                             command: show version
                             device: uut
                         - sleep:
                             sleep_time: 1

.. code-block:: YAML

    # Description: You can check whether if a saved_variable has the appropriate output
    
    test:
        source:
            pkg: genie.libs.sdk
            class: triggers.blitz.blitz.Blitz
        devices: ['uut']
        test_sections:
            - apply_config:
                - api:                                              # api output is equal to 1500
                     device: uut
                     function: get_interface_mtu_size
                     save:
                       - variable_name: gims_output                 # the 1500 is stored in gims_output
                     arguments:
                       interface: GigabitEthernet1
                - run_condition:
                       if: "%VARIABLES{gims_output} != 1500"        # if action gims_output is not equal 1500 the function should abort the section
                       function: aborted                            # the if statement is false hence, won't the actions
                       actions:
                         - parse:
                             command: show version
                             device: uut
                         - sleep:
                             sleep_time: 1

Looping in BLITZ
^^^^^^^^^^^^^^^^

In BLITZ, a loop is a sequence of actions that is repeated until a certain condition is reached.
Looping allows the development of more dynamic testcases.

Lets take a look at a basic examples of looping before diving deeper into looping in BLITZ.
In the below BLITZ section, the loop is above an execute action.

The goal is to run this action twice on the same device using 2 different commands, without writing two separate execute
actions with 2 different commands. This can be achieved simply by using loop like below.

In the below example The loop_variable_name will be the name of the loop value that will be reused in the action. 
The value here is a list of show commands. Here each show commands get saved into the variable_name “command” and in the execute action would be loaded as the actual command. 
The execute action would run twice once executing show version command and once executing show vrf command both times on the device PE1.

.. note::
    
    An iteration here means, one execution of all the actions below the keyword loop. In below example we have 2 iterations.

.. code-block:: YAML

    - apply_config:
        - loop:
            loop_variable_name: command
            value:
              - show version
              - show vrf
            actions:
              - execute:
                  alias: execute_
                  device: PE1
                  command: "%VARIABLES{command}"

Each loop can contains the following keywords:

* ``loop_variable_name``: It is variable name of the variable that will be reused during the loop lifecycle.
* ``value``: A value is a list or hash of items. For each iteration of a loop, an item in the list/hash will be stored into the loop_variable_name.
* ``range``: It is an integer. When range specified a list of integers is created containing values from 0 to range integer.
  The items of the list can be reused during the loop lifecycle similar to what stated previously in value.
* ``until``: A terminating condition, that upon reach the loop would stop working.
* ``do_until``: Another terminating condition, with one slight difference. If specified the loop will run once even if the terminating condition is met.
* ``max_time``: A max_time that should be specified in case of defining an until or do_until so the loop would finish at a certain point, without falling into infinite loop.
* ``every_seconds``: A value to set so each iteration of the loop run exactly to that amount of seconds.

.. note::
    
    A loop can only have one of the ``value``, ``range``, ``until``, ``do_until``.

There are a lot of use cases for looping with various features. Examples can be found below.

.. code-block:: YAML

    # Description: Loop over a dictionary/hash.
    # each dictionary is a collection of key value pairs.
    # To use the keys and values of the dictionary you can use the keywords ._keys and ._values

    - loop:
        # looping over a dictionary and applying values within action in same level and actions that re in the nested loop
        loop_variable_name: l_dict
        value:                          # l_dict will represent each item upon iteration in this dictionary
          inventory_save: inventory
          module_save: vrf
        actions:
            - execute:
                device: PE1
                command: show %VARIABLES{l_dict._values}            # l_dict.values will be inventory and vrf in order
                save:                                               # The output of the action gets saved respectively in the specified values.
                  - variable_name: "%VARIABLES{l_dict._keys}"       # l_dict.keys will be inventory_save and module_save in order.
                include:
                  - "state"

.. code-block:: YAML

    # Description: Loop over a list of device names, and run actions on the various devices without duplicating that action.

    - loop:
        # A loop that runs one action over different devices
        loop_variable_name: devices
        value:                                              # a list of device names
          - PE1
          - PE2
        actions:
          - execute:
              # The action name
              alias: execute_
              device: "%VARIABLES{devices}"                 # load the device here and execute show platform sequentially on various devices
              command: show platform

.. code-block:: YAML

    # Description: Loop over actions for maximum time of 5 seconds, execute actions once (one iteration).
    # If the result of first action was not equal to "passed", terminate the loop, else continue until the condition is met or
    # max_time is reached

    - loop:
        # Loop over an action at least running it once and if a condition met terminate the loop
        do_until: "%VARIABLES{api_mtu_size} != passed"
        max_time: 5
        actions:
              - api:
                  alias: api_mtu_size
                  description: get the api value and verify the output
                  device: "%{testbed.devices.PE1.alias}"
                  function: get_interface_mtu_size
                  save:
                    - variable_name: nbc
                  arguments:
                    interface: GigabitEthernet1
              - execute:
                  command: show vrf
                  device: PE2

.. code-block:: YAML

    # Description: Looping over an action twice (two iteration) since the range is 2, and each time, 
    # and run a couple of actions in parallel
    # Also after each parallel call sleep for amount of the range value, so once for one second and the other for two seconds.

    - loop:
        # Looping on a range of value, this instance it runs twice, you still can use the range number in your actions
        range: 2
        loop_variable_name: range_name
        actions:
          - parallel:
            - parse:
                device: PE1
                command: show version
            - execute:
                device: PE2
                command: show version
        - sleep:
            sleep_time: "%VARIABLES{range_name}"

The keyword ``every_seconds`` is defined so users can manage their loop and if possible run it with synchronized timing.
If the execution of an iteration of a loop exceeds the time assigned for every_seconds, the loop would still continue its work but a warning would be 
printed into the log. Below you can see the example of how ``every_seconds`` work.

.. code-block:: YAML

    # Description: this action is looping over a list of size two, hence two iteration and each iteration should take 8 seconds
    # if the iteration ends in less than 8 seconds, the loop would sleep for the remaining of that time and after reaching 8 seconds
    # it would execute the other iteration. The total time of execution in this case would be 16 seconds
    # Keep in mind if an iteration takes more than 8 seconds the loop continue the work and it wont stop

    - loop:
        loop_variable_name: banana
        value: 
          - version
          - vrf
        every_seconds: 8
        actions:
                - execute:  
                    alias: execute_
                    device: uut
                    command: show %VARIABLES{banana}
                - parse:
                    alias: parse_
                    device: uut
                    command: show version

Another feature that Looping in BLITZ supports is nested loops. There are cases that the users might want to iterate over
various values. Using nested loop would provide users with that functionality. Below shows the example of how you can implement nested loops
in your script.

.. code-block:: YAML

    # Description: in this example, the first loop has a dictionary value. The item of the second loop that is nested
    # in the first loop have access to both the values of the dictionary in the first loop and the list in the second loop.

    - loop:
        # looping over a dictionary and applying values within action in same level and actions that re in the nested loop
        loop_variable_name: l_dict
        value: 
          inventory_save: inventory
          module_save: vrf
        actions:
          - api:
              device: PE2
              function: get_interface_mtu_config_range
              arguments:
                interface: GigabitEthernet1
              save:
                - variable_name: max
                  filter: get_values('max')                        
          - loop:
              # Looping on a range of value, this instance it runs twice, you still can use the range number in your actions
              value: 
                - show version
                - show vrf
              loop_variable_name: list_name
              actions:
                - parallel:
                  - execute:
                      device: PE1
                      command: show %VARIABLES{l_dict._values}
                      save:
                        - variable_name: "%VARIABLES{l_dict._keys}"
                      include:
                        - "state"
                - execute:
                    command: "%VARIABLES{list_name}"
                    device: PE2