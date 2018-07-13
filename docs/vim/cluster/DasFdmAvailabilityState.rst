.. _connectedToMaster: ../../vim/cluster/DasFdmAvailabilityState.rst#connectedToMaster

.. _ClusterDasFdmHostState: ../../vim/cluster/DasFdmHostState.rst

.. _ClusterDasFdmAvailabilityState: ../../vim/cluster/DasFdmAvailabilityState.rst

.. _vim.cluster.DasFdmAvailabilityState: ../../vim/cluster/DasFdmAvailabilityState.rst

.. _ClusterDasVmSettingsIsolationResponse: ../../vim/cluster/DasVmSettings/IsolationResponse.rst

vim.cluster.DasFdmAvailabilityState
===================================
  The `ClusterDasFdmAvailabilityState`_ enumeration describes the availability states of hosts in a vSphere HA cluster. In the HA architecture, a agent called the Fault Domain Manager runs on each active host. These agents elect a master and the others become its slaves. The availability state assigned to a given host is determined from information reported by the Fault Domain Manager running on the host, by a Fault Domain Manager that has been elected master, and by vCenter Server. See `ClusterDasFdmHostState`_ for more information about the vSphere HA architecture.

  :type: `vim.cluster.DasFdmAvailabilityState`_

  :name: fdmUnreachable

values:
--------

uninitialized
   The Fault Domain Manager for the host has not yet been initialized. Hence the host is not part of a vSphere HA fault domain. This state is reported by vCenter Server or by the host itself.

hostDown
   The slave host appears to be down. This state is reported by the master of a slave host.

fdmUnreachable
   The Fault Domain Manager (FDM) on the host cannot be reached. This state is reported in two unlikely situations.
    * First, it is reported by a master if the host responds to ICMP pings sent by the master over the management network but the FDM on the host cannot be reached by the master. This situation will occur if the FDM is unable to run or exit the uninitialized state.
    * Second, it is reported by vCenter Server if it cannot connect to a master nor the FDM for the host. This situation would occur if all hosts in the cluster failed but vCenter Server is still running. It may also occur if all FDMs are unable to run or exit the uninitialized state.
    *

connectedToMaster
   The normal operating state for a slave host. In this state, the host is exchanging heartbeats with a master over the management network, and is thus connected to it. If there is a management network partition, the slave will be in this state only if it is in the same partition as the master. This state is reported by the master of a slave host.

master
   The Fault Domain Manager on the host has been elected a master. This state is reported by the the host itself.

election
   The Fault Domain Manager on the host has been initialized and the host is either waiting to join the existing master or is participating in an election for a new master. This state is reported by vCenter Server or by the host itself.

networkIsolated
   A host is alive but is isolated from the management network. See `ClusterDasVmSettingsIsolationResponse`_ for the criteria used to determine whether a host is isolated.

initializationError
   An error occurred when initilizating the Fault Domain Manager on a host due to a problem with installing the agent or configuring it. This condition can often be cleared by reconfiguring HA for the host. This state is reported by vCenter Server.

uninitializationError
   An error occurred when unconfiguring the Fault Domain Manager running on a host. In order to clear this condition the host might need to be reconnected to the cluster and reconfigured first. This state is reported by vCenter Server.

networkPartitionedFromMaster
   A slave host is alive and has management network connectivity, but the management network has been partitioned. This state is reported by masters that are in a partition other than the one containing the slave host; the master in the slave's partition will report the slave state as `connectedToMaster`_ .
