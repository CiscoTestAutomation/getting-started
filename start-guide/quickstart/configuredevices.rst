.. _configure-devices:

Configure devices
=====================
This topic describes how to use the ``Conf`` module of the |librarybold| to quickly and easily apply configuration changes when you want to automate your network testing.  You take care of the *what* --- the |library| takes care of the *how*!

.. include:: ../definitions/def_conf.rst
   :start-line: 3

Because the |library| uses a common, feature-based structure across platforms, you can save time and effort when you automate your network testing.

.. _cli-conf:

How you use the |library| to configure a device
------------------------------------------------
Like the :term:`parser`, the |library| ``Conf`` module uses the same :term:`key-value pair` structure across devices. This results in a *consistent* set of keys, which means that you can write *one* script that works to configure different devices. 

You simply define the feature attributes, and the |library| figures out how to apply the configuration to each different device.

To see a complete list of the structure and keys, visit the `Models <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/models>`_ page, select a :term:`feature`, and then select **MODEL**.

Examples of how to configure devices
----------------------------------------
This topic describes how to use the Python interpreter or a Python script to use the ``Conf`` module functionality. Because you use it primarily for automated test scripts, we have not provided a command line option.

The process to configure devices is simple:

 1. Define the device (:term:`object`) attributes.
 2. Tell the |library| to apply the configuration.

.. attention:: Before you try these examples, make sure that you :download:`download and extract the zip file <mock.zip>` that contains the mock data and Python script.

.. _config-feature:

Configure a feature on a device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This example shows you how to configure a single feature on a single device. You can use the device hostname or the device alias (defined in the testbed YAML file). In the following example, ``uut`` is the alias "unit under test" for the host ``nx-osv-1``.

#. In your virtual environment, change to the directory that contains the mock YAML file::

    (pyats) $ cd mock

#. Load the ``testbed`` API and create your testbed and device objects::

    (pyats) $ genie shell --testbed-file mock.yaml

        >>> uut = testbed.devices['uut']

#. Get the |library| ``Interface`` functionality, to configure an interface on the ``uut`` device::

        >>> from genie.conf.base import Interface

#. Connect to the device and tell the system to create an NXOS interface::

        >>> uut.connect()

#. Create an NXOS interface::

        >>> nxos_interface = Interface(device=uut, name='Ethernet4/3')

#. Configure the interface that you just created::

        >>> nxos_interface.ipv4 = '200.1.1.2'
        >>> nxos_interface.ipv4.netmask ='255.255.255.0'
        >>> nxos_interface.switchport_enable = False
        >>> nxos_interface.shutdown = False

#. Verify that the system generated the configuration::

        >>> print(nxos_interface.build_config(apply=False))

   The argument ``(apply=False)`` shows you what *will* be applied on the device if you go ahead with the build.     

   *Result*: The system displays the following configuration information::

        interface Ethernet4/3
        no shutdown
        no switchport
        ip address 200.1.1.2 255.255.255.0
        exit

#. To build the configuration and apply it to the device::

        >>> nxos_interface.build_config(apply=False)

   We've included the argument ``(apply=False)`` because you can't actually build the configuration on a mock device. |br| |br| 


#. To remove the configuration from the device::

        >>> nxos_interface.build_unconfig(apply=False)

Configure one attribute
^^^^^^^^^^^^^^^^^^^^^^^^
If you want to change the configuration of a device, or if you want to partially configure a device, you can tell the |library| which attributes to apply.

By default, the |library| applies the configuration from step 6 of the previous example. To limit the configuration to a single attribute, you can specify the attribute in an argument::

 >>> nxos_interface.build_config(apply=False, attributes={'ipv4':None})

In this example, the system applies *only* the configuration of the ``ipv4`` attribute to the device. Because the system uses a dictionary that stores key-value pairs, ``None`` serves as a placeholder value that has no effect on the configuration.

Configure multiple devices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can apply configuration settings to all the devices in your testbed, rather than to a specific device or feature. This means that you can do all of the configuration, and then apply the settings with just one "build". 

#. In your virtual environment, change to the directory that contains the mock YAML file::

    (pyats) $ cd mock

#. Load the ``testbed`` API and create your testbed and device objects::

    (pyats) $ genie shell --testbed-file mock.yaml

        >>> uut = testbed.devices['uut']

#. Get the |library| functionality that you need to create each feature, for example::

        >>> from genie.conf.base import Interface
        >>> from genie.libs.conf.ospf import Ospf
        >>> from genie.libs.conf.isis import Isis
        >>> from genie.libs.conf.rip import Rip

#. Connect to the device and tell the system to create an NXOS interface::

        >>> uut.connect()

#. Create two NXOS interfaces::

        >>> nxos_interface = Interface(device=uut, name='Ethernet4/3')
        >>> nxos_interface = Interface(device=uut, name='Ethernet4/4')


#. Configure all of the features on all of your testbed devices, line by line. 

   At this point, we provide examples because you cannot run the ``testbed.build_config`` command on the mock data. This example shows two devices, each with its own interface.

   .. tip:: Refer to the feature `model <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/models>`_ page to see which attributes (keys) you can configure.

   .. code-block:: python

    testbed.build_config() 
     >>> [2018-09-25 09:55:39,982] +++ csr1000v-1: config +++                            
        config term                                                                     
        Enter configuration commands, one per line.  End with CNTL/Z.                   
        csr1000v-1(config)#interface GigabitEthernet1                                   
        csr1000v-1(config-if)# ip address 200.1.1.2 255.255.255.0                       
        csr1000v-1(config-if)# no shutdown                                              
        csr1000v-1(config-if)# logging event link-status                                
        csr1000v-1(config-if)# ipv6 enable                                              
        csr1000v-1(config-if)# exit                                                     
        csr1000v-1(config)#end                                                          
        csr1000v-1#                                                                     
        [2018-09-25 09:55:41,382] +++ nx-osv-1: config +++                              
        config term                                                                     
        Enter configuration commands, one per line.  End with CNTL/Z.                   
        nx-osv-1(config)# interface Ethernet4/7                                         
        nx-osv-1(config-if)#  no shutdown                                               
        nx-osv-1(config-if)#  logging event port link-status                            
        nx-osv-1(config-if)#  no switchport                                             
        nx-osv-1(config-if)#  ip address 200.1.1.2 255.255.255.0                        
        nx-osv-1(config-if)#  exit                                                      
        nx-osv-1(config)# end                                                           
        nx-osv-1#                                                                       

   *Result*: This builds and applies the configuration settings all at once to your testbed devices.

.. note:: Remember that the output of the configuration may vary depending on the device context (such as cli or YANG), but the configuration keys remain the same across all devices!



See also...

* `Description of the Conf module <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/Conf/index.html#conf-guide>`_







