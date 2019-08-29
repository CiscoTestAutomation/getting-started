Run a test case
======================
This topic describes how you can use the |library| to build and run test cases and, ultimately, use the test cases for automated network testing.

Automated testing process
---------------------------
Perhaps a diagram of the testing process? (if time permits) - maybe log this as a user story for the future, with a priority 2 - see https://pubhub.devnetcloud.com/media/genie-docs/docs/cookbooks/harness.html

connect to all the devices
configure the devices
Verify the configuration was applied correctly
snapshot of the configuration and compared at the end of the run
snapshot of the operation state of your devices to be compared at the end of the run
pool of available tests (triggers and verifications, over 500) which works across multiple Operating systems
connections pool - Learn and send commands to the device in parallel
traffic Generator
much more

The flow of Genie Harness is divided into 3 main sections.

Common Setup
Get the devices ready and collect some information:

Connect to your devices
Configure your device (optional)
Setup Traffic Generator if needed
Take a snapshot of the system
Triggers and Verifications
Execute triggers and verification to perform tests on your devices.

Common Cleanup
Make sure the state of the devices are the same as in common Setup

a. Take a new snapshot and compare with the original snapshots from Common Setup b. Stop traffic

This is the typical Harness flow, however, everything can be customized

HTML log viewer!!!

What is a test case?
--------------------
Describe the key |library| and generic concepts that the user needs to understand before they begin to perform these tasks. We'll need to define what these are, but they should include |genieprfx| harness, jobs, datafiles, triggers, and verifications.

Structure of a test case
^^^^^^^^^^^^^^^^^^^^^^^^^

Reusable triggers (classes)
Then tell the system the order to run the triggers and what data to pass
APIs define the functions (steps) within each action

Trigger
^^^^^^^^^^^^^

Class
"""""

Function
""""""""
Point to Felipe's doc

Datafile
""""""""
The YAML datafiles control the flow of test execution. - testbed
mapping (optional) - to connect to more devices than uut
verification (optional) - there is a default
trigger (optional) - there is a default
subsection
configuration
pts (profile the system)

Job file
"""""""""





Verification
^^^^^^^^^^^^

What is a test script?
-----------------------

Example of a test case
------------------------

Set up your system
^^^^^^^^^^^^^^^^^^^

#. Connect to your devices
#. Configure your devices
#. Set up a traffic generator
#. Take a snapshot


Execute triggers and verifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Step one
#. Step two
#. Step n

Run a common cleanup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Step one
#. Step two
#. Step n


See also...
*a list of relevant links*

 * More information about functions: https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/apis/index.html#api-guidelines-and-good-practices
 * link 2
 * link 3






