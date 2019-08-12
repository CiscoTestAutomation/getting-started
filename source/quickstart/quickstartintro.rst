.. _quick-start:

Quick start guide
=============================
This topic will get you up and running quickly, and includes the following information:

* Tips on how to use the |library|
* Real-life scenarios
* Hands-on practice procedures
* A testbed file of mock devices

Important concepts
-------------------
This section describes the key concepts that you need to understand before you begin to use |pyATSbold| and the |librarybold|.

.. _qs-sdn::

Software-defined network
^^^^^^^^^^^^^^^^^^^^^^^^^
A software-defined network (SDN) decouples network control from network forwarding, which makes the control functions programmable and the network itself more dynamic and scalable. The |pyATS| ecosystem helps you test, maintain, and diagnose
the operational state of your agile SDN network.

|pyATS| provides a framework that standardizes how to programmatically interact with devices (routers, switches, servers, traffic generators, and other hardware products). The ecosystem provides the mechanisms you need to parse, model, configure, and test your SDN, and includes a set of ready-to-use test automation libraries built by the same engineering teams that built your Cisco products.

.. _qs-abstraction::

Abstraction
^^^^^^^^^^^
The term *abstraction* refers to the separation of network control from the actual, physical network infrastructure (devices). Abstraction enables you to monitor and manage changes -- such as network topology and traffic -- without having to change the underlying hardware.

:question:`Does this belong here, under abstraction? Or is this a different sort of thing?` For example, the |library| uses abstraction to model your network topology and protocols, which results in a generalized view of network *objects*. These objects represent protocols, testbeds, devices, interfaces, and links :question:`and anything else?`.

The following diagram shows an example of how topology objects are referenced and interconnected.

.. code-block:: text

    +--------------------------------------------------------------------------+
    | Testbed Object                                                           |
    |                                                                          |
    | +-----------------------------+          +-----------------------------+ |
    | | Device Object - myRouterA   |          | Device Object - myRouterB   | |
    | |                             |          |                             | |
    | |         device interfaces   |          |          device interfaces  | |
    | | +----------+ +----------+   |          |   +----------+ +----------+ | |
    | | | intf Obj | | intf Obj |   |          |   |  intf Obj| | intf Obj | | |
    | | | Eth1/1   | | Eth1/2 *-----------*----------*  Eth1/1| | Eth1/2   | | |
    | | +----------+ + ---------+   |     |    |   +----------+ +----------+ | |
    | +-----------------------------+     |    +-----------------------------+ |
    |                                     |                                    |
    |                               +-----*----+                               |
    |                               | Link Obj |                               |
    |                               |rtrA-rtrB |                               |
    |                               +----------+                               |
    +--------------------------------------------------------------------------+

The |library| uses the ``Abstraction`` package to make your tests agnostic, so that they run seamlessly over various operating systems, platforms, and communication protocols.

.. qs-features::

Features
^^^^^^^^^
The term *feature* typically refers to a network protocol, represented by the |library| as a Python object, with attributes that represent the feature (protocol) configuration on a device. Many networks use a combination of different features, such as MPLS, BGP, and EIGRP.

.. qs-statefulvalidation::

Stateful validation
^^^^^^^^^^^^^^^^^^^
Configuration changes often result in a series of operational state changes. For example, you might see changes to the following items:

* Interface status
* Routing
* Neighbors

With just a few commands or an automated script, you can use the |library| to profile your system before and after a configuration change to see a detailed list of the changes.

.. qs-testbedyaml::

Testbed YAML file
^^^^^^^^^^^^^^^^^^
Network test automation is based on the use of testbeds. With |pyATS| and the |library|, you describe your devices under test in a `YAML <http://www.yaml.org/start.html>`_ file named ``testbed.yaml``.

Use the YAML testbed file to describe your physical devices and how they link together to form the testbed network topology.

The following example shows a simple testbed file that contains a single device::

  devices:                # define all devices under the devices block
    csr1000v-1:           # the device definition must begin with its HOSTNAME
      type: router
      os: iosxe           # specify the device connection OS type
      tacacs:                         # login credentials
          username: devnetuser
      passwords:                      # password info
          tacacs: Cisco123!
          line: Cisco123!
      connections:        # define the mgmt interface connection details under this block
        mgmt:
          protocol: ssh
          ip: 172.25.192.90


When to use the |library|
-------------------------
Use the |library| any time you want to configure or check the health of your network. Cisco makes the automated tests used during product development available externally, so customers can run the same tests on their own networks. This is a win-win situation for Cisco and our customers!

Test script creation
^^^^^^^^^^^^^^^^^^^^^^^
Ideal for cross-OS/cross-platform development teams, the |library| enables you to

* develop in parallel
* conduct tests, and
* scale your respective features/components independently.

The |library| decouples your tests from topology and configuration so that you can address a wide variety of user requirements in your unit, sanity, regression, and system/solution tests.

:question:`What would be a specific, real-world scenario to show here? https://github.com/RunSi/DEVWKS-2601 (This example shows how to use a Robot Framework script, can we show an example that doesn't? This seems to go to the same workshop as the test automation one.)`

Test automation
^^^^^^^^^^^^^^^^^^
Use the |library| to combine any number of test scripts and run them at scheduled intervals, under different test conditions. The |library| gives you the flexibility to scale coverage, configuration, and runtime based on your testing requirements.

:question:`What would be a specific, real-world scenario of doing this with Genie?` https://github.com/CiscoTestAutomation/CL-DevNet-2595

.. qs-library-cli::

Use the |library| command line
----------------------------------------------
The |library| command line interface (CLI) is a powerful Linux-based command-line utility that gives you |library| Python functionality directly from a Linux terminal (or emulator). The CLI is easy to use, even if you don't know anything about Python or programming.

.. note::

  All |library| commands start with |geniecmd|, followed by the command and its options.

From your |pyATS| virtual environment, you can see a complete list of available commands::

  (|library|)$ |geniecmd| --help

*Result*: The system displays the following output, or similar:

.. code-block::

      Usage:
      |geniecmd| <command> [options]

    Commands:
        diff                Command to diff two snapshots saved to file or directory
        dnac                Command to learn DNAC features and save to file
        learn               Command to learn device features and save to file
        parse               Command to parse show commands
        run                 Run |geniecmd| triggers & verifications in pyATS runtime environment
        shell               enter Python shell and load a Genie testbed file and/or Pickled file

    General Options:
      -h, --help            Show help

    Run '|geniecmd| <command> --help' for more information on a command.

To see help for a specific command::

  (|library|)$ |geniecmd| <command name> --help


.. qs-update::

Keep |pyATS| up to date
-----------------------------
On the last Tuesday of the month, the team releases a new version of |pyATS| and the |library|. This section describes how to get the latest changes.

.. qs-upgrade::

To upgrade the |pyATS| and |library| :doc:`infrastructure </definitions/def_pyats_code_infrastructure>`, and any or all of the :doc:`feature libraries and components </definitions/def_pyatslibrary_code_structure>`, run the ``pip install --upgrade`` command from your virtual environment.

Internal Cisco users
^^^^^^^^^^^^^^^^^^^^^

.. tip:: Cisco members of the "pyats-notices" mailer list receive a notification about each release. :question:`Can external users be on this list? How does an internal user sign up to the notices?`

.. csv-table:: Upgrade options
    :header: "Upgrade option", "Use case", "Command"

    "All |pyATS| and |library|  infrastructure and packages", " ", "``(library) $ pip install --upgrade ats genie``"
    "|pyATS| infrastructure only", " ", "``(library) $ pip install --upgrade ats``"
    "Specific packages or libraries", " ", "``(|library|) $ pip install <package name> --upgrade``"

DevNet community users
^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Upgrade options
     :header: "Upgrade option", "Use case", "Command"

     "All |pyATS| and |library|  infrastructure and packages", " ", "``(library) $ pip install --upgrade pyats genie``"
     "|pyATS| infrastructure only", " ", "``(library) $ pip install --upgrade pyats``"
     "Specific packages or libraries", " ", "``(|library|) $ pip install <package name> --upgrade``"

*Result*: The installer checks for and upgrades any dependencies, and gives you the latest version of the |pyATS| and |library| core and library packages. To check the version::

  (|library|) $ pip list | egrep 'ats|genie'

*Result*: The system displays a list of the core packages and the version of each.

:question:`<Probably remove this list, it will be easier to maintain the doc without it.>`

