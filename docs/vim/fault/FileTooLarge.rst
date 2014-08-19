
vim.fault.FileTooLarge
======================
    :extends:

        `vim.fault.FileFault <vim/fault/FileFault.rst>`_

  This fault is thrown when an operation fails because the file is larger than the maximum file size supported by the datastore.

Attributes:

    datastore (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    fileSize (`long <https://docs.python.org/2/library/stdtypes.html>`_)

    maxFileSize (`long <https://docs.python.org/2/library/stdtypes.html>`_): is optional.




