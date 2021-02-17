.. _contribute:

Contribution guidelines
=======================
We strongly encourage everyone to contribute to the pyATS community. The more our users contribute to the pool of feature libraries and components, the more varied, scalable, and robust the |library| becomes. This saves you time and effort when you set up your own network automation.

.. _Helping-with-documentation-issues:

Helping with documentation issues
---------------------------------
If you look at the Github issue tracker (eg. pyats, genie, etc.), you will find various documentation problems that may need work. Issues vary from typos to unclear documentation and items lacking documentation, etc.

If you see a documentation issue that you would like to tackle, you can:

    - check to see if there is already an assignee to it, if not, go for it!
    - assign yourself to that issue.
    - leave a comment on the issue, mentioning the estimated time you will take to tackle the issue.
    - submit a pull request for the issue.

.. _Help-proofreading-documentation:

Help proofreading documentation
-------------------------------
While an issue filed on the issue tracker means there is a known issue somewhere, 
that does not mean that we have found all the issues. Proofreading is also an important part of the documentation.

Here are a few examples that could be great pull requests for proofreading:
    - Fix Typos
    - Better wording, easier explanation
    - More details, examples
    - Anything else to enhance the documentation.

Proofreading workflow: 
    1. read a section of the documentation from start to finish
    2. filing issues in the issue tracker for each major type of problem you find. 
    3. Simple typos don’t require issues of their own, but, instead, submit a pull request directly. 
    4. Try not to file a single issue for an entire section containing multiple problems. Break the issue down, and file several issues. Making it easier to divide the work up for multiple people to perform more efficient review.

.. _Helping-with-source-code:

Helping with source code 
------------------------

We offer the |library| feature libraries and components as open-source code, and we welcome your contributions to any of the following packages:

.. csv-table:: Open source package descriptions
    :header: "Package", "Description"
    :widths: 10 90

    "Conf", "Configuration library"
    "Ops", "Operational state library"
    "Robot", "These libraries support the Robot Framework."
    "SDK", "These libraries and datafiles define the test cases (:term:`Triggers <Trigger>` and :term:`Verifications <Verification>`), API functions, and parsers."

Check the existing components
-----------------------------
Before you begin this process, check to see if an existing ``conf`` or ``ops`` structure, :term:`Trigger`, or :term:`Parser` meets your requirements. On `the pyATS Library GitHub site <https://github.com/CiscoTestAutomation>`_, look at :monospace:`/genielibs/pkgs/<name>-pkg/src/genie/libs/<name>/`, where :monospace:`<name>` is the component that you want to check.

* If you need to create a new feature within the ``conf`` or ``ops`` packages, follow the `conf <https://github.com/CiscoTestAutomation/genielibs/blob/master/CONF.md>`_ or `ops <https://github.com/CiscoTestAutomation/genielibs/blob/master/OPS.md>`_ guidelines.

* If you want to write a new trigger, check to see if an existing trigger exists for the same action (such as ShutNoshut, ConfigUnconfig). Check by feature (such as BGP or OSPF) at `/genielibs/pkgs/sdk-pkg/src/genie/libs/sdk/triggers <https://github.com/CiscoTestAutomation/genielibs/tree/master/pkgs/sdk-pkg/src/genie/libs/sdk/triggers>`_

For verifications (parsers), check by OS and show command at `genieparser/src/genie/libs/parser <https://github.com/CiscoTestAutomation/genieparser/tree/master/src/genie/libs/parser>`_

Clone the source code repository
--------------------------------

.. _GitHub-basics:

GitHub basics
^^^^^^^^^^^^^
You need to know a few basic GitHub commands and processes to download, change, and upload a feature library or component.

.. note:: Internal Cisco developers and engineers use Bitbucket rather than GitHub to commit changes. The |library| team synchronizes the Bitbucket and GitHub repos as part of each monthly release.

In GitHub, *branches* separate different versions of the same repository (repo), so that more than one person can make changes at the same time. We use the following:

* *master* branch --- contains code that is already released or ready to be released.
* *dev* branch --- (internal, Bitbucket users only) contains code that is stable, reviewed, and ready to release.
* *fork* --- contains a complete copy of the original repository. This is what you use to make your changes.

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

#. Clone the repository::

    git clone repo_name

   where *repo_name* is the name of the repository you want to work on. |br| |br|

.. note:: For internal Cisco users on Bitbucket, make sure you are on the :monospace:`dev` branch of the repo when you clone it.

Write new code
--------------
After you clone the repo from GitHub (DevNet) or Bitbucket (internal), you can activate the develop mode, make your changes, and request approval (:ref:`open a pull request <open-pull-request>`).

As a guide, follow the `PEP 8 -- Style Guide for Python Code <https://www.python.org/dev/peps/pep-0008/>`_. Note the following items:

* PEP 8 naming conventions
* 80-character limit per line
* Two blank lines between classes, two lines between functions, and one line between methods
* Write the imports in the following order: 

    * Python native libraries
    * Third-party libraries
    * |library| modules

Tools to check your code
^^^^^^^^^^^^^^^^^^^^^^^^
You can use the following tools to check the PEP 8 and style conventions.

