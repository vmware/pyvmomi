.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.VirtualMachine: ../../../vim/VirtualMachine.rst


vim.cluster.DasFailoverLevelAdvancedRuntimeInfo.VmSlots
=======================================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    vm (`vim.VirtualMachine`_):

       The reference to the virtual machine
    slots (`int`_):

       The number of slots required by this virtual machine
