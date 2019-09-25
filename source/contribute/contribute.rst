.. _contribute:

Contribution guidelines
=======================
We offer the |library| feature libraries and components as open-source code, and we welcome your contributions to any of the following packages:

.. csv-table:: Open source package descriptions
    :header: "Package", "Description"
    :widths: 10 90

    "Conf", "Conf objects adhere to the IETF/OpenConfig standards."
    "Ops", "Ops objects adhere to the IETF/OpenConfig standards."
    "Robot", "These libraries support the Robot Framework."
    "SDK", "These libraries and datafiles define the test cases (:term:`Triggers <trigger>` and :term:`Verifications <verification>`)."

.. tip:: The more our users contribute to the pool of feature libraries and components, the more varied, scalable, and robust the |library| becomes. This saves you time and effort when you set up your own network automation.



Check the existing components
-----------------------------
Before you begin this process, check to see if an existing ``conf`` or ``ops`` :term:`feature` structure, :term:`trigger`, or :term:`parser` meets your requirements. On `the pyATS Library GitHub site <https://github.com/CiscoTestAutomation>`_, look at :monospace:`/genielibs/pkgs/<name>-pkg/src/genie/libs/<name>/`, where :monospace:`<name>` is the component that you want to check.

If you need to create a new feature within the ``conf`` or ``ops`` packages, follow these guidelines:

* `conf guidelines <https://github.com/CiscoTestAutomation/genielibs/blob/master/CONF.md>`_
* `ops guidelines <https://github.com/CiscoTestAutomation/genielibs/blob/master/OPS.md>`_

If you want to write a new trigger or verification, check to see if an existing trigger or verification exists for the same action (such as ShutNoshut, ConfigUnconfig), by feature (such as BGP or OSPF): `/genielibs/pkgs/sdk-pkg/src/genie/libs/sdk/triggers <https://github.com/CiscoTestAutomation/genielibs/tree/master/pkgs/sdk-pkg/src/genie/libs/sdk/triggers>`_

For verifications (parsers), check by OS and show command: `genieparser/src/genie/libs/parser <https://github.com/CiscoTestAutomation/genieparser/tree/master/src/genie/libs/parser>`_


Clone the source code repository
--------------------------------

.. _GitHub-basics:

GitHub basics
^^^^^^^^^^^^^
You'll need to know a few basic GitHub commands and processes so that you can download, change, and upload a feature library or component.

.. note:: Internal Cisco developers and engineers follow the same general process as described here, but use Bitbucket rather than GitHub to commit changes. We then synchronize the two when we release on the last Tuesday of every month.

In GitHub, *branches* separate different versions of the same repository (repo), so that more than one person can make changes at the same time. We use the following branches:

* master --- contains code that is already released or ready to be released
* dev --- (internal, Bitbucket users only) contains code that is stable, reviewed, and ready to release
* your_fork --- contains a copy of the repository that you can work on

.. _clone-repo:

Clone the repo
^^^^^^^^^^^^^^

#. Do you have a GitHub account?

   * If *yes*, go to the next step.
   * If *no*, go to https://github.com/join and create your account. |br| |br|


#. Find the repository for the component that you want to add or extend.

   .. csv-table:: Repository locations
    :file: repo_descriptions.csv
    :header-rows: 1
    :widths: 10 10 80

#. Fork a repository (see https://help.github.com/en/articles/fork-a-repo).

   * On GitHub (DevNet users), fork off of the master branch.
   * On Bitbucket (internal Cisco users), fork off of the dev branch. |br| |br|

   *Result*: This step creates a copy of the repository that you can work on without affecting anyone else's work. |br| |br|

#. Download the source files::

    git clone repo_name

   where *repo_name* is the name of the repository you want to work on. |br| |br|

    .. note:: For internal Cisco users on Bitbucket, make sure you are on the :monospace:`dev` branch of the repo when you clone it.

Now, you are ready to contribute! Once you have written your new code, you can :ref:`open a pull request <open-pull-request>` to ask the |library| team to accept your changes.

Write new code
--------------
After you download the repo from GitHub (DevNet) or Bitbucket (internal), you can move into develop mode, make your changes, and request approval (:ref:`open a pull request <open-pull-request>`).

All code follows the `PEP 8 -- Style Guide for Python Code <https://www.python.org/dev/peps/pep-0008/>`_. Note the following items:

* Strictly follow the PEP 8 naming conventions.
* Abide by the 80 character limit per line.
* Leave two blank lines between classes, two lines between functions, and one line between methods.
* Write the imports in the following order: Python native libraries, third party libraries, and |library| modules.

Conf or Ops packages
^^^^^^^^^^^^^^^^^^^^

#. :ref:`Clone the relevant repository <clone-repo>`. |br| |br|

#. Uninstall the packages::

    pip uninstall genie.libs.conf genie.libs.ops genie.libs.sdk genie.libs.robot

   *Result*: The system prompts you to uninstall each package. Enter :monospace:`y` to proceed. |br| |br|

