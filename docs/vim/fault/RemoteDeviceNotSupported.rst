
vim.fault.RemoteDeviceNotSupported
==================================
    :extends:

        `vim.fault.DeviceNotSupported <vim/fault/DeviceNotSupported.rst>`_

  The virtual machine has a currently connected device with a remote backing. This is an error when migrating a powered-on virtual machine, and can be returned as a subfault of DisallowedMigrationDeviceAttached.

Attributes:




