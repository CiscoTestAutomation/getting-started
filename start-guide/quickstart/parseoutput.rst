.. _parse-output:

Parse Device Output
===================
This topic describes the benefits of using parsed output for network automation, and provides an example of how a :term:`parser` works.

.. _parsed-output-benefits:

Device output can vary widely between different devices and for different show commands.

.. include:: ../definitions/def_parser.rst 
   :start-line: 3

For more information about the ``genie.metaparser`` package, see the topic `Metaparser Package <https://pubhub.devnetcloud.com/media/genie-docs/docs/metaparser/index.html#>`_.

The following example shows device output before it's parsed.

.. code-block:: text

    ---------------------------------------------------------------------------------
    Port   VRF          Status IP Address                              Speed    MTU
    ---------------------------------------------------------------------------------

    ---------------------------------------------------------------------------------
    Ethernet      VLAN    Type Mode   Status  Reason                   Speed     Port
    Interface                                                                    Ch #
    ---------------------------------------------------------------------------------
    Eth1/1        1       eth  routed up      none                       1000(D) --
    Eth1/2        --      eth  routed up      none                       1000(D) --
    Eth1/3        --      eth  routed up      none                       1000(D) --

And this is the output after it's parsed into a Python dictionary.

.. code-block:: text

    # parsed_output
    # -------------
      {'Eth1/1': {'Ethernet Interface': 'Eth1/1',
                  'Mode': 'routed',
                  'Port': '--',
                  'Reason': 'none',
                  'Speed': '1000(D)',
                  'Status': 'up',
                  'Type': 'eth',
                  'VLAN': '1'},
       'Eth1/2': {'Ethernet Interface': 'Eth1/2',
                  'Mode': 'routed',
                  'Port': '--',
                  'Reason': 'none',
                  'Speed': '1000(D)',
                  'Status': 'up',
                  'Type': 'eth',
                  'VLAN': '--'},
       'Eth1/3': {'Ethernet Interface': 'Eth1/3',
                  'Mode': 'routed',
                  'Port': '--',
                  'Reason': 'none',
                  'Speed': '1000(D)',
                  'Status': 'up',
                  'Type': 'eth',
                  'VLAN': '--'}}

Although the "before" example is human readable in this case, the output structure is *not* useful for automation. The "after" example, by contrast, is a useful dictionary that you can easily interact with in your automation script.

Available Parsers
-----------------
The |library| provides a parser for most of the Cisco-specific ``show`` commands. You can see a complete list on the `parser website <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers>`_.

.. tip:: Once you have the parsed, structured data, you can:

    * Easily search for specific key-value pairs.
    * Verify if the operational state is as expected.
    * Compare two output dictionaries to see if anything has changed.
    * Take any action that you need to - the possibilities are virtually limitless! 

.. _example-parse-output:

Parsing Examples
----------------
In the section :ref:`manage-connections`, you learned :ref:`how the system connects to devices <how-library-connects>`. Once you connect to a device, you can run ``show`` commands and parse the output.

.. attention:: Before you try these examples, make sure that you :download:`download and extract the zip file <mock.zip>` that contains the mock data and Python script.

Using Command Line
^^^^^^^^^^^^^^^^^^
You can use the :term:`library command line` ``Parse`` functionality to parse the output from a specified ``show`` command. Check the `parser website <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers>`_ for a list of available parsers that you can use.

#. In your virtual environment, change to the directory that contains the mock YAML file::

    (pyats) $ cd mock

#. Run the parser::

    (pyats) $ pyats parse "show version" --testbed-file mock.yaml --devices uut

   *Result*: The system returns the version information as a series of key-value pairs:

   .. code-block:: text

    {
        "platform": {
            "hardware": {
            "bootflash": "3184776 kB",
            "chassis": "NX-OSv",
            "cpu": "QEMU Virtual CPU version 2.5",
            "device_name": "nx-osv-1",
            "memory": "3064740 kB",
            "model": "NX-OSv",
            "processor_board_id": "TM00010000B",
            "rp": "NX-OSv Supervisor Module",
            "slots": "None"
            },
            "kernel_uptime": {
            "days": 6,
            "hours": 1,
            "minutes": 12,
            "seconds": 30
            },
            "name": "Nexus",
            "os": "NX-OS",
            "software": {
            "kickstart_compile_time": "1/11/2016 16:00:00 [02/11/2016 10:30:12]",
            "kickstart_image_file": "bootflash:///titanium-d1-kickstart.7.3.0.D1.1.bin",
            "kickstart_version": "7.3(0)D1(1)",
            "system_compile_time": "1/11/2016 16:00:00 [02/11/2016 13:08:11]",
            "system_image_file": "bootflash:///titanium-d1.7.3.0.D1.1.bin",
            "system_version": "7.3(0)D1(1)"
            }
        }
        }


