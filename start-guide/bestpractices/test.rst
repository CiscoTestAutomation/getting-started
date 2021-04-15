Test Suite Guidelines
=====================

Generic
-------
* Test suites shall be written following pyATS `script templates<https://github.com/CiscoTestAutomation/pyATS-project-template>`_ (eg, pyATS 
  project template, Genie Trigger/Verification template) 

* Test suites shall be unique. Inheritance should be used in cases where 
  test case re-use is applicable.

.. code-block:: python

        from script_a import OldTestcase

        class ReuseTestcase(OldTestcase):
            pass

* Test suites shall leverage existing libraries where possible.

* Test cases should be categorized using execution `grouping feature<https://pubhub.devnetcloud.com/media/pyats/docs/aetest/control.html#testcase-grouping>`_.

* Global variables shall not be used within test suites.

**Bad**

.. code-block:: python

    global variable

* Test suites shall never hard-code the required testbed devices, links and 
  interface names. It should either reference them using testbed aliases, or 
  accept a mapping as input argument to the test suite, satisfying its topology 
  requirements.

Headers
-------

* Test suites shall container a header (using docstring), detailing on:

  * Owner and support email
  * Script version
  * Purpose, description and expected results.
  * Test-plan and automation design documents pointer/references
  * Topology requirement and diagram
  * Input parameter/argument requirement, including each argument’s purpose and range.
  * Library requirement
  * Any other hardware/equipment used during testing.

* Test cases shall contain a header (using docstring), detailing on:

  * Purpose, description and expected result
  * Sub-topology requirement
  * Input parameter requirement
  * Summary of tests performed

* Each test shall have its own header:

  * Input parameters
  * Description of the test

  Example can be found `here<https://github.com/CiscoTestAutomation/pyATS-project-template/blob/master/template/template_script.py>`_.

Common Setup/Cleanup
--------------------

* Test suite should have a common setup section that performs the following tasks:

  * Environment checks
  * Script input argument check
  * Parsing of environment variables and command-line arguments (following argument propagation). Parsing shall be done using python argparse module.
  * Library existence check
  * Abstraction lookup object creations
  * Testbed device connection establishment
  * Testbed basic connectivity check: interface/network pings, link states, etc.
  * Testbed topology validation.
  * Testbed feature enablement: HA, licenses, etc.
  * Traffic generator initialization
  * Common configuration/setups shared by all test cases.
  * All other required validations/initializations.

* Test suite should have a common cleanup section that performs the following tasks:

  * Cleanup all left-over configurations from the testbed, regardless of failure/errors
  * Stop any traffic generator streams
  * Returning testbed and current environment to its initial states
  * Disconnect from everything.

* Common setup/cleanup sections shall be broken down into smaller subsections, with each subsection performing one unique task.

* Common cleanup shall be written in a fail-proof fashion: regardless of prior test case’s pass/fail/error results, it shall be able to run flawlessly, returning the environment to its initial state.

Test cases
----------

* Test cases shall be independent from each other and shall be able to be run in randomized order.

* Test cases should be tagged with their corresponding execution groups.

* Test cases should contain a setup section that configure/setup all test case specific environment settings such as:
  
  * Traffic generators
  * Testbed device configurations

* Test cases should contain that cleanup section that undo all changes made in this test case. This should be written in a fail-proof fashion: regardless of prior test’s results, this cleanup action should be thorough.

* Test cases shall contain one or more tests that performs the action testing. 

* Test cases that are not applicable to the current given environment (testbed) shall be skipped.

Tests
-----

* Tests shall receive all of its required parameters as function arguments.
* Tests should be further broken down into steps.
* Tests that are not applicable to the current given environment (testbed) shall be skipped.
* Tests should be independent from each other. 

Debugging
---------

* Test suites should collect for trace-backs, memory-leaks and core dumps at various strategic points in the script (e.g. at the end of test cases, at the end of common setup/cleanup sections). Look into `pyATS Health<https://pubhub.devnetcloud.com/media/genie-docs/docs/health/index.html>`_

* All code shall be written with the assumption that it may fail at any step: errors shall be handled intelligently and gracefully.
  
  * Report errors in the result report, with details of the error in the log file.
  * Collect all associated debug information (core dumps, debug commands, etc.) for post-mortem debugging purposes.
  * Exit gracefully after cleaning up the environment

**Good**

.. code-block:: python

   try:
       some code that might blow up
   except Exception:
       handle it

**Bad**

.. code-block:: python

    some code that might blow up

* Common-cleanup should always be executed to perform clean-up duty if something fails dramatically.



Code Coverage
-------------

Internal only links
`CTC<http://wwwin-pyats.cisco.com/cisco-shared/ctc/latest/index.html>`_
`CRFT<http://wwwin-pyats.cisco.com/cisco-shared/plugin_bundle/latest/>`_

* Test suites should measure, collect and support the analysis of its automated tests’ code-coverage.
* Test suites should strive for the best code coverage possible, whilst balancing runtime efficiency.
* Test suites should support execution on code-coverage instrumented images (e.g. code-coverage timing vs regular timing)
* If code-coverage is enabled, test suites should check for instrumented images before continuing.
* Code-coverage collection shall be performed only via use of common library functions and packages.
* Code-coverage metrics shall be collected and stored along with runtime log files.
