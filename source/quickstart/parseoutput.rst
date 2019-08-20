.. _parse-output:

Parse device output
====================
This section describes the benefits of using parsed output for network automation, and provides an example of how a :term:`parser` works.

.. _parsed-output-benefits:

Benefits of parsed device output
---------------------------------
Device output can vary widely between different devices and for different show commands.

.. include:: ../definitions/def_parser.rst 

Before and after examples
^^^^^^^^^^^^^^^^^^^^^^^^^

The following example shows device output before it's parsed.

.. code-block:: text

    --------------------------------------------------------------------------------
    Port   VRF          Status IP Address                              Speed    MTU
    --------------------------------------------------------------------------------

    --------------------------------------------------------------------------------
    Ethernet      VLAN    Type Mode   Status  Reason                   Speed     Port
    Interface                                                                    Ch #
    --------------------------------------------------------------------------------
    Eth1/1        1       eth  routed up      none                       1000(D) --
    Eth1/2        --      eth  routed up      none                       1000(D) --
    Eth1/3        --      eth  routed up      none                       1000(D) --

And this is the output after it's parsed into a Python dictionary.

.. code-block:: text

    # parsed_output
    # -------------
    # {'Eth1/1': {'Ethernet Interface': 'Eth1/1',
    #             'Mode': 'routed',
    #             'Port': '--',
    #             'Reason': 'none',
    #             'Speed': '1000(D)',
    #             'Status': 'up',
    #             'Type': 'eth',
    #             'VLAN': '1'},
    #  'Eth1/2': {'Ethernet Interface': 'Eth1/2',
    #             'Mode': 'routed',
    #             'Port': '--',
    #             'Reason': 'none',
    #             'Speed': '1000(D)',
    #             'Status': 'up',
    #             'Type': 'eth',
    #             'VLAN': '--'},
    #  'Eth1/3': {'Ethernet Interface': 'Eth1/3',
    #             'Mode': 'routed',
    #             'Port': '--',
    #             'Reason': 'none',
    #             'Speed': '1000(D)',
    #             'Status': 'up',
    #             'Type': 'eth',
    #             'VLAN': '--'}}

Although the "before" example is human readable in this case, the output structure is not consistent across devices. 

Available parsers
^^^^^^^^^^^^^^^^^^
The |library| provides a parser for most of the Cisco-specific ``show`` commands. You can see a complete list on the `parser website <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers>`_.

.. tip:: Once you have the parsed, structured data, which is consistent across devices and operating systems, you can:

    * Easily search for specific key-value pairs.
    * Verify if the operational state is as expected.
    * Compare two output dictionaries to see if anything has changed.
    * Take any action that you need to - the possibilities are virtually limitless! 

.. _example-parse-output:

Example: Parse output from a show command
---------------------------------------------
In the section :ref:`manage-connections`, you learned :ref:`how the system connects to devices <how-library-connects>`. Once you connect to a device, you can run ``show`` commands and parse the output.

The following example shows you how to parse output from the ``show inventory`` command, using a :term:`mock device`.

#. In your virtual environment, change to the directory that contains the mock YAML file::

    (pyats) $ cd mock

#. Open the Python interpreter::

    (pyats) $ python

#. Load the ``testbed`` API, create your testbed and device objects, and connect to the device::

    >>> from genie.testbed import load
    >>> tb = load('mock.yaml')
    >>> dev = tb.devices['nx-osv-1']
    >>> dev.connect()

   *Result*: The system connects to the device and displays the connection details. Once you're connected, you can run show commands and parse the output. |br| |br| 

#. Parse the output from the ``show inventory`` command and store the Python dictionary in a variable::

    >>> p1 = dev.parse('show inventory')

   *Result*: The system returns the inventory information as a series of key-value pairs:

   .. code-block:: text

    [2019-08-20 16:05:58,388] +++ nx-osv-1: executing command 'show inventory' +++
    show inventory
    NAME: "Chassis",  DESCR: "NX-OSv Chassis "
    PID: N7K-C7018           ,  VID: V00 ,  SN: TB00010000B

    NAME: "Slot 1",  DESCR: "NX-OSv Supervisor Module"
    PID: N7K-SUP1            ,  VID: V00 ,  SN: TM00010000B

    NAME: "Slot 2",  DESCR: "NX-OSv Ethernet Module"
    PID: N7K-F248XP-25       ,  VID: V00 ,  SN: TM00010000C

    NAME: "Slot 3",  DESCR: "NX-OSv Ethernet Module"
    PID: N7K-F248XP-25       ,  VID: V00 ,  SN: TM00010000D

    NAME: "Slot 4",  DESCR: "NX-OSv Ethernet Module"
    PID: N7K-F248XP-25       ,  VID: V00 ,  SN: TM00010000E

    NAME: "Slot 33",  DESCR: "NX-OSv Chassis Power Supply"
    PID:                     ,  VID: V00 ,  SN:

    NAME: "Slot 35",  DESCR: "NX-OSv Chassis Fan Module"
    PID:                     ,  VID: V00 ,  SN:
    switch#

#. Now that you have the parsed output stored as a Python dictionary in the variable ``p1``, you can use the structured data as you wish. For example, you can display a user-friendly message and the serial number for Slot 1:

    >>> print('My serial for slot1 is:' + p1['name']['Slot 1']['serial_number'])

   *Result*: The system prints the message and data on-screen::

    My serial for slot1 is:TM00010000B



#. To exit the Python interpreter::

    >>> exit()

Python example
^^^^^^^^^^^^^^^
*(This content can be re-used elsewhere.)*

#. Step one 
#. Step two
#. Step n 

Linux example
^^^^^^^^^^^^^^^
*(This content can be re-used elsewhere.)*

#. Step one 
#. Step two
#. Step n

See also...
*a list of relevant links*

* link 1
* link 2
* link 3








