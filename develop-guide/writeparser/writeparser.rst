
.. _write-parser:

##############
Write a parser
##############

This topic describes why and how to write your own parsers to meet your network automation requirements.

Remember to share your new parser with the rest of the |pyATS| user community! Please see the topic :ref:`contribute` for more information.

Heads up! This guide contains lots useful information and handy examples, which
also means that there's a lot to read before you can actually get to parts about coding a
parser. If you want to skip the reading and just get right to the fun stuff, then
by all means, skip ahead by clicking :ref:`here <regex-parser>`. We get it, it's cool.
Just be sure to read the rest of this guide before
contributing to the Genie parser repo. It will save you (and us) time in the end.

.. tip::
    If you're the kind of person who prefers to learn by video
    instead of reading about it, then please checkout these great videos
    about making pyATS parsers:

    - `How to write a Genie parser for Cisco! <https://youtu.be/ibLNilSfdTc>`_ - uploaded by `Juhi Mahajan <https://www.youtube.com/channel/UCA0EsjQEEJac9XIidC6v6Rg>`_
        - Juhi provides a good overview of parser creation process
    - `Creating a pyATS | Genie Parser from SCRATCH <https://youtu.be/knxkbWTamBY>`_ - uploaded by `Data Knox <https://www.youtube.com/channel/UCi7SD3zfCjkiDWvSFthIQSg>`_
        - Data Knox gives a full hands-on parser writing guide from start to finish


| 1. :ref:`What is a parser? <what_is_a_parser>`
| 2. :ref:`Why write a parser? <why_write_a_parser>`
| 3. :ref:`How the pyATS Library parsers work <how_the_parsers_work>`
| 4. :ref:`Setting up your development environment <setting_up_your_environment>`
| 5. :ref:`Writing the Schema Class <writing_the_schema_class>`
|   5.1 :ref:`Creating a schema <creating_a_schema>`
|     5.1.1. :ref:`Identifying keys directly from show command output <keys_from_show_command>`
|     5.1.2. :ref:`Identifying keys from XML output <keys_from_XML>`
|     5.1.3. :ref:`Identifying keys from the YANG data model <keys_from_YANG>`
|   5.2. :ref:`Creating a schema based on an existing model <schema_on_existing_model>`
|   5.3. :ref:`Explore other pyATS schemas <schemaexamples>`
| 6. :ref:`Writing the Parser Class <writing_the_parser_class>`
|   6.1. :ref:`Writing a parser class with RegEx <regex-parser>`
|   6.2. :ref:`Writing a parser class with the parsergen package <parsergen>`
| 7. :ref:`Testing your parser <testingyourparser>`
|   7.1. :ref:`Folder based testing <folder_based_testing>`
|   7.2. :ref:`Unittest based testing <unittest_based_testing>`
| 8. :ref:`Revising a parser <revising_a_parser>`
| 9. :ref:`Versioning a parser <versioning_a_parser>`
| 10. :ref:`Contributing your work to the pyATS project <contributing_your_work>`



.. _what_is_a_parser:

********************
1. What is a parser?
********************

.. include:: ../definitions/def_parser.rst
    :start-line: 3

* For a basic introduction to the |library| parsers, see the topic `Parse device output <https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/quickstart/parseoutput.html#parse-device-output>`_ in the *Get Started with pyATS* guide (recommended).
* For more information about the ``metaparser`` package, see the topic `Metaparser Package <https://pubhub.devnetcloud.com/media/genie-metaparser/docs/index.html#genie-metaparser-package>`_.


.. _why_write_a_parser:

**********************
2. Why write a parser?
**********************

The |library| provides you with many out-of-the box `parsers <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers>`_ for use with the most frequently-used Cisco show commands and OS/platform combinations.

But if you want to modify a parser, make a new parser, or if you need to parse output for a feature that does not yet have a |library| model, you can easily write your own parser.


.. _how_the_parsers_work:

*********************************
3. How the |library| parsers work
*********************************

A parser is composed of two Python classes:

- :ref:`Schema class <writing_the_schema_class>`
- :ref:`Parser class <writing_the_parser_class>`

| Each schema defines:
|   1. What the structure of the parsed data will be.
|   2. The data types used for the key-value pairs in the parsed output.


| Each parser performs four main actions:
|   1. Run a show command and collect the device output.
|   2. Define patterns that will be looked for in the device output.
|   3. Iterate through each line of the device output data.
|   4. Look for patterns in the output and add any matching patterns to a Python dictionary.

Using these classes together results in output that is standardized
and reliably structured. This is crucial for network automation
scripts to work across different types of OS's and communication
protocols.

Later sections will describe this process in more detail and multiple examples
will be provided.


.. _setting_up_your_environment:

******************************************
4. Setting up your development environment
******************************************

If this is your first time writing a pyATS parser or if you're looking for an easy way
to jump right into things, then start here. This section will outline how to
easily set up a development environment that can be used for writing a parser.

| Things you'll need before starting:
|   - Python 3.6 (or newer)
|   - pip (inlcuded with Python)
|   - git

#. `Fork <https://docs.github.com/en/github/getting-started-with-github/fork-a-repo>`_ the https://github.com/CiscoTestAutomation/genieparser repo.

   .. image:: ../images/fork_repo.png



#. Create a python virtual environment, activate it, and install pyATS into it.

   .. code-block:: python

    $ python -m venv <directory_of_your_choice>
    $ source <directory_of_your_choice>/bin/activate
    $ pip install pyats[full]

#. Once the installation has finished, clone your ``genieparser`` repo (replace ``YOUR_USERNAME`` with your Gihub account username) and run ``make develop`` to get your environment ready to work in.

   .. code-block:: python

    $ git clone https://github.com/<YOUR_USERNAME>/genieparser
    $ cd genieparser
    $ make develop


At this point, you are now ready to start writing your parser, but if you'd
like to follow along with some of the examples in this guide, then
follow these next few steps to set up a mock network environment.
First, :download:`download the zip file <mock_parser.zip>` and extract the contents
to a directory of your choice, such as :monospace:`mock_parser`. It's recommended
to use a separate terminal for your mock network operations.

