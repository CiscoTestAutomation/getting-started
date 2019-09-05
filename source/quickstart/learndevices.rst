.. _learn-features:

Learn device features
=====================
.. include:: ../definitions/def_feature.rst 

This topic describes how to use the ``learn`` function of the |librarybold| ``Ops`` module for stateful network validation of device features, such as protocols, interfaces, line cards, and other hardware.

.. _cli-learn:

How the |library| "learns" a feature
-------------------------------------
.. include:: ../definitions/def_ops.rst

The output is stored with the same :term:`key-value pair` structure across devices. The stored output makes it possible for you to take a snapshot of the network state at different points in time, and then to :ref:`compare-network-states`.

.. tip:: Why use ``learn`` instead of a :term:`parser`? The parsed output for different devices can result in different data structures. The ``learn`` function, by contrast, results in a *consistent* set of keys, which means that you can write *one* script that works on different devices.

To see a complete list of the features that the |library| can learn, and to see the resulting data structure for each feature, visit the `Models <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/models>`_ page.

Examples of how to learn device features
----------------------------------------
This topic describes how you can tell the system to learn one or more features.

.. attention:: Before you try these examples, make sure that you :download:`download and extract the zip file <mock.zip>` that contains the mock data and Python script.

Learn a single feature
^^^^^^^^^^^^^^^^^^^^^^
To learn one feature on a single device, you can use the device hostname or the device alias (defined in the testbed YAML file). In the following example, ``uut`` is the alias "unit under test" for the host ``nx-osv-1``.

#. In your virtual environment, change to the directory that contains the mock YAML file::

    (pyats) $ cd mock

#. You can use a Python interpreter or the :term:`library command line`.

    * If you want to use Python, you can use ``genie shell`` to load the ``testbed`` API and create your testbed and device objects. Then, connect to the device and tell the system to learn the feature. In this example, the system stores the output as a Python dictionary in the variable ``output``:

       .. code-block:: 

          (pyats) $ genie shell --testbed-file mock.yaml
            >>> dev = testbed.devices['uut']
            >>> dev.connect()
            >>> output = dev.learn('ospf')

      *Result*: The system displays a summary of the parsed ``show`` commands that ran. |br| |br| 

    * If you want to use the CLI::

      (pyats) $ genie learn ospf --testbed-file mock.yaml --devices uut --output output_folder

      *Result*: The system connects to the device, runs the show commands, stores the output in JSON format in the specified directory, and displays a "Learn Summary" that shows the names of the output files. These include:
        
          * Connection log
          * Structured JSON output
          * Device console output |br| |br| 

          .. code-block:: text

                +==============================================================================+
                | Genie Learn Summary for device nx-osv-1                                      |
                +==============================================================================+
                |  Connected to nx-osv-1                                                       |
                |  -   Log: output_folder/connection_uut.txt                                   |
                |------------------------------------------------------------------------------|
                |  Learnt feature 'ospf'                                                       |
                |  -  Ops structure:  output_folder/ospf_nxos_nx-osv-1_ops.txt                 |
                |  -  Device Console: output_folder/ospf_nxos_nx-osv-1_console.txt             |
                |==============================================================================|    

      To see the structured data, use a text editor to open the file :monospace:`output_folder/ospf_nxos_nx-osv-1_ops.txt`.



Learn multiple features
^^^^^^^^^^^^^^^^^^^^^^^^^
You can use the ``learn`` function to get the operational states of multiple or all features, as shown in the following examples.

Learn multiple features on all devices
******************************************
This example shows you how to learn the ``bgp`` and ``ospf`` features on all of the devices in your testbed.

      .. note:: The mock data only contains one device, so you will only see the results for that device.

#. In your virtual environment, change to the directory that contains the mock YAML file::

    (pyats) $ cd mock
    
