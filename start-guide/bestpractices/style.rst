Style Guide
===========

Test automation developed under pyATS ecosystem shall follow the basic coding 
style and conventions outlined in PEP 8. This section below only provides a 
brief highlight. For full details and rationales, refer to: 
https://www.python.org/dev/peps/pep-0008/. All users are expected to know PEP 8
guidelines. 

Code Layouts
------------

* Use 4 spaces per indentation level. Do NOT use tabs. Be consistent with the
  amount used.

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

    .. code-block:: python

        # Wrong
        p2 = re.compile(r'^\s*BGP +table +version +is'
                r' +(?P<bgp_table_version>[0-9]+), +[Ll]ocal +[Rr]outer'
                r' +ID +is +(?P<local_router_id>(\S+))$')

    .. code-block:: python

        # Correct
        p2 = re.compile(r'^\s*BGP +table +version +is'
                        r' +(?P<bgp_table_version>[0-9]+), +[Ll]ocal +[Rr]outer'
                        r' +ID +is +(?P<local_router_id>(\S+))$')

* Separate logic blocks using white lines, with two lines between major 
  function/class definitions.

* All import statements should occur at the top of the file, with one module 
  per import.

* All import statements shall be either absolute, or relative to the current
  module. Never do ``import *`` , this makes debugging very hard as you cannot
  know where the library comes from

    .. code-block:: python

        # Wrong
        from x.y import *

    .. code-block:: python

        # Correct
        from x.y import Z
        from . import x
        from .. import y

Comments and Docstrings
-----------------------

* Comments should be complete sentences in plain, readable English.

    .. code-block:: python

        # Wrong
        # dict check
        if arg in jsons_dict:
            mod_path = jsons_dict[arg]['module']
            file_name = jsons_dict[arg]['file']

    .. code-block:: python

        # Correct
        # Look up module's path and file's name in the dictionary
        if arg in jsons_dict:
            mod_path = jsons_dict[arg]['module']
            file_name = jsons_dict[arg]['file']

* Use inline comments sparingly, and only if the line (including comments) is 
  less than 79 characters.

.. code-block:: python

    # Not Recommended
    x = 5 ; # Setting 5 to value x

.. code-block:: python

    # Correct
    # Setting 5 to value x
    x = 5

* Write proper, useful docstrings for all modules, functions, classes and 
  methods, following PEP 257. Refer to Sphinx documentation requirements if
  library is to be auto-documented using Sphinx.

.. code-block:: python

    # Wrong
    def configure_cdp(device, interfaces=None):
        '''cdp configuration'''

.. code-block:: python

    # Correct
    def configure_cdp(device, interfaces=None):
        """ Enables cdp on target device
            Args:
                device ('obj'): Device object
                interfaces ('list'): List of interfaces to configure cdp on
            Returns:
                None
        """

* Docstrings should be in a Sphinx-friendly format in order to allow for 
  auto-generated API documentation, eg, Sphinx REST.

Naming Conventions
------------------

* Short, all ``lowercase`` names for modules.

    .. code-block:: python

        # Wrong
        genie.UTILS

    .. code-block:: python

        # Correct
        genie.utils

* ``CapWordCamelBack`` for class names

    .. code-block:: python

        # Wrong
        class mycustomclass():
            ...

    .. code-block:: python

        # Correct
        class MyCustomClass():
            ...

* Suffix Error for all exception classes.

.. code-block:: python

    # Wrong
    class BadName(Exception):
        pass

.. code-block:: python

    # Correct
    class MyError(Exception):
        pass

* All lowercase for function names, use underscore only if it improves 
  readability


    .. code-block:: python

        # Wrong
        def LoadAttribute(pkg, attr_name, device=None):

    .. code-block:: python

        # Correct
        def load_attribute(pkg, attr_name, device=None):

* Always use ``self`` for the first argument to instance methods

.. code-block:: python

    # Wrong
    class MyClass():
        def my_function(this):
            pass

.. code-block:: python

    # Correct
    class MyClass():
        def my_function(self):
            pass

* Always use ``cls`` for first argument to class methods

.. code-block:: python

    # Wrong
    class MyClass():
        @classmethod
        def my_function(self):
            pass

.. code-block:: python

    # Correct
    class MyClass():
        @classmethod
        def my_function(cls):
            pass

* Use ``CAPS_WITH_UNDERSCORES`` for constants
