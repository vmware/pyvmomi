
vim.fault.DeviceBackingNotSupported
===================================
    :extends:

        `vim.fault.DeviceNotSupported <vim/fault/DeviceNotSupported.rst>`_

  The device is backed by a backing type which is not supported for this particular device.If this fault is returned as a subfault of DisallowedMigrationDeviceAttached, this indicates that although this backing for the device may be supported on the destination host, the hosts do not support the requested migration of the virtual machine while using this device with this backing.

Attributes:

    backing (`str <https://docs.python.org/2/library/stdtypes.html>`_)




