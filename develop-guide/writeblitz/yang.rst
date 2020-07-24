.. _yang:

yang Action Details
^^^^^^^^^^^^^^^^^^^

YANG models can be boiled down to 3 required components in order to construct
the ``content`` of a simple message.

* Xpath based on `XML Path Language 1.0`_ identifying a resource
.. _XML Path Language 1.0: https://www.w3.org/TR/1999/REC-xpath-19991116/
* `Namespaces in XML 1.0`_
.. _Namespaces in XML 1.0: https://www.w3.org/TR/REC-xml-names/
* The value you wish to set the resource to

Description of Available YAML Components
----------------------------------------

.. code-block:: YAML

    - yang:
        device: # device name or alias
        connection: # device interface connection (in testbed file)
        operation:  # YANG message operation (based on NETCONF but mapped to other protocols)
                    # * edit-config - mapped to "set" for gNMI
                    # * get-config  - mapped to "get CONFIG mode" for gNMI
                    # * get         - mapped to "get STATE mode" for gNMI
                    # * subscribe
                    # * capabilities
        protocol: # [ netconf | gnmi ]
        datastore: # YANG datastores (if not defined MPTE will choose from device capabilities)
        format: # Various fomat options (see Format options below)
        banner: # (optional) Prominant log message with borders
        log: # (optional) Log INFO message
        content: # Content of YANG message being sent (see Example of configuration above)
        returns: # (optional) Expected return of YANG message (see Returns section below)

Format Options
--------------

Some format options are available relating to the message and return handling. For example, if
the message is related to a ``subscribe`` operation, you will need to communicate the type of
subscription or you may expect the test to fail (referred to as a negative test).

.. code-block:: YAML

    format:
      request_mode: STREAM # [STREAM, ONCE, POLL]
      sub_mode: SAMPLE     # [ON_CHANGE, SAMPLE]
      encoding: JSON_IETF  # [JSON, JSON_IETF]
      sample_interval: 5   # seconds (default)
      stream_max: 20       # seconds to stop stream (default no max)
      auto-validate: true  # automatically validate config messages
      negative-test: false # expecting device to return an error
      delay: 0             # pause N seconds between each test

Returns
-------

Expected return values can also be defined with the fexibility of approximation. The return
values are identified by the Xpath derived from the return message. The ``op`` is an 
operation performed between returned value and expected value

    * ``==`` equals
    * ``!=`` not equal
    * ``<`` less than
    * ``>`` greater than
    * ``<=`` less than or equal
    * ``>=`` greater than or equal
    * ``1 - 10`` range (example)

.. code-block:: YAML

    returns:
      - id:  # for referencing only
        name: # name of field for referencing only
        op:  # operation performed between returned value and expected value
        selected: # set this to ``false`` and field is ignored making it like a placeholder
        datatype: # datatype of field for general verification
        value: # expected value to compare to returned value
        xpath: # Xpath to field in YANG model (without prefixes because return prefixes may differ)

Using Variables
---------------

You should think about the portability of your test. Using variables to refer
to parameters in the ``yang`` action will allow you to run the same set of tests
over different protocols by only changing a couple variables or changing the
file that contains your content. A variable can be defined by wrapping a YAML
location inside ``%{ my.variable }`` and find the value at my: variable: value.
The location can also exist in a different file by adding ``extends: mydata.yml``
at the top of the test file.


Example of variables in external data file:

.. code-block:: YAML

    extends: data_test_file.yml

    - yang:
        device: '%{ data.device }'
        connection: '%{ data.connection }'
        operation: edit-config
        protocol: '%{ data.protocol }'
        datastore: '%{ data.datastore }'
        banner: YANG EDIT-CONFIG MESSAGE
        content: '%{ data.content.1 }'


Content in data_test_file.yml:

.. code-block:: YAML

  data:
    device: uut1
    connection: gnmi
    protocol: gnmi
    content:
      1:
        namespace:
          ios-l2vpn: http://cisco.com/ns/yang/Cisco-IOS-XE-l2vpn
        nodes:
          - value: 10.10.10.2
            xpath: /native/l2vpn-config/ios-l2vpn:l2vpn/ios-l2vpn:router-id
            edit-op: merge


