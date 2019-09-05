.. _manage-connections:

Manage device connections
=============================
This topic describes how to connect to network devices using the |librarybold|. It also gives you a quick example to try using mocked devices.

.. _how-library-connects:

How the |library| connects to devices
-------------------------------------
Because the |library| is based on Python, an :term:`object`-oriented programming language, it uses objects to represent your testbed topology.

#. Set up a testbed YAML file that contains your device details.
#. Use the |library| to create the testbed and device objects.
#. Tell the |library| which device to connect to.
#. Connect and run commands.

For a more detailed example that you can try, see :ref:`connect-to-device`.


.. _manageconnections-setup-testbed:

Set up a testbed YAML file
------------------------------
There are a few different ways to create a testbed file, but the two simplest are:

* Use a text editor to copy and edit an existing YAML file.
* Enter device information into an Excel file, and let the |library| create the YAML file for you.

The following sections explain both options.

Edit a YAML file directly
^^^^^^^^^^^^^^^^^^^^^^^^^
The YAML file must follow the |pyATS| `topology schema <https://pubhub.devnetcloud.com/media/pyats/docs/topology/schema.html#topology-schema>`_. The schema provides for a complete and thorough description of your testbed, including custom key-value pairs. 

.. tip:: Only the ``devices`` block is actually required, so it's easy to get started with a simple example.

The ``devices`` block contains a description of each network device, and must include the following keys.

.. csv-table:: Required device block details
    :header: "Key", "Description"
    :widths: 25 75

    "``hostname``", "This *must* be the configured hostname of the device."
    "``alias``", "The |library| uses the alias to identify the device during script execution. This makes the script reusable on another topology, when a device is assigned the same alias, such as ``uut`` (unit under test)."
    "``os``", "Device operating system"
    "``credentials``", "The username, password, and any other credentials required to log in to the device. |br| |br| For details about how passwords are stored, see the topic `Credential Password Modeling <https://pubhub.devnetcloud.com/media/pyats/docs/topology/schema.html#credential-password-modeling>`_. "
    "``type``", "Device type"
    "``ip``", "IP address"
    "``protocol``", "Any one of the supported protocols |br| (currently Telnet, SSH, REST, RESTCONF, NETCONF, and YANG)"
    "``port``", "Connection port"
 

The following example shows a YAML file with two devices defined::

 devices:
  nx-osv-1:
      type: 'router'
      os: 'nxos'
      alias: 'uut'
      credentials:
          default:
              username: admin
              password: admin
      connections:
          cli:
              protocol: ssh
              ip: "172.25.192.90"
              port: 17010

  csr1000v-1:
      type: 'router'
      os: "iosxe"
      alias: 'helper'
      credentials:
          default:
              username: cisco
              password: cisco
      connections:
          cli:
              protocol: ssh
              ip: "172.25.192.90"
              port: 17008

.. attention:: Remember that YAML is white-space and case-sensitive.

Use Excel to create the YAML file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can define all of your device data in a CSV (.csv) or Excel (.xls, .xlsx) file. The |geniecmd| ``create testbed`` command automatically converts the input and creates an equivalent YAML file. 

The following example shows an Excel file with the required columns.

.. image:: geniecreate_example_excel.png 

:download:`You can download a sample Excel file here. <SampleTestbedFile.xlsx>`

Follow these guidelines to create a valid YAML file:

    * Separate the ``ip`` and ``port`` with either a space or a colon (:).
    * The ``password`` column is the default password used to log in to the device.
    * If you leave the password blank, the system prompts you for the password when you connect to the device.
    * To enter privileged EXEC mode with the ``enable`` command, add a column with the header ``enable_password``. The value can be the same as or different from the default password.
    * Any additional columns that you define, such as ``alias`` or ``type``, are added to the YAML file as key-value pairs.
    * The columns can be in any order, as long as you include the required columns.

When you're ready to create the YAML file, from your virtual environment, run the command::

 (pyats) $ genie create testbed my_devices.xls --output yaml/my_testbed.yaml

where ``my_devices.xls`` is the name of your source file, and ``my_testbed.yaml`` is the name of your output file.

.. tip:: Add the ``--encode-password`` option to hide the password in the YAML file as a secret string. Note that this only *obfuscates* the password --- it does *not* make the password cryptographically secure. For more information, see the topic `Secret Strings <https://pubhub.devnetcloud.com/media/pyats/docs/utilities/secret_strings.html#secret-strings>`_.

For more details about the ``genie create`` functionality, see the topic `Genie Create Testbed <https://pubhub.devnetcloud.com/media/genie-docs/docs/cli/genie_create.html#genie-create-testbed>`_.

Other ways to create the testbed
---------------------------------
 * You can enter the device data manually, without having to first create a YAML or Excel/CSV file::

    (pyats) $ genie create testbed --output yaml/my_testbed.yaml --encode-password

   *Result*: The system prompts you for the device information and passwords. The ``--encode-password`` option obfuscates the password in the resulting YAML file. |br| |br|

 * If you have data in the form of a Python dictionary, you can create a testbed from that dictionary. For example, if you receive JSON-formatted data, you can convert that to a Python dictionary and then load the dictionary. For details about how to do this, see `Create a testbed from a dictionary <http://wwwin-pyats.cisco.com/cisco-shared/genie/latest/cookbooks/genie.html#create-a-testbed-from-a-dictionary>`_.

.. _connect-to-device:

Connect to a device
---------------------------
This step-by-step example shows you how to connect to a device. 

.. note:: You can run the commands in the following examples on real devices, if you have them available. If you don't have a real device to practice with, we offer a :term:`mock device` that you can use with most of the |library| examples. 

#. :download:`Download the zip file that contains the mock data and YAML file <mock.zip>`. |br| |br|

#. Extract the files to a location of your choice, and keep the zip file structure intact. This example uses the directory ``mock``. |br| |br|

#. In your virtual environment, change to the directory that contains the mock YAML file::

    (pyats) $ cd mock

   .. important:: The mock feature is location-sensitive. Make sure that you change to the directory that contains the ``mock.yaml`` file and keep the zip file structure intact.


#. Open the Python interpreter::

    (pyats) $ python

#. Load the |library| ``testbed`` API so that you can create the testbed and device objects::

    >>> from genie.testbed import load

#. Create a testbed object ``tb`` based on your :term:`testbed YAML file`. Specify the absolute or relative path, in this case, ``mock/mock.yaml``::

    >>> tb = load('mock.yaml')

   *Result*: The system creates a variable ``tb`` that points to the testbed object. This command also creates ``tb.devices``, which contains the YAML device information in the form of key-value pairs. |br| |br|

#. Create an object ``dev`` for the device that you want to connect to::

    >>> dev = tb.devices['nx-osv-1']

   *Result*: The |library| finds the device named ``nx-osv-1`` in ``tb.devices`` and stores the information in the ``dev`` object. |br| |br| 

#. Connect using the values stored in the ``device`` object::

    >>> dev.connect()

   *Result*: The system connects to the device and displays the connection details. Once you're connected, you can run show commands and :ref:`parse the output <parse-output>`. |br| |br| 

#. To exit the Python interpreter::

    >>> exit()

.. tip:: Remember - you can put all of these commands into a single script. We'll show you how in the :ref:`parse-output` section. 

See also...

* `Detailed description of the testbed file <https://realpython.com/start-here/>`_
* `Detailed description of the pyATS Library topology <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/Conf/user/topology.html?highlight=testbed%20yaml%20file#topology>`_










