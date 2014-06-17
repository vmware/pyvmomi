.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.FileFault: ../../vim/fault/FileFault.rst


vim.fault.FileTooLarge
======================
    :extends:

        `vim.fault.FileFault`_

  This fault is thrown when an operation fails because the file is larger than the maximum file size supported by the datastore.

Attributes:

    datastore (`str`_)

    fileSize (`long`_)

    maxFileSize (`long`_): is optional.




