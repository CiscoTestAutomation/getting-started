.. _contribute:

Contribution guidelines
=======================
Our |library| feature libraries and components are all open source. We welcome your contributions to any of the following ``genielibs`` modules:

.. csv-table:: Open source module descriptions
    :header: "Module", "Description"
    :widths: 10 90

    "Conf", "Conf objects are built as per the IETF/open-config standards."
    "Ops", "Ops objects are built as per the IETF/open-config standards."
    "Robot", "The libraries are related to the Robot Framework."
    "SDK", "These are the libraries and datafiles for the test cases (:term:`Triggers <trigger>` and :term:`Verifications <verification>`)."

.. _why-contribute

Why contribute?
---------------


Development process
-------------------
Before you begin this process, check Verify if an existing structure (feature structure, ex: BGP, OSPF,..) exists at genielibs/src/conf and genielibs/src/ops. If not, create a new one following conf structure building guide and ops structure building guide guides.


.. _GitHub-basics:



GitHub basics
^^^^^^^^^^^^^
You'll need to know a few basic GitHub commands and processes so that you can download, change, and upload a feature library or component.

.. note:: Internal Cisco developers and engineers follow the same general process as described here, but use Bitbucket rather than GitHub to commit changes. We then synchronize the two when we release on the last Tuesday of every month.

In GitHub, *branches* separate different versions of the same repository, so that more than one person can make changes at the same time. We use the following branches:

* master --- contains code that is already released or ready to be released
* dev --- (internal, Bitbucket users only) contains code that is stable, reviewed, and ready to release
* your_fork --- contains a copy of the repository that you can work on


#. Do you have a GitHub account?

   * If *yes*, go to the next step.
   * If *no*, go to https://github.com/join and create your account. 
    |br|

#. Find the repository for the item that you want to add or extend.

   .. csv-table:: Repository locations
    :file: repo_descriptions.csv
    :header-rows: 1
    :widths: 20 80

#. Fork a repository (see https://help.github.com/en/articles/fork-a-repo).

   * On GitHub (DevNet users), fork off of the master branch.
   * On Bitbucket (internal Cisco users), fork off of the dev branch. |br| |br|

   *Result*: This step creates a copy of the repository that you can work on without affecting anyone else's work. |br| |br|

#. Download the source files::

    git clone repo_name

   where *repo_name* is the name of the repository you want to work on. |br| |br|

Now you are ready to contribute!

Edit or add files
^^^^^^^^^^^^^^^^^
After you download the repo from GitHub (DevNet) or Bitbucket (internal), you can move into develop mode, make your changes, and request approval.

#. Uninstall the modules::

    pip uninstall genie.libs.conf genie.libs.ops genie.libs.sdk genie.libs.robot

   *Result*: The system prompts you to uninstall each module. Enter :monospace:`y` to proceed.

#. Change directories::

    cd genielibs

#. Activate the "develop" mode::

    make develop

   *Result*: The system installs dependencies and sets up the development environment for the ``conf``, ``ops``, ``robot``, and ``sdk`` modules.

#. Edit or add a file.

   See the following topics for details about how to:

    * :ref:`write-parser`
    * :ref:`write-trigger`

Run unit tests
^^^^^^^^^^^^^^
You must run unit tests on all new code. Your changes must not break existing unit tests, and you must include the test results when you open a pull request.

Update the changelog
^^^^^^^^^^^^^^^^^^^^
Before committing any trigger/verification/conf/ops object, you have to add it to the module corresponding changelog so we can keep track of our development efforts. Changelog directory is located at genielibs/pkgs/(pkg_name)/. It contains year/month.md files where we document our monthly development.

Commit your changes
^^^^^^^^^^^^^^^^^^^

Open a pull request
^^^^^^^^^^^^^^^^^^^

#. Add any new files that you create::

    git add filename.py

#. Commit (keep a record of) your changes as you develop new code::

    git commit -a -m 'Message that describes the change.'

#. Push the change to the Git repository::

    git push origin dev

   (Check that this is correct for both GitHub and Bitbucket)

#. Open a pull request to notify the |library| team that your code is ready to review. (Command line or browser?)

PEP8 is used as the reference for code style through out the project. However, the following items needed to be highlighted:

Strictly follow naming conventions in PEP8.
Abide by the 80 characters limit per line. Few exceptions can be allowed.
Leave 2 blank lines between classes, 2 lines between functions, and 1 line between methods.
Write the imports in the following order: Python native libraries, third parties, Genie libraries.











See also...

* `GitHub's "Hello World" get started guide <https://guides.github.com/activities/hello-world/#branch>`_