Examples
--------

- edit-config negative test using NETCONF

.. code-block:: YAML

    - yang:
        device: uut2
        connection: netconf
        operation: get-config
        protocol: netconf
        banner: NETCONF EDIT-CONFIG MESSAGE
        log: Negative test case
        format:
          auto-validate: false
          negative-test: true
        content:
          namespace:
            ios-l2vpn: http://cisco.com/ns/yang/Cisco-IOS-XE-l2vpn
          nodes:
          - xpath: /native/l2vpn-config/ios-l2vpn:l2vpn/ios-l2vpn:router-id
            value: '10.10.10.2'
            edit-op: delete
        returns:
          - id: 2
            name: router-id
            op: ==
            selected: true
            datatype: string
            value: 10.10.10.2
            xpath: /native/l2vpn-config/l2vpn/router-id


- Same edit-config using variables

.. code-block:: YAML

  extends: data_test_file.yml

    - yang:
        device: '%{ data.device }'
        connection: '%{ data.connection }'
        operation: edit-config
        protocol: '%{ data.protocol }'
        datastore: '%{ data.datastore }'
        format: '%{ data.format.1 }'
        banner: YANG EDIT-CONFIG MESSAGE
        content: '%{ data.contents.1 }'
        banner: NETCONF EDIT-CONFIG MESSAGE
        log: Negative test case


.. code-block:: YAML

  # data_test_file.yml contents

  data:
    device: uut2
    connection: netconf
    protocol:netconf
    datastore: candidate

    format:
      1:
        auto-validate: false
        negative-test: true
    contents:
      1:
        namespace:
            ios-l2vpn: http://cisco.com/ns/yang/Cisco-IOS-XE-l2vpn
        nodes:
        - xpath: /native/l2vpn-config/ios-l2vpn:l2vpn/ios-l2vpn:router-id
            value: '10.10.10.2'
            edit-op: delete
    returns:
      1:
        - id: 2
            name: router-id
            op: ==
            selected: true
            datatype: string
            value: 10.10.10.2
            xpath: /native/l2vpn-config/l2vpn/router-id


- get CONFIG state using gNMI with expected returns

.. code-block:: YAML

    - yang:
        device: uut2
        connection: gnmi
        operation: get-config
        protocol: gnmi
        banner: gNMI GET-CONFIG MESSAGE
        content:
          namespace:
            ios-l2vpn: http://cisco.com/ns/yang/Cisco-IOS-XE-l2vpn
          nodes:
          - xpath: /native/l2vpn-config/ios-l2vpn:l2vpn/ios-l2vpn:router-id
        returns:
          - id: 2
            name: router-id
            op: ==
            selected: true
            datatype: string
            value: 10.10.10.2
            xpath: /native/l2vpn-config/l2vpn/router-id
            

- gNMI subscribe testing a config change:

.. code-block:: YAML

    - configure:
        commmand:
          - l2vpn router-id 10.10.10.1
    - sleep:
        sleep_time: 5
    - yang:
        device: uut2
        connection: gnmi
        operation: subscribe
        protocol: gnmi
        banner: gNMI SUBCRIBE MESSAGE
        format:
          request_mode: STREAM
          sub_mode: SAMPLE
          encoding: JSON_IETF
          sample_interval: 5
          stream_max: 20       # test completes after 20 seconds
        content:
          namespace:
            ios-l2vpn: http://cisco.com/ns/yang/Cisco-IOS-XE-l2vpn
          nodes:
          - xpath: /native/l2vpn-config/ios-l2vpn:l2vpn/ios-l2vpn:router-id
        returns:
          - id: 2
            name: router-id
            op: ==
            selected: true
            datatype: string
            value: 10.10.10.2
            xpath: /native/l2vpn-config/l2vpn/router-id
    - sleep:
        sleep_time: 5
    # following event will trigger a returns check
    - configure:
        commmand:
          - l2vpn router-id 10.10.10.2
