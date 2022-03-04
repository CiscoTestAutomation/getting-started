Concept Introduction
====================

Dream
-----

Imagine a development environment where all libraries you need are there. You can re-use libraries to develop your testcases, business requirement, re-use all libraries which have been developped in previous testcase by anybody else. This mean, the Bgp team re-use the OSPF team libraries, routing re-using platform, IOSXR re-using NXOS when needed. Each have great log message in the case they fail, or pass. You could 100% focus on what you want to do, and not focus on how to do it.

If we had this, imagine what our testcases would look like.

.. code-block:: python

   dev.api.shut_interface(interface='Ethernet2/3')
   if dev.api.verify_interface_shut(interface='Ethernet2/3'):
       self.failed('Interface is not shut')
   ...

.. code-block:: python

   dev.reload()
   ...

It makes the script code very easy and quick to write. It also makes the code extremely readable by your teammate and other people that might inherits this script in the future.

If a library does not exists yet, add it and then continue with your automation. Each library follows good developing practice:

* One common library which is shared to all
* Re-usable library

  * Parsers
  * Apis
  * Connections
  * Testcases
  * ...
* No code duplication
* Debuggable
* Good comments

This is one of the goal of having good practice; Creating a development environment
that scales, simplify the work for all, and speed up development. As time pass, a larger and a better libraries exists for all to use.

For this to exists, we need guidelines and best practice.


Introduction
------------

Originating as Cisco engineering document, *EDCS-1529178*, this documentation expands
on the best practices of writing pyATS test cases and libraries. It was created 
with a few purposes in mind:

* To enforce device agnostic, modular automation 

* To help design better automation that is scalable and reliable

* To establish basic principles around what is and is not acceptable 
  in generic test automation life cycle – test automation is software as well.

* To be used as a tool for someone looking to review someone else’s code.

* Enable standard/consistency in automation for ease of port, inheritance 
  & maintenance


This document is a list of do’s and do-not’s for pyATS-based automation, 
and is written like a set of rules/regulations.

* The words “must” & “shall” means that the guideline is a non-optional
  requirement. 

* The word “should” means that the guideline is strongly suggested, but other 
  acceptable options may also be used (if applicable).

It is recommended that the content of this document be used during code reviews, 
and code design & planning.

This document is intended for individual & engineers using and developing 
automated test scripts and their supporting libraries, modules and packages
under the pyATS ecosystem. 


Forewords
---------

Test automation is no different than any other software development: using 
software to test software. It requires clear understanding of overall 
requirements, proper planning, solid design, and most importantly, 
disciplined programming. This document offers an organized collection of ideas 
and practices intended to guide pyATS users throughout this development process.

Automation must be cost-effective in the long-term. We should keep this in 
mind while planning, designing, and developing test automation. The following 
is a set of key principles that all test automation development shall follow.

We tried to add as much example as possible to make the content less dry, and
easier to follow.

Agnostic & Reusable
-------------------
The test code must remain generic enough such that the support of new 
OS/Platform/Versions shall only entail writing/enhancing libraries for
handling inputs/outputs/timings differences. All platform, OS and version 
specific code must be abstracted into libraries. This promotes code reusability 
whilst reducing overall code complexity.

Consider leveraging the `genie.abstract <https://pubhub.devnetcloud.com/media/genie-docs/docs/abstract/index.html>`_ package and `contributing <https://pubhub.devnetcloud.com/media/pyats-development-guide/docs/writeparser/writeparser.html>`_ your 
agnostic packages and libraries to genie.libs, benefiting the user community.
Follow guidelines outlined in the repository README files and development
guides.

    .. code-block:: python
      :name: this_just_bumps_code_over

        # Wrong
        if '17.2' in show_version:
            do_something()
        elif '17.3' in show_version:
            do something()
        elif '17.5' in show_version:
            do_something()
        ...


    .. code-block:: python
      :name: this_just_bumps_code_over

        # Correct
        # Because of abstraction, no need to do the ifs
        # and it will find the right library for this os, platform, image, ...
        dev.api.do_something()

* As new version of the OS appear, we should not be modifying all our scripts,
  but only the library that drives the script.

Effective & Efficient
---------------------
The effectiveness of a test suite is measured as a function of its execution 
time, resource requirements, and the number of unique problems/bugs/issues it 
catches. As test suites are expected to long-lived, they must be engineered to 
be both time-efficient and cost-effective whilst providing maximum coverage 
and attempting to catch all potential bugs/issues:

* Focus on the feature you are testing and avoid repeating the same test trail.

* Add new tests and/or enhance existing tests as the feature gets more stable. 

* Do things `asynchronously <https://pubhub.devnetcloud.com/media/pyats/docs/async/pcall.html>`_ when applicable to reduce execution time. 

* Refactor test suites often in order to make them more efficient whilst 
  maintaining the same test coverage. 
* When customers report problems, review your tests and see if you can improve 
  them in order to catch similar problems. 

* Lower the priority (tier) of tests when they lose their value, but do not 
  delete them – test coverage shall only increase, not decrease. 

* Use your knowledge of the source code and architecture and constantly seek 
  to improve the effectiveness of your test suites. 


**In summary**

* Effectiveness of a test script
  
  * execution time
  * resource requirements
  * number of unique problems/bugs/issues it catches
* Time limit per test suite

  * Reserve devices
  * Clean
  * Configure

* Use Asynchronous as much as possible
* Constant review of coverage
* Prioritize testcases

Reliable & Repeatable
---------------------
Tests that reports pass under failure conditions is worse than not having such 
tests. Automation is software, and is thus also prone to bugs. In order to 
avoid bugs slipping through, code logic shall be explicit and strict (eg, if 
statements covering all possible scenarios), flexible (eg, handles assorted 
environments & timing conditions), and code changes should always be reviewed 
by colleagues and/or subject matter experts.

**In summary**

* Test automation must always give the same result with the starting point
* Inconsistent results make you question everything

  * Is it the device?
  * Is it the script ?
  * Configuration ?
  * Let's rerun to try to find the issue - Waste of time

* Pass under Failure condition is worse than having no test

Sustainable & Responsible
-------------------------
Over the course of its life, a test suite goes through many revisions and its
ownership possibly transitioned through multiple groups. These revisions may 
be enhancements (increasing coverage/platform support), bug fixes (correcting
errors in the code logic), or amendments (conforming to changes in the product 
under test). As such, all test automation suites shall be designed to be 
maintainable: minimizing the amount of effort associated with revisions 
& sustainment. 

As an example, test suites typically rely heavily on device control I/O 
(e.g. CLI). As these are prone to change during a product’s life cycle, test 
suites shall be designed in such a way that these revisions can be reflected 
in the test code through minimal changes: e.g., by following a modular design 
using objects and classes, reusing and extending existing libraries whenever 
possible.

Keep test suites easy to read, comprehend & use by following consistent style 
and through thorough documentation. Describe what is being accomplished, comment 
on complex code and logic, and detail the different use-cases of your creations
and how to debug them in case of failures. Keep your comments to the point and 
accurate in the explanation.
 
**In summary**

* Scripts get modified

  * Increasing Coverage
  * Platform Support
  * Bug Fix

* Ownership will change over the course of script life
* The goal should be to Minimize effort each time it has to be modified
* Easy to read
* Consistent style across script, library
* Documentation

  * Header
  * Comments

* Maintain comments
* Be explicit with your errors
