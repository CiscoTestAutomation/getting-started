.. _upgrade-pyats:

Keep |pyATS| up to date
========================
On the last Tuesday of the month, the team releases a new version of |pyATS| and the |library|. This section describes how to get the latest changes.

.. qs-upgrade::

To upgrade the |pyATS| and |library| :doc:`infrastructure </definitions/def_pyats_code_infrastructure>`, and any or all of the :doc:`feature libraries and components </definitions/def_pyatslibrary_code_structure>`, run the ``pip install --upgrade`` command **from your virtual environment**.

Internal Cisco users
^^^^^^^^^^^^^^^^^^^^^

.. tip:: Cisco members of the "pyats-notices" mailer list receive a notification about each release. :question:`How does an internal user sign up to the notices?`

.. csv-table:: Internal Cisco user upgrade options
    :file: ../quickstart/UpgradeInternal.csv
    :header-rows: 1
    :widths: 25 35 40

*Result*: The installer checks for and upgrades any dependencies, and gives you the latest version of the |pyATS| and |library| core and library packages. To check the version::

  (pyats) $ pip list | egrep 'ats|library'

*Result*: The system displays a list of the packages and the installed versions.

.. attention:: The major and minor versions must all match. It's okay if the patch version varies.

DevNet community users
^^^^^^^^^^^^^^^^^^^^^^^
.. tip:: You can find the latest information about releases on Twitter at #pyATS.

.. csv-table:: DevNet user upgrade options
    :file: ../quickstart/UpgradeExternal.csv
    :header-rows: 1
    :widths: 25 35 40


*Result*: The installer checks for and upgrades any dependencies, and gives you the latest version of the |pyATS| and |library| core and library packages. To check the version::

  (pyats) $ pip list | egrep 'pyats|library'

*Result*: The system displays a list of the packages and the installed versions.

.. attention:: The major and minor versions must all match. It's okay if the patch version varies.

See also...
*a list of relevant links*

* link 1
* link 2
* link 3