In Python Interactive Shell
^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

   .. code-block:: python

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

    >>> print('My serial for slot1 is: ' + p1['name']['Slot 1']['serial_number'])

   *Result*: The system prints the message and data on-screen::

    My serial for slot1 is: TM00010000B



#. To exit the Python interpreter::

    >>> exit()


Optionally, if you already have the output from the device, then you can pass it into the parse method even if the device is not connected:

    .. code-block:: python
    
     output = """
     NAME: "1", DESCR: "WS-C3560CX-12PC-S"
     PID: WS-C3560CX-12PC-S , VID: V03  , SN: FOC2419L9KY
     """

     dev.parse('show inventory', output=output)

    *Result*: The ``.parse()`` method will return the parsed structure (a dictionary) that you can navigate to find the values you are looking for::

     {'slot': {'1': {'rp': {'WS-C3560CX-12PC-S': {'name': '1', 'descr': 'WS-C3560CX-12PC-S', 'pid': 'WS-C3560CX-12PC-S', 'vid': 'V03', 'sn': 'FOC2419L9KY'}}}}}

.. _example-run-parse-script:

In a Python Script
^^^^^^^^^^^^^^^^^^
This example shows you how easy it is to put all of your statements into a single script that you can run from your virtual environment.

#. Open ``new_script.py`` in a text editor.

   *Result*: You can see all of the commands that connect to a device and parse the output. |br| |br| 


#. In your virtual environment, change to the directory where you extracted the zip file::

    (pyats) $ cd mock


#. Run the script::

    (pyats) $ python3 new_script.py

   *Result*: The system displays the device output before and after it's parsed, and prints the user-friendly message on-screen::

    [2019-08-20 16:48:19,466] +++ nx-osv-1 logfile /tmp/nx-osv-1-cli-20190820T164819462.log +++
    [2019-08-20 16:48:19,467] +++ Unicon plugin nxos +++
    /mnt/c/Users/kacann/Documents/development/pyats/lib/python3.6/site-packages/unicon/bases/routers/connection.py:93: DeprecationWarning: Arguments 'username', 'enable_password','tacacs_password' and 'line_password' are now deprecated and replaced by 'credentials'.
    category = DeprecationWarning)
    Trying mock_device ...
    Connected to mock_device.
    Escape character is '^]'.

    [2019-08-20 16:48:23,447] +++ connection to spawn: mock_device_cli --os nxos --mock_data_dir mock_data --state connect, id: 139915288871992 +++
    [2019-08-20 16:48:23,451] connection to nx-osv-1

    switch#
    [2019-08-20 16:48:24,059] +++ initializing handle +++
    [2019-08-20 16:48:24,070] +++ nx-osv-1: executing command 'term length 0' +++
    term length 0
    switch#
    [2019-08-20 16:48:24,077] +++ nx-osv-1: executing command 'term width 511' +++
    term width 511
    switch#
    [2019-08-20 16:48:24,085] +++ nx-osv-1: executing command 'terminal session-timeout 0' +++
    terminal session-timeout 0
    switch#
    [2019-08-20 16:48:24,089] +++ nx-osv-1: config +++
    config term
    switch(config)#no logging console
    switch(config)#line console
    switch(config)#exec-timeout 0
    switch(config)#terminal width 511
    switch(config)#end
    switch#
    [2019-08-20 16:48:25,013] +++ nx-osv-1: executing command 'show inventory' +++
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
    My serial for slot1 is:TM00010000B



See also...

* `Library parse command <https://pubhub.devnetcloud.com/media/genie-docs/docs/cli/genie_parse.html#genie-parse>`_
* `Simple description of a Python dictionary <https://www.w3schools.com/python/python_dictionaries.asp>`_
* `Available parsers <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers>`_









