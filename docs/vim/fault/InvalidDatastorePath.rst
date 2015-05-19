.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.InvalidDatastore: ../../vim/fault/InvalidDatastore.rst


vim.fault.InvalidDatastorePath
==============================
    :extends:

        `vim.fault.InvalidDatastore`_

  An InvalidDatastorePath exception is thrown if a datastore path violates the expected format. The expected format is "[dsName] path", e.g. "[storage1] folder/Vm1.vmdk". This exception is also thrown if a datastore corresponding to the given datastore path is not found.

Attributes:

    datastorePath (`str`_)




