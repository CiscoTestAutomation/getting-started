********************
Design & Development
********************

Following Agile software development methodology, test suites shall be carefully
planned, designed, and iteratively developed. This section provides high-level
insights on how pyATS test automation development should be properly carried
out.

Automate Everything?
====================

Ideally, all tests should be automated. However, this isn’t always practical,
feasible, and/or cost-effective. The following questions should be answered as
part of your design phase for determining which tests should be automated:

* How critical is this feature?

* How likely will this test find potential bugs/errors/problems?

* What are the costs (both time/effort and hardware/software requirements) of
  automating this test?

* What is the longevity and long-term benefits of automating this test?

* Will it generate by-products (e.g., libraries) that others may leverage?

Make It Simple
==============

The simplest things are often the hardest: use and perform only what is
necessary to achieve your goals, and avoid overly complicating your design,
implementation and requirements. However, do not confuse simplicity and
straightforwardness with poor designs. A simple design can still be elegant,
extendable and effective.

The K.I.S.S. Principle
----------------------

Always consider factors such as hardware/software/license costs,
development/setup/execution times, and the skills & efforts required to use and
maintain your product. Keep in mind that your creations will be
used for years to come, passed from one engineer to the next: simplicity
facilitates the long-term sustenance costs.

  .. code-block:: python

        # Bad
        def GetMemory(self, testbed, testscript, method, param = False):
            uut_arr = testscript.parameters['devices']
            uut = testbed.devices[uut_arr[0]]
            uut.connect()
            result = uut.execute("show memory")
            if param is True:
                lines = result.splitlines()
                line = lines[0]
                words = line.split()
                free_memory = int(words[7][:-1])
                if free_memory <= 1048576:
                    log.error("Not enough free memory")
                    method.failed()
                    return
                else:
                    return

  .. code-block:: python

        # Good
        def verify_minimum_size(device, minimum_size):
        device.connect()
        result = device.parse('show memory')
        free_memory = result['free_memory']
        if free_memory <= minimum_size:
            raise Exception('Requires at least {minimium_size} of free memory; '
                            'but only {free_memory} is available'
                            .format(minimum_size=minimum_size,
                                    free_memory=free_memory))

Don't reinvent the wheel
------------------------

Prioritize the use of existing tools, packages and libraries. Where needed,
use best-of-breed open-source solutions – when doing so, make sure it is
popular, well developed & supported.

  .. code-block:: python

        # Bad
        d.sendline("reload\r")
        d.expect("Proceed with reload?", timeout=10)
        d.sendline("y\r")
        log.debug("Sleeping 200 seconds for CSR image reload")
        time.sleep(200)
        d.disconnect()


    .. code-block:: python

        # Good
        device.reload(timeout = sleep_time)

Leave it to the pros
--------------------

Always use these external components in
their originally intended fashion: taking unintended shortcuts and hacking
internals often leads to long-term technical debt.

    .. code-block:: python

        # Bad
        result = uut.execute("show processes | include CPU")
        words = result.split()
        #for five seconds
        fives_string = words[5]
        fives_number = int(fives_string[0:1])
        return fives_number

    .. code-block:: python

        # Good
        output = dev.parse('show processes')
        cpu = output['cpu_load']


Make it Modular
===============

Properly designed, modular software is independent, interchangeable, easy to
read, extend and debug. Test automation itself is software: and thus also
benefits from modular programming techniques. This includes both implementing
in an object-oriented fashion, as well as grouping these objects (classes) into
corresponding modules & packages, making it easy for others to leverage and use.

Use and enhance existing, shared libraries whenever possible (either through
direct modification and/or inheritance). Make sure your changes are backwards
compatible and/or do not break existing test suites and functionalities.

