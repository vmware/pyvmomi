.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _VI API 2.5: ../vim/version.rst#vimversionversion2

.. _recommendation: ../vim/ClusterComputeResource.rst#recommendation

.. _vim.HostSystem: ../vim/HostSystem.rst

.. _MigrateVM_Task: ../vim/VirtualMachine.rst#migrate

.. _vSphere API 5.0: ../vim/version.rst#vimversionversion7

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _vSphere API 4.1: ../vim/version.rst#vimversionversion6

.. _vim.fault.NoHost: ../vim/fault/NoHost.rst

.. _vim.ResourcePool: ../vim/ResourcePool.rst

.. _vim.VirtualMachine: ../vim/VirtualMachine.rst

.. _vim.ComputeResource: ../vim/ComputeResource.rst

.. _vim.host.ConnectSpec: ../vim/host/ConnectSpec.rst

.. _vim.cluster.DrsFaults: ../vim/cluster/DrsFaults.rst

.. _vim.option.OptionValue: ../vim/option/OptionValue.rst

.. _vim.fault.TooManyHosts: ../vim/fault/TooManyHosts.rst

.. _vim.cluster.ConfigInfo: ../vim/cluster/ConfigInfo.rst

.. _vim.fault.InvalidState: ../vim/fault/InvalidState.rst

.. _vim.cluster.ConfigSpec: ../vim/cluster/ConfigSpec.rst

.. _vim.fault.InvalidLogin: ../vim/fault/InvalidLogin.rst

.. _vim.fault.DuplicateName: ../vim/fault/DuplicateName.rst

.. _vim.cluster.DrsMigration: ../vim/cluster/DrsMigration.rst

.. _vmodl.fault.NotSupported: ../vmodl/fault/NotSupported.rst

.. _vim.fault.SSLVerifyFault: ../vim/fault/SSLVerifyFault.rst

.. _vim.cluster.ActionHistory: ../vim/cluster/ActionHistory.rst

.. _vim.cluster.Recommendation: ../vim/cluster/Recommendation.rst

.. _vim.fault.AlreadyConnected: ../vim/fault/AlreadyConnected.rst

.. _vim.fault.NotSupportedHost: ../vim/fault/NotSupportedHost.rst

.. _vim.fault.HostConnectFault: ../vim/fault/HostConnectFault.rst

.. _vmodl.fault.InvalidArgument: ../vmodl/fault/InvalidArgument.rst

.. _vim.fault.AgentInstallFailed: ../vim/fault/AgentInstallFailed.rst

.. _vim.fault.AlreadyBeingManaged: ../vim/fault/AlreadyBeingManaged.rst

.. _vim.cluster.DrsRecommendation: ../vim/cluster/DrsRecommendation.rst

.. _vmodl.fault.NotEnoughLicenses: ../vmodl/fault/NotEnoughLicenses.rst

.. _vim.cluster.HostRecommendation: ../vim/cluster/HostRecommendation.rst

.. _vim.cluster.DasAdvancedRuntimeInfo: ../vim/cluster/DasAdvancedRuntimeInfo.rst

.. _vim.cluster.EnterMaintenanceResult: ../vim/cluster/EnterMaintenanceResult.rst

.. _vim.fault.DisallowedOperationOnFailoverHost: ../vim/fault/DisallowedOperationOnFailoverHost.rst

.. _vim.fault.CannotDisableDrsOnClustersWithVApps: ../vim/fault/CannotDisableDrsOnClustersWithVApps.rst


vim.ClusterComputeResource
==========================
  The `ClusterComputeResource`_ data object aggregates the compute resources of associated `HostSystem`_ objects into a single compute resource for use by virtual machines. The cluster services such as HA (High Availability), DRS (Distributed Resource Scheduling), and EVC (Enhanced vMotion Compatibility), enhance the utility of this single compute resource.Use the `Folder`_ . `CreateClusterEx`_ method to create an instance of this object.


:extends: vim.ComputeResource_