.. csv-table:: Testing tools
   :header: "Tool", "Installation |br| (from your virtual environment)", "Execution"

   "pep8", ":monospace:`pip install pep8`", ":monospace:`pep8 myfile`"
   "pylint", ":monospace:`pip install pylint`", ":monospace:`pylint myfile`"

Conf or Ops packages
^^^^^^^^^^^^^^^^^^^^

#. :ref:`Clone the relevant repository <clone-repo>`. |br| |br|

#. Uninstall the packages::

    pip uninstall genie.libs.conf genie.libs.ops genie.libs.sdk genie.libs.robot -y

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

#. Uninstall the packages::

    pip uninstall genie.libs.parser -y

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

#. For ``conf``, change to the :monospace:`conf/tests` directory,

   .. code-block::

    cd genielibs/src/conf/tests/

   and run all of the ``conf`` tests::
    
    runAll

   *Result*: The system displays the test results. |br| |br|

#. For ``ops``, change to the :monospace:`ops/tests` directory,

   .. code-block::

    cd genielibs/src/ops/tests/

   and run all of the ``ops`` tests::

    runAll

   *Result*: The system displays the test results. |br| |br|

#. For parsers, see the section :ref:`parser-unit-test`. |br| |br|

#. Did all of the tests pass?

    * If *yes*, you can now :ref:`update the changelogs <update-changelog>`.
    * If *no*, check the errors, fix your code, and try again.

External DevNet users
^^^^^^^^^^^^^^^^^^^^^
#. For ``conf``, change to the :monospace:`conf/tests` directory,

   .. code-block::

    cd genielibs/src/conf/tests/

   and run all of the ``conf`` tests::
    
    python -m unittest discover

   *Result*: The system displays any failed tests and the number of tests run. |br| |br|

#. For ``ops``, change to the :monospace:`ops/tests` directory,

   .. code-block::

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

.. _Making-good-commits

Making good commits
-------------------
After you have successfully :ref:`run all of the unit tests <run-unit-tests>` and :ref:`updated the relevant changelogs <update-changelog>`, you can commit and push your changes.

Commit policy
^^^^^^^^^^^^^
* If you commit all of your changes at once, include *only one* feature or *one* bug fix in a single commit. For example, 1 commit = 1 parser (not more than one).
* It's okay to commit one small change at a time, but wait until you complete your changes before you open a pull request.
* Write a useful and descriptive message for each commit.

.. _commit-changes:

Commit your changes
-------------------

.. note:: It's okay to commit (but not push) your changes before you open a pull request. This helps you to track the changes you've made and to revert any changes, if necessary.

Commit procedure
^^^^^^^^^^^^^^^^

#. Did you add any new files?

   * If *yes*, use a git command to add them::

      git add <filename>

   * If *no*, go to the next step. |br| |br|

#. Commit your changes and include a descriptive message. You can commit all of your changes at once,

   .. code-block::

    git commit -a -m 'My descriptive message.'

   or "stage" each change as you make it,

   .. code-block::

    git add mod1
    git add mod2

   and then commit all of the changes::

    git commit -m 'My descriptive message.'

#. When you have committed all of your changes, you can "push" them to your fork.

   * Internal Cisco users -- :monospace:`dev` branch in Bitbucket::

      git push origin dev

   * External DevNet users -- :monospace:`master` branch in GitHub::

      git push origin master

.. _Making-good-pull-request:

Making good pull request
------------------------
Before submitting your pull request (PR), there are several things to be considered:

   * Make sure to follow the `PEP 8 -- Style Guide for Python Code <https://www.python.org/dev/peps/pep-0008/>`
   * Think about backward-compatibility, make sure your changes do not break other's code. (see `PEP 387 <https://www.python.org/dev/peps/pep-0387/>`
   * Please ensure that you have added proper tests to verify your changes work as expected.
   * Run the entire test suite and making sure all tests passed.
   * Remember to update the changelog file for your changes.

.. _open-pull-request:

Open a pull request
-------------------
Open a pull request when you want the |library| team to review your code and merge it into the main repository.

#. From a web browser, go to your fork in the relevant repo. |br| |br|

#. Select **New pull request**.

   .. image:: /images/pull_request.png
   
   |br|

#. On the page where you compare changes, select the **base repository** and branch that you want to merge *into*.

   * Internal Cisco users -- select the :monospace:`dev` branch.
   * External DevNet users -- select the :monospace:`master` branch. |br| |br| 

#. Select your fork as the **head repository**, and then select the **compare** branch that you worked on. |br| |br|

#. Drag and drop screen captures of your unit tests into the description box. For detailed information, see `the GitHub help page <https://help.github.com/en/articles/file-attachments-on-issues-and-pull-requests>`_. |br| |br|

#. Select **Create pull request**.

   *Result*: The |library| team receives a notification to review the request.

See also...

* `GitHub's "Hello World" get started guide <https://guides.github.com/activities/hello-world/#branch>`_
* `API guidelines and good practices <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/apis/index.html#api-guidelines-and-good-practices>`_
* `Conf Guide <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/Conf/index.html#conf-guide>`_
* `Ops Guide <https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/Ops/index.html#ops-guide>`_