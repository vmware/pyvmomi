.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.cluster.DasAdmissionControlInfo: ../../vim/cluster/DasAdmissionControlInfo.rst

.. _vim.cluster.FailoverHostAdmissionControlInfo.HostStatus: ../../vim/cluster/FailoverHostAdmissionControlInfo/HostStatus.rst


vim.cluster.FailoverHostAdmissionControlInfo
============================================
  The current admission control related information if the cluster was configured with a FailoverHostAdmissionControlPolicy.
:extends: vim.cluster.DasAdmissionControlInfo_
:since: `vSphere API 4.0`_

Attributes:
    hostStatus (`vim.cluster.FailoverHostAdmissionControlInfo.HostStatus`_, optional):

       Status of the failover hosts in the cluster.
