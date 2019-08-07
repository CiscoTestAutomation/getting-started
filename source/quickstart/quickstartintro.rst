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
On the last Tuesday of each month, the team releases a new version of |pyATS| and the |library|. This section describes how to get the latest changes.

.. tip:: Cisco members of the "pyats-notices" mailer list receive a notification about each release. :question:`Can external users be on this list? How does an internal user sign up to the notices?`

.. qs-upgrade-library::

Upgrade the |pyATS| infrastructure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. include:: /definitions/def_pyats_code_infrastructure.rst

You can upgrade the infrastructure with one command. From your virtual environment::

  (|library|) $ pip install |geniecmd| --upgrade

*Result*: The installer gives you the latest version of |pyATS| and the |library| infrastructure. To check the version::

  (|library|) $ pip list | egrep 'ats|genie'

*Result*: The system displays a list of the core packages and the version of each.

Upgrade the |library| packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. include:: /definitions/def_pyatslibrary_code_structure.rst

To upgrade the packages, you simply run the pip installer and specify each package that you want to upgrade. This means that you can install only those packages that you need for your specific requirements.

, or create a script that does this. Or, we can provide a command here that they can copy and paste, see the history from my meeting with Lubna. First, get the list of packages.>
<Probably remove this list, it will be easier to maintain the doc without it.>
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

To upgrade a specific package::

    (|library|) $ pip install <package name> --upgrade


For example::

    pip install genie.libs.robot --upgrade
    pip install genie.conf --upgrade

:question:`Does a user need to update the libraries, or does that happen with the core |library| upgrade?`

Test a network of mock devices
-------------------------------
*Procedure to download/clone the test file from Git, and then use Genie to connect to and test those devices.*

# 1. make sure pyATS is installed (including the libraries)
bash$ pip install pyats[full]

# 2. clone this repository into your environment
bash$ git clone https://github.com/CiscoTestAutomation/examples


Start with https://github.com/CiscoTestAutomation/examples/tree/master/libraries/harness_simple

Download or clone the Git repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Step one
#. Step two
#. Step n

Configure the testbed.yaml file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*(Make sure this concept was explained in the "Important concepts" section.)*

#. Step one
#. Step two
#. Step n

Connect to the mock devices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
