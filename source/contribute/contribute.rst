.. _contribute:

Contribution guidelines
=======================
Our |library| feature libraries and components are all open source....

.. _why-contribute

Why contribute?
---------------

.. _GitHub-basics:

GitHub basics
-------------
You'll need to know a few basic GitHub commands and processes so that you can download, change, and upload a feature library or component.

#. Do you have a GitHub account?

   * If *yes*, go to the next step.
   * If *no*, go to https://github.com/join and create your account. 
    |br|

#. Find the repository for the item that you want to add or extend.

   .. csv-table:: Repository locations
    :file: repo_descriptions.csv
    :header-rows: 1
    :widths: 20 80

#. Fork a repository (see https://help.github.com/en/articles/fork-a-repo). (Checking on master versus dev branch and also Bitbucket). 

   *Result*: This step creates a copy of the repository that you can work on without affecting anyone else's work.

Master: Only released code or about to be released
Dev: Only stable, reviewed and and ready to ship code should be committed here. Before committing to this branch make sure you run all the unitest and they all pass. (Please submit a pull request BEFORE committing code here. If you do without, the commit will be removed)
your_branch: All code development should be done in different branch. This is helpful for quickly changing work.

Fork a repo:


Download the source files
^^^^^^^^^^^^^^^^^^^^^^^^^

Change or add to the source files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
See the following topics for details about how to:

* :ref:`write-parser`
* :ref:`write-trigger`

PEP8 is used as the reference for code style through out the project. However, the following items needed to be highlighted:

Strictly follow naming conventions in PEP8.
Abide by the 80 characters limit per line. Few exceptions can be allowed.
Leave 2 blank lines between classes, 2 lines between functions, and 1 line between methods.
Write the imports in the following order: Python native libraries, third parties, Genie libraries.


Run unit tests
^^^^^^^^^^^^^^
All new code must have unittest and not break existing unittest.


Update the changelog
^^^^^^^^^^^^^^^^^^^^
Before committing any trigger/verification/conf/ops object, you have to add it to the module corresponding changelog so we can keep track of our development efforts. Changelog directory is located at genielibs/pkgs/(pkg_name)/. It contains year/month.md files where we document our monthly development.

Open a pull request
^^^^^^^^^^^^^^^^^^^

.. _submit-pr:

Submit a pull request
^^^^^^^^^^^^^^^^^^^^^

.. _make-dev-undev:

Make develop/undevelop
----------------------

.. _write-unit-tests:

Write unit tests
----------------
asdf

See also...

* `GitHub's "Hello World" get started guide <https://guides.github.com/activities/hello-world/#branch>`_