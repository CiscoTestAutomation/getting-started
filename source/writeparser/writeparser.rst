.. _write-parser:

Write a parser
======================
asdf

What is a parser?
-----------------

.. include:: ../definitions/def_parser.rst
    :start-line: 3

For a basic introduction to the |library| parsers, see the topic :ref:`parse-output`.



Why write a parser?
-------------------
Change the key value pairs from standard? Write a parser for a show command that doesn't have a |library| model?

.. tip:: Remember, the |library| parser functionality gives you *structured* output that makes reuse possible.

How the |library| parsers work
------------------------------

Regular expressions
^^^^^^^^^^^^^^^^^^^

 (sometimes shortened to regexp, regex, or re) are a tool for matching patterns in text. Regular expressions are the core backbone of all parsers.

If you are unfamiliar with what regular expressions are, here are a few good primers:

https://www.learnpython.org/en/Regular_Expressions
https://regexone.com/references/python
https://www.dataquest.io/blog/regex-cheatsheet/ 
Once you are familiar with what regular expressions are, the following online tools can help you build and test Python regular expressions:

https://pythex.org/
https://regex101.com/

Python library "re"

|library| parsers

Genie has two packages that are dedicated to the task of parsing (pattern matching) device output data (text). These packages are:

genie.metaparser: 
Metaparser is the core of Genie parsers and is used to standardize parsing any format of device data (CLI output, XML output, NETCONF/Yang output).
It is responsible for ensuring that a parser returns a fixed data-structure known as the parser's schema.

genie.libs.parser:
This package contains Python classes that breakdown raw Cisco device data (CLI output, XML output, etc.) by parsing the data using regular expressions into software-readable Python data-structures (dictionary) that match a defined schema.
One parser class can be used to parse CLI output, XML output or NETCONF output of a device command. However, the parser for each output must return the same Python data-structure defined in the schema.
The https://github.com/CiscoTestAutomation/genieparser/tree/master/src/genie/libs/parser contains all the Python parser classes developed in this package.

https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers



Create a parser schema
----------------------
With a model
Without a model

Is this a text file?
What is a level key?

Is the schema in JSON format? As an example, perhaps https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers/show%20lisp%20session IOSXE (for external) , choose platform, "show lisp session", explain what 'optional' means (keys that are not always expected to be found in device output are marked as "Optional". All other keys have a specific name (key) and value type (integer, string, boolean, list etc.). Ask the user to go there so they get used to finding these. Then, go to GitHub to get the actual code, modify to suit your purposes. And perhaps contribute <link>.



Use | xml with show commands to get xml key value pairs that you can use to write your schema

Schema class, parser class

(From w3schools: A Class is like an object constructor, or a "blueprint" for creating objects.)

Schema class: Basically shows the key-value pair data structure that will result from parsing the device output.
Parser class: Basically the class with definition of how to parse, inherits from the schema to return the format as a Python dictionary with the structure defined in the schema.

Parser process
--------------
Collect device data
Loop over each line
Regex to add to dictionary


Make JSON

Example of a parser
-------------------


Write a parser with regex
--------------------------
This example shows you how to write a ....



#. asdf

    .. code-block:: python

       from genie.testbed import load



#. asdf

Create and execute a unit test
-------------------------------
