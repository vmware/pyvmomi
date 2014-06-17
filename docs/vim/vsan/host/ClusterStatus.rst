.. _str: https://docs.python.org/2/library/stdtypes.html

.. _QueryHostStatus: ../../../vim/host/VsanSystem.rst#queryHostStatus

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _VsanHostHealthState: ../../../vim/vsan/host/HealthState.rst

.. _VsanHostClusterStatus: ../../../vim/vsan/host/ClusterStatus.rst

.. _vim.vsan.host.ClusterStatus.State: ../../../vim/vsan/host/ClusterStatus/State.rst


vim.vsan.host.ClusterStatus
===========================
  The `VsanHostClusterStatus`_ data object contains a host's cluster status information for the VSAN service. This data object is used to represent read-only state whose values may change during operation.See `QueryHostStatus`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    uuid (`str`_, optional):

       VSAN service cluster UUID.
    nodeUuid (`str`_, optional):

       VSAN node UUID for this host.
    health (`str`_):

       VSAN health state for this host.See `VsanHostHealthState`_ 
    nodeState (`vim.vsan.host.ClusterStatus.State`_):

       VSAN node state for this host.
    memberUuid (`str`_, optional):

       List of UUIDs for VSAN nodes known to this host.
