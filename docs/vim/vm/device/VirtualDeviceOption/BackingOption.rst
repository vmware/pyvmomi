
vim.vm.device.VirtualDeviceOption.BackingOption
===============================================
  The `VirtualDeviceBackingOption <vim/vm/device/VirtualDeviceOption/BackingOption.rst>`_ data class defines options for device-specific virtual backing objects.
:extends: vmodl.DynamicData_

Attributes:
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the class the client should use to instantiate backing for the virtual device.
