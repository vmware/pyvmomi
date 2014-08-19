
vim.vm.device.VirtualDiskId
===========================
  Identifier for a virtual disk.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):

       Virtual machine reference.
    diskId (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Device ID `key <vim/vm/device/VirtualDevice.rst#key>`_ of the virtual disk.
