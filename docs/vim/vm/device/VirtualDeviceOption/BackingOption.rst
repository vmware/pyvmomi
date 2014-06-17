.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _VirtualDeviceBackingOption: ../../../../vim/vm/device/VirtualDeviceOption/BackingOption.rst


vim.vm.device.VirtualDeviceOption.BackingOption
===============================================
  The `VirtualDeviceBackingOption`_ data class defines options for device-specific virtual backing objects.
:extends: vmodl.DynamicData_

Attributes:
    type (`str`_):

       The name of the class the client should use to instantiate backing for the virtual device.
