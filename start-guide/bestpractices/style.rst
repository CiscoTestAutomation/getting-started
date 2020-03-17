Style Guide
===========

Test automation developed under pyATS ecosystem shall follow the basic coding 
style and conventions outlined in PEP 8. This section below only provides a 
brief highlight. For full details and rationales, refer to: 
https://www.python.org/dev/peps/pep-0008/. All users are expected to study 
this thoroughly.

Code Layouts
------------

* Use 4 spaces per indentation level. Do NOT use tabs.

* Limit all lines to a maximum of 79 characters.

* Continuation lines should align wrapped elements vertically using 
  Python’s implicit line joining inside parenthesis, brackets and braces. 

* Separate logic blocks using white lines, with two lines between major 
  function/class definitions

* All import statements should occur at the top of the file, with one module 
  per import.

* All import statements shall be either absolute, or relative to the current 
  module, e.g.: 

  * ``from . import x``
  * ``from .. import y``
  * ``from x.y import Z``


Comments and Docstrings
-----------------------

* Comments should be complete sentences in plain, readable English.

* Use inline comments sparingly, and only if the line (including comments) is 
  less than 79 characters.

* Write proper, useful docstrings for all modules, functions, classes and 
  methods, following PEP 257. Refer to Sphinx documentation requirements if
  library is to be auto-documented using Sphinx.

* Docstrings should be in a Sphinx-friendly format in order to allow for 
  auto-generated API documentation, eg, Sphinx REST.


Naming Conventions
------------------

* Short, all ``lowercase`` names for modules.

* ``CapWordCamelBack`` for class names

* Suffix Error for all exception classes.

* All lowercase for function names, use underscore only if it improves 
  readability

* Always use ``self`` for the first argument to instance methods

* Always use ``cls`` for first argument to class methods

* Use ``CAPS_WITH_UNDERSCORES`` for constants
