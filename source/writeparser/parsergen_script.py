#Import Genie libraries
from genie.testbed import load
from genie import parsergen
import re

from pprint import pprint

#Create Testbed Object
testbed = load('mock_parser.yaml')

#Create Device Object
uut = testbed.devices.iosxe1

#Use connect method to initiate connection to the device under test
uut.connect()

#Execute command show nve nvi on connected device
output = uut.device.execute('show nve vni')

#Create list of header names from show nve nvi - must match exactly the output on the command line interface
header = ['Interface', 'VNI', 'Multicast-group', 'VNI state', 'Mode', 'BD', 'cfg', 'vrf']

#Use Parsergen to parse the output and create structured output (dictionary of operational stats)
result = parsergen.oper_fill_tabular(device_output=output, device_os='iosxe', header_fields=header, index=[0])

#Pretty Print the Dictionary
pprint(result.entries)

#Check the type to see that it's a dictionary
type(result.entries)