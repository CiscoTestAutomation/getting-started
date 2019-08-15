.. _install-pyats:

Install |pyATS|
========================
This topic describes how to install the |pyATSbold| ecosystem within your virtual environment.

Code structure
---------------
.. include:: /definitions/def_pyats_code_infrastructure.rst
.. include:: /definitions/def_pyatslibrary_code_structure.rst


Installation process
---------------------
The process that you follow depends on whether you are an internal, external, or Docker user, and whether you want to use the Robot Framework.

.. list-table:: |pyATS| installation process
   :header-rows: 1
   :widths: 35 65

   * - Type of user
     - Installation process
   * - Internal Cisco user
     -
        #. Check the :ref:`requirements`.
        #. Sign in to the `internal Wiki <https://wiki.cisco.com/display/PYATS/Installation>`_ for detailed instructions. The installation script will:
         
            * check your environment
            * create the virtual environment
            * install all |pyATS| and |library| packages and dependencies, and
            * clone the selected Git repositories from Bitbucket.

        
        #. Run the command ``pip install library`` to install the |library| infrastructure, features, and components.

   * - DevNet community user
     -
         #. Check the :ref:`requirements`.
         #. :ref:`configure-environment`.
         #. Upgrade and :ref:`run the package installer for Python (pip) <install-with-pip>`.
         #. Verify the installation:

            * ``$ pip list | grep pyats``
            * ``$ pip list | grep library`` |br| |br| 

         #. :ref:`clone-git-examples`.
         #. Run the example: ``$ pyats run job examples/basic/basic_example_job.py``

   * - Docker
     -
         #. Download the Docker image from https://hub.docker.com/r/ciscotestautomation/pyats/.
         #. Start the |pyATS| container.
         #. Run the examples.

   * - Robot Framework
     -
       Install the Robot Framework plugin.

        * Internal Cisco users:
          
            * ``$ pip install ats.robot``
            * ``$ pip install library.libs.robot``

        * DevNet users: 
          
            * ``$ pip install pyats.robot``
            * ``$ pip install library.libs.robot``

        * Docker users:
          
            * The Robot Framework is already installed.


.. _install-with-pip:

Install |pyATS| with pip
-------------------------
This section describes how to use the package installer for Python (pip) to install the |pyATS| system in your virtual environment.

.. note:: Cisco users should refer to the `internal Wiki <https://wiki.cisco.com/display/PYATS/Installation>`_ for detailed instructions.

#.  If you haven't already done so, activate your virtual environment::

        $ source bin/activate

    *Result*: The system displays the directory in parentheses before the command prompt::

        (pyats)$

#.  Upgrade pip with the latest setup tool packages::

        $ pip install --upgrade pip setuptools

#.  Install |pyATS| and the |library|::

        $ pip install pyats[library]

    .. hint:: Give the installer a few minutes to finish.

    *Result*: You're ready to start using |pyATS| and the |library|!

    .. note:: If you see warning messages, or the installation fails, first check your :ref:`system requirements <requirements>`, especially your Linux and Python versions. If you need more help, contact us at |br| pyats-support@cisco.com.

#. To test the installation, from the current (|pyATS|) directory, clone the Git examples repository::

            git clone https://github.com/CiscoTestAutomation/examples

#. Run the following example::

        pyats run job examples/basic/basic_example_job.py

  Or, for DevNet community users who want to receive an email summary::

        pyats run job examples/basic/basic_example_job.py --mailto <address>

  *Result*: |pyATS| runs three sample test cases, displays a summary of the results, and emails you the summary.


Install the Robot Framework plugin
----------------------------------

You can use the plugin after you install an additional component::

$ pip install pyats.robot library.libs.robot


.. _docker-label:

Run |pyATS| with Docker
------------------------------------------------------
If you know how to use Docker, you can work with our pre-built docker image, which includes both |pyATS| and the |library|. You can find the image and instructions at
https://hub.docker.com/r/ciscotestautomation/pyats/.

A number of image variants are available:

- Alpine Linux (lightweight)
- Standard image based on Python:3.6
- Standard image based on Python:3.6, with Robot Framework

#.  Download the image::

      $ docker pull ciscotestautomation/pyats:<latest>

    where *latest* is the current |pyATS| version. 
    
    |br|

#.  Start the |pyATS| container.

    * The pyATS docker container defaults to a Python interactive shell::

        $ docker run -it ciscotestautomation/pyats:latest

    * Alternatively, you can start the container in a shell::

        $ docker run -it ciscotestautomation/pyats:latest /bin/bash

#.  Run the basic example and get output::

      $ docker run -it ciscotestautomation/pyats:latest pyats run job /pyats/examples/basic/job/basic_example_job.py

    The pyATS virtual environment is sourced automatically, and your workspace is preset to be ``/pyats``. Note that this workspace directory (virtual environment) is declared to be a docker volume, so its content will persist between container reloads.

    |br|

#.  For more details and Docker options, go to https://hub.docker.com/r/ciscotestautomation/pyats/ .

.. qs-update::

Keep |pyATS| up to date
-----------------------------
On the last Tuesday of the month, the team releases a new version of |pyATS| and the |library|. This section describes how to get the latest changes.

.. qs-upgrade::

To upgrade the |pyATS| and |library| :doc:`infrastructure </definitions/def_pyats_code_infrastructure>`, and any or all of the :doc:`feature libraries and components </definitions/def_pyatslibrary_code_structure>`, run the ``pip install --upgrade`` command **from your virtual environment**.

Internal Cisco users
^^^^^^^^^^^^^^^^^^^^^

.. tip:: Cisco members of the "pyats-notices" mailer list receive a notification about each release. :question:`How does an internal user sign up to the notices?`

.. csv-table:: Internal Cisco user upgrade options
    :file: ../quickstart/UpgradeInternal.csv
    :header-rows: 1
    :widths: 25 35 40

*Result*: The installer checks for and upgrades any dependencies, and gives you the latest version of the |pyATS| and |library| core and library packages. To check the version::

  (pyats) $ pip list | egrep 'ats|library'

*Result*: The system displays a list of the packages and the installed versions.

.. attention:: The major and minor versions must all match. It's okay if the patch version varies.

DevNet community users
^^^^^^^^^^^^^^^^^^^^^^^
.. tip:: You can find the latest information about releases on Twitter at #pyATS.

.. csv-table:: DevNet user upgrade options
    :file: ../quickstart/UpgradeExternal.csv
    :header-rows: 1
    :widths: 25 35 40


*Result*: The installer checks for and upgrades any dependencies, and gives you the latest version of the |pyATS| and |library| core and library packages. To check the version::

  (pyats) $ pip list | egrep 'pyats|library'

*Result*: The system displays a list of the packages and the installed versions.

.. attention:: The major and minor versions must all match. It's okay if the patch version varies.

.. _clone-git-examples:

Download or clone the Git examples repository
-----------------------------------------------
We've provided some examples to help you start using the |library| for some simple scenarios that demonstrate how the |library| works.

.. note:: Make sure that you have |pyats| and the |library| :doc:`fully installed </install/installpyATS>`.

* To clone the Git repository from your virtual environment::

    (|library|) $ git clone https://github.com/CiscoTestAutomation/examples

* To download the Git repository from a browser:

  * Go to https://github.com/CiscoTestAutomation/examples.
  * Select **Clone or download**.
  * Select **Open in Desktop** to download and use the GitHub Desktop app, or **Download Zip** to download and extract a zip file.

 *Result*: You now have the example files stored in the ``examples`` directory.


See also...
*a list of relevant links*

* link 1
* link 2
* link 3
