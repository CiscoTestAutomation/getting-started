Job Guidelines
==============

Generic
-------

* Job files shall be written following the pyATS job file `template <https://github.com/CiscoTestAutomation/pyATS-project-template/blob/master/template/template_job.py>`_.
* Job files should have minimal programming logic.
* Job files shall contain and/or reference their required topology diagram drawings.
* Job files shall define a main() function as the entry point.

    .. code-block:: python

        from pyats.easypy import run
        def main(runtime):

            run(<script>)


Headers
-------

* Job file shall contain a docstring header containing:

  * Owner, support email
  * Tasks/test suites to be run
  * Topology requirement
  * Input arguments and environment variable requirements.

Parameters
----------

* Job files shall parse any job-file specific CLI arguments using python argparse, following pyATS argument propagation rules, and convert them into corresponding python objects.

    .. code-block:: python

        import argparse
        from pyats.easypy import run

        parser = argparse.ArgumentParser(description='example job file cli args parser')
        parser.add_argument('--argument_a',
                            help='example argument a',
                            default = None)
        parser.add_argument('--argument_b',
                            help='example argument b',
                            default = None)

        def main(runtime):

            custom_args = parser.parse_known_args()[0]
            run(<script>,
                arg_a = custom_args.argument_a,
                arg_b = custom_args.argument_b)

* Job files shall process any related environment input variables into task parameters.
* Job files shall allow a mechanism to allow default input variables/parameters to be overwritten by those from CLI and environment variables.
* Multiprocessing `shared variable <https://pubhub.devnetcloud.com/media/pyats/docs/easypy/jobfile.html#shared-states>`_ type parameters should be used if a task needs to propagate information back to its parent job file.

Tasks
-----

* Tasks shall refer to their test suite using relative path instead of hard-coded paths.
* Tasks shall be started/stopped only within the main() function.
* All tasks shall be waited for until they either finish, or time out.
* Tasks that time out shall be terminated and reported for error.
