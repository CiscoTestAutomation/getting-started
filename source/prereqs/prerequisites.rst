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

* Most flavors of Linux, including |ubuntu_reg|, CentOS, and Fedora, for example
* macOS (previously Mac OS X)
* Docker containers (`get our container here <https://hub.docker.com/r/ciscotestautomation/pyats/>`_)
* `Windows Subsystem for Linux <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`_

.. include:: supportedLinux.rst
   :start-line: 3

.. note:: 

    * The |pyATS| ecosystem does not support |windows_reg|.
    * If you're a Windows user, we recommend that you set up Windows Subsystem for Linux (WSL). With WSL, you can run |pyATS| and the |library| in your local environment. This enables on-the-go script development and execution on your local machine, without the need to connect to a server.
    * Your Linux emulator - such as Ubuntu - might already have Python installed. Make sure to :ref:`check your version of Python <check-python>`.

System and software
^^^^^^^^^^^^^^^^^^^^
|pyATS| and the |library| are written in Python. You don't need to know Python, but your system must have one of the following Python versions installed:

    .. include:: supportedpythonversions.rst
       :start-line: 5

.. note:: Python 3.4 has reached its end of life and is now deprecated. |pyATS| and the |library| no longer support Python 3.4.

After you install Python, check to make sure that you have the following packages:

* python3-venv
* python3-dev
* libpython3-dev
* build-essential

.. note:: You can check for installed packages using the standard Linux commands. In Ubuntu, for example, run ``apt list --installed``.

The section :ref:`configure-environment` includes instructions on how to :ref:`check your version of Python <check-python>` and :ref:`set up a Python virtual environment <set-up-venv>`.

Network connectivity
^^^^^^^^^^^^^^^^^^^^^
Your host platform must have internet access when you want to:

 * Install or upgrade |pyATS| (https://pypi.org) or use the Docker image (https://hub.docker.com/r/ciscotestautomation/pyats/).
 * Access the |pyATS| and |library| GitHub repository at https://github.com/CiscoTestAutomation, to use, develop, or contribute to the packages.

For test automation or command execution, you only need device connectivity. You can use Telnet, SSH, REST, RESTCONF, NETCONF, and YANG.

.. important:: The |pyATS| ecosystem *never* collects or streams any data or statistics back to Cisco.

..
    I checked on the devnet site and didn't see anything to add about data privacy.

See also...

* `Cisco DevNet <https://developer.cisco.com/>`_
* `The Python Tutorial <https://docs.python.org/3.7/tutorial/>`_
* `GitHub Learning Labs <https://lab.github.com/>`_
