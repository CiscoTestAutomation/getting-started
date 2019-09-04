.. _structure-of-pyats-statement:

Structure of a |pyATS| statement
----------------------------------
Although you don't need to know Python to use the |pyATS| ecosystem, it might help you to understand the structure of the Python-based commands described in this guide. 

.. tip:: Remember, you can use the :term:`library command line` for network automation and never have to enter a Python command!

The following example explains the statements used to connect to a device and parse output from the ``show inventory`` command.

.. csv-table:: Structure of a |pyATS| statement
   :header: "Number", "Statement", "Description"
   :widths: 5, 40, 55

   "1", "``from genie.testbed import load``", "Get the ``genie.testbed`` library and its ``load`` function."
   "2", "``tb = load('tb.yaml')``", "Load the ``tb.yaml`` testbed and store it in the ``tb`` variable."
   "3", "``dev = tb.devices['nx-osv-1']``", "Find the ``nx-osv-1`` device and store it in the variable ``dev``."
   "4", "``dev.connect()``", "Connect to the device you defined as ``dev``."
   "5", "``p1 = dev.parse('show inventory')``", "Parse the ``show inventory`` output for ``dev``, and store the output in the variable ``p1``."
   "6", "|line6|", "Print a meaningful message and the serial number for Slot 1."

.. tip:: If you want to know more about how to use Python, you can find many good online tutorials.