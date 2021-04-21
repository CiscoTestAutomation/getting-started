Library Guidelines
==================

General
-------

* All users shall prefer to reuse/extending existing libraries over the development of new ones.
* Library APIs shall raise python exceptions when errors are encountered, with clear information and stack trace of the reasons of error.

  .. code-block:: python

     # Wrong
     def my_func(var1, var2):
         if ...<some error>:
             return False

  .. code-block:: python

     # Correct
     def my_func(var1, var2):
         if ...<some error>:
             raise Exception('<some error>')

* Library APIs shall be designed and implemented to be pythonic: natively object-oriented and returning meaningful objects as opposed to raw strings.
* Library APIs shall receive pythonic arguments and parameters.
* All CLIs shall be spelled out in full, and never truncated, avoiding ambiguity.

  .. code-block:: python

     # Wrong
     device.execute('sh int')

  .. code-block:: python

     # Correct
     device.execute('show interface')

* Libraries should be written using `pyATS abstraction <https://pubhub.devnetcloud.com/media/genie-docs/docs/abstract/index.html>`_ package, and always contain the abstract-package declaration in their top-level __init__.py file. With time, token should be added when necessary, following the guidelines outlined in the abstraction package documentation.

* Avoid, at all-cost, the writing of local libraries and APIs specific to your script.

Headers
-------

* Library modules shall contain the following in its docstrings header:

  * Owner and support email
  * Library version
  * Purpose, description and expected results.

* Library classes and functions shall contain the following in its docstrings header:

  * Purpose, description and expected result
  * Input parameter requirement
  * Return values
  * Possible raised exceptions

* Example of docstring in the `script templates <https://github.com/CiscoTestAutomation/pyATS-project-template>`_ (eg, pyATS 

Configurations
--------------

* Configuration libraries shall take advantage of connection library’s `configure() <https://pubhub.devnetcloud.com/media/unicon/docs/user_guide/services/generic_services.html#configure>`_ method.
* Configuration errors shall be logged as errors. In case of negative testing, such errors shall be logged as debugs.
* Libraries that generate configuration shall also generate its anti-configuration (e.g. removal/cleanup)
* Configuration functions, classes and methods shall receive all of its inputs via function/class parameters, and global variables shall never be used. Optional configurations shall be enabled/disabled by optional arguments.

Parsers
-------
* Parsers shall be written using `Genie Parsers <https://pubhub.devnetcloud.com/media/pyats-development-guide/docs/writeparser/writeparser.html#>`_.
* Parser header shall contain an explanation of the resulting parsed dictionary-like structure and all available keys. All keys shall be in lowercase.
* Parsers shall be designed to parse as much as possible (parse thoroughly), given a CLI output. Avoid parsing partial information.
* Parsers shall support for variants of the same command, such as “| include”, “| exclude”, etc.

Videos `[1] <https://youtu.be/ibLNilSfdTc>`_ `[2] <https://youtu.be/knxkbWTamBY>`_ on how to develop parser.

Verification
------------

* Verification APIs shall only use parser outputs, and never parse raw outputs.
* Verifications shall only be done using constant polling, and never through a flat wait value. All polling shall have a maximum timeout/retry value. Such timeouts/retries shall be over writable.
* Verifications shall break out of the polling loop when desired state is reached (or if errors occurred).
* Verifications shall not report errors inside the polling loop. Use debug if necessary. The final result shall only be reported after the polling is complete (or broken out of).
* On errors, both the expected value and the retrieved values should be logged for comparisons, as well as a description of the problem statement.
* On pass, a confirmation of the expected/retrieve value should be logged.
* Verifications should be generic enough that no router configurations are done as part of it. Complex verifications should be done by combining smaller verifications together.

Dialog example
--------------

    .. code-block:: python

        # Bad
        def send_newline_and_wait_callback(spawn):
            time.sleep(0.5)
            spawn.sendline()

        def send_no_and_wait_callback(spawn):
            time.sleep(0.5)
            spawn.sendline("no")

        def send_yes_and_wait_callback(spawn):
            time.sleep(0.5)
            spawn.sendline("yes")

        def send_multiple_newlines(spawn):
            for _ in range(3):
                time.sleep(2)
                spawn.sendline()
            time.sleep(2)

        config_dialog = Dialog([
            Statement(pattern=r"Would you like to enter the "
                              r"initial configuration dialog\?\s\[yes/no\]:\s?$",
                        action=send_no_and_wait_callback,
                        loop_continue=True),
            Statement(pattern=r"^Would you like to terminate autoinstall\?\s?\[yes\]:\s?$",
                        action=send_yes_and_wait_callback,
                        loop_continue=True),
            Statement(pattern=r"Press RETURN to get started!",
                        action=send_multiple_newlines,
                        loop_continue=True),
            Statement(pattern=r'^(.*)>\s?$',
                        action=send_newline_and_wait_callback,
                        loop_continue=False,
                        continue_timer=False)
        ])


    .. code-block:: python

        # Good
        config_dialog = Dialog([
            Statement(pattern=r"Would you like to enter the initial configuration dialog\?\s\[yes/no\]:\s?$",
                    action=sendline(no),
                    loop_continue=True,
                    continue_timer=0.5),
            Statement(pattern=r"Would you like to terminate autoinstall\?\s\[yes\]:\s?$",
                    action=sendline(yes),
                    loop_continue=True,
                    continue_timer=0.5),
            Statement(pattern=r"Press RETURN to get started!",
                    action=sendline(),
                    loop_continue=True,
                    continue_timer=8),
            Statement(pattern=r"^(.*)>\s?$",
                    action=sendline(),
                    loop_continue=False)])
