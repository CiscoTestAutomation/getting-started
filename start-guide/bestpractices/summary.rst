Summary
=======

Ideology
--------

- breakdown a large test plan into small, idempotent testcases

- avoid writing one-use test scripts. Focus on writing reusable testcases,
  and contribute your agnostic testcase to the overall pool of available tests.

- divide each testcase into logical test sections, with each section further
  broken down into individual test steps. The goal is to create test flows that
  are compartmentalized and clear.

- do not hard-code values/configuration directly within your testcases. Use
  input arguments and data files for that.

- call standard API libraries (eg, pyATS/Genie libs and parsers). If an API you
  are looking for is missing, contribute to the common ecosystem and benefit
  everyone. **Avoid, at all-cost, the writing of local libraries and APIs 
  specific to your script**.

- where possible, perform actions in parallel

- catch failures where you can. If something is failing, fail-fast.


Recommended Features
--------------------

- Tag/group your testcases using the AEtest testcase grouping feature: it 
  enables you to run selective groups of testcases without modifying your 
  test script.
 
- Max failures/max runtime: turn on these options to ensure your script fails
  fast when errors are encountered, and no testbed times are wasted

- Healthchecks: leverage the pyATS healthcheck feature to ensure the auto collection
  of device cores/tracebacks before/after each test case


Am I Done?
----------

The following checklist will help you to review & revisit whether your work is
truly finished:

- Did you add documentation, docstrings, and README files? Make sure your
  script runtime environment/testbed requirement is well documented

- Are healthchecks enabled?

- Are you leveraging script max runtime/failure features?

- Are your testcases dynamic, data-driven, and reusable? Should any of them 
  be committed into the pyATS/Genie trigger/verification library?

- Does your script leverage pyATS/Genie parsers and libraries? Does it contain
  local libraries, that could be committed to the common set and benefiting
  all users?

- Did you user a linter (Flake8, PyLint etc) to lint your code?
