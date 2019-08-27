.. _compare-network-states:

Compare network states
======================
Once you know how to :ref:`parse-output` or :ref:`learn device features <learn-features>`, you can begin to unleash the power of the |librarybold| for stateful network validation! This topic describes how to use the ``learn`` and ``Diff`` functionality to collect and compare information about your network, after an event or over time. This helps you to verify that your network is performing as expected.

.. include:: ../definitions/def-diff.rst 

How stateful validation works
-----------------------------
The |library| provides an easy way for you to collect and compare network information, either in real-time or as scheduled jobs that run your automation scripts. In the following examples, we show you the basics of how to:

 #. Learn the topology of the network (see the topic :ref:`learn-features`). Remember that the ``learn`` function parses the output of show commands into a common data structure that's consistent across devices and platforms.
 #. :ref:`configure-devices` to change a feature on a device.
 #. Use the ``Diff`` library to collect and compare before and after states. The result is a Linux-style list of additions, deletions, and changes.

You can use the ``Diff`` library to monitor your network state over time, to check if anything changes. Just take a new snapshot every day.


Examples of stateful validation
-------------------------------
The following examples show how you can monitor changes in configuration or changes over time.

.. tip:: For a more detailed, step-by-step introduction, see the workshop `DevNet-2595: Stateful Network Validation using pyATS+Genie and Robot Framework <https://github.com/CiscoTestAutomation/CL-DevNet-2595/blob/master/README.md>`_.

Changes in configuration
^^^^^^^^^^^^^^^^^^^^^^^^
In this example, you'll see how to take snapshots with the ``learn`` function, save them to different directories, and then compare them. 

.. note:: Because you can't configure the mock data, we'll show you all of the actions and results. The `workshop <https://github.com/CiscoTestAutomation/CL-DevNet-2595/blob/master/README.md>`_ provides examples that you can try yourself.

#. With your devices already configured and running (see :ref:`configure a feature <config-feature>`), take a snapshot of the ``bgp`` feature and save it to the directory (or variable) ``output1``. You can use a Python interpreter or the :term:`library command line`.

    * If you want to use Python, you can use ``genie shell`` to load the ``testbed`` API and create your testbed and device objects. Then, tell the system to connect to each device and to learn the specified feature::

       (pyats) $ genie shell --testbed-file tb.yaml
          >>> output1 = {}
          >>> for name, dev in tb.devices.items():
          ...     dev.connect()
          ...     output1[name] = {}
          ...     output1[name]['bgp'] = dev.learn('bgp')
          ...

      This example uses a Python ``for`` loop to execute each statement on all devices in the testbed. The system stores the feature information in Python dictionaries, each identified by the device name. |br| |br| 

    * If you want to use the CLI::

       (pyats) $ genie learn "bgp" --testbed-file tb.yaml --output output1

      *Result*: Within the output directory, the system creates the output files and displays a summary for each device.

#. Change a device configuration. For example, shut down an interface.

#. Repeat step 1 to take another snapshot, but specify a different output directory or variable, such as ``output_2``.

#. Compare the two snapshots:

    * Python::

        >>> from genie.utils.diff import Diff
        >>> diff = Diff(output1.info, output2.info)
        >>> diff.findDiff()
        >>> print(diff)
    
    * |library| CLI::

       $ (pyats) genie diff output1 output2 

      *Result*: The system displays any differences:

      .. code-block:: text

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
    


Changes over time
^^^^^^^^^^^^^^^^^
In this example, you can see how to :ref:`parse the output <parse-output>` of a ``show`` command at two different points in time, and then use ``diff`` to compare the output.






See also...
*a list of relevant links*
 
 * Master workshop: https://github.com/CiscoTestAutomation/CL-DevNet-2595/blob/master/workshop.md
 * More ``Diff`` examples: https://pubhub.devnetcloud.com/media/genie-docs/docs/cli/genie_diff.html#genie-diff
 * link 3






