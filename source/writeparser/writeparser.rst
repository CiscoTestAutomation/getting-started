.. _write-parser:

Write a parser
======================
This topic describes why and how to write your own parsers to create Python dictionaries. These dictionaries have data structures that facilitate automated testing. 

.. tip:: Remember to share your new parser with the rest of the |pyATS| user community! See the topic :ref:`contribute` for more information.

What is a parser?
-----------------

.. include:: ../definitions/def_parser.rst
    :start-line: 3

* For a basic introduction to the |library| parsers, see the topic :ref:`parse-output`.
* For more information about the ``metaparser`` package, see the topic `Metaparser Package <https://pubhub.devnetcloud.com/media/genie-metaparser/docs/index.html#genie-metaparser-package>`_.

Why write a parser?
-------------------
Change the key value pairs from standard? Write a parser for a show command that doesn't have a |library| model?

.. tip:: Remember, the |library| parser functionality gives you *structured* output that makes reuse possible.

How the |library| parsers work
------------------------------

Parser process
^^^^^^^^^^^^^^
Collect device data
Loop over each line
Regex to add to dictionary

Regular expressions
^^^^^^^^^^^^^^^^^^^
You definitely need to know regex to write a parser.

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

Schema and parser class
-----------------------
(From w3schools: A Class is like an object constructor, or a "blueprint" for creating objects.)

Schema class: Basically shows the key-value pair data structure that will result from parsing the device output.
Parser class: Basically the class with definition of how to parse, inherits from the schema to return the format as a Python dictionary with the structure defined in the schema.

Create a parser schema
----------------------
With a model
^^^^^^^^^^^^
 |library| ops model: https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/models, for example bgp?

