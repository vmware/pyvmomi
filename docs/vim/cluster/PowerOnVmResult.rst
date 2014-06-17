.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _PowerOnMultiVM_Task: ../../vim/Datacenter.rst#powerOnVm

.. _vim.cluster.Recommendation: ../../vim/cluster/Recommendation.rst

.. _vim.cluster.AttemptedVmInfo: ../../vim/cluster/AttemptedVmInfo.rst

.. _vim.cluster.NotAttemptedVmInfo: ../../vim/cluster/NotAttemptedVmInfo.rst


vim.cluster.PowerOnVmResult
===========================
  PowerOnVmResult is the base class of the result returned to the `PowerOnMultiVM_Task`_ method.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    attempted (`vim.cluster.AttemptedVmInfo`_, optional):

       The list of virtual machines the Virtual Center has attempted to power on. For a virtual machine not managed by DRS, a task ID is also returned.
    notAttempted (`vim.cluster.NotAttemptedVmInfo`_, optional):

       The list of virtual machines DRS can not find suitable hosts for powering on. There is one fault associated with each virtual machine.
    recommendations (`vim.cluster.Recommendation`_, optional):

       The list of recommendations that need the client to approve manually.
