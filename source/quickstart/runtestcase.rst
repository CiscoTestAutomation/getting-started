Run a test case
======================
This topic describes how you can use the |library| to build and run test cases and use them for automated network testing. You don't need to know Python --- you can use the :term:`library command line` ``genie run`` functionality from your Linux terminal.

Simply stated, you tell the system the test cases to run, the order to execute them, and the data to pass to the system at runtime.

.. _auto-testing-process:

Automated testing process
---------------------------
The |library| provides the building blocks that make it easy for you to automate your network testing. Simply:

 * Select from a pool of pre-written test cases.
 * Tell the system to run them in a specific order, and the data to use for each case. 
 * You can also specify any pre- and post-processing that you want to apply.

The ``Harness`` module controls the flow of your network automation in three stages, as described in the following table.

.. csv-table:: Automated testing process
    :file: HarnessProcess.csv
    :header-rows: 1
    :widths: 5 40 55

.. note:: The ``Harness`` is modular, and you can customize all of the components, including a :term:`trigger` or :term:`verification` to meet your automated testing requirements.

At runtime, the ``Harness`` pulls together all of the data that you've defined in the :ref:`job file <job-file>` and :ref:`datafiles <datafiles>`.

Advantages of a modular strategy
--------------------------------
 * Consistent, standards-based test cases are reusable.
 * You can write test scripts efficiently, using the reusable, plug and play test cases as building blocks.
 * It's easy to customize the standard test cases to meet your requirements.
 * The automated testing process is *data-driven* --- you don't have to re-write tests, just modify the datafiles.
 * You can choose from a few hundred |library| `open-source functions <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/apis>`_ to define your test case actions and steps. 

Triggers
---------

What is a trigger?
^^^^^^^^^^^^^^^^^^

.. include:: ../definitions/def_trigger.rst  

You can think of a trigger as equivalent to a |pyATS| *test case*. The |library| provides you with `a pool of triggers for the most common actions <https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/triggers>`_, already written and available to use out-of-the-box. Select a trigger name from the list to see a description.

Structure of a trigger
^^^^^^^^^^^^^^^^^^^^^^^
If you know or want to learn a bit of Python, you can customize a trigger to meet your requirements. A trigger is a Python :monospace:`(*.py)` file that has a standard structure, as shown in the following example.

.. code-block:: python

    from genie.harness.base import Trigger
    from pyats import aetest 

    class TriggerClassName(Trigger):    

        @aetest.test
        def section_1(self, uut, steps):
            ''' Learn prerequisite information
                Args:
                    uut ('obj'): Device object 
                    steps ('obj'): steps context manager                                
            '''
            with steps.start('Step 1 check if bgp neighbor is shut down') as step:
                is_expected = uut.api.is_bgp_neighbors_shutdown
                if is_expected:
                    step.passed('Reason this step passed')
                else:
                    step.failed('Reason this step failed')

The ``class`` is the name of the trigger and inherits from the |library| ``Trigger`` object. Each class performs one specific task, which can have multiple ``steps``. For more detailed information, see the `Harness Developer Guide <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/harness/developer/index.html#harness-developer-guide>`_.
         

Verifications
---------------

What is a verification?
^^^^^^^^^^^^^^^^^^^^^^^^
.. include:: ../definitions/def_verification.rst

How do verifications work?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
By taking an initial snapshot (a parsed show command), and then taking the same snapshot after each trigger runs, the system can compare the snapshots to ensure that the triggers have not caused any unexpected changes to your network configuration or operational state. 

.. _datafiles:

Datafiles
----------
The `YAML <https://yaml.org>`_ datafiles control the flow of test execution. This makes your automated testing *data-driven*, with no hard-coded values required in your testing scripts. The datafiles contain the values to pass to the system at runtime.

Trigger datafile
^^^^^^^^^^^^^^^^
A trigger datafile is a `YAML <https://yaml.org>`_ file that specifies the following minimum information:

 * Trigger name
 * Trigger source --- the path and *class* (trigger)
 * Devices on which to run the test (use the ``-- device`` argument to specify devices other than 'uut')
 * Any parameters (input) to pass as arguments to the trigger functions

Each trigger description tells you the mandatory and optional fields of its associated datafile.

.. tip:: If you use the standard |library| triggers, you don't have to provide a trigger datafile. The system will use the default datafile stored in your virtual environment at ``/genie_yamls/<uut_os>/trigger_datafile_<uut_os>.yaml``. The default trigger datafile specifies the device 'uut', which you define in your :term:`testbed yaml file`.

For more details, see the `complete trigger datafile schema <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/harness/user/datafile.html#trigger-datafile>`_.

Verification datafile
^^^^^^^^^^^^^^^^^^^^^^
Similar to a  trigger datafile, a verification datafile specifies the following minimum information:

 * Verification name
 * Verification source --- the path and *class* (trigger)
 * Devices on which to run the test (use the ``-- device`` argument to specify devices other than 'uut')
 * Any parameters (input) to pass as arguments to the trigger functions

.. _job-file:

Job file
--------------
A job file defines the information that the system requires to create and run a dynamic test script:   

 * |library| functionality to import
 * gRun command
 * Trigger UIDs to indicate which trigger classes to execute
 * Verification UIDs to indicate which verifications to execute

.. tip:: For a more detailed example and to see an actual job file, go to https://github.com/CiscoTestAutomation/examples/tree/master/libraries/harness_triggers.

How to run a test case
--------------------------
You can run the following example using the :download:`mock device <mock.zip>`.

Run a test case using the command line
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. In your virtual environment, change to the directory that contains the mock YAML file::

    (pyats) $ cd mock

#. Use ``genie run`` and specify the testbed, trigger, verification, device, and log details::

    (pyats) $ genie run --testbed-file mock.yaml --trigger-uids="TriggerShutNoShutBgp" --verification-uids="Verify_BgpProcessVrfAll" --devices uut --html-logs .
    
   *Result*: The system displays the test results on-screen and creates an HTML log file named :monospace:`TaskLog.html` in the current directory.

   .. tip:: 
      
      * The argument ``--html-logs .`` creates the :monospace:`TaskLog.html` file. This is a user-friendly file that you can easily read in a web browser. It organizes the data so that you can drill down for more details as needed.
      * If you're a DevNet user and you want to receive an email with the results, add the argument ``--mailto <address>``.

   The following example shows part of the log where you can see the overall :ref:`automated testing process <auto-testing-process>`. Note that the verification ran before and after the trigger.

   .. image:: ../images/tasklog_example.png
      

Run a test case using Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


See also...

 * More information about functions: https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/apis/index.html#api-guidelines-and-good-practices
 * Detailed description of the ``Harness`` module: https://pubhub.devnetcloud.com/media/genie-docs/docs/cookbooks/harness.html
 * link 3






