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


   Features
    The term *feature* typically refers to a network protocol, represented by the |library| as a Python object, with attributes that represent the feature (protocol) configuration on a device. Many networks use a combination of different features, such as MPLS, BGP, and EIGRP.


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

   |library| command line
    The |library| command line interface (CLI) is a powerful, Linux-based command-line utility that gives you |library| Python functionality directly from a Linux terminal (or emulator). The CLI is easy to use, even if you don't know anything about Python or programming.

   Trigger
    A trigger is an action or sequence of actions performed on a device, which changes the device state or configuration. 

   Verification
    A verification is the execution of a show command to retrieve the current state of one or more devices. A verification typically runs before and after an action (trigger) to compare the previous and current device states.

   Show command
    The term *show command* refers to a type of Linux command that you use to get information about a networking device, such as a router or switch. For example, ``show version`` returns information about the OS version of a device.

   Parser
    A parser converts device output into a Python dictionary, which stores the device data as a set of key-value pairs. This process harmonizes the data (makes it consistent) across different types of communication interfaces, including CLI, REST, NETCONF, and others. 
    
    The |library| parsers create standardized output for ``show`` commands, which means that you can write and run reusable automation scripts. In the |pyATS| ecosystem, parsers are typi cally written using the Metaparser package.

   Harness
    The |library| Harness module controls the flow of your network automation and testing, based on user-provided input (arguments). For example, you can input the sequence of setup, triggers, verifications, and tear-down (cleanup) that you want to execute.


   Devices
    Devices are network components such as routers, switches, servers, traffic generators, and other hardware products.

   Ops 
    The |library| Ops module is a representation of the current operational state of a device, per feature (protocol). It "learns" the operational state by executing a series of show commands and parsing them into a Python dictionary.

   Conf 
    The |library| Conf module provides a way for you to configure a network device without having to build the configuration yourself. Instead, you can generate reusable, multi-line configuration strings and apply them to one or more devices all at once.

   Robot Framework
    Robot Framework is a generic Python test automation framework that focuses on acceptance test automation using English-like, easy-to-use keywords to define test cases.

   Argument
    An argument is an input parameter.

   SDK library functions/API
    A |library| function is a series of actions or retrieval commands executed on a device, such as an interface shutdown. The functions provide clear exception messages if an action fails.

   Object 
    The term *object* refers to an entity that the |pyATS| ecosystem can access and act on. You can think of an object as a "container" of information, with actual values. 

   Key-value pair 
    A key-value pair is a set of linked data, where the key is an identifier and the value is the actual information. For example, ``Device name: nx-osv-1`` has the key "Device name" and the value "nx-osv-1".

   |pyATS| packages
    * For *internal Cisco users*, a |pyATS| package
    * For *DevNet community users*, a |pyATS| package 




