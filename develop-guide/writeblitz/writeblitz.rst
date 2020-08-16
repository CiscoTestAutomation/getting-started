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

configure
_________

The `configure` action is used to configure the device.

.. code-block:: YAML

    - configure: # ACTION
        device: device_name
        command: |
            router bgp 65000
            shutdown

api
___

The ``api`` action use pyATS `Api
<https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/apis>`_.

You can use `include/exclude` to query the results of the apis that their outputs are ``dictionary``.
See `section
<#querying-actions-output>`_.

.. code-block:: YAML

        - api: # ACTION
            continue: True
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
        continue: True
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

``print`` action allows you to print messages, vairables and actions output into the console. 

.. code-block:: YAML

    - print:
        continue: True
        print_item1: "%VARIABLES{parse_output}"
        print_item2: "%VARIABLES{configure_output}"
        ...

yang
____

The :ref:`yang action` action is designed to work with differring underlying protocols, but, at the
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

Documentation in development

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
                  continue: True
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
            continue: True
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

Verification of non dictionary outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At this moment, it is only action `api` that supports this feature, as it is the only
action that have ``integer``, ``float`` and ``string`` outputs.

In below `example` , we want to verify that the numerical output of :monospace:`get_interface_mtu_size` is 
smaller or equal 2000

.. code-block:: YAML

    # code_block_5

    - api: # ACTION
        continue: True
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
        continue: True
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
        continue: True
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

Below you can see an `example` of the action ``execute`` handeling a prompt message.

.. code-block:: YAML

    # Looking for the parse_output variable in the action execute
    - apply_configuration:    
        - execute:
            continue: True
            device: PE1
            command: write erase
            reply:
            - pattern: .*Do you wish to proceed anyway\? \(y/n\)\s*\[n\]
              action: sendline(y)
              loop_continue: True
              continue_timer: False

Filter, Save and Load variables 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Another very useful feature that ``Blitz`` has, is the ability to save actions output.
You can save actions outputs to a variable name and later use that variable in other actions.
You can apply various filters to outputs (`Dq
<https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#dq>`_ queries) that are of the type dictionary  
and save the filtered results into a variable.
You can apply multiple filters to a single output.  

Below you can see an `example` of how to save outputs to a variable and apply filter on them.

.. code-block:: YAML

    # Looking for the parse_output variable in the action execute
    - apply_configuration:    
          - parse:
              continue: True
              command: show module
              device: PE2
              save: 

                - variable_name: parse_output
                  filter: contains('ok').get_values('lc', index=2)
                  # The output is '4'

                # You can save the entire output of an action
                # without applying a filter 
                - variable_name: an_another_parser_output
          - execute:
              continue: True
              device: PE1
              command: show version
              include:
                - "w"   
                # check if '4' exists within the result of this action
                - "%VARIABLES{parse_output}"


The following `example` is showing how to use our specific markup language
to load the saved variable in another action. In this example we save the output
of the :monospace:`get_interface_mtu_size` api and later use it within the command
of the action ``configure``.

.. code-block:: YAML

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

.. note::

    The name of the device that the action is being executed on will be saved automatically upon
    execution of the action and stay usable till the end of that action lifecycle. You can use that 
    name as a variable using ``%VARIABLES{device.name}`` for various purposes in your action. 

Quick Trigger parallel
^^^^^^^^^^^^^^^^^^^^^^

Up to this point of this tutorial, we were mainly talking about how to operate with ``Blitz`` and execute
different actions in a sequential manner. This means that upon running the :monospace:`trigger_datafile`
actions are getting executed one after the other and each action should completely finish its job before 
another action starts. In some testcases executing actions sequentially could be quite time consuming. 

In this section we will discuss how to execute multiple actions in parallel and at the same time. Running actions 
in parallel allows you to execute numerous actions all together, which make the execution of a  :monospace:`trigger_datafile`
way more faster.

You can run multiple actions concurently by defining your actions after the keyword `parallel` within 
your :monospace:`trigger_datafile`. Below you can see an example of multiple actions that are running in parallel.
In below example actions ``api`` and ``learn`` are executed on device ``PE1`` and ``parse`` is executed on device ``PE2``
and all at the same time.

.. code-block:: YAML

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
                continue: True
                device: PE2
                function: get_interface_mtu_config_range
                save:
                - variable_name: min
                  filter: contains('min')
                - variable_name: max
                  filter: contains('max')
            - parallel:
                - api:
                    continue: True
                    device: PE1
                    function: get_interface_mtu_size
                    arguments:
                      interface: GigabitEthernet1
                    include:
                      - ">= %VARIABLES{min} && <= %VARIABLES{max} "
                - configure:
                    continue: True
                    device: PE1
                    save: 
                      - variable_name: another_configure_output
                    command: |
                        router bgp 65000
            - execute:
                  continue: True
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
