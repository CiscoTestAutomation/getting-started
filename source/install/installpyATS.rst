Install |pyATS|
========================
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
         * *Stage 1 and link*
         * *etc*
  


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








