Run a test case
======================
This topic describes how you can use the |library| to build and run test cases anduse them for automated network testing.

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
If you know or want to learn a bit of Python, you can customize a trigger to meet your requirements. A trigger has a standard structure::

from genie.harness.base import Trigger

 class  TriggerName(Trigger)
    def FunctionName (arguments from datafile, arg2..., steps from pyATS) - see example.py
         



Verifications
---------------

Datafiles
----------
The `YAML <https://yaml.org>`_ datafiles control the flow of test execution. 

- testbed
mapping (optional) - to connect to more devices than uut
verification (optional) - there is a default
trigger (optional) - there is a default
subsection
configuration
pts (profile the system)

Trigger datafile
^^^^^^^^^^^^^^^^

A trigger datafile is a `YAML <https://yaml.org>`_ file that specifies the following minimum information:

 * Trigger name
 * Trigger source --- the path and *class* (trigger)
 * Devices on which to run the test
 * Any parameters (input) to pass as arguments to the trigger functions

.. note:: The term *class* refers to the Python file structure of a trigger. The class is the same as the trigger name.

Each trigger description tells you the mandatory and optional fields of its associated datafile.

.. tip:: If you use the standard |library| triggers, you don't have to provide a trigger datafile. The system will use the default datafile stored in your virtual environment at ``/genie_yamls/<uut_os>/trigger_datafile_<uut_os>.yaml``. The default trigger datafile specifies the device ``uut``, which you define in your :term:`testbed yaml file`.

For more details, see the `complete trigger datafile schema <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/harness/user/datafile.html#trigger-datafile>`_.


Job files
--------------




HTML log viewer!!!

How to run a test case
--------------------------


Reusable triggers (classes)
Then tell the system the order to run the triggers and what data to pass
APIs define the functions (steps) within each action


Set up your system
^^^^^^^^^^^^^^^^^^^

#. Connect to your devices
#. Configure your devices
#. Set up a traffic generator
#. Take a snapshot


Execute triggers and verifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Step one
#. Step two
#. Step n

Run a common cleanup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Step one
#. Step two
#. Step n


See also...

 * More information about functions: https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/apis/index.html#api-guidelines-and-good-practices
 * Detailed description of the ``Harness`` module: https://pubhub.devnetcloud.com/media/genie-docs/docs/cookbooks/harness.html
 * link 3






