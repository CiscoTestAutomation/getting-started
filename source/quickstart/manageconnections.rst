Manage device connections
=============================
This section describes how to connect to network devices using the |librarybold|, and gives you a quick example that you can try yourself.

How the |pyATS| connects to devices
-------------------------------------
The following table describes the process that the |library| uses to connect to a network device.

.. csv-table::
    :file: ConnectionProcess.csv
    

|pyATS| uses the information contained in your :term:`testbed YAML file` to create an *object*
*Describe the process that JB described to me today...*

.. manageconnections-setup-testbed

Set up your testbed file
------------------------------
Your :term:`testbed YAML file` defines the :term:`devices` in your network and how to connect to each device. There are a few different ways to create a testbed file, but the two simplest are:

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
    "``alias``", "Not required, but strongly recommended. The |library| uses the alias to identify the device during script execution. This makes the script reusable on another topology, when a device is assigned the same alias, such as uut (for unit under test)."
    "``os``", "Device operating system"
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









