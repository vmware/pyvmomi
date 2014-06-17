.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../../../vim/version.rst#vimversionversion9

.. _VsanHostNodeState: ../../../../vim/vsan/host/NodeState.rst

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _vim.vsan.host.ClusterStatus.State.CompletionEstimate: ../../../../vim/vsan/host/ClusterStatus/State/CompletionEstimate.rst


vim.vsan.host.ClusterStatus.State
=================================
  Data object representing the VSAN node state for a host.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    state (`str`_):

       VSAN node state for this host.See `VsanHostNodeState`_ 
    completion (`vim.vsan.host.ClusterStatus.State.CompletionEstimate`_, optional):

       An estimation of the completion of a node state transition; this value may be populated for transitory node states.See `VsanHostNodeState`_ 
