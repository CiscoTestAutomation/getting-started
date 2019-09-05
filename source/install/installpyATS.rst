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

        

   * - DevNet community user
     -
         #. Check the :ref:`requirements`.
         #. :ref:`configure-environment`.
         #. Upgrade and :ref:`run the package installer for Python (pip) <install-with-pip>`:

            ``pip install pyats[library]`` |br| |br|

         #. Verify the installation:

            * ``$ pip list | grep pyats``
            * ``$ pip list | grep genie`` |br| |br| 

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
          
          ``$ pip install ats[robot]``

        * DevNet users: 
          
          ``$ pip install pyats[robot]``

        * Docker users:
          
            * Use the tag **latest-robot** (https://hub.docker.com/r/ciscotestautomation/pyats/tags).

.. tip:: Once you install the |pyATS| ecosystem, remember to :ref:`keep your system up to date <upgrade-pyats>`.


.. _install-with-pip:

Install |pyATS| with pip
-------------------------
This topic describes how to use the package installer for Python (pip) to install the |pyATS| system in your virtual environment.

.. note:: Cisco users should refer to the `internal Wiki <https://wiki.cisco.com/display/PYATS/Installation>`_ for detailed instructions.

#.  If you haven't already done so, activate your virtual environment::

        $ source bin/activate

    *Result*: The system displays the directory in parentheses before the command prompt::

        (pyats)$

#.  Upgrade pip with the latest setup tool packages::

        $ pip install --upgrade pip setuptools

#.  Install |pyATS| and the |library|, using the options described in the following table.

    .. csv-table:: Installation options
      :file: InstallOptions.csv
      :header-rows: 1
      :widths: 25 35 40

    .. hint:: Give the installer a few minutes to finish.

    *Result*: You're ready to start using |pyATS| and the |library|!

    .. note:: If you see warning messages, or the installation fails, first check your :ref:`system requirements <requirements>`, especially your Linux and Python versions. If you need more help, contact us at |br| pyats-support-ext@cisco.com.

#. To test the installation, from the current (|pyATS|) directory, clone the Git examples repository::

            git clone https://github.com/CiscoTestAutomation/examples

#. Run the following example::

        pyats run job examples/basic/basic_example_job.py

  Or, for DevNet community users who want to receive an email summary::

        pyats run job examples/basic/basic_example_job.py --mailto <address>

  *Result*: |pyATS| runs three sample test cases, displays a summary of the results, and emails you the summary.


Install the Robot Framework plugin
----------------------------------

You can use the plugin after you install an additional component.

* Internal Cisco users::
   
   $ pip install ats[robot]

* DevNet users::
   
   $ pip install pyats[robot]

* Docker users:

  Use the tag **latest-robot** (https://hub.docker.com/r/ciscotestautomation/pyats/tags).

.. _docker-label:

Run |pyATS| with Docker
------------------------------------------------------
If you know how to use Docker, you can work with our pre-built docker image, which includes both |pyATS| and the |library|. You can find the image and instructions at
https://hub.docker.com/r/ciscotestautomation/pyats.


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

* `Wiki for internal Cisco users <https://wiki.cisco.com/pages/viewpage.action?pageId=80375302>`_
* `Robot Framework website <https://robotframework.org/>`_
* `How to clone a GitHub repository <https://help.github.com/en/articles/cloning-a-repository>`_
