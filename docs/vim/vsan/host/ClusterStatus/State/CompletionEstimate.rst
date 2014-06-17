.. _int: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../../../../vim/version.rst#vimversionversion9

.. _VsanHostNodeState: ../../../../../vim/vsan/host/NodeState.rst

.. _vmodl.DynamicData: ../../../../../vmodl/DynamicData.rst


vim.vsan.host.ClusterStatus.State.CompletionEstimate
====================================================
  Estimated completion status for transitory node states.See `VsanHostNodeState`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    completeTime (`datetime`_, optional):

       Estimated time of completion.
    percentComplete (`int`_, optional):

       Estimated percent of completion as a value in the range [0, 100].
