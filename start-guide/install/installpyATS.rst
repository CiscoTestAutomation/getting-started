.. _install-pyats:

Installation
============

.. sidebar:: See also...

    - `Python virtual environments <https://docs.python.org/3/tutorial/venv.html>`_

    - `pyenv <https://github.com/pyenv/pyenv>`_

This topic describes how to install the |pyATSbold| within your system.

.. warning::
    
    For all internal Cisco engineering users, skip this section, and refer to the 
    `engineering internal Wiki <https://wiki.cisco.com/display/PYATS/Installation>`_ for detailed instructions
    on installing pyATS within Cisco.


.. list-table:: |pyATS| installation process
   :header-rows: 1
   :widths: 30 70

   * - Type of user
     - Installation process

   * - Virtual Environment
     -
         #. Check the :ref:`requirements`.
         #. :ref:`configure-environment`.
         #. Upgrade and :ref:`run the package installer for Python (pip) <install-with-pip>`:

            ``pip install "pyats[full]"`` |br| |br|

         #. Verify the installation:

            * ``$ pyats version check``

         #. :ref:`clone-git-examples`.
         #. Run the example: ``$ pyats run job examples/basic/basic_example_job.py``

   * - Docker
     -
         #. Download the Docker image from https://hub.docker.com/r/ciscotestautomation/pyats/.
         #. Start the |pyATS| container.
         #. Run the examples.

.. tip:: Once you install the |pyATS| ecosystem, remember to :ref:`keep your system up to date <upgrade-pyats>`.


.. _install-with-pip:

Virtual Environment
-------------------

pyATS development team recomments you to always develop and run Python scripts
with a Python virtual environment. This section describes how to check your
Python version, and creating a virtual environment using your available binary.

.. _check-python:

Python Version
^^^^^^^^^^^^^^
.. note:: Make sure your system has a supported version of Python installed:
        
        .. include:: ../prereqs/supportedpythonversions.rst
           :start-line: 5

To check your installed version::

$ python --version

*Result*: The system returns the installed version number::

$ Python 3.7.4

.. tip::

    ``pyenv`` a great utility for managing multiple Python versions within your
    system. 

.. _set-up-venv:

Create Virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^

A Python Virtual Environment is simply a directory (folder). Within this virtual 
environment, you install the |pyATS| and |library| packages, dependencies, and 
libraries, including everything else you need to run the system.

.. note:: In our examples, we use the directory ``pyats``, but you can give your directory a different name.

#.  Create a new directory::

        $ mkdir pyats


#.  Go to the new directory::

        $ cd pyats

#.  Initialize a virtual environment in this directory::

        $ python3 -m venv .

    *Result*: This creates a project "folder" (space) within the current directory. The folder keeps all dependencies, features, and components together in one place. |br| |br|
    

#.   Activate the virtual environment::

        $ source bin/activate .

    *Result*: The system displays the directory in parentheses before the command prompt::

        (pyats)$

    When you install the |pyATS| ecosystem within this virtual environment, the packages remain separate from those in other project spaces.

    .. hint:: When you're done with your |pyATS| session, you can close the terminal window or exit the environment::

        $ deactivate


Pip Install
^^^^^^^^^^^

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
      :widths: 20 35 45

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

.. _upgrade-pyats:

Update Environment
^^^^^^^^^^^^^^^^^^
On the last Tuesday of the month, the team releases a new version of |pyATSbold|. 
This topic describes how to get the latest changes.

To upgrade the |pyATS| and |library| :doc:`infrastructure </definitions/def_pyats_code_infrastructure>`, and any or all of the :doc:`feature libraries and components </definitions/def_pyatslibrary_code_structure>`, run the relevant upgrade command **from your virtual environment**.

.. tip:: You can find the latest information about releases on Twitter at #pyATS. 

For information about all things |pyATS|, see our discussion on `Webex Teams <https://eurl.io/#r18UzrQVr>`_.

You can check and upgrade your pyATS installation straigth from the command line:

.. code-block:: shell

    # to check your current pyats version
    (pyats)$ pyats version check

    # to check if any packages are out-dated
    (pyats)$ pyats version check --outdated

    # to update version
    (pyats)$ pyats version update

Otherwise, you can also update the packages manually using Pip:

.. csv-table:: Pip upgrade options
    :file: ../quickstart/UpgradeExternal.csv
    :header-rows: 1
    :widths: 25 35 40


*Result*: The installer checks for and upgrades any dependencies, and gives you the latest version of the |pyATS| and |library| core and library packages. To check the version::

  (pyats) $ pyats version check

*Result*: The system displays a list of the packages and the installed versions.

.. attention:: The major and minor versions must all match. It's okay if the patch version varies.

See also...

* `pyATS change log <https://developer.cisco.com/docs/pyats/api/>`_
* `pyATS Library change log <https://developer.cisco.com/docs/genie-docs/>`_


.. _docker-label:

Using Docker
------------
If you know how to use Docker, you can work with our pre-built docker image, which includes both |pyATS| and the |library|. You can find the image and instructions at
https://hub.docker.com/r/ciscotestautomation/pyats.

.. code-block:: text

    bash$ docker pull ciscotestautomation/pyats:latest

.. _clone-git-examples:

Examples Repository
-------------------
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
