.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../../../vim/version.rst#vimversionversion9

.. _vim.vm.device.VirtualDevice.BackingInfo: ../../../../vim/vm/device/VirtualDevice/BackingInfo.rst

.. _VirtualSriovEthernetCardSriovBackingInfo: ../../../../vim/vm/device/VirtualSriovEthernetCard/SriovBackingInfo.rst

.. _vim.vm.device.VirtualPCIPassthrough.DeviceBackingInfo: ../../../../vim/vm/device/VirtualPCIPassthrough/DeviceBackingInfo.rst


vim.vm.device.VirtualSriovEthernetCard.SriovBackingInfo
=======================================================
  The `VirtualSriovEthernetCardSriovBackingInfo`_ data object contains information about the SR-IOV physical function and virtual function backing for a passthrough NIC.
:extends: vim.vm.device.VirtualDevice.BackingInfo_
:since: `vSphere API 5.5`_

Attributes:
    physicalFunctionBacking (`vim.vm.device.VirtualPCIPassthrough.DeviceBackingInfo`_, optional):

    virtualFunctionBacking (`vim.vm.device.VirtualPCIPassthrough.DeviceBackingInfo`_, optional):

    virtualFunctionIndex (`int`_, optional):

