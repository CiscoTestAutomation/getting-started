Definition of a parser
======================

A parser converts device output into a Python dictionary, which stores the 
device data as a set of key-value pairs. This process harmonizes the data 
structure for different types of communication interfaces, including CLI, REST, NETCONF, and others. 

The |library| parsers create standardized output for commands, which means 
that you can write and run reusable automation scripts. In the |pyATS| ecosystem, 
parsers are typically written using the ``genie.metaparser`` module.