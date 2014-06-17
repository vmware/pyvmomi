.. _vim.fault.InvalidDeviceSpec: ../../vim/fault/InvalidDeviceSpec.rst


vim.fault.DeviceUnsupportedForVmPlatform
========================================
    :extends:

        `vim.fault.InvalidDeviceSpec`_

  A DeviceUnsupportedForVmPlatform exception is thrown if the specified device is not supported on the platform on which the virtual machine is being created/configured. For example, this exception might be thrown if a client incorrectly attempts to add a device supported only on ESX Server to a virtual machine on a hosted product.

Attributes:




