.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.VirtualMachine: ../../vim/VirtualMachine.rst


vim.host.GraphicsInfo
=====================
  This data object type describes information about a single graphics device.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    deviceName (`str`_):

       The device name.
    vendorName (`str`_):

       The vendor name.
    pciId (`str`_):

       PCI ID of this device composed of "bus:slot.function".
    graphicsType (`str`_):

       Graphics type (@see GraphicsType).
    memorySizeInKB (`long`_):

       Memory capacity of graphics device or zero if not available.
    vm ([`vim.VirtualMachine`_], optional):

       Virtual machines using this graphics device.
