.. _write-python-script:

Write a Python script
======================
As a network engineer or programmer, you can write your own Python scripts that use the |pyATSbold| libraries to automate your network testing. A script is simply a Python file that lists different actions and lets you run them with a single command. In |pyATS| terms, a script is an aggregation of :term:`triggers <trigger>` and :term:`verifications <verification>`.

This topic describes how to write a basic script and how to add complexity to that script. You can run the example scripts on the `Cisco DevNet sandbox IOS XE device <https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology>`_ or on your real network devices (if you have them).

Why write a test script?
------------------------
*Automation* means that you can programmatically establish connections to your testbed devices and perform operations on them. Test scripts automate your network testing --- you simply define a list of commands once and then reuse the script as often as required, on-demand or at scheduled intervals.

For example, let's say that you have a device with over 100 interfaces, and that you need to monitor these daily to make sure they are up. You could, of course, manually execute a command on each interface. This is time consuming, however, and introduces the possibility of human error, which could adversely affect the state of your network. 

The |library| provides a better solution!

* Write a script that automates the process using the |librarybold| functionality to connect, configure, and verify the device state. 
* Rerun the script as needed, either as a scheduled job or on demand. 
* Because the |library|'s reusable :term:`triggers <trigger>` and :term:`verifications <verification>` are data-driven (not hard-coded), you can simply feed in data to specify other devices or :term:`features <feature>`, error-free. 

.. tip:: Remember, the |library| gives you *structured* output that makes reuse possible.

.. _write-basic-script:

Write a basic script
---------------------
This example shows you how to write a basic script to check the state of a device interface.

.. note:: This example uses pure Python. For information about how to use the |library| command line interface, see the |getstartedguide| topic :ref:`genie-cli`

#. First, decide on the functionality that you need from |pyATS| and the |library|, and import it. Remember that you always need to load the :term:`testbed YAML file`.

    .. code-block:: python

       from genie.testbed import load

   .. tip:: For a description of the more commonly used functionality that you might want to import, see the topic `Useful Libraries <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/utils/index.html#useful-libraries>`_.

#. If you'd like your script to display formatted messages as it runs, you can use the ``banner`` functionality.

   .. note:: Internal Cisco users use ``ats`` rather than ``pyats``.

   .. code-block:: python

       from pyats.log.utils import banner

#. You imported the ``load`` functionality in step 1, so now you can actually load the testbed file and display useful messages.

   .. code-block:: python

      print(banner("Loading testbed"))
      testbed = load('testbed.yaml')
      print("\n\nSuccessfully loaded testbed '{}'\n\n".format(testbed.name))

#. Now connect to one of the devices in the testbed. In this example, ``N95_1`` is the hostname of a device in the :term:`testbed yaml file`.

   .. code-block:: python

      device = testbed.devices['N95_1']
      device.connect()
      print("\n\nSuccessfully connected to device 'N95_1'\n\n")

#. Check the current state of the interface and parse the output into a data structure with :term:`key-value pairs <key-value pair>`. We expect that the interface ``Ethernet1/1`` is currently down.

   .. code-block:: python

      pre_output = device.parse("show interface Ethernet1/1 brief")

#. With the data parsed into a structure with key-value pairs and stored as the :term:`object` ``pre_output``, check the value of the ``status`` key.

   .. code-block:: python

      pre_status = pre_output['interface']['ethernet']['Eth1/1']['status']
      if pre_status == 'down':
          print("\n\nInterface Ethernet1/1 status is 'down' as expected\n\n")
      else:
          print("\n\nInterface Ethernet1/1 status is not 'down' as expected\n\n")
          exit()

#. Bring the interface up using the ``Conf`` module.

   .. code-block:: python

      device.configure("interface Ethernet1/1\n"
                  " no shutdown")
      print("\n\nSuccessfully unshut interface Ethernet1/1\n\n")

#. Re-check the interface state -- parse the output and store it in the ``post_output`` object, and print the result.

   .. code-block::  python

      post_output = device.parse("show interface Ethernet1/1 brief")
      post_status = post_output['interface']['ethernet']['Eth1/1']['status']
      if post_status == 'up':
          print("\n\nInterface Ethernet1/1 status is 'up' as expected\n\n")
      else:
          print("\n\nInterface Ethernet1/1 status is not 'up' as expected\n\n")       

And there you have it! 

To run the script, first :download:`download and extract the relevant testbed and script files <simple_script.zip>`. Open :monospace:`simple_script.py` in a text editor to see additional print statements that make the on-screen output clear.

When you're ready to see the output, from the directory where you put the extracted files, run::

  (pyats) python3 simple_script.py

Result:

.. code-block:: text

    coming soon

   *Result*: You are now connected to the device. |br| |br|

#. asdf

Use case crc-errors (show crc-errors)



Assume they don't know python
connect
execute
parse
configure
learn



Example of looping

multiple 'for' loops

See also...

* `How the Python import works <https://docs.python.org/3/tutorial/modules.html?highlight=import>`_