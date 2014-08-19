
vim.fault.DeviceNotSupported
============================
    :extends:

        `vim.fault.VirtualHardwareCompatibilityIssue <vim/fault/VirtualHardwareCompatibilityIssue.rst>`_

  The virtual machine uses a device type that is not supported on the host.If this fault is returned as a subfault of `DisallowedMigrationDeviceAttached <vim/fault/DisallowedMigrationDeviceAttached.rst>`_ , this indicates that although this device may be supported on the destination host, the hosts do not support the requested migration of the virtual machine while using this device.

Attributes:

    device (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    reason (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.




