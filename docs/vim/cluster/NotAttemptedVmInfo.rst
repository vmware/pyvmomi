
vim.cluster.NotAttemptedVmInfo
==============================
  This data class reports one virtual machine powerOn failure.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):

       The virtual machine that can not be powered on.
    fault (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

       The exception returned.