When developing from scratch, follow object-oriented programming practices,
and create objects (classes) that contains both data (attributes), and code
(methods) that acts on those data, encapsulating unnecessary details and complex
operations, promoting code reuse, and enabling object inheritance/extensions. If
applicable, commit your newly creations into corresponding existing libraries in
order to further expand their usefulness. Otherwise, create a new shared
library. Avoid local, private libraries and silo-development.

    .. code-block:: python

        # Bad
        def get_release_version(ctlr):
        try:
            if ctlr.is_connected() is False:
                ctlr.connect()
            buffer = ctlr.execute('show version')
            ver = buffer.splitlines()
            ver_line = ''
            version_num = '16.12'
            for line in ver:
                res = re.search('Experimental Version (\d+\.\d+)\.\d+\:\d+.*',line)
                if res:
                    version_num = res.group(1)
                    break
            if version_num:
                logger.info("Release Image version : "+str(version_num))
            return version_num
        except Exception as e:
            logger.info("Unable to get release Image version from the device: {}".format(ctlr.name))
            logger.info("Exception Debug {} ....".format(e))
            return None

    .. code-block:: python

        # Good
        def get_release_version(device):
            if not device.is_connected():
                device.connect()

            output = device.parse('show version')
            return output['version']

        if get_release_version(device) != '16.12':
            raise Exception('...')

Here are some generic principles to remember when coding:

* Use classes, objects and methods over functions and procedures
* Segregate independent concepts/features/functionalities into different classes & objects
* Inherit & extend existing classes when commonalities exist
* Make your implementation generic and catch-all
* Avoid unnecessary deep nesting of loops and procedures
* Limit the number of logic path per function, avoid using too many input parameters

Make It Dynamic
===============
Dynamic software can be driven with different inputs (parameters) yield
different results and/or do different things. This promotes code-reusability
and increases code flexibility.

Avoid hard-coding values within your classes, functions and test suite. Avoid
duplicating the same code and only changing a minor piece of it
(configuration/data/value). Always separate data variables (such as
configuration, timing, name, etc) apart from the procedural implementation
(eg, function, class, method). This encourages for a design that is more
generic, robust and extendable.

    .. code-block:: python

        # Bad
        @aetest.subsection
        def copy_codecov(self, testbed):
            d = testbed.devices['csr127']
            d.execute('cflow copy')
            d.sendline("request platform software system shell\r")
            d.expect("Are you sure you want to continue?", timeout=10)
            d.send("y\r")
            d.expect("\[csr127:\/\]\$", timeout=10)
            d.send("chmod 777 bootflash/cflow\r")
            d.expect("\[csr127:\/\]\$", timeout=10)
            d.send("tar -zcvf bootflash/codecov.tar.gz bootflash/cflow/\r")
            d.expect("\[csr127:\/\]\$", timeout=10)
            d.send("exit\r")
            d.expect("csr127#", timeout=10)
            ## config "file prompt quiet" to disable prompts
            d.sendline("copy bootflash:codecov.tar.gz tftp://223.255.254.254/alllo/FIBModelTest/copyout/\r")
            d.expect("csr127#", timeout=1000)
            d.disconnect() #always on the last action on box

    .. code-block:: python

        # Good
        @aetest.subsection
        def copy_codecov(self, testbed, device_name, base_dir, target_dir, zip_file, ip_mount):

            d = testbed.devices[device_name]
            d.execute('cflow copy')

            dialog = Dialog([
                Statement(pattern=r'Are you sure you want to continue\?',
                        action='sendline(y)')])

            d.execute("request platform software system shell", reply=dialog, timeout=10)
            d.execute('chmod 777 %s' % target_dir, timeout=10)
            d.execute('tar -zcvf %s/%s %s' % (base_dir, zip_file, target_dir), timeout=10)
            d.execute('exit', timeout=10)
            d.execute('copy %s:%s tftp:%s' % (base_dir, zip_file, ip_mount), timeout=1000)
            d.disconnect()

