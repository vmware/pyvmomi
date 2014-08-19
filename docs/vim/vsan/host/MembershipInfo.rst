
vim.vsan.host.MembershipInfo
============================
  The `VsanHostMembershipInfo <vim/vsan/host/MembershipInfo.rst>`_ data object contains VSAN cluster membership information for a single host, as observed from a given host. This data object is used to represent read-only state whose values may change during operation.See `vsanRuntimeInfo <vim/host/RuntimeInfo.rst#vsanRuntimeInfo>`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    nodeUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       VSAN node UUID for the host of this MembershipInfo.See `nodeUuid <vim/vsan/host/ClusterStatus.rst#nodeUuid>`_ 
    hostname (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Hostname for the host of this MembershipInfo. May be the empty string "" if the hostname is unavailable.
