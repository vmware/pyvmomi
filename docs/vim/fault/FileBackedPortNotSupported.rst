.. _vim.fault.DeviceNotSupported: ../../vim/fault/DeviceNotSupported.rst


vim.fault.FileBackedPortNotSupported
====================================
    :extends:

        `vim.fault.DeviceNotSupported`_

  The virtual machine has a port (either a SerialPort or a ParallelPort) which is backed by a file. This is an error when migrating a virtual machine with the device connected, and can be returned as a subfault of DisallowedMigrationDeviceAttached.

Attributes:




