Style Guide
===========

Test automation developed under pyATS ecosystem shall follow the basic coding 
style and conventions outlined in PEP 8. This section below only provides a 
brief highlight. For full details and rationales, refer to: 
https://www.python.org/dev/peps/pep-0008/. All users are expected to know PEP 8
guidelines. 

Code Layouts
------------

* Use 4 spaces per indentation level. Do NOT use tabs.

**Good**

.. code-block:: python

    for x in my_list:
        print(x)

**Bad**

.. code-block:: python

    for x in my_list:
      print(x)

* Limit all lines to a maximum of 79 characters, unless it makes the logic
  harder to understand.

* Continuation lines should align wrapped elements vertically using 
  Python’s implicit line joining inside parenthesis, brackets and braces. 

# Lukas

* Separate logic blocks using white lines, with two lines between major 
  function/class definitions.

* All import statements should occur at the top of the file, with one module 
  per import.

* All import statements shall be either absolute, or relative to the current 
  module, e.g.: 

**Good**

.. code-block:: python

    from x.y import Z
    from . import x
    from .. import y

**Bad**

.. code-block:: python

    from x.y import *


Comments and Docstrings
-----------------------

* Comments should be complete sentences in plain, readable English.

# Lukas

* Use inline comments sparingly, and only if the line (including comments) is 
  less than 79 characters.

* Write proper, useful docstrings for all modules, functions, classes and 
  methods, following PEP 257. Refer to Sphinx documentation requirements if
  library is to be auto-documented using Sphinx.

**Good**

.. code-block:: python

    def configure_cdp(device, interfaces=None):
        """ Enables cdp on target device
            Args:
                device ('obj'): Device object
                interfaces ('list'): List of interfaces to configure cdp on
            Returns:
                None
        """
  
**Bad**

.. code-block:: python

    def configure_cdp(device, interfaces=None):
        '''cdp configuration'''

* Docstrings should be in a Sphinx-friendly format in order to allow for 
  auto-generated API documentation, eg, Sphinx REST.

Naming Conventions
------------------

* Short, all ``lowercase`` names for modules.

# Lukas

* ``CapWordCamelBack`` for class names

# Lukas

* Suffix Error for all exception classes.

**Good**

.. code-block:: python

    class MyError(Exception):
        pass

**Bad**

.. code-block:: python

    class BadName(Exception):
        pass

* All lowercase for function names, use underscore only if it improves 
  readability

# Lukas

* Always use ``self`` for the first argument to instance methods

**Good**

.. code-block:: python

    class MyClass():
        def my_function(self):
            pass

**Bad**

.. code-block:: python

    class MyClass():
        def my_function(this):
            pass


* Always use ``cls`` for first argument to class methods

**Good**

.. code-block:: python

    class MyClass():
        @classmethod
        def my_function(cls):
            pass

**Bad**

.. code-block:: python

    class MyClass():
        @classmethod
        def my_function(self):
            pass

* Use ``CAPS_WITH_UNDERSCORES`` for constants
