
vim.vm.device.VirtualSriovEthernetCard.SriovBackingInfo
=======================================================
  The `VirtualSriovEthernetCardSriovBackingInfo <vim/vm/device/VirtualSriovEthernetCard/SriovBackingInfo.rst>`_ data object contains information about the SR-IOV physical function and virtual function backing for a passthrough NIC.
:extends: vim.vm.device.VirtualDevice.BackingInfo_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    physicalFunctionBacking (`vim.vm.device.VirtualPCIPassthrough.DeviceBackingInfo <vim/vm/device/VirtualPCIPassthrough/DeviceBackingInfo.rst>`_, optional):

    virtualFunctionBacking (`vim.vm.device.VirtualPCIPassthrough.DeviceBackingInfo <vim/vm/device/VirtualPCIPassthrough/DeviceBackingInfo.rst>`_, optional):

    virtualFunctionIndex (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

