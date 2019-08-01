.. _quick-start:

Quick start guide
=============================
This topic will get you up and running quickly. It provides the following information:

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
The term *abstraction* refers to the separation of network control from the actual, physical network infrastructure (devices). Abstraction enables you to monitor and manage changes programmatically, such as network topology and traffic, without having to change the underlying hardware.

:question:`Does this belong here, under abstraction? Or is this a different sort of thing?` For example, the |library| uses abstraction to model your network topology and protocols, which results in a generalized view of network *objects*. These objects represent testbeds, devices, interfaces, and links :question:`and anything else?`.

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

The |library| uses the ``Abstraction`` package to execute its parsers, triggers, verifications, and all other functions across Cisco and non-Cisco operating systems, agnostically.

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
Use the |library| any time you want to check the health of your network. You can also use the |library| for Cisco-customer partnerships -- the automated tests used by Cisco during product development are also available externally. This is a win-win situation for Cisco and our customers!

Test script creation
^^^^^^^^^^^^^^^^^^^^^^^
Ideal for cross-OS and cross-platform development teams, the |library| enables you to

* develop in parallel
* conduct tests, and
* scale your respective features/components independently.

The |library| decouples your tests from topology and configuration so that you can address a wide variety of user requirements in your unit, sanity, regression, and system/solution tests.

:question:`What would be a specific, real-world scenario to show here? https://github.com/RunSi/DEVWKS-2601 (This example shows how to use a Robot Framework script, can we show an example that doesn't? This seems to go to the same workshop as the test automation one.)`

"Learn the good state of the network
Rerun periodically or when a disaster occurs to figure out what happened"

Test automation
^^^^^^^^^^^^^^^^^^
The |library| has the functionality to combine any number of tests and run them under various test conditions. This provides you with the flexibility to scale coverage, configuration, and runtime based on your testing requirements.

:question:`What would be a specific, real-world scenario of doing this with Genie?` https://github.com/CiscoTestAutomation/CL-DevNet-2595

Use the |library| command line interface (CLI)
----------------------------------------------
*This section explains what the CLI is and how to use it, along with a link to a CLI reference (if there is one).*

Keep the |library| up to date
-----------------------------
*(This content can be re-used elsewhere.)*

Get the latest core (infrastructure?) updates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Procedure for using pip install |geniecmd| --upgrade (will this be the same?) and info about how often we update the packages, recommendations for how often the user should run this.

Update the |library| packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Procedure for using pip install <package name> --upgrade to update the packages. How does a user know when there has been an upgrade? Can they sign up for notifications or watch the Git repo? If yes, we should explain that procedure here.*

Test a network of mock devices
-------------------------------
*Procedure to download/clone the test file from Git, and then use Genie to connect to and test those devices.*

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