The best approach to test automation is to design generic test suites and
libraries that can be driven with data that alters its footprint (e.g.
configuration/scaling/HW/SW) whilst still performing, testing and reporting to
the same degree. This way, test cases become only a particular combination of
calls to library functions with arguments/parameters unique to that test case,
offsetting major development effort into creating sharable, reusable and
independent libraries.

Make It Agnostic
================

Agnostic, single-source test suites have the potential to work across a variety
of releases, platforms, OSes, as well as through different management interfaces
such as CLI, NETCONF, RESTCONF and gRPC. This vastly increases test suite
sustainability, reducing development and maintenance costs by allowing users
to keep reusing the same suite and simply provide the set of libraries that
handles these new deltas.

Take advantage of object-oriented programming paradigms such as inheritance,
duck-typing and factory functions.  Avoid duplicating anything
(scripts/libraries), and always look for ways to re-use, uplift and/or
refactor existing ones. Your neighbors will thank you dearly when your test
suites are written to leverage abstraction (genie.abstract) from day-one.

Make it Unique & Independent
============================

Each test suite should be unique, and should contain a collection of independent
tests that tests the different facets of the same feature or component. This
allows runs to be able to pick & choose tests (tiers), and as well be able to
run tests in randomized order.

Each library should also be unique. E.g. it is a collection of classes,
functions, methods and procedures that acts on a common, unique domain/topic.
Leverage code search tools (eg, grep, GitHub search) to find out whether what
you’re looking for already exists.

Optimize, Optimize, Optimize
============================

Optimization can be done in many ways: logic flow optimization, test pattern
optimization, runtime optimization (asynchronous executions), source code
modularization/modernization, etc. As your libraries and test suites grow in
order to support the ever-increasing number of releases, hardware and features,
it’s important to refactor and optimize when possible (without reducing
coverage) in order to keep the source code lean and effective.

Here are some tips regarding generic optimizations:

* Run things in parallel: when possible (e.g., no race conditions),
  run functions/methods/tests/suites in parallel (asynchronously) in order
  to save runtime.

* Poll states: instead of flat-out waiting a number of seconds for an external
  system to finish processing, polling for expected states using short
  intervals with a maximum timeout is a better, more effective method.

* Prioritize tests through tiers: group test cases and suites into different
  priority/feature tiers, and only run the necessary tiers at each
  regression/test level.

* Concatenate similar tests: combine similar tests into a larger test
  (if applicable), saving overheads.

* Test only what makes sense: do not try to test all possible hardware/software
  combinations. Select only those that are architecturally significant. Identify
  the reference platform for each feature, release, branch, and test
  accordingly.

* Mixed coverage trails: Use varying methods to setup, test and teardown in
  order to test the product from different directions. (e.g., CLI, NETCONF,
  RESTCONF, SNMP, … etc)

Assume Nothing
==============

The purpose of test automation is to comb through a given target
(software/hardware) for errors, bugs and problems, and validating for expected
states, outputs and results. Do not impose unreasonable requirements on the
test environment, but as well, do not assume that things will “just work”.

As a general rule of thumb, design your test suites so that they are easy
to set-up and run in a variety of possible environments:

* Be explicit with input requirements: if your test suite requires inputs,
  they should be provided as script arguments. If environment variables are to
  be used, they should be processed and converted to script arguments instead
  of being directly accessed through the script.

* Avoid hard-coding names: decouple device/server/interface names from the
  actual topology/device requirement and map them using aliases and/or labels
  instead. This allows your test suite to run on a variety of hardware
  environments.

* Check your inputs: even-though Python does not promote type-checking inside
  core libraries, it is often beneficial in test automation to validate script
  inputs (type/range) before starting, in order to avoid wasting valuable
  testbed time.

Follow the Guidelines
=====================

Always follow the guidelines and templates when creating test suites and
libraries. This ensures that the end product always looks & feels the same,
and assures easy hand-off between teams, greatly simplifying long-term
maintenance costs.

