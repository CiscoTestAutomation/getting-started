Concept Introduction
====================

Originating as Cisco engineering document, *EDCS-1529178*, this sections expands
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

Agnostic & Reusable
-------------------
The test code must remain generic enough such that the support of new 
OS/Platform/Versions shall only entail writing/enhancing libraries for
handling inputs/outputs/timings differences. All platform, OS and version 
specific code must be abstracted into libraries. This promotes code reusability 
whilst reducing overall code complexity.

Consider leveraging the genie.abstract package and contributing your 
agnostic packages and libraries to genie.libs, benefiting the user community. 
Follow guidelines outlined in the repository README files and development 
guides.

Effective & Efficient
---------------------
The effectiveness of a test suite is measured as a function of its execution 
time, resource requirements, and the number of unique problems/bugs/issues it 
catches. As test suites are expected to long-lived, they must be engineered to 
be both time-efficient and cost-effective whilst providing maximum coverage 
and attempting to catch all potential bugs/issues:

* Focus on the feature you are testing and avoid repeating the same test trail.

* Add new tests and/or enhance existing tests as the feature gets more stable. 

* Do things asynchronously when applicable to reduce execution time. 

* Refactor test suites often in order to make them more efficient whilst 
  maintaining the same test coverage. 
* When customers report problems, review your tests and see if you can improve 
  them in order to catch similar problems. 

* Lower the priority (tier) of tests when they lose their value, but do not 
  delete them – test coverage shall only increase, not decrease. 

* Use your knowledge of the source code and architecture and constantly seek 
  to improve the effectiveness of your test suites. 

Reliable & Repeatable
---------------------
Tests that reports pass under failure conditions is worse than not having such 
tests. Automation is software, and is thus also prone to bugs. In order to 
avoid bugs slipping through, code logic shall be explicit and strict (eg, if 
statements covering all possible scenarios), flexible (eg, handles assorted 
environments & timing conditions), and code changes should always be reviewed 
by colleagues and/or subject matter experts.

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
 
