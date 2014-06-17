.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.DeviceNotSupported: ../../vim/fault/DeviceNotSupported.rst


vim.fault.DeviceControllerNotSupported
======================================
    :extends:

        `vim.fault.DeviceNotSupported`_

  The device in question is supported, but the device-controller combination is not supported.If this fault is returned as a subfault of DisallowedMigrationDeviceAttached, this indicates that although this device-controller combination may be supported on the destination host, the hosts do not support the requested migration of the virtual machine while using this device and controller.

Attributes:

    controller (`str`_)




