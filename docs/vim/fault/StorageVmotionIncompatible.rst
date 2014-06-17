.. _string: ../../str

.. _vim.fault.VirtualHardwareCompatibilityIssue: ../../vim/fault/VirtualHardwareCompatibilityIssue.rst


vim.fault.StorageVmotionIncompatible
====================================
    :extends:

        `vim.fault.VirtualHardwareCompatibilityIssue`_

  This fault is thrown when Storage DRS tries to migrate disks of a virtual machine to a datastore, but finds that the datastore is incompatible with the given virtual machine.

Attributes:

    datastore (`str`_): is optional.




