
vim.cluster.FailoverHostAdmissionControlInfo
============================================
  The current admission control related information if the cluster was configured with a FailoverHostAdmissionControlPolicy.
:extends: vim.cluster.DasAdmissionControlInfo_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    hostStatus ([`vim.cluster.FailoverHostAdmissionControlInfo.HostStatus <vim/cluster/FailoverHostAdmissionControlInfo/HostStatus.rst>`_], optional):

       Status of the failover hosts in the cluster.
