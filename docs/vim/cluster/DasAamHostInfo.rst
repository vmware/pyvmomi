.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _ClusterDasAamHostInfo: ../../vim/cluster/DasAamHostInfo.rst

.. _vim.cluster.DasHostInfo: ../../vim/cluster/DasHostInfo.rst

.. _vim.cluster.DasAamNodeState: ../../vim/cluster/DasAamNodeState.rst


vim.cluster.DasAamHostInfo
==========================
  The `ClusterDasAamHostInfo`_ object contains a list of the ESX hosts in an HA cluster and a list that identifies theprimaryhosts. (AAM is a component of the HA service.) The primary hosts share the joint responsibility of maintaining all cluster state and one will initiate failover actions should a failure occur.When you add an ESX host to a vSphere HA cluster, the host downloads HA agent components from the vCenter Server. The HA agent maintains communication with the vCenter Server.When the host downloads the HA agent, the host configures the agent to communicate with other agents in the cluster. A host that joins the cluster communicates with an existing primary host to complete its configuration (except when you are adding the first host to the cluster).
   * The first five hosts added to the cluster are designated as primary hosts. All subsequent hosts are designated as secondary hosts.
   * If a primary host is removed from the cluster, the vCenter Server promotes another host to primary status.
   * There must be at least one functional primary host for vSphere HA to operate correctly. If there is not an available primary host (no response), host configuration for HA will fail. If there is a total cluster failure, HA will begin restarting virtual machines as soon as one host recovers and its HA agent is up and running.One of the primary hosts assumes the role of the active primary host. The active primary host responsibilities include the following activities:
   * Decides where to restart virtual machines.
   * Tracks failed restart attempts.
   * Determines when it is appropriate to continue attempts to restart a virtual machine.If the active primary host fails, another primary host replaces it.
:extends: vim.cluster.DasHostInfo_
:since: `vSphere API 4.0`_
**deprecated**


Attributes:
    hostDasState ([`vim.cluster.DasAamNodeState`_], optional):

       The state of HA on the hosts.
    primaryHosts ([`str`_], optional):

       The list of primary hosts.
