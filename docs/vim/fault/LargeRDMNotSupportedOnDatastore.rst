.. _str: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vim.fault.VmConfigFault: ../../vim/fault/VmConfigFault.rst


vim.fault.LargeRDMNotSupportedOnDatastore
=========================================
    :extends:

        `vim.fault.VmConfigFault`_

  The virtual machine is configured with a 2TB+ Raw Disk Mapping. This is not supported on the datastore.

Attributes:

    device (`str`_)

    datastore (`str`_)

    datastoreName (`str`_)




