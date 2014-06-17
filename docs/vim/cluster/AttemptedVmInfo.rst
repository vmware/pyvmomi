.. _vim.Task: ../../vim/Task.rst

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.VirtualMachine: ../../vim/VirtualMachine.rst


vim.cluster.AttemptedVmInfo
===========================
  This data class reports virtual machine powerOn information.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    vm (`vim.VirtualMachine`_):

       The virtual machine being powered on.
    task (`vim.Task`_, optional):

       The ID of the task, which monitors powering on.
