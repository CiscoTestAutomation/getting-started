.. _manage-connections:

Manage device connections
=============================
This section describes how to connect to network devices using the |librarybold|. It also gives you a quick example to try using mocked devices.

How the |library| connects to devices
-------------------------------------
Because the |library| is based on Python, an object-oriented programming language, it uses an :term:`object` to represent your testbed topology, and another object to represent a device. You connect to a device by specifying the device object name.

#. :ref:`manageconnections-setup-testbed` file that contains your device details.
#. Use the |library| to create the testbed and device objects.
#. Tell the |library| which device to connect to.
#. Connect and run commands.

For a more detailed example that you can try, see :ref:`connect-to-device`.


.. _manageconnections-setup-testbed:

Set up a testbed YAML file
------------------------------
There are a few different ways to create a testbed file, but the two simplest are:

* Use a text editor to copy and edit an existing YAML file.
* Enter device information into an Excel file, and let the |library| create the YAML file for you.

The following sections explain both options.

Edit a YAML file directly
^^^^^^^^^^^^^^^^^^^^^^^^^
The YAML file must follow the |pyATS| `topology schema <https://developer.cisco.com/docs/pyats/api/>`_. The schema provides for a complete and thorough description of your testbed, including custom key-value pairs. 

.. tip:: Only the ``devices`` block is actually required, so it's easy to get started with a simple example.

The ``devices`` block contains a description of each network device, and must include the following keys.

.. csv-table:: Required device block details
    :header: "Key", "Description"
    :widths: 25 75

    "``hostname``", "This *must* be the hostname of the device."
    "``alias``", "The |library| uses the alias to identify the device during script execution. This makes the script reusable on another topology, when a device is assigned the same alias, such as ``uut`` (unit under test)."
    "``os``", "Device operating system"
    "``credentials``", "The username, password, and any other credentials required to log in to the device."
    "``type``", "Device type"
    "``ip``", "IP address"
    "``protocol``", "Any one of the supported protocols |br| (currently Telnet, SSH, REST, RESTCONF, NETCONF, and YANG)"
    "``port``", "Connection port"
 

The following example shows a YAML file with two devices defined :question:`Should we show SSH instead of telnet, and would that require more credentials in the credentials block? Do we need to show/explain the "enable" block here?` ::

 devices:
  nx-osv-1:
      type: 'router'
      os: 'nxos'
      alias: 'uut'
      credentials:
          default:
              username: admin
              password: admin
      connections:
          defaults:
            class: 'unicon.Unicon'
          cli:
              protocol: telnet
              ip: "172.25.192.90"
              port: 17010

  csr1000v-1:
      type: 'router'
      os: "iosxe"
      alias: 'helper'
      credentials:
          default:
              username: cisco
              password: cisco
      connections:
          defaults:
            class: 'unicon.Unicon'
          cli:
              protocol: telnet
              ip: "172.25.192.90"
              port: 17008

.. attention:: Remember that YAML is white-space and case-sensitive.

Use Excel to create the YAML file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can define all of your device data in a CSV (.csv) or Excel (.xls, .xlsx) file. The |library| ``create testbed`` command automatically converts the input and creates an equivalent YAML file. 

The following example shows an Excel file with the required columns.

.. image:: geniecreate_example_excel.png 

.. tip:: 

    * The ip and port can be separated by either a space or a colon (:).
    * If you leave a password cell blank, the system prompts you for the password when you try to connect to the device.

When you're ready to create the YAML file, from your virtual environment, run the command::

 (pyats) $ genie create testbed my_devices.xls --output yaml/my_testbed.yaml

where ``my_devices.xls`` is the name of your source file, and ``my_testbed.yaml`` is the name of your output file.


.. _connect-to-device:

Connect to a mock device
---------------------------
This step-by-step example shows you how to connect to a mock device, so that you can practice using the |library| without having to connect to a real device.

#. Copy or clone the repo? No, it's probably out of date because of the credentials? https://github.com/CiscoTestAutomation/examples/tree/master/libraries/harness_simple Use mock devices. We have used the Unicon playback feature to record all interactions with the device so you can use it smoothly without connecting to real devices as below.
pyats run job demo1_harness_simple_job.py --testbed-file cisco_live.yaml --replay mock_device

#. From your virtual environment, open the Python interpreter::

    (pyats) $ python

#. Load the |library| ``testbed`` API so that you can create the testbed and device objects::

    >>> from genie.testbed import load

#. Create a testbed object ``tb`` based on your :term:`testbed YAML file`. Specify the absolute or relative path, in this case, ``tb.yaml``::

    >>> tb = load('tb.yaml')

   *Result*: The system creates a variable ``tb`` that points to the testbed object. This command also creates ``tb.devices``, which contains the YAML device information in the form of key-value pairs. |br|

   |br|

#. Create an object ``device`` for the device that you want to connect to::

    >>> device = tb.devices['nx-osv-1']

   *Result*: The |library| finds the device named ``nx-osv-1`` in ``tb.devices`` and stores the information in the ``device`` object. |br|

   |br|

#. Connect using the values stored in the ``device`` object::

    >>> device.connect()

   *Result*: The system connects to the device and displays the connection details.

Once you're connected, you can run show commands and :ref:`parse the output <parse-output>`. 



See also...
*a list of relevant links*

* link 1
* link 2
* link 3









