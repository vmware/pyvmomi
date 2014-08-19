
vim.cluster.PowerOnVmResult
===========================
  PowerOnVmResult is the base class of the result returned to the `PowerOnMultiVM_Task <vim/Datacenter.rst#powerOnVm>`_ method.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    attempted ([`vim.cluster.AttemptedVmInfo <vim/cluster/AttemptedVmInfo.rst>`_], optional):

       The list of virtual machines the Virtual Center has attempted to power on. For a virtual machine not managed by DRS, a task ID is also returned.
    notAttempted ([`vim.cluster.NotAttemptedVmInfo <vim/cluster/NotAttemptedVmInfo.rst>`_], optional):

       The list of virtual machines DRS can not find suitable hosts for powering on. There is one fault associated with each virtual machine.
    recommendations ([`vim.cluster.Recommendation <vim/cluster/Recommendation.rst>`_], optional):

       The list of recommendations that need the client to approve manually.
