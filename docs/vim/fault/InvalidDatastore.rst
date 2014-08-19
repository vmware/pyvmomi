
vim.fault.InvalidDatastore
==========================
    :extends:

        `vim.fault.VimFault <vim/fault/VimFault.rst>`_

  An InvalidDatastore exception is thrown if an operation fails because of a problem with the specified datastore. Typically, a subclass of this exception is thrown, indicating a problem such as an inaccessible datastore or an invalid datastore path.

Attributes:

    datastore (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    name (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.




