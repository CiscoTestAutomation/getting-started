Manage device connections
=============================
This section describes how to connect to network devices using the |librarybold|. It also gives you quick examples that you can try yourself.

How the |library| connects to devices
-------------------------------------
Because the |library| is based on Python, an object-oriented programming language, it uses an :term:`object` to represent your testbed topology, and another object to represent a device.

The following example shows how this works:

#. Load the |library| API that creates a testbed object::

    $ from genie.testbed import Load

#. Define a variable ``tb`` that contains the absolute or relative path to your :term:`testbed YAML file`, in this case, ``tb.yaml``::

    $ tb = load('tb.yaml')

   *Result*: The system creates a testbed object called ``tb``. |br|

   |br|

#. Define a variable ``device`` that contains a hostname or alias from the ``tb`` object::

    $ device = tb.devices['nx-osv-1']

   *Result*: The system creates a device object called ``device``. |br|

   |br|

#. Connect to the device object::

    $ device.connect()

   *Result*: The system connects to the device and displays the connection details.

Once you're connected, you can run show commands and :ref:`parse the output <parse-output>`. 


.. _manageconnections-setup-testbed:

Set up your testbed file
------------------------------
There are a few different ways to create a testbed file, but the two simplest are:

* Use a text editor to copy and edit an existing YAML file.
* Enter device information into an Excel file, and let the |library| create the YAML file for you.

The following sections explain both options.

Edit a YAML file directly
^^^^^^^^^^^^^^^^^^^^^^^^^
The YAML file must follow the |pyATS| `topology schema <https://developer.cisco.com/docs/pyats/api/>`_. The schema provides for a complete and thorough description of your testbed, including custom key-value pairs. Only the ``devices`` block is actually required, however, so it's easy to get started with a simple example.

The ``devices`` block contains a description of each network device, and must include the following keys.

.. csv-table:: Required device block details
    :header: "Key", "Description"
    :widths: 25 75

    "``name``", "This *must* be the hostname of the device."
    "``alias``", "The |library| uses the alias to identify the device during script execution. This makes the script reusable on another topology, when a device is assigned the same alias, such as uut (unit under test)."
    "``os``", "Device operating system"
    "credentials", "The username and password to log in to the device."
    "``type``", "Device type"
    "``ip``", "IP address"
    "``protocol``", "Any supported protocol |br| (currently Telnet, SSH, REST, RESTCONF, NETCONF, and YANG)"
    "``port``", "Connection port"
 

The following example shows a YAML file with two devices defined::

  devices:

   nx-osv-1:
     alias: 'uut'
     os: nxos
     type: NX-OSv
     credentials:
       credentialname1:
         username: admin1
         password: admin1
     connections:
       defaults:
         class: unicon.Unicon
       console:
         ip: 10.10.20.160
         protocol: SSH
         port: 17003
   csr1000v-1:
     alias: 'helper'
     os: iosxe
     type: CSR1000v
     credentials:
       credentialname2:
         username: admin2
         password: admin2
     connections:
       defaults:
         class: unicon.Unicon
       console:
         ip: 10.10.20.161
         protocol: SSH
         port: 17005


.. attention:: Remember that YAML is white-space and case-sensitive.

Use Excel to create the YAML file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can define all of your device information in an Excel file. The |library| automatically converts the input and creates an equivalent YAML file. *See Nathan's documentation for more info about this.*



See also...
*a list of relevant links*

* link 1
* link 2
* link 3









