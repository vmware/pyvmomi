.. _str: https://docs.python.org/2/library/stdtypes.html

.. _nodeUuid: ../../../vim/vsan/host/ClusterStatus.rst#nodeUuid

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vsanRuntimeInfo: ../../../vim/host/RuntimeInfo.rst#vsanRuntimeInfo

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _VsanHostMembershipInfo: ../../../vim/vsan/host/MembershipInfo.rst


vim.vsan.host.MembershipInfo
============================
  The `VsanHostMembershipInfo`_ data object contains VSAN cluster membership information for a single host, as observed from a given host. This data object is used to represent read-only state whose values may change during operation.See `vsanRuntimeInfo`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    nodeUuid (`str`_):

       VSAN node UUID for the host of this MembershipInfo.See `nodeUuid`_ 
    hostname (`str`_):

       Hostname for the host of this MembershipInfo. May be the empty string "" if the hostname is unavailable.
