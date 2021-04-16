General Guidelines
==================

Environment Requirements
------------------------
* Test suites, shall not presume (depend on) any pre-existing 
  configuration of the environment (e.g. routers, switches), and shall always 
  perform its own configurations, unless explicitly coded to be and/or 
  provided/told otherwise.

* Test suites shall always leave the environment (e.g. routers and switches) 
  in the same state as they were found in (before the script started), 
  regardless of its results and whether any errors occurred.

* Test suites shall support both real and virtual (simulated) 
  environment/hardware seamlessly.

* Test suites shall be able to support a wide variety of execution environments,
  eg: Jenkins, docker containers, VMs, etc.

Headers & Comments
------------------

* All files (modules) shall have headers using Python docstring notation, 
  describing in detail its author, support contacts, purpose, description, 
  usages & etc.

    ..
        Lukas

    .. code-block:: python
      :name: this_just_bumps_code_over

        # Wrong
        import os
        import json
        import logging
        import importlib
        ...


    .. code-block:: python
      :name: this_just_bumps_code_over

        # Correct
        '''
            Author(s): Mr. Snow, Mr. Wayne, Mr. The Ripper
            Contact(s): john@gmail.com
            Purpose: Collect string manipulation tools in one place
            Description: A string processing package that allows easier string 
                manipulation by handling all of the slicing, indexing, and 
                bookkeeping in one place
            Usages:
                import JTR
                from JTR import cracker
        '''

        import os
        import json
        import logging
        import importlib

* All classes, functions, methods shall have headers using Python docstring 
  notation, describing its purpose, usage, arguments, return values and 
  providing examples.

    ..
        Lukas

    .. code-block:: python
      :name: this_just_bumps_code_over

        # Wrong
        def extract_module(i, j, k):

            ...

            return find(i, j.expand(), k)

    .. code-block:: python
      :name: this_just_bumps_code_over

        # Correct
        def extract_module(name, root_dir, timeout):
            '''
            Purpose
            -------
            Function used to extraxt a specific module/package by searching 
            through a given directory and all of its subdirectories. 

            Parameters
            ----------
            name : str
                Name of module. Not case-sensitive
            root_dir : str
                Directory to start search in. All subdirectories will be 
                searched until module is found.
            max_depth : int
                Optional. Specifies the maximum depth of subdirectories to 
                search in. Default is infinite
            
            Returns
            -------
            path : str
                If module is found, the absolute path of the module. 
                If module is not found, an empty string.

            Usage
            -----
            path = extract_module(name, dir)
            path = extract_module(name, dir, 5)
            '''

            ...

            return find(i, j.expand(), k)


* Code blocks shall be commented, describing its steps and purpose

    ..
        Lukas

    .. code-block:: python
      :name: this_just_bumps_code_over

        # Wrong:
        #### workaround Code ####​
        s.send('conf t\r')​
        s.expect('conf t.*#')​
        s.send('hostname {}\r'.format(ctrl.custom.name))​
        s.expect('hostname.*#')​
        s.send('end\r')​
        s.expect('end.*#')​
        s.send('wri mem\r')​
        s.expect('wri mem.*#',timeout = 120)​
        s.send('conf t\r')​
        s.expect('conf t.*#')​
        s.send('hostname {}\r'.format(ctrl.custom.name))​
        s.expect('hostname.*#')​
        s.send('end\r')​
        #########################

    .. code-block:: python
      :name: this_just_bumps_code_over

        # Correct:
        #### workaround Code ####​
        # Send commands in altered order to set up environment​
        # for proceeding tests. This code is a workaround for​
        # host image memory not initializing properly​
        device.hostname = device.custom.name​
        device.configure('hostname {}'.format(device.custom.name))​
        device.execute('write memory', timeout=120)​
        device.configure('hostname {}'.format(device.custom.name))​
        #########################

* Convoluted logic shall be commented, including descriptions for each 
  logic path.

    ..
        Lukas

    .. code-block:: python
      :name: this_just_bumps_code_over

        # Wrong
        for device in route.hops():
            net_freq = 0 if device[0] < 0 else max_freq - 1 if device[0] > max_freq - 1 else device[0]
            net_addr = 0 if device[1] < 0 else max_addr - 1 if device[1] > max_addr - 1 else device[1]


    .. code-block:: python
      :name: this_just_bumps_code_over

        # Correct
        '''
        Loop through devices and ensure network fabric frequencies and addresses 
        always fall within allowed values. Reassign values if less than 0 or 
        greater than max_freq/max_addr
        '''
        for device in route.hops():
            net_freq = 0 if device[0] < 0 else max_freq - 1 if device[0] > max_freq - 1 else device[0]
            net_addr = 0 if device[1] < 0 else max_addr - 1 if device[1] > max_addr - 1 else device[1]

* Code changes shall have in-line comments before the change, with the bug ID 
  and a brief explanation of what’s changed.

Libraries & Packages
--------------------

* All users shall prioritize using and contributing to `genie libraries<https://developer.cisco.com/docs/pyats-development-guide/>`_. 
  Uplifts should be made as needed with the required review process.

