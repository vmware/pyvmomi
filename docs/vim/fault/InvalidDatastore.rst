.. _str: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vim.fault.VimFault: ../../vim/fault/VimFault.rst


vim.fault.InvalidDatastore
==========================
    :extends:

        `vim.fault.VimFault`_

  An InvalidDatastore exception is thrown if an operation fails because of a problem with the specified datastore. Typically, a subclass of this exception is thrown, indicating a problem such as an inaccessible datastore or an invalid datastore path.

Attributes:

    datastore (`str`_): is optional.

    name (`str`_): is optional.