Is the schema in JSON format? As an example, perhaps https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers/show%20lisp%20session IOSXE (for external) , choose platform, "show lisp session", explain what 'optional' means (keys that are not always expected to be found in device output are marked as "Optional". All other keys have a specific name (key) and value type (integer, string, boolean, list etc.). Ask the user to go there so they get used to finding these. Then, go to GitHub to get the actual code, modify to suit your purposes. And perhaps contribute <link>.

Without a model
^^^^^^^^^^^^^^^
How to figure out the schema
1. show command output
2. show command with xml output
3. from YANG data model

Consider parent and child keys, and when the levels depend on arguments defined at runtime when you execute the show command.

vrf, address_family/protocol(ipv4 or ipv6),  instance, interface

.. code-block:: text

    'vrf': {
        "VRF1": {
            'address_family': {
                'ipv4': {
                    'instance': {
                        'process1': {
                            'interfaces': {
                                'Ethernet1': {
                                    'key1': value,
                                    'key2': value,
                                }
                            }
                        }
                    }
                }
            }
        }
    }




Use | xml with show commands to get xml key value pairs that you can use to write your schema

Get schema idea from show command output. Please check indentation in the output, indentation always tells you if you need to have a level key
Example: As you can see, information should be under 'Ethernet 0' in this case.

Router# show interfaces
Ethernet 0 is up, line protocol is up
  Hardware is MCI Ethernet, address is 0000.0c00.750c (bia 0000.0c00.750c)
  Internet address is 10.108.28.8, subnet mask is 255.255.255.0
  MTU 1500 bytes, BW 10000 Kbit, DLY 100000 usec, rely 255/255, load 1/255
  Encapsulation ARPA, loopback not set, keepalive set (10 sec)
  ARP type: ARPA, ARP Timeout 4:00:00
(snip)
Schema could be:

'interfaces': {
     'Ethernet 0': {
         'state': 'up',
         'protocol': 'up',
         'hardware': 'MCI Ethernet',
         'address': '0000.0c00.750c',
another thing, please check how you can do grouping the data based on output such as 'input'vs'output', 'counters', 'statistics'. Below lines look like having patterns for both 'input' and 'output'

1127576 packets input, 447251251 bytes, 0 no buffer
Received 354125 broadcasts, 0 runts, 0 giants, 57186* throttles
0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
5332142 packets output, 496316039 bytes, 0 underruns
0 output errors, 432 collisions, 0 interface resets, 0 restarts
Schema could be:

'counters': {  # categorize the value as 'counters'
    'input': {   # categorize the 'input' related values
        'packets': 1127576,
        'bytes': 447251251,
        (snip)
    },
    'output': {
        'packets': 5332142,
        'bytes': 496316039,
    }



Schema class, parser class

Write a parser class with RegEx
--------------------------------
This class contains the regular expressions that can parse each line of the device output into the Python dictionary defined in the Parser Schema Class. The Parser Class inherits from the Parser Schema Class to ensure that the Python dictionary returned by the class is exactly in the format of the defined schema. The following is a Parser Class that returns the Python dictionary defined in the Parser Schema Class above: You need to know what you're looking for from the output in order to set up the correct RegEx search/compile.

# Python (this imports the Python re module for RegEx)
import re
 
# ==============================
# Parser for 'show lisp session'
# ==============================
class ShowLispSession(ShowLispSessionSchema):
 
    ''' Parser for "show lisp session"'''
 
    cli_command = 'show lisp session'
 
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
 
        # Init vars (this is the dictionary, indicated by {})
        parsed_dict = {}
 
        # Sessions for VRF default, total: 3, established: 3 (this is the python regex, re.compile compiles the regex pattern into a regular expression object, then use that to search or match)
        p1 = re.compile(r'Sessions +for +VRF +(?P<vrf>(\S+)),'
                         ' +total: +(?P<total>(\d+)),'
                         ' +established: +(?P<established>(\d+))$')
 
        # Peer                           State      Up/Down        In/Out    Users
        # 2.2.2.2                        Up         00:51:38        8/13     3
        p2 = re.compile(r'(?P<peer>(\S+)) +(?P<state>(Up|Down)) +(?P<time>(\S+))'
                         ' +(?P<in>(\d+))\/(?P<out>(\d+)) +(?P<users>(\d+))$')
 
        for line in out.splitlines():
            line = line.strip()
 
            # Sessions for VRF default, total: 3, established: 3
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf = group['vrf']
                vrf_dict = parsed_dict.setdefault('vrf', {}).\
                            setdefault(vrf, {}).setdefault('sessions', {})
                vrf_dict['total'] = int(group['total'])
                vrf_dict['established'] = int(group['established'])
                continue
 
            # 8.8.8.8                        Up         00:52:15        8/13     3
            m = p2.match(line)
            if m:
                group = m.groupdict()
                peer = group['peer']
                peer_dict = vrf_dict.setdefault('peers', {}).setdefault(peer, {})
                peer_dict['state'] = group['state'].lower()
                peer_dict['time'] = group['time']
                peer_dict['total_in'] = int(group['in'])
                peer_dict['total_out'] = int(group['out'])
                peer_dict['users'] = int(group['users'])
                continue
 
        return parsed_dict

As seen above, the regular expressions for each line of device output are defined and compiled within the parser class (p1, p2, etc). We then loop over each line of device output and test each line against the regular expressions defined within the Parser class. If the line matches the regular expression pattern, we go ahead and create/set the Python dictionary keys as per the defined Schema.

Write a parser with the parsergen package
-----------------------------------------
Parses both tabular and non-tabular show command output (either or both).
The Parsergen Class is particularly useful where Genie Ops does not have a model for the particular state you are looking to parse.

The Genie Parsergen Class can deal with both Tabular and Non Tabular device output from a networking device. We shall initially explore Tabular parsing (need to use the example yaml file and test exactly how this works as it's not entirely clear from the passive voice).

Consider the output from the show command 'show nve vni'

Interface  VNI        Multicast-group VNI state  Mode  BD    cfg vrf                      
nve1       6001       N/A             Up         L2DP  1     CLI N/A 
The testbed object 'uut.device' has a method of execute. Execute will run the command on the device and return a string as the result of the command

from genie import parsergen (add the other import functions from the script, then run the commands as in the full script, attach the script as a .py?)

output = uut.device.execute('show nve vni')

Create a list identifying the headers of the expected column output: (not 'is created')

header = ['Interface', 'VNI', 'Multicast-group', 'VNI state', 'Mode', 'BD', 'cfg', 'vrf']
We will now use the parsergen oper_fill_tabular method to parse the string and store as structured data

result = parsergen.oper_fill_tabular(device_output=output, device_os='iosxe', header_fields=header, index=[0])

(0 is the index which is the Interface value/name)

Now print the structured data returned

import pprint

pprint.result.entries
{'nve1': {'BD': '1',
          'Interface': 'nve1',
          'Mode': 'L2DP',
          'Multicast-group': 'N/A',
          'VNI': '6010',
          'VNI state': 'Up',
          'cfg': 'CLI',
          'vrf': 'N/A'},
 'nve2': {'BD': '2',
          'Interface': 'nve2',
          'Mode': 'L2DP',
          'Multicast-group': 'N/A',
          'VNI': '6020',
          'VNI state': 'Up',
          'cfg': 'CLI',
          'vrf': 'N/A'},
 'nve3': {'BD': '3',
          'Interface': 'nve3',
          'Mode': 'L2DP',
          'Multicast-group': 'N/A',
          'VNI': '6030',
          'VNI state': 'Up',
          'cfg': 'CLI',
          'vrf': 'N/A'}}

Determine the type of the result object entries attribute

type(result.entries)
As you will see the returned data is now structured data in the form of a dictionary
(The output is:)
<class 'dict'>

Full Script

#Import Genie libraries
from genie.conf import Genie
from genie import parsergen
import re

from pprint import pprint

#Create Testbed Object with Genie
testbed = Genie.init('mocked_first.yaml')

#Create Device Object
uut = testbed.devices.iosxe1

#Use connect method to initiate connection to the device under test
uut.connect()

#Execute command show nve nvi on connected device
output = uut.device.execute('show nve vni')

#Create list of Header names of the table from show nve nvi - must match exactly to that which is output on cli
header = ['Interface', 'VNI', 'Multicast-group', 'VNI state', 'Mode', 'BD', 'cfg', 'vrf']

#Use Parsergen to parse the output and create structured output (dictionary of operational stats)
result = parsergen.oper_fill_tabular(device_output=output, device_os='iosxe', header_fields=header, index=[0])

#Pretty Print the Dictionary
pprint(result.entries)

#Check the type to see that it's a dictionary
type(result.entries)

Make JSON




#. asdf

    .. code-block:: python

       from genie.testbed import load



#. asdf

Create and execute a unit test
-------------------------------
If you want to contribute your new parser to the open-source |pyATS| feature libraries and components, you must :ref:`write a unit test <write-unit-tests>` and attach the results for each parser that you want to contribute.

See the topic :ref:`contribute` for more details.

See also...

* `Cisco Live DevNet workshop 2601 - pyATS/GENIE ops and parsers <https://github.com/RunSi/DEVWKS-2601>`_
* asdf