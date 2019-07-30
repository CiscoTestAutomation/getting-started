Install |pyATS|
========================
This topic describes how to install the |pyATS| ecosystem within your virtual environment. The process that you follow depends on whether you are an internal, external, or Docker user.

* If you are a Cisco internal user, see the internal Wiki for installation instructions.
* If you are a Docker user, go to https://hub.docker.com/r/ciscotestautomation/pyats/ for the image and instructions.

Install pyATS | Genie with pip (the Python package installer).

# upgrade pip/setuptools to get the latest packages
bash$ pip install --upgrade pip setuptools

# install pyATS/Genie
bash$ pip install pyats genie
It's a simple as that! Give it a test to make sure it's all working.

# test that it's working by running the basic example
bash$ pyats run job examples/basic/job/basic_example_job.py

# when you're done with pyATS, close your terminal window or exit the virtual
# environment by deactivating it
bash$ deactivate
If you want to use RobotFramework to build scripts with pyATS | Genie using our RobotFramework plugin, you can also install it now.

# if you are a RobotFramework user, install the additional component
bash$ pip install pyats.robot genie.libs.robot



To do so, the steps boils down to:

ensure system package dependencies are met.
create a python virtual environment in a directory for installing pyATS
install pyATS packages and optional dependencies
create standard directories
update env.sh/csh to include standard directories into PYTHONPATH
git clone any repositories you are interested in.


Example Installation on Ubuntu 14.04
# ensure system packages met
$ sudo apt-get install python3 python3-pip python3-venv

# create virtual environment
$ python3-m venv /path/to/pyats

# symlink env.sh/csh if you want
$ cd /path/to/pyats
$ ln -s bin/activate env.sh
$ ln -s bin/activate.csh env.csh

# activate environment by sourcing bin/activate or env.sh
$ source bin/activate

# update pip and setuptools
$ pip install --upgrade pip setuptools

# install pyATS packages - there's two ways to do this
# option 1: - copy pip.conf from /auto/pyats/bin to root of your environment and pip install
# eg:
$ scp pyats-training:/auto/pyats/bin/pip.conf .
$ pip install ats unicon
# or option 2: use pip directly
# (note that this means future packages installed via pyATS pypi will need these added arguments instead of the simplicity of using just pip.conf file
$ pip install ats unicon --index-url=http://pyats-pypi.cisco.com/simple/ --trusted-host=pyats-pypi.cisco.com

# create the std directories
$ mkdir projects
$ mkdir pypi

# update env.sh/csh
$ echo 'export PYTHONPATH="$PYTHONPATH:$VIRTUAL_ENV/projects"' >> bin/activate
$ echo 'setenv PYTHONPATH "$PYTHONPATH:$VIRTUAL_ENV/projects"' >> bin/activate.csh

# clone your git repositories
# browse https://bitbucket-eng-sjc1.cisco.com/bitbucket/projects/PYATS-PROJ/ for repos to clone to projects/ directory
# browse https://bitbucket-eng-sjc1.cisco.com/bitbucket/projects/PYATS-PYPI/ for repos to clone to pypi directory

# and voila

Installation process
---------------------
*Describe the overall process - check prereqs, install |pyATS|*

.. list-table:: |pyATS| installation process
   :header-rows: 1

   * - Type of user
     - Installation process
   * - Internal
     -
         * *Stage 1 and link*
         * *etc*

   * - External
     -
         * Check that your system meets the :ref:`requirements`.
         * :ref:`configure-environment`.
         * Within your virtual environment, upgrade and run the pip installer.
         *

   * - Docker
     -
         * Image
         * instructions





Ways to install |pyATS|
------------------------

*Explain that there are different ways to install* |pyATS|, depending on the platform. Link to each section within this file for different options. Explain briefly the concepts of core (infrastructure) and feature libraries, and that these will be installed.

* :ref:`pip-install-label`
* :ref:`docker-label`

.. _pip-install-label:

Install |pyATS| with pip
^^^^^^^^^^^^^^^^^^^^^^^^
*Procedure for using pip install.*

.. _docker-label:

Run |pyATS| and the |library| from a Docker container
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Procedure for pulling a Docker image and running |pyATS| in a Docker container.*

Install the RobotFramework
---------------------------
*Describe how to do this.*

Test your installation
-----------------------
*Provide a few steps to make sure all necessary components are installed at this point.*

See also...
*a list of relevant links*

* link 1
* link 2
* link 3
