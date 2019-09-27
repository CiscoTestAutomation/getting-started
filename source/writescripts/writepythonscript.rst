.. _write-python-script:

Write a Python script
======================
As a network engineer or programmer, you can write your own Python scripts that use the |pyATSbold| libraries to automate your network testing. A script is simply a Python file that lists different actions and lets you run them with a single command. In |pyATS| terms, a script is an aggregation of :term:`triggers <trigger>` and :term:`verifications <verification>`.

This topic describes how to write a basic script and how to add complexity to that script. You can run the example scripts on the `Cisco DevNet sandbox IOS XE device <https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology>`_ or on your real network devices (if you have them).

Why write a test script?
------------------------
*Automation* means that you can programmatically establish connections to your testbed devices and perform operations on them. Test scripts automate your network testing --- you simply define a list of commands once and then reuse the script as often as required, on-demand or at scheduled intervals.

For example, let's say that you have a device with over 100 interfaces, and that you need to monitor these daily to make sure they are up. You could, of course, manually execute a show command and then read through hundreds of lines of code to find the state of each interface. This is time consuming, however, and introduces the possibility of human error, which could adversely affect the state of your network. 

The |library| provides a better solution!

* Write a script that automates the process using the |librarybold| functionality to connect, configure, and verify the device state. 
* Rerun the script as needed, either as a scheduled job or on demand. 
* Because the |library|'s reusable :term:`triggers <trigger>` and :term:`verifications <verification>` are data-driven (not hard-coded), you can simply feed in data to specify other devices or :term:`features <feature>`, error-free. 

.. tip:: Remember, the |library| gives you *structured* output that makes reuse possible.

.. _write-basic-script:

Write a basic script
---------------------
This example shows you how to write and run a basic script to check the state of a device interface.

.. note:: This example uses pure Python. For information about how to use the |library| command line interface, see the |getstartedguide| topic :ref:`genie-cli`

Sample script - basic
^^^^^^^^^^^^^^^^^^^^^
We provide you with an example of a commented script that:

* checks the status of a network interface
* changes the configuration, and 
* re-checks the interface status.

We also provide you with pre-recorded output so that you can see the results. :download:`Download the sample <simple_script1.zip>` file, and then extract the files to a directory of your choice. Take a look at the :monospace:`testbed.yaml`, and open :monospace:`simple_script1.py` in a text editor to see additional :monospace:`log.info` statements that make the on-screen output clear.

To run the script:

#. In your Linux terminal, source the environment variables.

   * For Bash::

      source script1_env.sh

   * For C shell::

      source script1_env.csh

#. Run the script::

    python3 simple_script1.py


Steps to write a basic script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following procedure describes the steps that you take to write the same sample script.

#. Open a text editor and start a new :monospace:`.py` file.

#. First, import the functionality that you need from Python, |pyATS|, and the |library|. For a description of the more commonly used functionality that you might want to import, see the topic `Useful Libraries <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#useful-libraries>`_.

Remember that you always need to load the :term:`testbed YAML file`.

   .. note:: Internal Cisco users must use ``ats`` rather than ``pyats``.

    .. code-block:: python

      # Python
      import sys
      import time
      import logging

      # Enable logger
      logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')
      log = logging.getLogger(__name__)

      # Import pyATS the pyATS library
      from genie.testbed import load


#. If you'd like your script to display formatted messages as it runs, you can use the ``banner`` functionality.

   .. code-block:: python

       from pyats.log.utils import banner

#. You imported the ``load`` functionality in step 1, so now you can load the testbed file and display useful messages.

   .. code-block:: python

      log.info(banner("Loading testbed"))
      testbed = load('testbed.yaml')
      log.info("\nPASS: Successfully loaded testbed '{}'\n".format(testbed.name))

#. Now connect to one of the devices in the testbed. In this example, ``nx-osv-1`` is the hostname of a device in the :term:`testbed yaml file`.

   .. code-block:: python

      device = testbed.devices['nx-osv-1']
      device.connect(via='cli')

#. Check the current state of the interface and parse the output into a data structure with :term:`key-value pairs <key-value pair>`. We expect that the interface ``Ethernet2/1`` is currently down.

   .. code-block:: python

      pre_output = device.parse("show interface Ethernet2/1 brief")

#. With the data parsed into a structure with key-value pairs and stored as the :term:`object` ``pre_output``, check the value of the ``status`` key.

   .. code-block:: python

      pre_status = pre_output['interface']['ethernet']['Eth2/1']['status']
      if pre_status == 'down':
          log.info("\nPASS: Interface Ethernet2/1 status is 'down' as expected\n")
      else:
          log.error("\nFAIL: Interface Ethernet2/1 status is not 'down' as expected\n")
      exit()

#. Bring the interface up using the ``Conf`` module.

   .. code-block:: python

      device.configure("interface Ethernet2/1\n"
                 " no shutdown")

#. Use ``sleep`` to give the configuration time to take effect.

   .. code-block:: python

      time.sleep(15)

#. Re-check the interface state -- parse the output and store it in the ``post_output`` object.

   .. code-block::  python

      post_output = device.parse("show interface Ethernet2/1 brief")

#. Verify that the interface is now :monospace:`up`.

   .. code-block:: python

      post_status = post_output['interface']['ethernet']['Eth2/1']['status']
      if post_status == 'up':
          log.info("\nPASS: Interface Ethernet2/1 status is 'up' as expected\n")
      else:
          log.error("\nPASS: Interface Ethernet2/1 status is not 'up' as expected\n")       

#. Save the file as :monospace:`myscript1.py`.

And there you have it! 


See also...

* `How the Python import works <https://docs.python.org/3/tutorial/modules.html?highlight=import>`_