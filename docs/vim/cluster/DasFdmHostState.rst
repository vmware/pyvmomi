
vim.cluster.DasFdmHostState
===========================
  The `ClusterDasFdmHostState <vim/cluster/DasFdmHostState.rst>`_ data object describes the availability state of each active host in a vSphere HA enabled cluster.In a vSphere HA cluster, the active hosts form a fault domain. A host is inactive if it is in standby or maintenance mode, or it has been disconnected from vCenter Server. A vSphere HA agent, called the Fault Domain Manager (FDM), runs on each host in the fault domain.One FDM serves as the master and the remaining FDMs as its slaves. The master is responsible for monitoring the availability of the hosts and VMs in the cluster, and restarting any VMs that fail due to a host failure or non-user-initiated power offs. The master is also responsible for reporting fault-domain state to vCenter Server.The master FDM is determined through election by the FDMs that are alive at the time. An election occurs in the following circumstances:
   * When the vSphere HA feature is enabled for the cluster.
   * When the master's host fails.
   * When the management network is partitioned. In a network partition there will be a master for each partition. However, only one master will be responsible for a given VM. When the partition is resolved, all but one of the masters will abdicate.
   * After a host in a vSphere HA cluster powers back up following a failure that caused all hosts in the cluster to power off.
   * 
   * The slaves are responsible for reporting state updates to the master and restarting VMs as required. All FDMs provide the VM/Application Health Monitoring Service.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    state (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The Availability State of a host based on information reported by the entity given by the `stateReporter <vim/cluster/DasFdmHostState.rst#stateReporter>`_ property. See `ClusterDasFdmAvailabilityState <vim/cluster/DasFdmAvailabilityState.rst>`_ for the set of states.
    stateReporter (`vim.HostSystem <vim/HostSystem.rst>`_, optional):

       The entity reporting the state of the host. If the reporter is a host, the property reports which host, whereas if the reporter is vCenter Server, the property is unset.
