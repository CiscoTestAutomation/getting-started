Do & Don't
==================

* Do not hardcode IP address, sleep timeout, device name, interfaces, etc,
  within a script. Do pass the information from `datafile` and/or job
  arguments. A sleep timeout will need to be adjusted on the load and scale of
  the configuration.

* Do not hardcode anything which is dependent on

  * Topology
  * Configuration
  * Image version

  The script must work with different topology (use alias), configuration (use
  datafile) and different image version.

* 

