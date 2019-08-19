.. _pre-reqs:

Prerequisites
=============================

Knowledge and skills
---------------------
To understand and use the |getstartedguide|, you'll need to have the knowledge and skills described in the following table.

.. csv-table:: Prerequisite knowledge and skills
   :header: "You should know...", "So that you can..."

   "Linux (on Mac and Windows)", "Install and use the ecosystem"
   "Fundamentals of network test automation", "Configure the ecosystem with testbed data"
   "(Optional) GitHub clone and download procedures", "Get |library| packages |br| |br| Contribute to the |pyATS| libraries"
   "(Optional) Docker image usage (optional)", "Run |pyATS| from the Docker image"
  
.. _requirements:

Requirements
------------
Make sure you have the correct platform, system, and network connectivity in place before you install |pyATSbold| and the |librarybold|.

Hardware
^^^^^^^^^
The |pyATS| ecosystem is lightweight and scalable --- you only need 1 GB of RAM and 1 vCPU to start your network automation. If you have a large network with more complex configuration, you'll need to increase the memory and processing power of your system. The types of tests that you run also affect the amount of memory required.

Platform
^^^^^^^^^
The |pyATS| ecosystem runs in a Linux or Linux-type environment. You can install |pyATS| on any of the following platforms:

* Any flavor of Linux, including Ubuntu, CentOS, and Fedora, for example
* macOS (previously Mac OS X)
* `Windows Subsystem for Linux <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`_
* Docker containers (`get our container here <https://hub.docker.com/r/ciscotestautomation/pyats/>`_)

.. include:: supportedLinux.rst

.. tip:: If you're a **Windows user**, we recommend that you set up Windows Subsystem for Linux (WSL). With WSL, you can run |pyATS| and the |library| in your local environment. This enables on-the-go script development and execution on your local machine, without the need to connect to a server.

System and software
^^^^^^^^^^^^^^^^^^^^
|pyATS| and the |library| are written in Python. You don't need to know Python, but your system must have one of the following Python versions installed:

    .. include:: supportedpythonversions.rst

The section :ref:`configure-environment` includes details about how to install Python.

.. note:: Python 3.4 has reached its end of life and is now deprecated. |pyATS| and the |library| no longer support Python 3.4.

Network connectivity
^^^^^^^^^^^^^^^^^^^^^
Your host platform must have internet access when you want to:

 * Install or upgrade |pyATS| (https://pypi.org) or use the Docker image (https://hub.docker.com).
 * Access the |pyATS| and |library| GitHub repository at https://github.com/CiscoTestAutomation, to use, develop, or contribute to the :question:`packages (to be decided 2019/08/19 about the terminology)`.

For test automation or command execution, you only need device connectivity. You can use Telnet, SSH, REST, RESTCONF, NETCONF, and YANG.

.. important:: The |pyATS| ecosystem *never* collects or streams any data or statistics back to Cisco.

..
    I checked on the devnet site and didn't see anything to add about data privacy.

See also...
*a list of relevant links once we know what these will be*

* link 1
* link 2
* link 3