* Library & package requirements shall be clearly identified within the
  script header

* Libraries & packages should be leveraging `Genie abstraction<https://pubhub.devnetcloud.com/media/genie-docs/docs/abstract/index.html#>`_ concept/solution 
  whenever possible

* All import statements shall be explicit and shall occur at the top of the file.
 
* Traffic generation/control shall be done by using central, common functions
  and libraries.

* All configurations shall be done/generated by calling functions/classes and 
  providing them with corresponding parameter values. These functions/classes 
  should belong to common libraries.

* All device output parsing (including screen scraping) shall be done using 
  `common library parsers<https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers>`_. 

.. code-block:: python

   device.parse('show version')


Errors & Exceptions
-------------------

* All exceptions and errors (including expected ones) shall be logged. 
  Avoid silent exceptions

    ..
        Lukas - show example of bad logging from the slide

    .. code-block:: python
      :name: this_just_bumps_code_over

        # Wrong:
        try:​
            log.info("Try to connect to console (connection a)")​
            uut.connect(alias='con', via='a')​

        except Exception as e:​
            self.errored("Errored connecting to console. You're on your own.\n" + str(err))

    .. code-block:: python
      :name: this_just_bumps_code_over

        # Correct:
        try:​
            log.info("Try to connect to console (connection a)")​
            uut.connect(alias='con', via='a')​

        except TimeoutError as te:​
            log.error("Log relevant connection info here")​
            self.errored("Connection timed out!\n" + str(te))​
        ​
        except InterruptedError as ie:​
            log.error("Log relevant connection info here")​
            self.errored("Connection interupted!\n" + str(ie))​
        ​
        except Exception as err:​
            log.error("Log ALL connection info here")​
            self.errored("Unexpected error!\n" + str(err))    


* Exception catching shall be explicit: never blanket catch all exceptions 
  (``except:`` statement without exception class type), or catching for 
  ``BaseException`` types.


.. code-block:: python

   # Wrong:
   try:
       some code
   except:
       some other code

.. code-block:: python

   # Correct:
   try:
       some code
   except Exception:
       some other code

|

* All code should prefer raising built-in exceptions whenever possible. Avoid 
  creating excessive new exception types.

.. code-block:: python

   # Correct:
   raise TypeError('...')

|
* Test suite shall always test for both positive and negative logic paths.

.. code-block:: python

   # Wrong:
   if api():
       do something

.. code-block:: python

   # Correct:
   if api():
       do something
   else:
       do something else

Execution
---------

* Test suite shall be executable through job files (pyats run job execution).


* Test suite shall leverage asynchronous (`parallel<https://pubhub.devnetcloud.com/media/pyats/docs/async/pcall.html>`_) executions whenever possible.

* Temporary file generation shall be done using python tempfile module, 
  generated under the current runtime directory. All temporary files shall be 
  deleted at the end of the run.

* Test suite shall detect and report any anomalies during execution, such as 
  crash, CPU freeze, memory leaks, etc. Look into `pyATS Health Check`<https://pubhub.devnetcloud.com/media/genie-docs/docs/health/index.html>`_.

Logging
-------

* Logging shall be done only through using python native logging module and 
  functionality. ``print()`` function should never be used in Test suites and libraries.

**Good**

.. code-block:: python

   log.info('This is some message')

**Bad**

.. code-block:: python

   print('This is some message')

* Test suites must log thorough and informative messages describing its 
  actions, purposes, progress and intermediate/final result.

**Good**

.. code-block:: python

   log.info('Performing check 1 to verify x is up')
   perform check 1

   log.info('Performing check 2 to verify z is down')
   perform check 2

   if all passed:
       log.info('All worked as expected')
   else:
       log.info('Failed because step <...> has failed')
       some logic

**Bad**

.. code-block:: python

   perform check 1
   perform check 2


* Point of failures and expected output/behavior/values shall be clearly 
  identified in the log file.

    .. code-block:: python

        # Wrong:
        if dbgObj.verify_poe_deployment() == False:​
            self.failed()​
        else:​
            self.passed()

    .. code-block:: python

        # Correct:
        if dbgObj.verify_poe_deployment() == False:​
            # Give debug information ... ​
            log.error("Debug History:" + dbgObj.command_history + "\n \​
                    Status: " + dbgObj.status)​
            self.failed("Point of entry deployment verification failed.")​
        else:​
            self.passed()

* Test results and any diagnostic information that may be helpful for debugging 
  and bug-raising purposes shall be logged thoroughly.

# JB - Talk to Dave/Thomas tomorrow

* Avoid using warnings excessively: in test automation, warnings are typically 
  ignored.

* Test suite should log a test topology diagram per test case if applicable.

Governance
----------

* Core infrastructure changes and feature requests shall follow the governance 
  and priority matrix outlined in pyATS documentation.

* Internally shared and/or externally open-sourced packages and libraries 
  needs to have one or more identified owners. Each and every owner shall be 
  responsible for their own project’s maintenance, and publishing guidelines 
  in their repository README file.

* Each test suite shall have an owner (individual or team), responsible of 
  reviewing pull requests and changes to the test suite.

