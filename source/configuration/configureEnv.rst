.. _configure-environment:

Configure your environment
=============================


Internal Cisco users
--------------------
Cisco engineers and developers can skip this topic, because the internal installer sets up a virtual environment for you. For more information about how to install |pyATS| and the |library|, see the internal Wiki pages.

Docker users
-------------
If you use Docker, you can run |pyATS| and the |library| from a Docker image. Get the image and instructions at https://hub.docker.com/r/ciscotestautomation/pyats/.

For more information about how to use |pyATS| and the |library| see the :ref:`quick-start`.

External users
---------------
Before you install |pyATS|, you must :ref:`install-python` and :ref:`set-up-venv`.

.. _install-python:

Install Python
^^^^^^^^^^^^^^^
#.  Go to https://www.python.org/ and download the correct version of Python for your OS.

    .. note:: Make sure you select a :ref:`supported version of Python <supported-python-versions>`.

#.  Run the installer and respond to the prompts. |br| *Result*: The Python interpreter is installed in the specified directory.

    |br|

#.  To verify the installed version::

        python --version

    *Result*: The system returns the installed version number::

        Python 3.7.4

.. _set-up-venv:

Set up a Python virtual environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A |pyATSbold| instance is simply a directory (folder) in the file system that houses a Python Virtual Environment. Within your virtual environment, you install the |pyATS| and |library| :question:`packages and dependencies`.

We strongly recommend that you install |pyATS| and the |library| from within a virtual environment. This keeps all of the libraries and dependencies together for your current project. :question:`We haven't introduced the concept of a "project" yet, should we do that here? Also, do we want to say "libraries and dependencies" or "components" and "objects"?`

#.  Create a new directory::

        $ mkdir pyats

    .. tip:: Windows users can just add a new folder in the File Explorer.

#.  Go to the new directory::

        $ cd pyats

#.  Initialize a virtual environment in this directory::

        $ python3 -m venv .

#.   Activate the virtual environment::

        $ source bin/activate .

    *Result*: The system displays the directory in parentheses before the command prompt::

        (pyats)$

    This makes the local directories the first place that the :question:`installer or pyATS?` looks for needed files.


See also...
*a list of relevant links*

* link 1
* link 2
* link 3
