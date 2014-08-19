
vim.vm.SriovInfo
================
  Description of a SRIOV device that can be attached to a virtual machine.
:extends: vim.vm.PciPassthroughInfo_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    virtualFunction (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether corresponding PCI device is a virtual function instantiated by a SR-IOV capable device.
    pnic (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The name of the physical nic that is represented by a SR-IOV capable physical function.
