Library Guidelines
==================

General
-------

* All users shall prefer to reuse/extending existing libraries over the development of new ones.
* Library APIs shall raise python exceptions when errors are encountered, with clear information and stack trace of the reasons of error.
* Library APIs shall be designed and implemented to be pythonic: natively object-oriented and returning meaningful objects as opposed to raw strings. 
* Library APIs shall receive pythonic arguments and parameters.
* All CLIs shall be spelled out in full, and never truncated, avoiding ambiguity.
* Libraries should be written using genie abstraction package, and always contain the abstract-package declaration in their top-level __init__.py file. With time, token should be added when necessary, following the guidelines outlined in the abstraction package documentation.

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


Configurations
--------------

* Configuration libraries shall be designed using classes representing features/components/hardware on the live device, with each method of the class destined to generate and apply configuration.
* Configuration libraries shall take advantage of connection library’s config() method.
* Configuration errors shall be logged as errors. In case of negative testing, such errors shall be logged as debugs.
* Libraries that generate configuration shall also generate its anti-configuration (e.g. removal/cleanup)
* Configuration functions, classes and methods shall receive all of its inputs via function/class parameters, and global variables shall never be used. Optional configurations shall be enabled/disabled by optional arguments.

Parsers
-------
* Parsers shall be written using Genie MetaParser package
* Parser headers shall contain a sample of each version of supported CLI output.
* Parser header shall contain an explanation of the resulting parsed dictionary-like structure and all available keys. All keys shall be in lowercase.
* Parsers shall be designed to parse as much as possible (parse thoroughly), given a CLI output. Avoid parsing partial information.
* Parsers shall support for variants of the same command, such as “| include”, “| exclude”, etc.

Verification
------------

* Verification APIs shall only use parser outputs, and never parse raw outputs.
* Verifications shall only be done using constant polling, and never through a flat wait value. All polling shall have a maximum timeout/retry value. Such timeouts/retries shall be over writable.
* Verifications shall break out of the polling loop when desired state is reached (or if errors occurred).
* Verifications shall not report errors inside the polling loop. Use debug if necessary. The final result shall only be reported after the polling is complete (or broken out of).
* On errors, both the expected value and the retrieved values should be logged for comparisons, as well as a description of the problem statement.
* On pass, a confirmation of the expected/retrieve value should be logged.
* Verifications should be generic enough that no router configurations are done as part of it. Complex verifications should be done by combining smaller verifications together.
