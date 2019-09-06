.. _compare-network-states:

Compare network states
======================
Once you know how to :ref:`parse device output <parse-output>` or :ref:`learn device features <learn-features>`, you can begin to unleash the power of the |librarybold| for stateful network validation! 

This topic describes how to use the ``Diff`` functionality to monitor your network and to verify that your network is performing as expected.

.. include:: ../definitions/def_diff.rst 
   :start-line: 3

.. tip:: You don't need to know Python -- the :ref:`Library CLI <genie-cli>` includes a ``Diff`` command that you can run in your Linux terminal.

How stateful validation works
-----------------------------
Using the |library|, you can collect and compare network state information on demand, or as scheduled jobs that run your automation scripts. The process is simple:

 #. Take a snapshot of your network.
 #. Make or observe a change in your network.
 #. Take another snapshot.
 #. Use ``Diff`` to see the changes.
 
For example, you can set up a scheduled job to take a new snapshot every day, to make sure your network is running as it should and to see any configuration changes. The result is a Linux-style list of additions, deletions, and changes.


Examples of stateful validation
-------------------------------
The following examples show how you can monitor changes in configuration and state, using both learned and parsed output. 

Remember that ``learn`` runs multiple ``show`` commands and creates a consistent output structure across devices. By contrast, ``parse`` typically parses the output of a single ``show`` command, with output structure that is consistent for each device but can vary across devices.

.. tip:: For a detailed example that includes automation, see the workshop `DevNet-2595: Stateful Network Validation using pyATS+Genie and Robot Framework <https://github.com/CiscoTestAutomation/CL-DevNet-2595/blob/master/README.md>`_.

Compare learned snapshots
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In this example, you'll see how to take snapshots with the ``learn`` function, save the snapshots to different directories, and then compare the data.

.. note:: We'll show you all of the actions and results, because mock data doesn't work with this example. The `workshop <https://github.com/CiscoTestAutomation/CL-DevNet-2595/blob/master/README.md>`_ provides examples that you can try yourself.

#. With your devices already configured and running, take a snapshot of the ``bgp`` feature and save it to the directory (or variable) ``output1``. You can use a Python interpreter or the :term:`Library command line`.

    * If you want to use Python, use ``genie shell`` to load the ``testbed`` API and create your testbed and device objects. Then, tell the system to connect to each device and to learn the specified feature::

       (pyats) $ genie shell --testbed-file tb.yaml
          >>> output1 = {}
          >>> for name, dev in tb.devices.items():
          ...     dev.connect()
          ...     output1[name] = {}
          ...     output1[name]['bgp'] = dev.learn('bgp')
          ...

      This example uses a Python ``for`` loop to execute each statement on all devices in the testbed. 
      
      *Result*: The system stores the feature information in a Python dictionary, which includes the data for all devices. |br| |br| 

    * If you want to use the CLI::

       (pyats) $ genie learn "bgp" --testbed-file tb.yaml --output output1

      *Result*: The system creates the output directory ``output1``, stores the ``ops.txt`` device files in JSON format, and displays a summary for each device:

       .. code-block:: text

        +==============================================================================+
        | Genie Learn Summary for device nx-osv-1                                      |
        +==============================================================================+
        |  Connected to nx-osv-1                                                       |
        |  -   Log: output1/connection_nx-osv-1.txt                                    |
        |------------------------------------------------------------------------------|
        |  Learnt feature 'bgp'                                                       |
        |  -  Ops structure:  output1/bgp_nxos_nx-osv-1_ops.txt                       |
        |  -  Device Console: output1/bgp_nxos_nx-osv-1_console.txt                   |
        |==============================================================================|


#. Change the configuration of a feature on a device, or shut down/bring up an interface.

#. Repeat step 1 to take another snapshot, but specify a different output directory or variable, such as ``output2``.

