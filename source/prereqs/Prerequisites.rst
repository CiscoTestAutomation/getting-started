Prerequisites
=============================

Knowledge and skills
---------------------
To understand and use the |getstartedguide|, you'll need to have the knowledge and skills described in the following table.

.. csv-table:: Prerequisite knowledge and skills
   :header: "You should know...", "So that you can..."

   "How to use a command line interface (CLI)", "Install the ecosystem"
   "Fundamentals of network test automation", "Configure the ecosystem with testbed data"
   "GitHub clone and download procedures", "Get |library| packages |br| |br| Contribute to the |pyATS| libraries"
   "Docker image usage (optional)", "Run |pyATS| from the Docker image"
   ":question:`add to this as we go along` ", " "
   " ", " "
   " ", " "
   " ", " "


Requirements
------------
Make sure you have the correct platform, system, and network connectivity in place before you install |pyATSbold| and the |librarybold|.

Hardware
^^^^^^^^^
The |pyATS| ecosystem is lightweight and scalable --- you only need 1 GB of RAM and 1 vCPU to connect to :question:`a small number of` devices. If you have a larger network with more complex configuration, you'll need to increase the memory and processing power of your system. :question:`Can we provide a guideline for memory and processing per number of devices?`

Platform
^^^^^^^^^
The |pyATS| ecosystem runs in a Linux or Linux-type environment. You can install |pyATS| on any of the following platforms:

* Any flavor of Linux, including Ubuntu, CentOS, and Fedora, for example
* macOS (previously Mac OS X)
* `Windows Subsystem for Linux <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`_
* Docker containers (`get our container here <https://hub.docker.com/r/ciscotestautomation/pyats/>`_)

.. tip:: If you're a **Windows user**, we recommend that you set up Windows Subsystem for Linux (WSL). With WSL, you can run |pyATS| and the |library| in your local environment. This enables on-the-go script development and execution over VPN without the need for a server :question:`Does this apply to both internal and external users?`. Use an app such as Ubuntu Terminal to run commands, including bash, ssh, git, and others.

System and software
^^^^^^^^^^^^^^^^^^^^
|pyATS| and the |library| are written in Python. You don't need to know Python, but your system must have one of the following Python versions installed:

.. _supported-python-versions:

* Python 3.5.x
* Python 3.6.x
* Python 3.7.x

The section :ref:`configure-environment` includes details about how to install Python.

.. note:: Python 3.4 has reached its end of life and is now deprecated. |pyATS| and the |library| no longer support Python 3.4.

Network connectivity
^^^^^^^^^^^^^^^^^^^^^
Your host platform must have internet access so that you can:

* Download the Python installation packages (https://pypi.org) or Docker image (https://hub.docker.com).
* Connect to your test devices. You can use Telnet, SSH, Rest, YANG, :question:`What else, and should this list match what's in the Introduction?`
* Access the |pyATS| and |library| GitHub repository at https://github.com/CiscoTestAutomation, to use, develop, or contribute to the :question:`packages`.

.. important:: The |pyATS| ecosystem *never* collects or streams any data or statistics back to Cisco.
:question:`We will probably need a formal legal statement or link to the DevNet privacy policy.`

See also...
*a list of relevant links once we know what these will be*

* link 1
* link 2
* link 3
