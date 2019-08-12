.. _key-concepts:

Important concepts
=============================

This section describes the key concepts that you need to understand before you begin to use |pyATSbold| and the |librarybold|.

.. glossary::
   :sorted:

   Software-defined network
    A software-defined network (SDN) decouples network control from network forwarding, which makes the control functions programmable and the network itself more dynamic and scalable. The |pyATS| ecosystem helps you test, maintain, and diagnose the operational state of your agile SDN network.
    
    |pyATS| provides a framework that standardizes how to programmatically interact with devices (routers, switches, servers, traffic generators, and other hardware products). The ecosystem provides the mechanisms you need to parse, model, configure, and test your SDN, and includes a set of ready-to-use test automation libraries built by the same engineering teams that built your Cisco products.

   Abstraction
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


   Features
    The term *feature* typically refers to a network protocol, represented by the |library| as a Python object, with attributes that represent the feature (protocol) configuration on a device. Many networks use a combination of different features, such as MPLS, BGP, and EIGRP.


   Stateful validation
    Configuration changes often result in a series of operational state changes. For example, you might see changes to the following items:

    * Interface status
    * Routing
    * Neighbors

    With just a few commands or an automated script, you can use the |library| to profile your system before and after a configuration change to see a detailed list of the changes.

.. qs-testbedyaml::

   Testbed YAML file
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


   Test script creation
    Ideal for cross-OS/cross-platform development teams, the |library| enables you to

    * develop in parallel
    * conduct tests, and
    * scale your respective features/components independently.

    The |library| decouples your tests from topology and configuration so that you can address a wide variety of user requirements in your unit, sanity, regression, and system/solution tests.

    :question:`What would be a specific, real-world scenario to show here? https://github.com/RunSi/DEVWKS-2601 (This example shows how to use a Robot Framework script, can we show an example that doesn't? This seems to go to the same workshop as the test automation one.)`

   Test automation
    Use the |library| to combine any number of test scripts and run them at scheduled intervals, under different test conditions. The |library| gives you the flexibility to scale coverage, configuration, and runtime based on your testing requirements.

    :question:`What would be a specific, real-world scenario of doing this with Genie?` https://github.com/CiscoTestAutomation/CL-DevNet-2595


   |library| command line
    The |library| command line interface (CLI) is a powerful Linux-based command-line utility that gives you |library| Python functionality directly from a Linux terminal (or emulator). The CLI is easy to use, even if you don't know anything about Python or programming.

    .. note::

      All |library| commands start with |geniecmd|, followed by the command and its options.

    From your |pyATS| virtual environment, you can see a complete list of available commands::

      (|library|)$ |geniecmd| --help

    To see help for a specific command::

      (|library|)$ |geniecmd| <command name> --help