.. code-block:: text

    |geniecmd|                         Main Genie package
    |geniecmd|.abstract                Abstraction package for OS Agnostic
    |geniecmd|.conf                    Genie core for Configuration object
    |geniecmd|.examples                Example for Genie Conf/Ops/Robot and Harness
    |geniecmd|.harness                 Genie core for Test Harness
    |geniecmd|.libs.conf               Libraries for Configuration object
    |geniecmd|.libs.filetransferutils  Libraries for File Transfer utils
    |geniecmd|.libs.ops                Genie core for Operation state object
    |geniecmd|.libs.parser             Libraries containing all the parsers
    |geniecmd|.libs.robot              Libraries containing all Robot keywords
    |geniecmd|.libs.sdk                Libraries containing all Triggers and Verifications
    |geniecmd|.libs.telemetry          Librarires for Genie Telemetry
    |geniecmd|.metaparser              Genie Core for Parser
    |geniecmd|.ops                     Genie Core for operational state
    |geniecmd|.parsergen               Genie Core for parsergen - Automatically parse output
    |geniecmd|.predcore                Genie Core for predcore
    |geniecmd|.telemetry               Genie Core for telemetry - Monitor testbed
    |geniecmd|.utils                   Genie utilities


:question:`Does a user need to update the libraries, or does that happen with the core |library| upgrade?`

Test a network of virtual devices
----------------------------------

Launch the |library|
^^^^^^^^^^^^^^^^^^^^^

Parse...
^^^^^^^^^

Run a test script
^^^^^^^^^^^^^^^^^^^


This section describes how you can use the |library| to run some initial tests on a testbed of our mock devices. This will help you to start using the |library| for some simple scenarios that demonstrate how the |library| works.

.. note:: Make sure that you have |pyats| and the |library| :doc:`fully installed </install/installpyATS>`.

First, you'll download or clone the Git repository that contains the testbed file, and then use the |library| to connect to and test those devices.

Download or clone the Git repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* To clone the Git repository from your virtual environment::

    (|library|) $ git clone https://github.com/CiscoTestAutomation/examples

* To download the Git repository from a browser:

  * Go to https://github.com/CiscoTestAutomation/examples.
  * Select **Clone or download**.
  * Select **Open in Desktop** to download and use the GitHub Desktop app, or **Download Zip** to download and extract a zip file.

 *Result*: You now have the example files stored in the ``examples`` directory.

Configure the testbed.yaml file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following example shows the testbed file used for the mock devices::

  testbed:
    name: 'virl'

  devices:
    nx-osv-1:
        type: "NX-OSv 9000"
        os: "nxos"
        alias: uut
        tacacs:
            login_prompt: 'login:'
            password_prompt: 'Password:'
            username: admin
        passwords:
            tacacs: admin
            enable: admin
            line: admin
        connections:
            defaults:
                class: 'unicon.Unicon'
            a:
                protocol: telnet
                ip: 172.25.192.90
                port: 17023
        custom:
            abstraction:
                order: [os]
    csr1000v-1:
        type: asr1k
        os: "iosxe"
        alias: helper
        tacacs:
            login_prompt: 'login:'
            password_prompt: 'Password:'
            username: cisco
        passwords:
            tacacs: cisco
            enable: cisco
            line: cisco
        connections:
            defaults:
                class: 'unicon.Unicon'
            a:
                protocol: telnet
                ip: 172.25.192.90
                port: 17021
        custom:
            abstraction:
                order: [os]

:question:`Is it okay to publish these ip addresses externally?`

.. note::

   * Each device name must match the hostname of the device. Otherwise, the connection will hang.
   * At least one device must have the alias 'uut' in the testbed YAML file.

Connect to the mock devices and show the version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
By default, the |library| connects to all devices in the testbed YAML file. To override the default behavior:

  * specify one or more devices as a command line argument, or
  * provide a mapping datafile, to control connections per device. :question:`Add a link here to a relevant topic.`


Try manually connecting to a device and showing its ???: https://pubhub.devnetcloud.com/media/genie-docs/docs/cookbooks/genie.html#how-to-keep-genie-up-to-date-how-to-upgrade-genie

*Describe what each command does one at a time*

#. Step one
#. Step two
#. Step n

Use the |library| to test a device upgrade
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*These are the steps for upgrading the device versions and then seeing the before and after views.*

#. Step one
#. Step two
#. Step n

See also...
*a list of relevant links*

* `Cisco Open Network Environment <https://www.cisco.com/c/en/us/products/collateral/switches/nexus-1000v-switch-vmware-vsphere/white_paper_c11-728045.html>`_
* Example of stateful validation https://github.com/CiscoTestAutomation/CL-DevNet-2595/blob/master/workshop.md
* link 3
