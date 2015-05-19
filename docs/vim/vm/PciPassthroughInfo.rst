.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.vm.TargetInfo: ../../vim/vm/TargetInfo.rst

.. _vim.host.PciDevice: ../../vim/host/PciDevice.rst


vim.vm.PciPassthroughInfo
=========================
  Description of a generic PCI device that can be attached to a virtual machine.
:extends: vim.vm.TargetInfo_
:since: `vSphere API 4.0`_

Attributes:
    pciDevice (`vim.host.PciDevice`_):

       Details of the PCI device, including vendor, class and device identification information.
    systemId (`str`_):

       The ID of the system the PCI device is attached to.
