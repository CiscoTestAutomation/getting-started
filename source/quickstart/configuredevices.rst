.. _configure-devices:

Configure devices
=====================
This section describes how to use the ``Conf`` module of the |librarybold| to quickly and easily apply configuration changes when you want to automate your network testing.

.. include:: ../definitions/def_conf.rst

Because the |library| uses a common structure across devices, you can save time and effort when you automate your network testing.

.. _cli-conf:

How you use the |library| to configure a device
------------------------------------------------
Like the :term:`parser`, the |library| ``Conf`` module uses the same :term:`key-value pair` structure across devices. This results in a *consistent* set of keys, which means that you can write *one* script that works to configure different devices. You simply define the feature attributes, and the |library| figures out how to apply the configuration to each different device.

To see a complete list of the structure and keys, visit the `Models <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/models>`_ page, select a :term:`feature`, and then select **MODEL**.

Examples of how to configure devices
----------------------------------------
This section describes how you can tell the system to learn one or more features.

.. attention:: Before you try these examples, make sure that you :download:`download and extract the zip file <mock.zip>` that contains the mock data and Python script.

Learn a single feature
^^^^^^^^^^^^^^^^^^^^^^
To learn one feature on a single device, you can use the device hostname or the device alias (defined in the testbed YAML file). In the following example, ``uut`` is the alias "unit under test" for the host ``nx-osv-1``.

#. In your virtual environment, change to the directory that contains the mock YAML file::

    (pyats) $ cd mock

#. You can use a Python interpreter or the :term:`library command line`.

    * If you want to use Python, you can use ``|geniecmd| shell`` to load the ``testbed`` API and create your testbed and device objects. Then, connect to the device and tell the system to learn the feature and store the output in a directory::

       (pyats) $ genie shell --testbed-file mock.yaml
          >>> dev = testbed.devices['uut']
          >>> dev.connect()
          >>> output = dev.learn('ospf') WHAT IS THE OPTION TO PRINT THE OUTPUT TO A FILE FOR LATER DIFF?

      *Result*: The system displays a summary of the parsed ``show`` commands that ran. |br| |br| 

    * If you want to use the CLI::

      (pyats) $ |geniecmd| learn ospf --testbed-file mock.yaml --devices uut --output output_folder

      *Result*: The system connects to the device, runs the show commands, stores the output in the specified directory, and displays a "Learn Summary" that shows the names of the output files. These include:
        
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

#. To see the structured data, use a text editor to open the file ``output_folder/ospf_nxos_nx-osv-1_ops.txt``.



Learn multiple features
^^^^^^^^^^^^^^^^^^^^^^^^^
You can use the "learn" function to get the operational states of multiple or all features, as shown in the following examples. :question:`Should we show Python examples also?`

Learn multiple features on all devices
******************************************

Run the command::

 (pyats) $ |geniecmd| learn bgp ospf --testbed-file mock.yaml --output output_folder

*Result*: Within the output directory, the system creates the output files and displays a summary for each device.

  .. code-block::

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

Learn all features on one device
**********************************

Run the command::

 (pyats) $ |geniecmd| learn all --testbed-file mock.yaml --devices uut --output output_folder

*Result*: The system saves all of the console and structured output files to the specified directory and displays a summary of the results for each feature, as shown in the following snippet. 

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


See also...
*a list of relevant links*

* link 1
* link 2
* link 3