#. Change directories::

    cd genielibs

#. Activate the "develop" mode::

    make develop

   *Result*: The system installs dependencies and packages, and sets up the development environment for the ``conf``, ``ops``, ``robot``, and ``sdk`` packages. |br| |br|

#. Write your own code as required.

   See the following topics for details about how to:

    * :ref:`write-parser`
    * :ref:`write-trigger`

Parsers
^^^^^^^
#. :ref:`Clone the relevant repository <clone-repo>`. |br| |br|

#. Change directories::

    cd genieparser

#. Activate the "develop" mode::

    make develop

   *Result*: The system installs dependencies and packages, and sets up the development environment. |br| |br|

#. See detailed steps for writing and testing a parser in the topic :ref:`write-parser`.

.. _run-unit-tests:

Run unit tests
--------------
.. important:: 

   * You must run unit tests on all new code. 
   * Your changes must not break existing unit tests.
   * You must include the test results when you :ref:`open a pull request <open-pull-request>`.

Internal Cisco users
^^^^^^^^^^^^^^^^^^^^
#. Install cisco-distutils::

    pip install cisco-distutils

#. For ``conf``, change to the :monospace:`conf/tests` directory::

    cd genielibs/src/conf/tests/

   and run all of the ``conf`` tests::
    
    runAll

   *Result*: The system displays the test results. |br| |br|

#. For ``ops``, change to the :monospace:`ops/tests` directory::

    cd genielibs/src/ops/tests/

   and run all of the ``ops`` tests::

    runAll

   *Result*: The system displays the test results. |br| |br|

#. For parsers, see the section :ref:`parser-unit-test`. |br| |br|

#. Did all of the tests pass?

    * If *yes*, go to the next step.
    * If *no*, check the errors, re-write your code, and try again.

#. (Talk with SME about the script that creates and diffs verifications.)

External DevNet users
^^^^^^^^^^^^^^^^^^^^^
#. For ``conf``, change to the :monospace:`conf/tests` directory::

    cd genielibs/src/conf/tests/

   and run all of the ``conf`` tests::
    
    python -m unittest discover

   *Result*: The system displays any failed tests and the number of tests run. |br| |br|

#. For ``ops``, change to the :monospace:`ops/tests` directory::

    cd genielibs/src/ops/tests/

   and run all of the ``ops`` tests::

    python -m unittest discover

   *Result*: The system displays any failed tests and the number of tests run. |br| |br|

#. For parsers, see the section :ref:`parser-unit-test`. |br| |br|

#. Did all of the tests pass?

    * If *yes*, you can now :ref:`update the changelogs <update-changelog>`.
    * If *no*, check the errors, re-write your code, and try again.

.. _update-changelog:

Update the changelog
--------------------
We use changelogs for each package (:monospace:`genielibs/pkgs/<name>-pkg/changelog`) to track all development efforts by month and year.

#. In the repo, locate the year and month for the next release.

#. In your fork of the main repo, in the :monospace:`<month>.md` file, add a clear and brief description of your change.

You can either edit the file directly, or change it locally and then :ref:`commit your changes <commit-changes>`.

.. _commit-changes:

Commit your changes
-------------------
After you have successfully :ref:`run all of the unit tests <run-unit-tests>` and :ref:`updated the relevant changelogs <update-changelog>`, you can commit and push your changes.

.. note:: It's okay to commit (but not push) your changes before you open a pull request. This helps you to track the changes you've made and to revert any changes, if necessary.

Commit policy
^^^^^^^^^^^^^
* If you commit all of your changes at once, include *only one* feature or *one* bug fix in a single commit. For example, 1 commit = 1 parser (not more than one).
* It's okay to commit one small change at a time, but wait until you complete your changes before you open a pull request.
* Write a useful and descriptive message for each commit.

Commit procedure
^^^^^^^^^^^^^^^^

#. Did you add any new files?

   * If *yes*, use a git command to add them::

      git add <filename>

   * If *no*, go to the next step. |br| |br|

#. Commit your changes and include a descriptive message. You can commit all of your changes at once::

    git commit -a -m 'My descriptive message.'

   or "stage" each change as you make it... ::

    git add <modified_filename1>
    git add <modified_filename2>

   and then commit all of the changes::

    git commit -m 'My descriptive message.'

#. When you have committed all of your changes, you can "push" them to your fork.

   * Internal Cisco users -- :monospace:`dev` branch in Bitbucket::

      git push origin dev

   * External DevNet users -- :monospace:`master` branch in GitHub::

      git push origin master



.. _open-pull-request:

Open a pull request
-------------------
Open a pull request to notify the |library| team that your code is ready to review and merge into the main repository.















See also...

* `GitHub's "Hello World" get started guide <https://guides.github.com/activities/hello-world/#branch>`_