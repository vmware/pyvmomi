.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _vim.vm.PciPassthroughInfo: ../../vim/vm/PciPassthroughInfo.rst


vim.vm.SriovInfo
================
  Description of a SRIOV device that can be attached to a virtual machine.
:extends: vim.vm.PciPassthroughInfo_
:since: `vSphere API 5.5`_

Attributes:
    virtualFunction (`bool`_):

       Indicates whether corresponding PCI device is a virtual function instantiated by a SR-IOV capable device.
    pnic (`str`_, optional):

       The name of the physical nic that is represented by a SR-IOV capable physical function.
