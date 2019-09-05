.. _configure-environment:

Configure your environment
=============================


Internal Cisco users
--------------------
Cisco engineers and developers can skip this topic, because the internal installer sets up a virtual environment for you. For more information about how to install |pyATS| and the |library|, see the topic :ref:`install-pyats`.

Docker users
-------------
If you use Docker, you can run |pyATS| and the |library| from a Docker image. Get the image and instructions at https://hub.docker.com/r/ciscotestautomation/pyats/.

For more information about how to use |pyATS| and the |library| see the :ref:`quick-start`.

DevNet community users
----------------------
Before you install |pyATS|, you must:

 * :ref:`check-python`
 * :ref:`set-up-venv`

.. _check-python:

Check your version of Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    .. note:: Make sure your system has a supported version of Python installed:
        
        .. include:: ../prereqs/supportedpythonversions.rst

To check your installed version::

$ python --version

*Result*: The system returns the installed version number::

$ Python 3.7.4

.. _set-up-venv:

Set up a Python virtual environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A |pyATSbold| instance is simply a directory (folder) in the file system that houses a Python Virtual Environment. Within your virtual environment, you install the |pyATS| and |library| packages, dependencies, and libraries, which include everything you need to run the system.

We strongly recommend that you install |pyATS| and the |library| from within a virtual environment.

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


See also...

* `Wiki for internal Cisco users <https://wiki.cisco.com/pages/viewpage.action?pageId=80375302>`_
* `Python virtual environments and packages <https://docs.python.org/3/tutorial/venv.html>`_
