Topology Guidelines
===================

Format
------

* Testbed physical topology shall be defined following pyATS topology YAML format and template.
* Testbed topology file shall adhere to pyATS topology production schema.
* Custom topology information shall always be defined under ``custom:`` section.
* Testbed topology file shall only contain physical devices and links (this also includes actual software-based and virtual devices).
* When bringup is used, the topology file may contain logical routers (placeholders until replaced with actual router information)
* Testbed topology file shall not hard-code configurations, dynamic and test suite input information.

Usage
-----
* Testbed topology file shall be provided to pyATS using ``–-testbed-file`` argument.

* Test suites sections that requires access to testbed topology shall access the topology objects via testbed parameter.

* Testbed devices and interfaces shall be dereferenced using alias feature. Testbed devices names shall never be referenced directly.

* Where you have multiple testbeds that are similar, and or are supersets of each other, make use of the pyATS YAML extension feature,
  and create YAML files that extend each other. Eg: start with base testbed YAML, create extended testbed YAML (auto-including the content from 
  base, etc).