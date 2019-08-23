.. _pre-reqs:

Prerequisites
=============================

Knowledge and skills
---------------------
To understand and use the |getstartedguide|, you'll need to have the knowledge and skills described in the following table.

.. csv-table:: Prerequisite knowledge and skills
   :header: "You should know...", "So that you can..."

   "|linux_reg| (on |mac_reg| and |windows_reg|)", "Install and use the ecosystem"
   "Fundamentals of network test automation", "Configure the ecosystem with testbed data"
   "(Optional) |github_reg| clone and download procedures", "Get |library| packages |br| |br| Contribute to the |pyATS| libraries"
   "(Optional) |docker_reg| image usage (optional)", "Run |pyATS| from the Docker image"

.. _statement-structure:

Structure of a |pyATS| statement
----------------------------------
Although you don't need to know Python to use the |pyATS| ecosystem, it might help you to understand the structure of the Python-based commands described in this guide. 

.. tip:: Remember, you can use the :term:`library command line` for network automation and never have to enter a Python command!

The following example explains the statements used to connect to a device and parse output from the ``show inventory`` command.

.. csv-table:: Structure of a |pyATS| statement
   :header: "Number", "Statement", "Description"
   :widths: 5, 40, 55

   "1", "``from genie.testbed import load``", "Get the ``genie.testbed`` library and its ``load`` function."
   "2", "``tb = load('tb.yaml')``", "Load the ``tb.yaml`` testbed and store it in the ``tb`` variable."
   "3", "``dev = tb.devices['nx-osv-1']``", "Find the ``nx-osv-1`` device and store it in the variable ``dev``."
   "4", "``dev.connect()``", "Connect to the device you defined as ``dev``."
   "5", "``p1 = dev.parse('show inventory')``", "Parse the ``show inventory`` output for ``dev``, and store the output in the variable ``p1``."
   "6", "|line6|", "Print a meaningful message and the serial number for Slot 1."

.. tip:: If you want to know more about how to use Python, you can find many good online tutorials.
  
.. _requirements:

Requirements
------------
Make sure you have the correct platform, system, and network connectivity in place before you install |pyATSbold| and the |librarybold|.

Hardware
^^^^^^^^^
The |pyATS| ecosystem is lightweight and scalable --- you only need 1 GB of RAM and 1 vCPU to start your network automation. If you have a large network with more complex configuration, you'll need to increase the memory and processing power of your system. The types of tests that you run also affect the amount of memory required.

Platform
^^^^^^^^^
The |pyATS| ecosystem runs in a |linux_reg| or Linux-type environment. You can install |pyATS| on any of the following platforms:

* Any flavor of Linux, including |ubuntu_reg|, CentOS, and Fedora, for example
* macOS (previously Mac OS X)
* Docker containers (`get our container here <https://hub.docker.com/r/ciscotestautomation/pyats/>`_)
* `Windows Subsystem for Linux <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`_

.. include:: supportedLinux.rst

.. note:: 

    * The |pyATS| ecosystem does not support |windows_reg|.
    * If you're a Windows user, we recommend that you set up Windows Subsystem for Linux (WSL). With WSL, you can run |pyATS| and the |library| in your local environment. This enables on-the-go script development and execution on your local machine, without the need to connect to a server.
    * Your Linux emulator - such as Ubuntu - might already have Python installed. Make sure to :ref:`check your version of Python <check-python>`.

System and software
^^^^^^^^^^^^^^^^^^^^
|pyATS| and the |library| are written in Python. You don't need to know Python, but your system must have one of the following Python versions installed:

    .. include:: supportedpythonversions.rst

.. note:: Python 3.4 has reached its end of life and is now deprecated. |pyATS| and the |library| no longer support Python 3.4.

The section :ref:`configure-environment` includes instructions on how to :ref:`check your version of Python <check-python>` and :ref:`set up a Python virtual environment <set-up-venv>`.

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
