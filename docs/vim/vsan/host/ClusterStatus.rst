
vim.vsan.host.ClusterStatus
===========================
  The `VsanHostClusterStatus <vim/vsan/host/ClusterStatus.rst>`_ data object contains a host's cluster status information for the VSAN service. This data object is used to represent read-only state whose values may change during operation.See `QueryHostStatus <vim/host/VsanSystem.rst#queryHostStatus>`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    uuid (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       VSAN service cluster UUID.
    nodeUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       VSAN node UUID for this host.
    health (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       VSAN health state for this host.See `VsanHostHealthState <vim/vsan/host/HealthState.rst>`_ 
    nodeState (`vim.vsan.host.ClusterStatus.State <vim/vsan/host/ClusterStatus/State.rst>`_):

       VSAN node state for this host.
    memberUuid ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       List of UUIDs for VSAN nodes known to this host.
