.. _quick-start:

Quick start instructions
=============================
This topic will get you up and running quickly, and includes the following information:

* Tips on how to use the |library|
* Real-life scenarios
* Hands-on practice procedures








Practice using the |library| for network automation
----------------------------------------------------
The following sections provide step-by-step instructions that will give you some guided practice with the |library|.

Launch a simulated testbed
^^^^^^^^^^^^^^^^^^^^^^^^^^^
This section describes how you can connect to a simulated testbed of devices using the `Cisco Virtual Internet Routing Lab (VIRL) <http://virl.cisco.com>`_. This enables you to give the |library| a try, even if you don't have your own network of devices.

#. We recommend that  you reserve and use the `Multi-IOS Cisco Test Network Sandbox <https://devnetsandbox.cisco.com/RM/Diagram/Index/6b023525-4e7f-4755-81ae-05ac500d464a?diagramType=Topology>`_. 

    .. tip:: The sandbox can get busy, so you might want to reserve it a few days in advance.

    * Go to the `Multi-IOS Cisco Test Network Sandbox <https://devnetsandbox.cisco.com/RM/Diagram/Index/6b023525-4e7f-4755-81ae-05ac500d464a?diagramType=Topology>`_.

    * At the top right, select **Reserve**.

    * In the **Schedule** section, choose your preferred time slot.

    * In the **Parameter** section, from the **Value** list, select **None**.

        .. image:: ../images/ReserveSandbox.png

    * Select **Reserve**, and then follow the instructions to complete the reservation.

#. Next step...

Parse...
^^^^^^^^^

Run a test script
^^^^^^^^^^^^^^^^^^^





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

.. _clone-git-examples:

Download or clone the Git repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
