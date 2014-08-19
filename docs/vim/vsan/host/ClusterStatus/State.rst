
vim.vsan.host.ClusterStatus.State
=================================
  Data object representing the VSAN node state for a host.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    state (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       VSAN node state for this host.See `VsanHostNodeState <vim/vsan/host/NodeState.rst>`_ 
    completion (`vim.vsan.host.ClusterStatus.State.CompletionEstimate <vim/vsan/host/ClusterStatus/State/CompletionEstimate.rst>`_, optional):

       An estimation of the completion of a node state transition; this value may be populated for transitory node states.See `VsanHostNodeState <vim/vsan/host/NodeState.rst>`_ 
