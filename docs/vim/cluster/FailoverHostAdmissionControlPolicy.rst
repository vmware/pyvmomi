.. _hostStatus: ../../vim/cluster/FailoverHostAdmissionControlInfo.rst#hostStatus

.. _vim.HostSystem: ../../vim/HostSystem.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _admissionControlInfo: ../../vim/ClusterComputeResource/Summary.rst#admissionControlInfo

.. _ClusterComputeResourceSummary: ../../vim/ClusterComputeResource/Summary.rst

.. _vim.cluster.DasAdmissionControlPolicy: ../../vim/cluster/DasAdmissionControlPolicy.rst

.. _ClusterFailoverHostAdmissionControlPolicy: ../../vim/cluster/FailoverHostAdmissionControlPolicy.rst


vim.cluster.FailoverHostAdmissionControlPolicy
==============================================
  The `ClusterFailoverHostAdmissionControlPolicy`_ dedicates one or more hosts for use during failover. When a host fails with this policy in place, vSphere HA attempts to restart its virtual machines on a dedicated failover host. If this is not possible, for example the failover host itself has failed or it has insufficient resources, HA attempts to restart those virtual machines on another host in the cluster.To support the availabilty of a failover host, the vCenter Server will prevent users from powering on virtual machines on that host, or from using vMotion to migrate virtual machines to the host. Also, DRS does not use the failover host for load balancing.To obtain the status of a failover host, use the `hostStatus`_ property ( `ClusterComputeResourceSummary`_ . `admissionControlInfo`_ . `hostStatus`_ ).
:extends: vim.cluster.DasAdmissionControlPolicy_
:since: `vSphere API 4.0`_

Attributes:
    failoverHosts ([`vim.HostSystem`_], optional):

       List of managed object references to failover hosts.
