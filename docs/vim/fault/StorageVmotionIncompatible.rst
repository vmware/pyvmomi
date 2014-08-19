
vim.fault.StorageVmotionIncompatible
====================================
    :extends:

        `vim.fault.VirtualHardwareCompatibilityIssue <vim/fault/VirtualHardwareCompatibilityIssue.rst>`_

  This fault is thrown when Storage DRS tries to migrate disks of a virtual machine to a datastore, but finds that the datastore is incompatible with the given virtual machine.

Attributes:

    datastore (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.




