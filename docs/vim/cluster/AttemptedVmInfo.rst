
vim.cluster.AttemptedVmInfo
===========================
  This data class reports virtual machine powerOn information.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):

       The virtual machine being powered on.
    task (`vim.Task <vim/Task.rst>`_, optional):

       The ID of the task, which monitors powering on.