Attributes
----------
    configuration (`vim.cluster.ConfigInfo`_):
       Configuration of the cluster.
    recommendation (`vim.cluster.Recommendation`_):
      privilege: System.Read
       List of recommended actions for the cluster. It is possible that the current set of recommendations may be empty, either due to not having any running dynamic recommendation generation module, or since there may be no recommended actions at this time.
    drsRecommendation (`vim.cluster.DrsRecommendation`_):
       If DRS is enabled, this returns the set of recommended migrations from the DRS module. The current set of recommendations may be empty, since there may be no recommended migrations at this time, or it is possible that DRS is not enabled.
    migrationHistory (`vim.cluster.DrsMigration`_):
       The set of migration decisions that have recently been performed.This list is populated only when DRS is in automatic mode.
    actionHistory (`vim.cluster.ActionHistory`_):
       The set of actions that have been performed recently.
    drsFault (`vim.cluster.DrsFaults`_):
      privilege: System.Read
       A collection of the DRS faults generated in the last DRS invocation. Each element of the collection is the set of faults generated in one recommendation. DRS faults are generated when DRS tries to make recommendations for rule enforcement, power management, etc., and indexed in a tree structure with reason for recommendations and VM to migrate (optional) as the index keys. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.


Methods
-------


ReconfigureCluster(spec, modify):
   Reconfigures a cluster.


  Privilege:
               Host.Inventory.EditCluster



  Args:
    spec (`vim.cluster.ConfigSpec`_):
       A set of configuration changes to apply to the cluster. The specification can be a complete set of changes or a partial set of changes, applied incrementally.


    modify (`bool`_):
       Flag to specify whether the specification ("spec") should be applied incrementally. If "modify" is false and the operation succeeds, then the configuration of the cluster matches the specification exactly; in this case any unset portions of the specification will result in unset or default portions of the configuration.




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.CannotDisableDrsOnClustersWithVApps`_: 
       If DRS is being disabled and the cluster contains one or more vApps.


ApplyRecommendation(key):
   Applies a recommendation from the drsRecommendation or the recommendation list. Each recommendation can be applied only once.resource.applyRecommendation privilege is required if the recommendation is DRS migration or power management recommendations.


  Privilege:
               dynamic



  Args:
    key (`str`_):
       The key field of the DrsRecommendation or Recommendation.




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       If the specified key refers to a non-existent or an already executed recommendation.


CancelRecommendation(key):
   Cancels a recommendation. Currently only initial placement recommendations can be cancelled. Migration or power management recommendations cannot.
  since: `vSphere API 4.1`_


  Privilege:
               System.Read



  Args:
    key (`str`_):
       The key field of the Recommendation.




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       If the specified key refers to a non-existent or an already executed recommendation.


RecommendHostsForVm(vm, pool):
   Gets a recommendation for where to power on, resume, revert from powered-off state to powered on state, or to migrate a specific virtual machine. If no host is found, an empty list is returned.The type of operation is implied by the state of the virtual machine. Returned hosts are intended for power-on or resume if the virtual machine is powered-off or suspended. However, if the virtual machine is powered-on, the request is assumed to be for migrating a virtual machine into a DRS enabled cluster. In that case, the ResourcePool argument should be specified and the ResourcePool and the virtual machine cannot be in the same cluster.


  Privilege:
               System.Read



  Args:
    vm (`vim.VirtualMachine`_):
       Specifies the virtual machine for which the user is requesting a recommendations.


    pool (`vim.ResourcePool`_, optional):
       Specifies the ResourcePool into which the virtual machine is to be migrated. If the virtual machine is powered-on, this argument must be specified and it is relevant only when the virtual machine is powered-on. This ResourcePool cannot be in the same cluster as the virtual machine.




  Returns:
    `vim.cluster.HostRecommendation`_:
         An array of HostRecommendation ordered by their rating.

  Raises:

    `vmodl.fault.NotSupported`_: 
       if DRS is not enabled.

    `vmodl.fault.InvalidArgument`_: 
       if the virtual machine is powered on and the optional ResourcePool argument is either not specified or is in the same cluster as the virtual machine.


AddHost(spec, asConnected, resourcePool, license):
   Adds a host to the cluster. The hostname must be either an IP address, such as 192.168.0.1, or a DNS resolvable name. DNS names may be fully qualified names, such as host1.domain1.com, or a short name such as host1, providing host1 resolves to host1.domain1.com. The system uses DNS to resolve short names to fully qualified names. If the cluster supports nested resource pools and the user specifies the optional ResourcePool argument, then the host's root resource pool becomes the specified resource pool. The stand-alone host resource hierarchy is imported into the new nested resource pool.If the cluster does not support nested resource pools, then the stand-alone host resource hierarchy is discarded and all virtual machines on the host are put under the cluster's root resource pool.In addition to the Host.Inventory.AddHostToCluster and Resource.AssignVMToPool privileges, it requires System.View privilege on the VM folder that the VMs of the host will be placed on.


  Privilege:
               Host.Inventory.AddHostToCluster



  Args:
    spec (`vim.host.ConnectSpec`_):
       Specifies the host name, port, and password for the host to be added.


    asConnected (`bool`_):
       Flag to specify whether or not the host should be connected immediately after it is added. The host will not be added if a connection attempt is made and fails.


    resourcePool (`vim.ResourcePool`_, optional):
       the resource pool for the root resource pool from the host.


    license (`str`_, optional, since `vSphere API 4.0`_ ):
       Provide a licenseKey or licenseKeyType. See `LicenseManager`_ 




  Returns:
     `vim.Task`_:
         the newly added HostSystem.

  Raises:

    `vim.fault.InvalidLogin`_: 
       if "asConnected" is specified but authentication with the new host fails.

    `vim.fault.HostConnectFault`_: 
       if an error occurred when connecting to a host. Typically, a more specific subclass, such as AlreadyBeingManaged, is thrown.

    `vim.fault.DuplicateName`_: 
       if another host in the same cluster has the name.

    `vim.fault.AlreadyBeingManaged`_: 
       if the host is already being managed by a VirtualCenter server.

    `vmodl.fault.NotEnoughLicenses`_: 
       if no licenses are available to add this host.

    `vim.fault.NoHost`_: 
       if the host cannot be contacted.

    `vim.fault.NotSupportedHost`_: 
       if the host is running a software version that does not support clustering features. It may still be possible to add the host as a stand-alone host.

    `vim.fault.TooManyHosts`_: 
       if no additional hosts can be added to the cluster.

    `vim.fault.AgentInstallFailed`_: 
       if there is an error installing the VirtualCenter agent on the host.

    `vim.fault.AlreadyConnected`_: 
       if asConnected is true and the host is already connected to VirtualCenter.

    `vim.fault.SSLVerifyFault`_: 
       if the host certificate could not be authenticated


MoveInto(host):
   Moves an existing host into a cluster. The host must be part of the same datacenter, and if the host is part of a cluster, the host must be in maintenance mode.If the host is part of a stand-alone ComputeResource, then the stand-alone ComputeResource is removed as part of this operation.All virtual machines associated with a host, regardless of whether or not they are running, are moved with the host into the cluster. If there are virtual machines that should not be moved, then migrate those virtual machines off the host before initiating this operation.For stand-alone hosts, the host resource pool hierarchy is discarded in this call. To preserve a host resource pools from a stand-alone host, call moveHostInt, specifying an optional resource pool. This operation is transactional only with respect to each individual host. Hosts in the set are moved sequentially and are committed, one at a time. If a failure is detected, then the method terminates with an exception. Since hosts are moved one at a time, if this operation fails while in the process of moving multiple hosts, some hosts are left unmoved.In addition to the privileges mentioned, the user must also hold Host.Inventory.EditCluster on the host's source ComputeResource object.


  Privilege:
               Host.Inventory.EditCluster



  Args:
    host (`vim.HostSystem`_):
       The list of hosts to move into the cluster.




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.DuplicateName`_: 
       if the host is already in the cluster

    `vim.fault.TooManyHosts`_: 
       if no additional hosts can be added to the cluster.

    `vim.fault.InvalidState`_: 
       if a host is already part of a cluster and is not in maintenance mode.

    `vmodl.fault.InvalidArgument`_: 
       if one of the hosts is not part of the same datacenter as the cluster.

    `vim.fault.DisallowedOperationOnFailoverHost`_: 
       if the host is being moved from a cluster and was configured as a failover host in that cluster. See `ClusterFailoverHostAdmissionControlPolicy`_ .


