
vim.cluster.FailoverHostAdmissionControlInfo.HostStatus
=======================================================
  Data object containing the status of a failover host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    host (`vim.HostSystem <vim/HostSystem.rst>`_):

       The failover host.
    status (`vim.ManagedEntity.Status <vim/ManagedEntity/Status.rst>`_):

       The status of the failover host. The status is green for a connected host with no vSphere HA errors and no virtual machines running on it. The status is yellow for a connected host with no vSphere HA errors and some virtual machines running on it. The status red for a disconnected or not responding host, a host that is in maintenance or standby mode or that has a vSphere HA error on it.
