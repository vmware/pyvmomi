
vim.vsan.host.ClusterStatus.State.CompletionEstimate
====================================================
  Estimated completion status for transitory node states.See `VsanHostNodeState <vim/vsan/host/NodeState.rst>`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    completeTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Estimated time of completion.
    percentComplete (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Estimated percent of completion as a value in the range [0, 100].