MoveHostInto(host, resourcePool):
   Moves an existing host into a cluster. The host must be part of the same datacenter, and if the host is part of a cluster, the host must be in maintenance mode.If the host is a stand-alone host, the stand-alone ComputeResource is removed as part of this operation.All virtual machines associated with the host, regardless of whether or not they are running, are moved with the host into the cluster. If there are virtual machines that should not be moved, then migrate those virtual machines off the host before initiating this operation.If the host is a stand-alone host, the cluster supports nested resource pools, and the user specifies the optional resourcePool argument, then the stand-alone host's root resource pool becomes the specified resource pool and the stand-alone host resource hierarchy is imported into the new nested resource pool. If the cluster does not support nested resource pools or the resourcePool argument is not specified, then the stand-alone host resource hierarchy is ignored.


  Privilege:
               Host.Inventory.EditCluster



  Args:
    host (`vim.HostSystem`_):
       The list of hosts to move into the cluster.


    resourcePool (`vim.ResourcePool`_, optional):
       The resource pool to match the root resource pool of stand-alone hosts. This argument has no effect if the host is part of a cluster.




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.TooManyHosts`_: 
       if no additional hosts can be added to the cluster.

    `vim.fault.InvalidState`_: 
       if a host is already part of a cluster and is not in maintenance mode.

    `vmodl.fault.InvalidArgument`_: 
       if the host is not a part of the same datacenter as the cluster or if the specified resource pool is not part of the cluster or if the source and destination clusters are the same.


RefreshRecommendation():
   Make DRS invoke again and return a new list of recommendations. Concurrent "refresh" requests may be combined together and trigger only one DRS invocation.The recommendations generated is stored at `recommendation`_ .
  since: `VI API 2.5`_


  Privilege:
               Host.Inventory.EditCluster



  Args:


  Returns:
    None
         


RetrieveDasAdvancedRuntimeInfo():
   Retrieve DAS advanced runtime info for this cluster.
  since: `vSphere API 4.0`_


  Privilege:
               System.Read



  Args:


  Returns:
    `vim.cluster.DasAdvancedRuntimeInfo`_:
         


ClusterEnterMaintenanceMode(host, option):
   The API takes a list of hosts in the cluster as input, and returns a list of hosts in "ClusterMaintenanceResult" that the server can successfully evacuate given the existing constraints in the cluster, such as HA, FT, Vmotion compatibility, reservations, affinity rules, etc. The client is allowed to pass all hosts in the cluster to the API, even though all of them cannot enter maintenance mode at the same time. The list returned from the API contains the largest number of hosts that the server can evacuate simultaneously. The client can then request to enter each host in the returned list into maintenance mode. The client can specify an integer "DemandCapacityRatioTarget" option in the "option" parameter. The allowed values of the option range from 40 to 200, and the default value is 100. This option controls how much resource overcommitment the server should make in consolidating the VMs onto fewer hosts. A value of 100 means the server will keep the same amount of powered-on capacity as the current VM demands. A value less than 100 means undercommitted resources. A value greater than 100 means overcommitted resources. The hosts are recommended based on the inventory at the time of the API invocation. It is not guaranteed that the actual enter-maintenance tasks on the hosts will succeed, if the inventory changes after the API returns, or if vmotions fail due to unexpected conditions. For possible exceptions thrown by the necessary relocate operations, see `MigrateVM_Task`_ .
  since: `vSphere API 5.0`_


  Privilege:
               System.View



  Args:
    host (`vim.HostSystem`_):
       The array of hosts to put into maintenance mode.


    option (`vim.option.OptionValue`_, optional):
       An array of `OptionValue`_ options for this query. The specified options override the advanced options in `ClusterDrsConfigInfo`_ .




  Returns:
    `vim.cluster.EnterMaintenanceResult`_:
         A `ClusterEnterMaintenanceResult`_ object, which consists of an array of recommendations for hosts that can be evacuated and an array of faults for hosts that cannot be evacuated.

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       for unknown option keys or bad values.