#. You can use a Python interpreter or the :term:`library command line`.

    * If you want to use Python, you can use ``genie shell`` to load the ``testbed`` API and create your testbed and device objects. Then, tell the system to connect to each device and to learn the specified features. In this example, the system stores the output as a Python dictionary in the variable ``learnt`` and displays the output::

       (pyats) $ genie shell --testbed-file mock.yaml
          >>> learnt = {}
          >>> for name, dev in testbed.devices.items():
          ...     dev.connect()
          ...     learnt[name] = {}
          ...     learnt[name]['bgp'] = dev.learn('bgp')
          ...     learnt[name]['ospf'] = dev.learn('ospf')
          ...

      This example uses a Python ``for`` loop to execute each statement on all devices in the testbed. The system stores the feature information in Python dictionaries, each identified by the device name. |br| |br| 

    * If you want to use the CLI::

       (pyats) $ genie learn bgp ospf --testbed-file mock.yaml --output output_folder

      *Result*: Within the output directory, the system creates the output files and displays a summary for each device.

      The following example shows what you would see.

      .. code-block:: text

        +==============================================================================+
        | Genie Learn Summary for device nx-osv-1                                      |
        +==============================================================================+
        |  Connected to nx-osv-1                                                       |
        |  -   Log: genie_learn/connection_nx-osv-1.txt                                |
        |------------------------------------------------------------------------------|
        |  Learnt feature 'bgp'                                                        |
        |  -  Ops structure:  genie_learn/bgp_nxos_nx-osv-1_ops.txt                    |
        |  -  Device Console: genie_learn/bgp_nxos_nx-osv-1_console.txt                |
        |------------------------------------------------------------------------------|
        |  Learnt feature 'ospf'                                                       |
        |  -  Ops structure:  genie_learn/ospf_nxos_nx-osv-1_ops.txt                   |
        |  -  Device Console: genie_learn/ospf_nxos_nx-osv-1_console.txt               |
        |==============================================================================|

        +==============================================================================+
        | Genie Learn Summary for device csr1000v-1                                    |
        +==============================================================================+
        |  Connected to csr1000v-1                                                     |
        |  -   Log: genie_learn/connection_csr1000v-1.txt                              |
        |------------------------------------------------------------------------------|
        |  Could not learn feature 'bgp'                                               |
        |  -  Exception:      genie_learn/bgp_nxos_csr1000v-1_exception.txt            |
        |  -  Ops structure:  genie_learn/bgp_nxos_csr1000v-1_ops.txt                  |
        |  -  Device Console: genie_learn/bgp_nxos_csr1000v-1_console.txt              |
        |------------------------------------------------------------------------------|
        |  Learnt feature 'ospf'                                                       |
        |  -  Ops structure:  genie_learn/ospf_nxos_csr1000v-1_ops.txt                 |
        |  -  Device Console: genie_learn/ospf_nxos_csr1000v-1_console.txt             |
        |==============================================================================|

      To see the structured data, use a text editor to open any of the ``ops.txt`` files.

Learn all features on one device
**********************************

.. tip:: Use the ``learn all`` functionality to learn all of the supported features on a device. The system returns the results in a format with key-value pairs, and notifies you of any exceptions for features it did not learn.

#. In your virtual environment, change to the directory that contains the mock YAML file::

    (pyats) $ cd mock
    
#. You can use a Python interpreter or the :term:`library command line`.

    * If you want to use Python, you can use ``genie shell`` to load the ``testbed`` API and create your testbed and device objects. Then, connect to the device and tell the system to learn all of the features. In this example, the system stores the output as a Python dictionary in the variable ``output``::

       (pyats) $ genie shell --testbed-file mock.yaml
          >>> dev = testbed.devices['uut']
          >>> dev.connect()
          >>> output = dev.learn('all')

      .. the dev.learn('all') didn't work for me

    * If you want to use the CLI::

      (pyats) $ genie learn all --testbed-file mock.yaml --devices uut --output output_folder

      *Result*: The system saves all of the console and structured output files in JSON format to the specified directory and displays a summary of the results, as shown in the following example. 

      .. code-block:: text

        +=================================================================================+
        | Genie Learn Summary for device nx-osv-1                                         |
        +=================================================================================+
        |  Connected to nx-osv-1                                                          |
        |  -   Log: genie_learn_all/connection_uut.txt                                    |
        |---------------------------------------------------------------------------------|
        |  Could not learn feature 'acl'                                                  |
        |  -  Exception:      genie_learn_all/acl_nxos_nx-osv-1_exception.txt             |
        |  -  Feature not yet developped for this os                                      |
        |---------------------------------------------------------------------------------|
        |  Learnt feature 'bgp'                                                           |
        |  -  Ops structure:  genie_learn_all/bgp_nxos_nx-osv-1_ops.txt                   |
        |  -  Device Console: genie_learn_all/bgp_nxos_nx-osv-1_console.txt               |
        |---------------------------------------------------------------------------------|
        |  Could not learn feature 'dot1x'                                                |
        |  -  Exception:      genie_learn_all/dot1x_nxos_nx-osv-1_exception.txt           |
        |  -  Feature not yet developed for this os                                       |
        |---------------------------------------------------------------------------------|

      To see the structured data, use a text editor to open any of the ``ops.txt`` files.

See also...
*a list of relevant links*

* link 1
* link 2
* link 3