#. Go to the directory that contains the extracted files::

    $ cd mock_parser
    $ python

#. In your Python interpreter, load the :term:`Testbed YAML file`, and connect to a device.

   .. code-block:: python

    from genie.testbed import load
    testbed = load('mock_parser.yaml')
    dev = testbed.devices['iosxe1']
    dev.connect()

   .. note:: Ignore the prompt to continue to connect.

Now that you have your development environment and mock network set up,
it's time to get programming!

.. _writing_the_schema_class:

***************************
5. Writing the Schema Class
***************************

A good schema is one of the most crucial
(and in some cases, most challenging) aspects of creating a parser.
It's where you must examine the output from a device
and determine what information is important and how that information should be
structured. In pyATS, a schema is used to define all of the key-value pairs that will
be stored in a Python dictionary. This dictionary is what will contain all of
the output from our parser.

If you intend to contribute your parser to the pyATS project, then you must
build and implement a schema class as it results in the following benefits:

* *Time-saving*: You can quickly see the data structure without having to read hundreds of lines of regex output. This saves you time when troubleshooting.
* *Future-proof* and *robust*: When you or others modify code, you're less likely to break something.
* *Scalable*: It's more efficient to modify a schema than to have multiple developers working with just the regex output.


.. _creating_a_schema:

5.1 Creating a schema
=====================

This section covers the making of your own new schema.

To start creating a new schema, you'll first need to gather device output.
Once you have some, you can identify the keys that you'll need in a number of ways, including:

| :ref:`5.1.1<keys_from_show_command>` Examining the ``show`` command output directly.
| :ref:`5.1.2<keys_from_XML>` Using the XML output option with a ``show`` command to display the output as key-value pairs.
| :ref:`5.1.3<keys_from_YANG>` Using the YANG data model to identify the relevant keys.

.. note:: You can also :ref:`create a schema based on an existing model <schemabasedonanexistingmodel>`

.. tip:: You can find more examples of schemas :ref:`here <schemaexamples>`


.. _keys_from_show_command:

5.1.1 Identifying keys directy from show command output
-------------------------------------------------------

Writing a schema based on device output can range from straightforward to
surprisingly complex. Having multiple examples of device output for a given
command can be incredibly helpful when designing a schema.

For example, the output from the ``show track`` command for IOSXE can look like
this:

.. code-block::

    Track 1
    Interface GigabitEthernet3.420 line-protocol
    Line protocol is Up
        1 change, last change 00:00:27
    Tracked by:
        VRRP GigabitEthernet3.420 10

Or it can look like this:

.. code-block::

    Track 2
    IP route 10.21.12.0 255.255.255.0 reachability
    Reachability is Down (no ip route), delayed Up (1 sec remaining) (connected)
        1 change, last change 00:00:24
    Delay up 20 secs, down 10 secs
    First-hop interface is unknown (was Ethernet1/0)
    Tracked by:
        HSRP Ethernet0/0 3
        HSRP Ethernet0/1 3

Or even this:

.. code-block::

    Track 1
    IP route 172.16.52.0 255.255.255.0 metric threshold
    Metric threshold is Down (no route)
        1 change, last change 00:00:35
    Metric threshold down 255 up 254
    Delay up 2 secs, down 1 sec
    First-hop interface is unknown

Comparing these three outputs reveals a lot about the structure of the information
given by that particular show command. Using these output examples, a schema that
looks like this can be created:

.. code-block:: python

    class ShowTrackSchema(MetaParser):
        """ Schema for 'show track' """
        schema = {
            'type': {
                Any(): {
                    Optional('name'): str,
                    Optional('address'): str,
                    Optional('mask'): str,
                    'state': str,
                    Optional('state_description'): str,
                    Optional('delayed'): {
                        Optional('delayed_state'): str,
                        Optional('secs_remaining'): float,
                        Optional('connection_state'): str,
                    },
                    'change_count': int,
                    'last_change': str,
                    Optional('threshold_down'): int,
                    Optional('threshold_up'): int,
                },
            },
            Optional('delay_up_secs'): float,
            Optional('delay_down_secs'): float,
            Optional('first_hop_interface_state'): str,
            Optional('prev_first_hop_interface'): str,
            Optional('tracked_by'): {
                Optional(Any()): {   #increasing index 0, 1, 2, 3, ...
                    Optional('name'): str,
                    Optional('interface'): str,
                    Optional('group_id'): str,
                }
            },
        }

If you want to jump ahead and see what the parsed output is when using this
schema, then click :ref:`here <golden_output_example>`.
The file that contains the above ShowTrackSchema class can be found `here <https://github.com/CiscoTestAutomation/genieparser/blob/master/src/genie/libs/parser/iosxe/show_track.py>`_.

In the above schema example, you can see the use of two schema subclasses; ``Any`` and ``Optional``.
As you might expect, ``Any`` is used to match anything and is often used in larger
or more complicated schemas. ``Optional`` is used to indicate that a key may or
may not exist in the device output.

There are other helpful subclasses that can be used in the creation of your schema such as ``Default``, ``And``,
and ``Or``. Visit the `Schema Engine Documentation <https://pubhub.devnetcloud.com/media/genie-metaparser/docs/advanced/schemaengine.html#other-types-of-schema>`_ to read more about them and how to use them.


Generate mock device output
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow the mock device example below to generate some sample device output for yourself,
examine output indentation behaviour, see how you might want
to group data into containers, and use the Python's pretty print module.

