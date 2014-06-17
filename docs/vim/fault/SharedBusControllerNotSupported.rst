.. _vim.fault.DeviceNotSupported: ../../vim/fault/DeviceNotSupported.rst


vim.fault.SharedBusControllerNotSupported
=========================================
    :extends:

        `vim.fault.DeviceNotSupported`_

  The virtual machine has one or more SCSI controllers that are engaged in bus sharing. This is an error when migrating a powered-on virtual machine, and can be returned as a subfault of DisallowedMigrationDeviceAttached.

Attributes:




