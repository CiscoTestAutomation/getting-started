.. _quick-start:

Quick start instructions
=============================
This topic will get you up and running quickly, and includes the following information:

* Tips on how to use the |library|
* Real-life scenarios
* Hands-on practice procedures

When to use the |library|
-------------------------
Use the |library| any time you want to configure or check the health of your network. Cisco makes the automated tests used during product development available externally, so customers can run the same tests on their own networks. This is a win-win situation for Cisco and our customers!

.. qs-update::

Keep |pyATS| up to date
-----------------------------
On the last Tuesday of the month, the team releases a new version of |pyATS| and the |library|. This section describes how to get the latest changes.

.. qs-upgrade::

To upgrade the |pyATS| and |library| :doc:`infrastructure </definitions/def_pyats_code_infrastructure>`, and any or all of the :doc:`feature libraries and components </definitions/def_pyatslibrary_code_structure>`, run the ``pip install --upgrade`` command from your virtual environment.

Internal Cisco users
^^^^^^^^^^^^^^^^^^^^^

.. tip:: Cisco members of the "pyats-notices" mailer list receive a notification about each release. :question:`How does an internal user sign up to the notices?`

.. csv-table:: Upgrade options
    :file: UpgradeInternal.csv
    :header-rows: 1
    :widths: 20 30 50



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
* `Cisco Virtual Internet Routing Lab <http://virl.cisco.com/>`