#. Compare the two snapshots:

    * Python::

        >>> from genie.utils.diff import Diff
        >>> diff = Diff(output1.info, output2.info)
        >>> diff.findDiff()
        >>> print(diff)
    
    * |library| CLI::

       $ (pyats) genie diff output1 output2 

    *Result*: The system displays any differences. 
    
    .. note:: ``+`` indicates an addition, ``-`` indicates a deletion, and ``+`` followed by ``-`` indicates a change.

    .. code-block:: python

        more output/diff_bgp_nxos_nxos-osv-1_ops.txt
        --- output1/bgp_nxos_nxos-osv-1_ops.txt
        +++ output2/bgp_nxos_nxos-osv-1_ops.txt
        info:
        instance:
        default:
        vrf:
            default:
            neighbor:
            50.1.1.101:
            address_family:
                ipv4 multicast:
        +         session_state: active
        -         session_state: idle
                ipv4 unicast:
        +         session_state: active
        -         session_state: idle
    
    In this example, you can see that ``ipv4 multicast`` and ``ipv4 unicast`` both changed from idle to active.

Compare parsed snapshots
^^^^^^^^^^^^^^^^^^^^^^^^^
In this example, you can see how to :ref:`parse the output <parse-output>` of a single ``show`` command at two different points in time, and then use ``Diff`` to compare the output.

.. tip:: Because the parsed output structure can vary across devices, this example shows you how to take a snapshot on a single device. You can, of course, write a script that automates this process for every device in your network.

#. With your device already configured and running, take a snapshot and save it to the directory (or variable) ``po1``. You can use a Python interpreter or the :term:`Library command line`.

    * If you want to use Python, use ``genie shell`` to load the ``testbed`` API and create your testbed and device objects. Then, tell the system to connect to a device and parse the specified command::

       (pyats) $ genie shell --testbed-file tb.yaml
          >>> dev = tb.devices['uut']
          >>> dev.connect()
          >>> po1 = dev.parse('show ip ospf interface brief')

      *Result*: The system stores the parsed output in a Python dictionary. |br| |br| 

    * If you want to use the CLI::

       (pyats) $ genie parse "show ip ospf interface brief" --testbed-file tb.yaml --devices uut --output po1

      *Result*: The system creates the output directory ``po1``, stores the ``parsed.txt`` file in JSON format, and displays a summary for the device:

       .. code-block:: text

        +==============================================================================+
        | Genie Parse Summary for nx-osv-1                                             |
        +==============================================================================+
        |  Connected to nx-osv-1                                                       |
        |  -  Log: po1/connection_nx-osv-1.txt                                         |
        |------------------------------------------------------------------------------|
        |  Parsed command 'show ip ospf interface brief'                               |
        |  -  Parsed structure: po1/nx-osv-1_show-ip-ospf-interface-brief_parsed.txt   |
        |  -  Device Console:   po1/nx-osv-1_show-ip-ospf-interface-brief_console.txt  |
        |------------------------------------------------------------------------------|

#. Shut down an interface.

#. Repeat step 1 to take another snapshot, but specify a different output directory or variable, such as ``po2``.

#. Compare the two snapshots:

    * Python:

     .. code-block:: python

        >>> from genie.utils.diff import Diff
        >>> diff = Diff(po1, po2)
        >>> diff.findDiff()
        >>> print(diff)
    
    * |library| CLI::

       $ (pyats) genie diff po1 po2 

    *Result*: The system displays any differences.

     .. code-block:: python

         GigabitEthernet2:
        +      nbrs_count: 0
        -      nbrs_count: 1
        +      nbrs_full: 0
        -      nbrs_full: 1
        +      state: DOWN
        -      state: P2P

    You can see in this example that ``GigabitEthernet2`` is now down.

See also...
 
 * `Master workshop <https://github.com/CiscoTestAutomation/CL-DevNet-2595/blob/master/workshop.md>`_
 * `More Diff examples <https://pubhub.devnetcloud.com/media/genie-docs/docs/cli/genie_diff.html#genie-diff>`_
 * `Use case for parsed output <https://pubhub.devnetcloud.com/media/genie-docs/docs/solutions/index.html#genie-solutions>`_






