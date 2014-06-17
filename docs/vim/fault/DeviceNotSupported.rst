.. _str: https://docs.python.org/2/library/stdtypes.html

.. _DisallowedMigrationDeviceAttached: ../../vim/fault/DisallowedMigrationDeviceAttached.rst

.. _vim.fault.VirtualHardwareCompatibilityIssue: ../../vim/fault/VirtualHardwareCompatibilityIssue.rst


vim.fault.DeviceNotSupported
============================
    :extends:

        `vim.fault.VirtualHardwareCompatibilityIssue`_

  The virtual machine uses a device type that is not supported on the host.If this fault is returned as a subfault of `DisallowedMigrationDeviceAttached`_ , this indicates that although this device may be supported on the destination host, the hosts do not support the requested migration of the virtual machine while using this device.

Attributes:

    device (`str`_)

    reason (`str`_): is optional.




