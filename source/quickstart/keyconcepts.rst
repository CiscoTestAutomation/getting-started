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
    The term *abstraction* refers to the separation of network control from the actual, physical network infrastructure (devices). This enables you to use |pyATS| and the |library| across different platforms, operating systems, and hardware.


   Feature
    .. include:: ../definitions/def_feature.rst 


   Stateful validation
    Configuration changes often result in a series of operational state changes. For example, you might see changes to the following items:

    * Interface status
    * Routing
    * Neighbors

    With just a few commands or an automated script, you can use the |library| to profile your system before and after a configuration change to see a detailed list of the changes.


   Testbed 
    In the |pyATS| ecosystem, a testbed represents a set of connected devices. You run your automated network tests on the testbed that you define.

   Testbed YAML file
    With |pyATS| and the |library|, you describe your devices under test (your testbed) in a `YAML <http://www.yaml.org/start.html>`_ file named ``testbed.yaml``. The file describes your physical devices and how they link together to form the testbed network topology.

   
   Test automation
    The term *test automation* refers to how you use the |library| to combine any number of test scripts and run them at scheduled intervals, under different test conditions. The |library| gives you the flexibility to scale coverage, configuration, and runtime based on your testing requirements.

   Library command line
    The |library| command line interface (CLI) is a powerful, Linux-based command-line utility that gives you |library| Python functionality directly from a Linux terminal (or emulator). The CLI is easy to use, even if you don't know anything about Python or programming.

   Trigger
    A trigger is an action or sequence of actions performed on a device, which changes the device state or configuration. 

   Verification
    A verification is the execution of a show command to retrieve the current state of one or more devices. A verification typically runs before and after an action (trigger) to compare the previous and current device states.

   Show command
    The term *show command* refers to a type of Linux command that you use to get information about a networking device, such as a router or switch. For example, ``show version`` returns information about the OS version of a device.

   Parser
    .. include:: ../definitions/def_parser.rst 

   Harness
    The |library| Harness module controls the flow of your network automation and testing, based on user-provided :term:`arguments` (input). For example, you can input the sequence of setup, triggers, verifications, and tear-down (cleanup) that you want to execute.


   Devices
    Devices are network components such as routers, switches, servers, traffic generators, and other hardware products.

   Ops 
    .. include:: ../definitions/def_ops.rst

   Conf 
    .. include:: ../definitions/def_conf.rst

   Robot Framework
    Robot Framework is a generic Python test automation framework that focuses on acceptance test automation using English-like, easy-to-use keywords to define test cases.

   Arguments
    Arguments are simply input parameters.

   SDK library functions/API
    A |library| function is a series of actions or retrieval commands executed on a device, such as an interface shutdown. The functions provide clear exception messages if an action fails.

   Object 
    The term *object* refers to an entity that the |pyATS| ecosystem can access and act on. You can think of an object as a "container" of information, with actual values. 

   Key-value pair 
    A key-value pair is a set of linked data, where the key is an identifier and the value is the actual information. For example, ``Device name: nx-osv-1`` has the key ``Device name`` and the value ``nx-osv-1``.

   |pyATS| packages
    The |pyATS| ecosystem is available externally through `Cisco DevNet <https://developer.cisco.com/pyats/>`_. We release slightly different packages for internal and external users to ensure that the packages work correctly in different environments. Differences include:

    * Package format - where the code is not open source
    * Package names - ``ats`` internally, ``pyats`` externally
    * Source location for installation files
    * Architecture (32-bit available internally *only*)
    * Defaults - no Cisco-specific defaults for external release

   Mock devices
    The term *mock device* refers to a set of recorded device interactions that you can replay any time you want to practice with or demo the |pyATS| ecosystem. 

   Unicon
    Unicon is a framework for developing device control libraries for routers, switches and servers. It is developed purely in Python, with no dependency on Tcl-based infrastructure. Unicon is also test framework agnostic and can be used with |pyATS|. We use *Unicon.playback* to create :term:`mock devices`.