#. Get some device out put by executing the ``show interfaces`` command in your mock exmaple.

   .. code-block:: python

    dev.execute('show interfaces')

   *Result*: The system displays the unparsed output. The following example shows some of the output that you can use to identify keys for your parser::

    GigabitEthernet1 is up, line protocol is up
        Hardware is CSR vNIC, address is 0800.2729.3800 (bia 0800.2729.3800)
        Internet address is 10.0.2.15/24
        MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec,
            reliability 255/255, txload 1/255, rxload 1/255
        Encapsulation ARPA, loopback not set
        Keepalive set (10 sec)
        Full Duplex, 1000Mbps, link type is auto, media type is Virtual
        output flow-control is unsupported, input flow-control is unsupported
        ARP type: ARPA, ARP Timeout 04:00:00
        Last input 00:00:00, output 00:00:00, output hang never
        Last clearing of "show interface" counters never
        ...
    ...


#. Check the indentation in the output. The indentation tells you about the parent-child relationship of the keys.

   .. note:: Remember to use the indentation (parent-child relationships) to ensure that values don't overwrite other values at the same level. In the following example, the keys for :monospace:`interface_name` are indented so that the :monospace:`mac_address` value for Interface1 won't be overwritten by the :monospace:`mac_address` value for Interface2.

   Your schema might begin with the following lines:

   .. code-block:: python

        'interfaces': {
            Any(): {                  # GigabitEthernet1
                'oper_status': str,   # up
                'line_protocol': str, # up
                'hardware': str,      # CSR vNIC
                'mac_address': str,   # 0800.2729.3800
                ...
            ...


#. You can also check for ways to group the data based on counters, input and output, as well as other statistics. For the following output:

   .. code-block::

        4243 packets input, 361948 bytes, 0 no buffer
        Received 0 broadcasts (0 IP multicasts)
        0 runts, 0 giants, 0 throttles
        0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
        0 watchdog, 0 multicast, 0 pause input
        3616 packets output, 1637917 bytes, 0 underruns
        0 output errors, 0 collisions, 0 interface resets
        0 unknown protocol drops
        0 babbles, 0 late collision, 0 deferred
        0 lost carrier, 0 no carrier, 0 pause output
        0 output buffer failures, 0 output buffers swapped out

   Your schema could be::

    'counters': {  # categorize the value as 'counters'
        'input': {   # categorize the 'input' related values
            'packets': int,
            'bytes': int,

        },
        'output': {
            'packets': int,
            'bytes': int,
        }

#. To see the output with a more readable structure, you can use Python's "pretty-print" module:

   .. code-block:: python

    output = dev.parse('show interfaces')
    import pprint
    pprint.pprint(output)

   *Result*: The following snippet shows the output formatted so that it's easier to read::

    {'GigabitEthernet1': {'arp_timeout': '04:00:00',
                      'arp_type': 'arpa',
                      'auto_negotiate': True,
                      'bandwidth': 1000000,
                      'counters': {'in_broadcast_pkts': 0,
                                   'in_crc_errors': 0,
                                   'in_errors': 0,
                                   'in_frame': 0,



.. _keys_from_XML:

5.1.2 Identifying keys from XML output
--------------------------------------

NXOS device ``show`` commands have an XML option that formats the output as key-value pairs. If you have an IOSXE or IOSXR device, you can usually find a similar NXOS command to run so that you can see the XML output:

.. code-block:: text

 nx-osv9000-1# show interface | xml

*Result*::

    <?xml version="1.0" encoding="ISO-8859-1"?>
    <nf:rpc-reply xmlns="http://www.cisco.com/nxos:1.0:if_manager" xmlns:nf="urn:iet
    f:params:xml:ns:netconf:base:1.0">
    <nf:data>
    <show>
    <interface>
        <__XML__OPT_Cmd_show_interface_quick>
        <__XML__OPT_Cmd_show_interface___readonly__>
        <__readonly__>
        <TABLE_interface>
            <ROW_interface>
            <interface>mgmt0</interface>
            <state>up</state>
            <admin_state>up</admin_state>
            <eth_hw_desc>Ethernet</eth_hw_desc>
            <eth_hw_addr>5e01.c005.0000</eth_hw_addr>
            <eth_bia_addr>5e01.c005.0000</eth_bia_addr>
            <eth_ip_addr>10.0.0.0</eth_ip_addr>

In this example, your schema could include the keys :monospace:`state`, :monospace:`admin_state`, :monospace:`eth_hw_desc`, and others.


.. _keys_from_YANG:

5.1.3 Identifying keys from the YANG data model
-----------------------------------------------

#. Install the ``pyang`` package in your virtual environment::

    pip install pyang

#. Clone the git repository for the YANG model::

    git clone https://github.com/YangModels/yang.git

#. Look for the latest model. (At the time of writing, this is |br| :monospace:`./yang/experimental/ietf-extracted-YANG-modules/ietf-arp@2019-11-04.yang`)::

    find . | grep ietf-arp

#. View the model and identify the keys::

    pyang -f tree ./yang/experimental/ietf-extracted-YANG-modules/ietf-arp@2019-11-04.yang

   *Result*: You can see the YANG model with the keys and data types::

     module: ietf-arp
        +--rw arp
            +--rw dynamic-learning?   boolean

        augment /if:interfaces/if:interface/ip:ipv4:
            +--rw arp
            +--rw expiry-time?        uint32
            +--rw dynamic-learning?   boolean
            +--rw proxy-arp
            |  +--rw mode?   enumeration
            +--rw gratuitous-arp
            |  +--rw enable?     boolean
            |  +--rw interval?   uint32
            +--ro statistics
                +--ro in-requests-pkts?      yang:counter32
                +--ro in-replies-pkts?       yang:counter32
                +--ro in-gratuitous-pkts?    yang:counter32
                +--ro out-requests-pkts?     yang:counter32
                +--ro out-replies-pkts?      yang:counter32
                +--ro out-gratuitous-pkts?   yang:counter32
        augment /if:interfaces/if:interface/ip:ipv4/ip:neighbor:
            +--ro remaining-expiry-time?   uint32


.. _schema_on_existing_model:

5.2 Creating a schema based on an existing model
================================================

Check Genie Model to check if the parser feature you are working on has a Model: Genie Models

    Check the Model Ops structure
    Create the Parser Schema to be as close as possible to the Genie Model Ops Structure

If you want to create a new schema, you can base it on the keys for an existing feature.

#. In a web browser, go to the `list of models <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/models>`_ on which you can base a new parser schema.

#. For this example, select **interface**, and then select **MODEL** to open a PDF file that contains the interface model.

#. Navigate to the **Interface Ops structure** section.

   .. image:: ../images/ops_structure.png
      :scale: 40 %

   |br|  *Result*: The ops structure lists the keys that you can use to create your own parser schema. |br|

#. In a text editor, define the schema class, and then add the keys that you want your parser to return, as shown in the following example of part of a schema definition. Use JSON format and save the file as a :monospace:`*.py` file.

   .. code-block:: python

    class ShowInterfacesSchema(MetaParser):
    """schema for show interfaces
                  show interfaces <interface>"""

    schema = {
            Any(): {
                'oper_status': str,
                Optional('line_protocol'): str,
                'enabled': bool,
                Optional('connected'): bool,
                Optional('description'): str,
                'type': str,


   .. note:: You must specify the value type, such as integer, float, string, boolean, or list.

   You can see `the complete parser file on GitHub <https://github.com/CiscoTestAutomation/genieparser/blob/master/src/genie/libs/parser/iosxe/show_interface.py#L178>`_.


.. _schemaexamples:

5.3 Explore other pyATS schemas
===============================

If you want to do some exploration of existing schemas, or if you
want to see more schema examples to help with the creation of your own,
then go check out all of the available parsers on the `Parsers List
website
<https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers>`_!

1. At the top of the page, search for a show command, such as :monospace:`show interfaces`.
2. Select an OS, in this example, **IOSXE**.
3. Select **show interfaces**, and then scroll down to the IOSXE schema. The following illustration shows part of the schema.

.. image:: ../images/schema_example.png
    :align: center
    :scale: 70 %


|
|

.. _writing_the_parser_class:

***************************
6. Writing the Parser Class
***************************

The |library| parsers look for specific patterns in the device output and then structure the output as a set of key-value pairs. When you write a parser, you specify the patterns that you want the parser to match. For example, the ``show interfaces`` parser looks for patterns and returns the information as a set of key-value pairs, as shown in the following example of a section of parsed output::

 {
  "GigabitEthernet1": {
    "arp_timeout": "04:00:00",
    "arp_type": "arpa",
    "auto_negotiate": true,
    "bandwidth": 1000000,

There are two main ways to write the parser class:

#. :ref:`Writing a parser class with regular expressions. <regex-parser>`
#. :ref:`Writing a parser class with the parsergen package. <parsergen>`

Most of the parsers in the pyATS parser library are written using regular
expressions. It's a little more work to write regexes for each piece of
data, but it offers excellent control for pattern matching and for assigning
the right values to the right keys in the right way.

The |library| parsers use regular expressions (regex) to match patterns in the device output. Regexes are the backbone of all parsers, so you must know how to use them before you can write a parser.

The following references provide detailed information about how to use regular expressions:

* https://www.learnpython.org/en/Regular_Expressions
* https://regexone.com/references/python
* https://www.dataquest.io/blog/regex-cheatsheet/

The following online tools can help you build and test Python regular expressions:

* https://pythex.org/
* https://regex101.com/

.. note:: The |library| standard parsers use regular expressions for scalability. You can, however, write a parser that uses any of the following tools:

  * `TextFSM <https://github.com/google/textfsm/wiki/TextFSM>`_
  * `Template Text Parser (TTP) <https://ttp.readthedocs.io/en/latest/>`_
  * :ref:`Parsergen <parsergen>`


.. _regex-parser:

6.1 Writing a parser class with RegEx
=====================================

When you write a new parser class, you can define the regular expressions used to match patterns in the device output. The parser adds the matched patterns as key-value pairs to a Python dictionary. The parser class inherits from the schema class to ensure that the resulting Python dictionary exactly follows the format of the defined schema.

The following example shows a schema and parser class for the ``show lisp session`` command. As you can see, the schema and parser classes are defined in the same Python file. Take a look at the example, and then we'll explain how it works.

.. code-block:: python

    # Metaparser
    from genie.metaparser import MetaParser
    from genie.metaparser.util.schemaengine import Any, Or, Optional

    # ==============================
    # Schema for 'show lisp session'
    # ==============================
    class ShowLispSessionSchema(MetaParser):

        ''' Schema for "show lisp session" '''

    # These are the key-value pairs to add to the parsed dictionary
        schema = {
            'vrf': {
                Any(): {
                    'sessions': {
                        'total': int,
                        'established': int,
                        'peers': {
                            Any(): {
                                'state': str,
                                'time': str,
                                'total_in': int,
                                'total_out': int,
                                Optional('users'): int,
                            }
                        }
                    }
                }
            }
        }

    # Python (this imports the Python re module for RegEx)
    import re

    # ==============================
    # Parser for 'show lisp session'
    # ==============================

    # The parser class inherits from the schema class
    class ShowLispSession(ShowLispSessionSchema):

        ''' Parser for "show lisp session"'''

        cli_command = 'show lisp session'

        # Defines a function to run the cli_command
        def cli(self, output=None):
            if output is None:
                out = self.device.execute(self.cli_command)
            else:
                out = output

            # Initializes the Python dictionary variable
            parsed_dict = {}

            # Defines the regex for the first line of device output, which is:
            # Sessions for VRF default, total: 3, established: 3
            p1 = re.compile(r'Sessions +for +VRF +(?P<vrf>(\S+)),'
                            ' +total: +(?P<total>(\d+)),'
                            ' +established: +(?P<established>(\d+))$')

            # Defines the regex for the next line of device output, which is:
            # Peer                           State      Up/Down        In/Out    Users
            # 2.2.2.2                        Up         00:51:38        8/13     3
            p2 = re.compile(r'(?P<peer>(\S+)) +(?P<state>(Up|Down)) +(?P<time>(\S+))'
                            ' +(?P<in>(\d+))\/(?P<out>(\d+)) +(?P<users>(\d+))$')

            # Defines the "for" loop, to pattern match each line of output
            for line in out.splitlines():
                line = line.strip()

                # Processes the matched patterns for the first line of output
                # Sessions for VRF default, total: 3, established: 3
                m = p1.match(line)
                if m:
                    group = m.groupdict()
                    vrf = group['vrf']
                    vrf_dict = parsed_dict.setdefault('vrf', {}).\
                                setdefault(vrf, {}).setdefault('sessions', {})
                    vrf_dict['total'] = int(group['total'])
                    vrf_dict['established'] = int(group['established'])
                    continue

                # Processes the matched patterns for the second line of output
                # Peer                           State      Up/Down        In/Out    Users
                # 2.2.2.2                        Up         00:51:38        8/13     3
                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    peer = group['peer']
                    peer_dict = vrf_dict.setdefault('peers', {}).setdefault(peer, {})
                    peer_dict['state'] = group['state'].lower()
                    peer_dict['time'] = group['time']
                    peer_dict['total_in'] = int(group['in'])
                    peer_dict['total_out'] = int(group['out'])
                    peer_dict['users'] = int(group['users'])
                    continue

            return parsed_dict

The following table describes the structure of the parser class in more detail.

.. csv-table:: Structure of a parser class
   :file: parser_class_structure.csv
   :header-rows: 1
   :widths: 48 52

For consistency and compatibility when an interface name is parsed in its shortened form
it should be converted to a standard format.
The easiest way to accomplish this is with use of the Common library, found in /genie/parser/utils/common.py.

.. code-block:: python

    # take the example of a Ten Gigabit Ethernet port. When parsed out it may look like this:
    >>> interface_name = "Te0/0/1"

    # for consistency and compatibility we want to convert this to be a standardized name.
    >>> from genie.libs.parser.utils.common import Common
    >>> interface_name
    'Te0/0/1'

    >>> converted_name = Common.convert_intf_name(interface_name)
    >>> converted_name
    'TenGigabitEthernet0/0/1'


.. note:: You need to know the patterns that you want to match before you write the parser class. These patterns can be some or all of the keys defined in the schema class.

.. _parsergen:

6.2 Writing a parser class with the parsergen package
=====================================================

The |library| ``parsergen`` package provides a one-step parsing mechanism that can parse dynamic tabular and non-tabular device output. The ``parsergen`` produces significantly fewer lines of code than standard parsing mechanisms.

The ``parsergen`` package is a generic parser for show commands. You can use the package to create a parser class for any given show command, and then reuse your new class to create tests for the output values.

Using ``parsergen`` to create a parser class is particularly useful when you don't have a |library| model for a feature. In this example, we'll create a new parser class for the VXLAN related parser.

#. In a Python interpreter, import the required |library| and Python functionality (``re`` is the Python regex functionality):

   .. code-block:: python

    import re
    from pprint import pprint
    from genie.testbed import load
    from genie import parsergen

#. Load the testbed, create the device object, and connect to the device:

   .. code-block:: python

     testbed = load('mock_parser.yaml')
     dev = testbed.devices['iosxe1']
     dev.connect()

#. Execute the show command and store the output in the variable ``output``:

   .. code-block:: python

    output = dev.execute('show nve vni')

   *Result*: You can see the tabular output::

    Interface  VNI        Multicast-group VNI state  Mode  BD    cfg vrf
    nve1       6010       N/A             Up         L2DP  1     CLI N/A
    nve2       6020       N/A             Up         L2DP  2     CLI N/A
    nve3       6030       N/A             Up         L2DP  3     CLI N/A

#. Define a variable ``header`` that contains the list of header names from the table. The names must exactly match the output:

   .. code-block:: python

    header = ['Interface', 'VNI', 'Multicast-group', 'VNI state', 'Mode', 'BD', 'cfg', 'vrf']

#. Use ``parsergen`` to parse the output, where index 0 is the :monospace:`Interface` column header. This process creates a Python dictionary of operational statistics per interface:

   .. code-block:: python

    result = parsergen.oper_fill_tabular(device_output=output, device_os='iosxe', header_fields=header, index=[0])

#. Print the value of the ``result`` object that contains the dictionary:

   .. code-block:: python

    pprint(result.entries)

   *Result*: Easy-to-read and easy-to-automate structured data:

   .. code-block:: text

    {'nve1': {'BD': '1',
            'Interface': 'nve1',
            'Mode': 'L2DP',
            'Multicast-group': 'N/A',
            'VNI': '6010',
            'VNI state': 'Up',
            'cfg': 'CLI',
            'vrf': 'N/A'},
    'nve2': {'BD': '2',
            'Interface': 'nve2',
            'Mode': 'L2DP',
            'Multicast-group': 'N/A',
            'VNI': '6020',
            'VNI state': 'Up',
            'cfg': 'CLI',
            'vrf': 'N/A'},
    'nve3': {'BD': '3',
            'Interface': 'nve3',
            'Mode': 'L2DP',
            'Multicast-group': 'N/A',
            'VNI': '6030',
            'VNI state': 'Up',
            'cfg': 'CLI',
            'vrf': 'N/A'}}

.. tip:: You can run all of these commands as a script. :download:`Download the attached zip file <parsergen_script.zip>`, extract the file to a directory of your choice, cd to that directory, and then run the following command::

   (pyats) $ python parsergen_script.py

|
|

.. _testingyourparser:

**********************
7. Testing your parser
**********************

Now that you've finished writing your parser, the time has come to test it!

There are currently two types of tests, those being Folder Based and Unittest Based.
The testing strategy is currently in a state of transition.
Moving to folder based testing helps us avoid merge conflicts and duplicate boilerplate code
while ensuring tests are faster and easier create and use.
When creating tests for a new parser do so in the Folder Based style.

:ref:`Folder based testing <folder_based_testing>` is currently completed for:

  * ASA
  * IOS
  * IOSXE
  * IOSXR
  * JUNOS

All other OS's are in transition from :ref:`unittest based testing <unittest_based_testing>`.

.. important::
    If you want to contribute your new parser to the open-source |pyATS| feature
    libraries and components, you must attach Folder Based testing results for each parser
    that you want to contribute.


Make JSON
=========

Before we can run any tests, we need to incorporate your new parser into the pyATS
``genie.libs.parser`` package using the `make json` command.

The `make json` command makes it easy to let pyATS know about how to use your new
parser. Simply navigate to the root directory of the genieparser repo and execute
`make json`.

.. code-block:: bash

    .../genieparser$ make json

`make json` will then create/update a json file which will link commands to
their related class.
This json file will be used when device.parse is executed in order to find
the correct parser class based on the given command.

.. attention::
    Remember to execute `make json` every time you create a new parser!
    Without `make json`, device.parse will not be able to find the parser class
    and you'll end up with a ``Could not find parser`` error when trying to test
    your parser.

|

**Try your parser on a real device**

If possible, it is recommended to run your parser on a real device to make sure
that you get the expected parsed output. The following example shows how to do
this in pure Python:

.. code-block:: python

 from genie.testbed import load
 tb = load('yourtestbed.yaml')
 dev = tb.devices['uut']
 dev.connect()
 parsed_output = dev.parse('show inventory')


|
.. _folder_based_testing:

7.1 Folder based testing (ASA, IOS, and IOSXE)
==============================================

To create a folder based test with cli based output, follow these simple tests.

  * Create a folder in the tests directory named exactly the same as the class name in the respective folder.

    * As an example, the code `class ShowClock(ShowClockSchema)` would point you to creating a folder called `ShowClock`.
    * The `tests` directory is a OS specific folder such as `src/genie/libs/parser/iosxe/tests/`.

  * Create a folder within the class name directory called `cli`.

    * e.g. `src/genie/libs/parser/iosxe/tests/ShowClock/cli`.
  * Create folders for `empty` and `equal` within the `cli` folder.

    * e.g. `src/genie/libs/parser/iosxe/tests/ShowClock/cli/empty`.
    * e.g. `src/genie/libs/parser/iosxe/tests/ShowClock/cli/equal`.
  * Within the `empty` folder create a file that ends with `_output.txt`

    * e.g. `src/genie/libs/parser/iosxe/tests/ShowClock/cli/empty/empty_output.txt`.
    * This file should be either empty or partial output that will not raise a `SchemaEmptyParserError` error.
  * Within the `equal` folder create the raw output, expected value, and potential arguments.

    * The files are grouped together by stripping `_output.txt`, `_expected.py`, and `_arguments.json` and comparing the names that match.

      * As an example `golden_output1_arguments.json`, `golden_output1_expected.py`, and `golden_output1_output.txt` are understood to be part of the same test.
    * The output file, should be a simple txt file with the expected output.
    * The expected Python file, should be a Python file with a single variable called `expected_output` that has the expected data structure.
    * The arguments JSON file, should be a single dictionary that is a set of key/value pairs.
  * Repeat this process for as many tests outputs you would like to verify, meaning you are not limited to a single test per command. This is helpful when output may be different based on any number of conditions.

Following that process, you should end up with a folder structure that looks similar to:

.. code-block:: bash

    ShowClock
    └── cli
        ├── empty
        │   └── empty_output_output.txt
        └── equal
            ├── golden_output_expected.py
            └── golden_output_output.txt

    4 directories, 3 files

Ideally, this entire process once known, should only take a few seconds to create files and a few minutes to populate those files. For testing purposes you can run the tests locally. You can either run all tests, run a single OS tests, or run a single command tests for a single OS, as shown below from *within the tests folder*.

.. code-block:: bash

    .../genieparser/tests$ python folder_parsing_job.py
    .../genieparser/tests$ python folder_parsing_job.py -o iosxe
    .../genieparser/tests$ python folder_parsing_job.py -o iosxe -c ShowClock

The output will show you the something similar, which will provide the `PASSED` and `FAILED` results.

.. code-block:: bash

    .../genieparser/tests$ python folder_parsing_job.py -o iosxe -c ShowClock
    <cut for brevity>
    2020-09-19T16:14:17: %AETEST-INFO: |                               Detailed Results                               |
    2020-09-19T16:14:17: %AETEST-INFO: +------------------------------------------------------------------------------+
    2020-09-19T16:14:17: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT
    2020-09-19T16:14:17: %AETEST-INFO: --------------------------------------------------------------------------------
    2020-09-19T16:14:17: %AETEST-INFO: .
    2020-09-19T16:14:17: %AETEST-INFO: `-- FileBasedTest                                                         PASSED
    2020-09-19T16:14:17: %AETEST-INFO:     `-- check_os_folder[operating_system=iosxe]                           PASSED
    2020-09-19T16:14:17: %AETEST-INFO:         |-- Step 1: iosxe -> ShowClock                                    PASSED
    2020-09-19T16:14:17: %AETEST-INFO:         |-- Step 1.1: Test Golden -> iosxe -> ShowClock                   PASSED
    2020-09-19T16:14:17: %AETEST-INFO:         |-- Step 1.1.1: Gold -> iosxe -> ShowClock -> golden_output       PASSED
    2020-09-19T16:14:17: %AETEST-INFO:         |-- Step 1.2: Test Empty -> iosxe -> ShowClock                    PASSED
    2020-09-19T16:14:17: %AETEST-INFO:         `-- Step 1.2.1: Empty -> iosxe -> ShowClock -> empty_output       PASSED
    2020-09-19T16:14:17: %AETEST-INFO: +------------------------------------------------------------------------------+
    2020-09-19T16:14:17: %AETEST-INFO: |                                   Summary                                    |
    2020-09-19T16:14:17: %AETEST-INFO: +------------------------------------------------------------------------------+
    2020-09-19T16:14:17: %AETEST-INFO:  Number of ABORTED                                                            0
    2020-09-19T16:14:17: %AETEST-INFO:  Number of BLOCKED                                                            0
    2020-09-19T16:14:17: %AETEST-INFO:  Number of ERRORED                                                            0
    2020-09-19T16:14:17: %AETEST-INFO:  Number of FAILED                                                             0
    2020-09-19T16:14:17: %AETEST-INFO:  Number of PASSED                                                             1
    2020-09-19T16:14:17: %AETEST-INFO:  Number of PASSX                                                              0
    2020-09-19T16:14:17: %AETEST-INFO:  Number of SKIPPED                                                            0
    2020-09-19T16:14:17: %AETEST-INFO:  Total Number                                                                 1
    2020-09-19T16:14:17: %AETEST-INFO:  Success Rate                                                            100.0%
    2020-09-19T16:14:17: %AETEST-INFO: --------------------------------------------------------------------------------
    root@197979f5dbd6:/genieparser/tests$


.. _golden_output_example:

Golden output example files
---------------------------

In section  :ref:`5.1.1 <keys_from_show_command>`, there are examples of the output from the ``show track``
command for IOSXE. Below is what the parsed output from one of those
examples looks like. You can explore these test files yourself by
clicking `here <https://github.com/CiscoTestAutomation/genieparser/tree/master/src/genie/libs/parser/iosxe/tests/ShowTrack/cli/equal>`_.

So, given this device output in ``golden_output1_output.txt``,

.. code-block:: python

  Track 2
    IP route 10.21.12.0 255.255.255.0 reachability
    Reachability is Down (no ip route), delayed Up (1 sec remaining) (connected)
      1 change, last change 00:00:24
    Delay up 20 secs, down 10 secs
    First-hop interface is unknown (was Ethernet1/0)
    Tracked by:
      HSRP Ethernet0/0 3
      HSRP Ethernet0/1 3

the expected output from the parser in ``golden_output1_expected.py`` would be:

.. code-block:: python

    expected_output = {
        'type': {
            'IP route': {
                'address': '10.21.12.0',
                'mask': '255.255.255.0',
                'state': 'Down',
                'state_description': 'no ip route',
                'delayed': {
                    'delayed_state': 'Up',
                    'secs_remaining': 1.0,
                    'connection_state': 'connected',
                },
                'change_count': 1,
                'last_change': '00:00:24',
            }
        },
        'delay_up_secs': 20.0,
        'delay_down_secs': 10.0,
        'first_hop_interface_state': 'unknown',
        'prev_first_hop_interface': 'Ethernet1/0',
        'tracked_by': {
            1: {
                'name': 'HSRP',
                'interface': 'Ethernet0/0',
                'group_id': '3'
            },
            2: {
                'name': 'HSRP',
                'interface': 'Ethernet0/1',
                'group_id': '3'
            }
        }
    }

|

.. _unittest_based_testing:

7.2 Unittest based testing
==========================

The old testing strategy leverages unittest. The `Python unittest.mock library <https://docs.python.org/3/library/unittest.mock.html>`_ returns mock device output. Use your parser class to parse the mock data and return a Python dictionary that contains the results.

The following example shows how to create a unit test file for :ref:`the show lisp session example <regex-parser>`.

.. code-block:: python

    # Import the Python mock functionality
    import unittest
    from unittest.mock import Mock

    # pyATS
    from pyats.topology import Device
    from pyats.topology import loader

    # Metaparser
    from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

    # iosxe show_lisp
    from genie.libs.parser.iosxe.show_lisp import ShowLispSession

    # =================================
    # Unit test for 'show lisp session'
    # =================================
    class test_show_lisp_session(unittest.TestCase):

        '''Unit test for "show lisp session"'''

        empty_output = {'execute.return_value': ''}

        # Specify the expected result for the parsed output
        golden_parsed_output1 = {
            'vrf':
                {'default':
                    {'sessions':
                        {'established': 3,
                        'peers':
                            {'2.2.2.2':
                                {'state': 'up',
                                'time': '00:51:38',
                                'total_in': 8,
                                'total_out': 13,
                                'users': 3},
                            '6.6.6.6':
                                {'state': 'up',
                                'time': '00:51:53',
                                'total_in': 3,
                                'total_out': 10,
                                'users': 1},
                            '8.8.8.8':
                                {'state': 'up',
                                'time': '00:52:15',
                                'total_in': 8,
                                'total_out': 13,
                                'users': 3}},
                        'total': 3},
                    },
                },
            }

        # Specify the expected unparsed output
        golden_output1 = {'execute.return_value': '''
            204-MSMR#show lisp session
            Sessions for VRF default, total: 3, established: 3
            Peer                           State      Up/Down        In/Out    Users
            2.2.2.2                        Up         00:51:38        8/13     3
            6.6.6.6                        Up         00:51:53        3/10     1
            8.8.8.8                        Up         00:52:15        8/13     3
            '''}

        def test_show_lisp_session_full1(self):
            self.maxDiff = None
            self.device = Mock(**self.golden_output1)
            obj = ShowLispSessionNew(device=self.device)
            parsed_output = obj.parse()
            self.assertEqual(parsed_output, self.golden_parsed_output1)

        def test_show_lisp_session_empty(self):
            self.maxDiff = None
            self.device = Mock(**self.empty_output)
            obj = ShowLispSessionNew(device=self.device)
            with self.assertRaises(SchemaEmptyParserError):
                parsed_output = obj.parse()

    if __name__ == '__main__':
    unittest.main()

To create your own unit test, complete the following steps.

#. Make sure to save your parser file in the directory for the device OS::

   /genie/libs/parser/iosxe/show_lisp.py

   .. note::
   The idea where adding your parser is, if show command is ``show lisp <something>``,
   add to `show_lisp.py`. So that we can easily find the parser code based on file name.

#. Open a new text file, and save it in the :monospace:`tests` folder for the OS.

#. In this new file, import the functionality shown in the example. Also, import your new parser class. In this example, :monospace:`show_lisp` is the parser file and :monospace:`ShowLispSessionNew` is the new parser class:

   .. code-block:: python

    import unittest
    from unittest.mock import Mock
    from ats.topology import Device
    from ats.topology import loader
    from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError
    from genie.libs.parser.iosxe.show_lisp import ShowLispSession

#. Define the expected parsed and unparsed output. We refer to this as the "golden" output.

#. Define the tests as shown in the example, and use your new parser class name for the ``obj`` variable.

#. Execute the tests:

    .. code-block:: bash

        python test_show_lisp.py -v

   *Result*:

   .. image:: ../images/unit_test_results.png


#. After you push your parser code to your branch, GitHub Actions will check it on your pull request. Please make sure your parser testing passes.

.. attention:: Test on real devices whenever possible. If you use the Python mock functionality, make sure the expected output is from a real device.

|

.. _revising_a_parser:

**********************************************
8. Revising a parser
**********************************************

.. note:: Wondering when you should revise a parser? Follow this general rule: If the schema must be changed in a way that's incompatible with current unittests, revise it!

As CLI parsers continue to evolve, updates may introduce breaking
changes that result in errors within previously functional jobs. To address this
issue, we have implemented a revision system that allows us to update parsers,
without changing the existing implementations.

When commands are parsed, the most recent revision of the relevant
parser will be automatically identified and used.

To create a revision for a parser/api/ops, a new revision folder must be
established within the existing OS folder, following the naming convention
`rv<Revision Number>`.

    .. code-block::

        genieparser/
        └── src/
            └── genie/
                └── libs/
                    └── parser/
                        └── <OS>/
                            ├── rv1/
                            ├── rv2/
                            └── rv3/

Within the revision folder, two steps must be taken:

#. Create a new `__init__.py` file with the following contents:

    .. code-block:: python

        from genie import abstract
        abstract.declare_token(revision='<Revision Number>')

   The `<revision number>` should match the number used in the folder name (for
   instance, `rv1` would use `'1'` as the revision number).

#. Create a new file with the same name as the file of the feature you are
   revising. For example, if the `"show platform"` command is to be revised,
   create a `show_platform.py` in the revision folder.

#. Once the new file has been created, open it and create the revised version
   of whatever feature you would like with **the exact same function/class name**.
   If you were to create a revision for the `show platform` parser, you
   would create a new class `ShowPlatform` and the accompanying schema.

As an example, assume the first revision is being created for the IOSXE version
of the `"show platform"` command, the resulting file structure would resemble:

    .. code-block::

        genieparser/
        └── src/
            └── genie/
                └── libs/
                    └── parser/
                        └── iosxe/
                            └── rv1/
                                ├── __init__.py
                                └── show_platform.py

By default, the parser in `iosxe/rv1/show_platform.py` will then be used instead of
the original `iosxe/show_platform.py` file. If you want to use a specific revision, pass
the revision number to the ``parse()`` command, e.g. `dev.parse('show version', revision=1)`. If you want to use the original parser, use `dev.parse('show version', revision=None)`.


To change the default behavior of revision selection to use either the latest ,
use the CLI argument `\-\-abstract-revision 1`

|

.. _versioning_a_parser

**********************
9. Versioning a Parser
**********************

Sometimes, rarely, but sometimes, you may find that the output of a command changes between versions of
IOSXE, IOSXR, or any other OS. When this happens, you can create a new version of the parser to handle
the new output. This is similar to creating a revision, but requires a different keyword to be used.

To create a new version for a parser/api/ops, a new version folder must be
established within the existing OS folder, following the naming convention
`v<Version Number>`.

    .. code-block::

        genieparser/
        └── src/
            └── genie/
                └── libs/
                    └── parser/
                        └── <OS>/
                            ├── v1_0/
                            ├── v1_1/
                            └── v2_0/

.. important::
    Ensure that you do not use periods in your folder names. This will cause import errors

To define a version range, create a new `__init__.py` file with the following contents:

    .. code-block:: python

        from genie import abstract
        from genie.abstract.token import VersionRange
        abstract.declare_token(version=VersionRange("<Minimum Version Number>", "<Maximum Version Number>"))

The `<Minimum Version Number>` and `<Maximum Version Number>` should match the version numbers used in the folder name (for instance, `v1_0` would use `'1.0'` as the minimum version number and `'1.1'` as the maximum version number).

From there you can create your parsers as you normally would. When Genie connects to the device, it will automatically
pick up the device's OS version and use the appropriate parser.

.. note::
    It's important to understand the difference between revisions and versions. Revisions are used to update parsers
    that were poorly made or in need of a rewrite, while versions are used to handle changes in the output of a command
    between different versions of the OS.

|

.. _contributing_your_work:

**********************************************
10. Contributing your work to the pyATS project
**********************************************

You've written your parser, you've run tests on your parser, and you're ready
to contribute your parser. Great! For your convenience, the steps required to
make a good pull request are outlined here, but before you start them, go read the
`pyATS contribution guide <https://pubhub.devnetcloud.com/media/pyats-development-guide/docs/contribute/contribute.html#contribute>`_.
Seriously. It's good stuff. Please follow the steps closely as it saves time for you and also for our
development team! The `genieparser repo README <https://github.com/CiscoTestAutomation/genieparser#genie-parser>`_
also contains useful information on submitting your parser.

#. Make sure your testing passed via GitHub Actions.

#. Fix any errors found in GitHub Actions result.

#. Create a new changelog file in ``genieparser/changelog/undistributed/``. The genieparser repo README explains how in the `how to write changelog <https://github.com/CiscoTestAutomation/genieparser#how-to-write-changelog>`_ section.

#. Commit and push your changes to your forked genieparser repo.

#. Create a pull request

#. Fill out the Description, Motivation and Context, Impact, and Screenshots sections of the pull request form.

#. Complete the Checklist section.

#. Submit your pull request!

|
|

See also...

* `Cisco Live DevNet workshop 2601 - pyATS/GENIE ops and parsers <https://github.com/RunSi/DEVWKS-2601>`_
* `Available parsers <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers>`_
* `This excellent blog post <https://anirudhkamath.github.io/network-automation-blog/notes/genie-parsing.html>`_ by `Anirudh Kamath <https://github.com/anirudhkamath>`_
* :ref:`contribute`
