.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _VirtualDeviceBusSlotOption: ../../../../vim/vm/device/VirtualDeviceOption/BusSlotOption.rst


vim.vm.device.VirtualDeviceOption.BusSlotOption
===============================================
  The `VirtualDeviceBusSlotOption`_ data class defines options for device-specific bus slot objects.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    type (`str`_):

       The name of the class the client should use to instantiate bus slot object for the virtual device.
