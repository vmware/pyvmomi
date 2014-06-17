.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.VirtualMachine: ../../../vim/VirtualMachine.rst


vim.vm.device.VirtualDiskId
===========================
  Identifier for a virtual disk.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    vm (`vim.VirtualMachine`_):

       Virtual machine reference.
    diskId (`int`_):

       Device ID `key`_ of the virtual disk.
