Install |pyATS|
========================
This topic describes how to install the |pyATSbold| ecosystem within your virtual environment.

Code structure
---------------
The |library| code base is divided into two sections:

1. *Infrastructure* -- the core and base class, released through pip packages.
2. *Feature libraries and components* -- user-community owned and developed, automatically installed with the |library|.

:question:`We probably want to add more info to this section, specifically about pyATS.`

Installation process
---------------------
The process that you follow depends on whether you are an internal, external, or Docker user.

.. list-table:: |pyATS| installation process
   :header-rows: 1
   :widths: 25 75

   * - Type of user
     - Installation process
   * - Internal
     -
         #. Check the :ref:`requirements`.
         #. Sign in to the `internal Wiki <https://wiki.cisco.com/display/PYATS/Installation>`_ for detailed instructions. :question:`How permanent is the Wiki link? Should we keep and maintain the hyperlink here?`
         #. Run the command ``pip install pyats full`` to

            * check your environment
            * create the virtual environment
            * install all |pyATS| and |library| packages and dependencies :question:`components?`, and
            * clone the selected Git repositories from Bitbucket.

   * - External
     -
         #. Check the :ref:`requirements`.
         #. :ref:`configure-environment`.
         #. Upgrade and :ref:`run the package installer for Python (pip) <install-with-pip>`.
         #. Verify the installation.
         #. Run the example.

   * - Docker
     -
         #. Download the Docker image from https://hub.docker.com/r/ciscotestautomation/pyats/.
         #. Mount a pip requirements file.
         #. Customize your workspace.
         #. Start the |pyATS| container.
         #. Run the examples.

.. note:: If you want to use Robot Framework to build scripts, you can also install the |library| Robot Framework plugin. :question:`Does Robot Framework work with a Docker image?`



# clone your git repositories
# browse https://bitbucket-eng-sjc1.cisco.com/bitbucket/projects/PYATS-PROJ/ for repos to clone to projects/ directory
# browse https://bitbucket-eng-sjc1.cisco.com/bitbucket/projects/PYATS-PYPI/ for repos to clone to pypi directory

# and voila

.. _install-with-pip:

Install |pyATS| with pip
-------------------------
This section describes how to use the package installer for Python (pip) to install the |pyATS| system in your virtual environment.

.. note:: Cisco users should refer to the `internal Wiki <https://wiki.cisco.com/display/PYATS/Installation>`_ for detailed instructions.

#.  If you haven't already done so, activate your virtual environment::

        $ source bin/activate .

    *Result*: The system displays the directory in parentheses before the command prompt::

        (pyats)$

#.  Upgrade pip with the latest setup tool packages::

        $ pip install --upgrade pip setuptools

#.  Install |pyATS| and the |library|::

        $ pip install pyats library

    .. hint:: Give the installer a few minutes to complete its work.

    *Result*: You're ready to start using |pyATS| and the |library|!

    :question:`Is this how it will really work? What should we say about any warning messages or failed installations?`

    .. note:: If you see warning messages, or the installation fails, :question:`???`

#. To test the installation, run the example provided::

        pyats run job examples/basic/job/basic_example_job.py

   *Result*: :question:`When I tried to run this, I got an error: The provided jobfile 'examples/basic/job/basic_example_job.py' does not exist. What is the expected behavior? Does this verify that all required components are installed? Can we include the test file with the installation?`


Install the Robot Framework plugin
----------------------------------

You can use the plugin after you install an additional component::

$ pip install pyats.robot library.libs.robot


.. _docker-label:

Run |pyATS| and the |library| from a Docker container
------------------------------------------------------
If you know how to use Docker, you can work with our pre-built docker image, which includes both |pyATS| and the |library|. You can find the image and instructions at
https://hub.docker.com/r/ciscotestautomation/pyats/.

A number of image variants are available:

- Alpine Linux (lightweight)
- Standard image based on Python:3.6
- Standard image based on Python:3.6, with Robot Framework

#.  Download the image::

      $ docker pull ciscotestautomation/pyats:latest

    where *latest* is the current |pyATS| version.

    |br| :question:`I tried to test this but couldn't get Docker set up properly. Can't connect to daemon. Can someone with Docker test this command?`

#.  Start the |pyATS| container.

    * The pyATS docker container defaults to a Python interactive shell::

        $ docker run -it ciscotestautomation/pyats:latest

    * Alternatively, you can start the container in a shell::

        $ docker run -it ciscotestautomation/pyats:latest /bin/bash

#.  Run the basic example and get output::

      $ docker run -it ciscotestautomation/pyats:latest pyats run job /pyats/examples/basic/job/basic_example_job.py

    The pyATS virtual environment is sourced automatically, and your workspace is preset to be /pyats. Note that this workspace directory (virtual environment) is declared to be a docker volume, so its content will persist between container reloads.

#.  For more details and Docker options, go to https://hub.docker.com/r/ciscotestautomation/pyats/ .

See also...
*a list of relevant links*

* link 1
* link 2
* link 3
