
vim.DistributedVirtualSwitch
============================
  A `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ managed object is a virtual network switch that is located on a vCenter Server. A distributed virtual switch manages configuration for proxy switches ( `HostProxySwitch <vim/host/HostProxySwitch.rst>`_ ). A proxy switch is located on an ESXi host that is managed by the vCenter Server and is a member of the switch. A distributed switch also provides virtual port state management so that port state is maintained when vCenter Server operations move a virtual machine from one host to another.A proxy switch performs network I/O to support the following network traffic and operations:
   * Network traffic between virtual machines on any hosts that are members of the distributed virtual switch.
   * Network traffic between virtual machines that uses a distributed switch and a virtual machine that uses a VMware standard switch.
   * Network traffic between a virtual machine and a remote system on a physical network connected to the ESXi host.
   * vSphere system operations to support capabilities such as VMotion or High Availability.A `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ is the base distributed switch implementation. It supports a VMware distributed virtual switch implementation and it supports third party distributed switch implementations. The base implementation provides the following capabilities ( `DVSFeatureCapability <vim/DistributedVirtualSwitch/FeatureCapability.rst>`_ ):
   * NIC teaming
   * Network I/O control
   * Network resource allocation
   * Quality of service tag support
   * User-defined resource pools
   * I/O passthrough (VMDirectPath Gen2)A `VmwareDistributedVirtualSwitch <vim/dvs/VmwareDistributedVirtualSwitch.rst>`_ supports the following additional capabilities ( `DVSFeatureCapability <vim/DistributedVirtualSwitch/FeatureCapability.rst>`_ and `VMwareDVSFeatureCapability <vim/dvs/VmwareDistributedVirtualSwitch/FeatureCapability.rst>`_ ):
   * Backup, restore, and rollback for a VMware distributed virtual switch and its associated portgroups.
   * Maximum Transmission Unit (MTU) configuration.
   * Health check operations for NIC teaming and VLAN/MTU support.
   * Monitoring switch traffic using Internet Protocol Flow Information Export (IPFIX).
   * Link Layer Discovery Protocol (LLDP).
   * Virtual network segmentation using a Private VLAN (PVLAN).
   * VLAN-based SPAN (VSPAN) for virtual distributed port mirroring.
   * Link Aggregation Control Protocol (LACP) defined for uplink portgroups.Distributed Virtual Switch ConfigurationTo use a distributed virtual switch, you create a switch and portgroups on a vCenter Server, and add hosts as members of the switch.
   * Create a distributed virtual switch (
   * `Folder <vim/Folder.rst>`_
   * .
   * `CreateDVS_Task <vim/Folder.rst#createDistributedVirtualSwitch>`_
   * ). Use a
   * `DVSConfigSpec <vim/DistributedVirtualSwitch/ConfigSpec.rst>`_
   * to create a switch for a third-party implementation. Use a
   * `VMwareDVSConfigSpec <vim/dvs/VmwareDistributedVirtualSwitch/ConfigSpec.rst>`_
   * to create a VMware distributed virtual switch.
   * Create portgroups (
   * `CreateDVPortgroup_Task <vim/DistributedVirtualSwitch.rst#addPortgroup>`_
   * ) for host and virtual machine network connections and for the connection between proxy switches and physical NICs. A
   * `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_
   * specifies how virtual ports (
   * `DistributedVirtualPort <vim/dvs/DistributedVirtualPort.rst>`_
   * ) will be used. When you create a distributed virtual switch, the vCenter Server automatically creates one uplink portgroup (
   * `config <vim/DistributedVirtualSwitch.rst#config>`_
   * .
   * `uplinkPortgroup <vim/DistributedVirtualSwitch/ConfigInfo.rst#uplinkPortgroup>`_
   * ). Uplink portgroups are distributed virtual portgroups that support the connection between proxy switches and physical NICs.
   * Port creation on a distributed switch is determined by the portgroup type (
   * `DVPortgroupConfigSpec <vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst>`_
   * .
   * `type <vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst#type>`_
   * ):
   * 
   * 
   * If a portgroup is early binding (static), then
   * `DVPortgroupConfigSpec <vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst>`_
   * .
   * `numPorts <vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst#numPorts>`_
   * determines the number of ports that get created when the portgroup is created. This number can be increased if
   * `DVPortgroupConfigSpec <vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst>`_
   * .
   * `autoExpand <vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst#autoExpand>`_
   * is
   * true
   * .
   * If a portgroup is ephemeral (dynamic), then
   * `numPorts <vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst#numPorts>`_
   * is ignored and ports are created as needed.You can also specify standalone ports that are not associated with a port group and uplink ports that are created on ESXi hosts ( `DVSConfigSpec <vim/DistributedVirtualSwitch/ConfigSpec.rst>`_ . `numStandalonePorts <vim/DistributedVirtualSwitch/ConfigSpec.rst#numStandalonePorts>`_ ).The `DVPortgroupConfigInfo <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst>`_ . `numPorts <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#numPorts>`_ property is the total number of ports for a distributed virtual switch. This total includes the ports generated by the static and dynamic portgroups and the standalone ports.
   * If you have created additional uplink portgroups, use the
   * `ReconfigureDvs_Task <vim/DistributedVirtualSwitch.rst#reconfigure>`_
   * method to add the portgroup(s) to the
   * `DVSConfigSpec <vim/DistributedVirtualSwitch/ConfigSpec.rst>`_
   * .
   * `uplinkPortgroup <vim/DistributedVirtualSwitch/ConfigSpec.rst#uplinkPortgroup>`_
   * array.
   * Retrieve physical NIC device names from the host (
   * `HostSystem <vim/HostSystem.rst>`_
   * .
   * `config <vim/HostSystem.rst#config>`_
   * .
   * `network <vim/host/ConfigInfo.rst#network>`_
   * .
   * `pnic <vim/host/NetworkInfo.rst#pnic>`_
   * [].
   * `device <vim/host/PhysicalNic.rst#device>`_
   * ).
   * Add host member(s) to the distributed virtual switch. To configure host members:
   * 
   * 
   * Specify hosts (
   * `DVSConfigSpec <vim/DistributedVirtualSwitch/ConfigSpec.rst>`_
   * .
   * `host <vim/DistributedVirtualSwitch/ConfigSpec.rst#host>`_
   * []).
   * For each host, specify one or more physical NIC device names to identify the pNIC(s) for the host proxy connection to the network (
   * `DistributedVirtualSwitchHostMemberConfigSpec <vim/dvs/HostMember/ConfigSpec.rst>`_
   * .
   * `backing <vim/dvs/HostMember/ConfigSpec.rst#backing>`_
   * .
   * `pnicSpec <vim/dvs/HostMember/PnicBacking.rst#pnicSpec>`_
   * [].
   * `pnicDevice <vim/dvs/HostMember/PnicSpec.rst#pnicDevice>`_
   * )
   * Use the
   * `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_
   * .
   * `ReconfigureDvs_Task <vim/DistributedVirtualSwitch.rst#reconfigure>`_
   * method to update the switch configuration.When you add a host to a distributed virtual switch ( `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ . `config <vim/DistributedVirtualSwitch.rst#config>`_ . `host <vim/DistributedVirtualSwitch/ConfigInfo.rst#host>`_ ), the host automatically creates a proxy switch. The proxy switch is removed automatically when the host is removed from the distributed virtual switch.
   * Connect hosts and virtual machines to the distributed virtual switch.
   * 
   * 
   * 
   * Host connection
   * 
   * Specify port or portgroup connections in the host virtual NIC spec (
   * `HostVirtualNicSpec <vim/host/VirtualNic/Specification.rst>`_
   * .
   * `distributedVirtualPort <vim/host/VirtualNic/Specification.rst#distributedVirtualPort>`_
   * or
   * `HostVirtualNicSpec <vim/host/VirtualNic/Specification.rst>`_
   * .
   * `portgroup <vim/host/VirtualNic/Specification.rst#portgroup>`_
   * ).
   * 
   * 
   * 
   * Virtual machine connection
   * 
   * Specify port or portgroup connections in the distributed virtual port backing (
   * `VirtualEthernetCardDistributedVirtualPortBackingInfo <vim/vm/device/VirtualEthernetCard/DistributedVirtualPortBackingInfo.rst>`_
   * ) for the virtual Ethernet cards on the virtual machine (
   * `VirtualEthernetCard <vim/vm/device/VirtualEthernetCard.rst>`_
   * .
   * `backing <vim/vm/device/VirtualDevice.rst#backing>`_
   * ).
   * 
   * 
   * Backup, Rollback, and Query OperationsIf you are using a `VmwareDistributedVirtualSwitch <vim/dvs/VmwareDistributedVirtualSwitch.rst>`_ , you can perform backup and rollback operations on the switch and its associated distributed virtual portgroups.When you reconfigure a VMware distributed virtual switch ( `ReconfigureDvs_Task <vim/DistributedVirtualSwitch.rst#reconfigure>`_ ), the Server saves the current switch configuration before applying the configuration updates. The saved switch configuration includes portgroup configuration data. The Server uses the saved switch configuration as a checkpoint for rollback operations. You can rollback the switch or portgroup configuration to the saved configuration, or you can rollback to a backup configuration ( `EntityBackupConfig <vim/dvs/EntityBackup/Config.rst>`_ ).
   * To backup the switch and portgroup configuration, use the
   * `DistributedVirtualSwitchManager <vim/dvs/DistributedVirtualSwitchManager.rst>`_
   * .
   * `DVSManagerExportEntity_Task <vim/dvs/DistributedVirtualSwitchManager.rst#exportEntity>`_
   * method. The export method produces a
   * `EntityBackupConfig <vim/dvs/EntityBackup/Config.rst>`_
   * object. The backup configuration contains the switch and/or portgroups specified in the
   * SelectionSet
   * parameter. To backup the complete configuration you must select the distributed virtual switch and all of its portgroups.
   * To rollback the switch configuration, use the
   * `DVSRollback_Task <vim/DistributedVirtualSwitch.rst#rollback>`_
   * method to determine if the switch configuration has changed. If it has changed, use the
   * `ReconfigureDvs_Task <vim/DistributedVirtualSwitch.rst#reconfigure>`_
   * method to complete the rollback operation.
   * To rollback the portgroup configuration, use the
   * `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_
   * .
   * `DVPortgroupRollback_Task <vim/dvs/DistributedVirtualPortgroup.rst#rollback>`_
   * method to determine if the portgroup configuration has changed. If it has changed, use the
   * `ReconfigureDVPortgroup_Task <vim/dvs/DistributedVirtualPortgroup.rst#reconfigure>`_
   * method to complete the rollback operation.To perform query operations on a distributed virtual switch, use the `DistributedVirtualSwitchManager <vim/dvs/DistributedVirtualSwitchManager.rst>`_ methods.


:extends: vim.ManagedEntity_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


Attributes
----------
    uuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Generated UUID of the switch. Unique across vCenter Server inventory and instances.
    capability (`vim.DistributedVirtualSwitch.Capability <vim/DistributedVirtualSwitch/Capability.rst>`_):
       Capability of the switch. Capabilities are indicated at the port, portgroup and switch levels, and for version-specific features. When you retrieve this property from an ESXi host, `capability <vim/DistributedVirtualSwitch.rst#capability>`_ . `dvsOperationSupported <vim/DistributedVirtualSwitch/Capability.rst#dvsOperationSupported>`_ should always be set to false.
    summary (`vim.DistributedVirtualSwitch.Summary <vim/DistributedVirtualSwitch/Summary.rst>`_):
       Summary of the switch.
    config (`vim.DistributedVirtualSwitch.ConfigInfo <vim/DistributedVirtualSwitch/ConfigInfo.rst>`_):
       Switch configuration data.
    networkResourcePool ([`vim.dvs.NetworkResourcePool <vim/dvs/NetworkResourcePool.rst>`_]):
       Network resource pool information for the switch.
    portgroup ([`vim.dvs.DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_]):
       Portgroups that are defined on the switch.
    runtime (`vim.DistributedVirtualSwitch.RuntimeInfo <vim/DistributedVirtualSwitch/RuntimeInfo.rst>`_):
       Runtime information of the distributed virtual switch.


Methods
-------


FetchDVPortKeys(criteria):
   Return the keys of ports that meet the criteria. On an ESXi host, the property shows only the connected ports currently on the host.


  Privilege:
               System.Read



  Args:
    criteria (`vim.dvs.PortCriteria <vim/dvs/PortCriteria.rst>`_, optional):
       The port selection criteria. If unset, the operation returns the keys of all the ports in the switch.




  Returns:
    [`str <https://docs.python.org/2/library/stdtypes.html>`_]:
         


FetchDVPorts(criteria):
   Return the ports that meet the criteria.


  Privilege:
               System.Read



  Args:
    criteria (`vim.dvs.PortCriteria <vim/dvs/PortCriteria.rst>`_, optional):
       The port selection criteria. If unset, the operation returns the keys of all the ports in the portgroup.




  Returns:
    [`vim.dvs.DistributedVirtualPort <vim/dvs/DistributedVirtualPort.rst>`_]:
         


QueryUsedVlanIdInDvs():
   Return the used VLAN ID (PVLAN excluded) in the switch.


  Privilege:
               System.Read



  Args:


  Returns:
    [`int <https://docs.python.org/2/library/stdtypes.html>`_]:
         


ReconfigureDvs(spec):
   Reconfigures a distributed virtual switch. You can use this method to set switch properties or to reset the switch to a previous state.Reconfiguring a Standard Distributed Virtual SwitchTo reconfigure a `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ , use a `DVSConfigSpec <vim/DistributedVirtualSwitch/ConfigSpec.rst>`_ to set the switch properties.Reconfiguring a VMware Distributed Virtual SwitchIf you use a `VmwareDistributedVirtualSwitch <vim/dvs/VmwareDistributedVirtualSwitch.rst>`_ , you can perform the following switch reconfiguration:
    * Use a
    * `VMwareDVSConfigSpec <vim/dvs/VmwareDistributedVirtualSwitch/ConfigSpec.rst>`_
    * to set the switch properties.
    * Use the
    * `VMwareDVSConfigSpec <vim/dvs/VmwareDistributedVirtualSwitch/ConfigSpec.rst>`_
    * returned by
    * `DVSRollback_Task <vim/DistributedVirtualSwitch.rst#rollback>`_
    * to reset the switch to a previous state.Reconfiguring the switch may require any of the following privileges, depending on what is being changed:
    * DVSwitch.PolicyOp if
    * `policy <vim/DistributedVirtualSwitch/ConfigSpec.rst#policy>`_
    * is set.
    * DVSwitch.PortSetting if
    * `defaultPortConfig <vim/DistributedVirtualSwitch/ConfigSpec.rst#defaultPortConfig>`_
    * is set.
    * DVSwitch.HostOp if
    * `policy <vim/DistributedVirtualSwitch/ConfigSpec.rst#policy>`_
    * is set. The user will also need the Host.Config.Network privilege on the host.
    * DVSwitch.Vspan if
    * `vspanConfigSpec <vim/dvs/VmwareDistributedVirtualSwitch/ConfigSpec.rst#vspanConfigSpec>`_
    * is set.
    * DVSwitch.Modify for anything else.


  Privilege:
               dynamic



  Args:
    spec (`vim.DistributedVirtualSwitch.ConfigSpec <vim/DistributedVirtualSwitch/ConfigSpec.rst>`_):
       The configuration of the switch




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if operation fails on any host or if there are other update failures.

    `vim.fault.ConcurrentAccess <vim/fault/ConcurrentAccess.rst>`_: 
       vim.fault.ConcurrentAccess

    `vim.fault.DuplicateName <vim/fault/DuplicateName.rst>`_: 
       vim.fault.DuplicateName

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       vim.fault.InvalidState

    `vim.fault.InvalidName <vim/fault/InvalidName.rst>`_: 
       vim.fault.InvalidName

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       vim.fault.NotFound

    `vim.fault.AlreadyExists <vim/fault/AlreadyExists.rst>`_: 
       vim.fault.AlreadyExists

    `vim.fault.LimitExceeded <vim/fault/LimitExceeded.rst>`_: 
       vim.fault.LimitExceeded

    `vim.fault.ResourceInUse <vim/fault/ResourceInUse.rst>`_: 
       vim.fault.ResourceInUse

    `vim.fault.ResourceNotAvailable <vim/fault/ResourceNotAvailable.rst>`_: 
       If there is no port available in the portgroup

    `vim.fault.DvsNotAuthorized <vim/fault/DvsNotAuthorized.rst>`_: 
       if login-session's extension key does not match the switch's configured `extensionKey <vim/DistributedVirtualSwitch/ConfigInfo.rst#extensionKey>`_ .

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if called directly on a host or if the spec includes settings for any vNetwork Distributed Switch feature that is not supported on this switch.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if any of the hosts being added lack support for any of the overlay classes of the switch's overlay instances.

    `vim.fault.VspanPortConflict <vim/fault/VspanPortConflict.rst>`_: 
       if dvPort is used as both the transmitted source and destination ports in Distributed Port Mirroring sessions.

    `vim.fault.VspanPromiscuousPortNotSupported <vim/fault/VspanPromiscuousPortNotSupported.rst>`_: 
       if a promiscuous port is used as transmitted source or destination in the Distributed Port Mirroring sessions.

    `vim.fault.VspanSameSessionPortConflict <vim/fault/VspanSameSessionPortConflict.rst>`_: 
       if a dvPort is used as both the source and destination in the same Distributed Port Mirroring session.

    `vim.fault.VspanDestPortConflict <vim/fault/VspanDestPortConflict.rst>`_: 
       if a dvPort is used as desination ports in multiple Distributed Port Mirroring sessions.


PerformDvsProductSpecOperation(operation, productSpec):
   This method updates the `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ product specifications.


  Privilege:
               DVSwitch.Modify



  Args:
    operation (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The operation. See `DistributedVirtualSwitchProductSpecOperationType <vim/DistributedVirtualSwitch/ProductSpecOperationType.rst>`_ for valid values. For `VmwareDistributedVirtualSwitch <vim/dvs/VmwareDistributedVirtualSwitch.rst>`_ , only `upgrade <vim/DistributedVirtualSwitch/ProductSpecOperationType.rst#upgrade>`_ is valid.


    productSpec (`vim.dvs.ProductSpec <vim/dvs/ProductSpec.rst>`_, optional):
       The product info of the implementation.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       vim.fault.TaskInProgress

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       vim.fault.InvalidState

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if operation fails on any host or if there are other update failures.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       If called directly on a host.

    `vim.fault.DvsNotAuthorized <vim/fault/DvsNotAuthorized.rst>`_: 
       if login-session's extension key does not match the switch's configured `extensionKey <vim/DistributedVirtualSwitch/ConfigInfo.rst#extensionKey>`_ .


MergeDvs(dvs):
   Merge an existing DistributedVirtualSwitch (source) to this switch (destination). The host members and the connected entity of the source switch will be transferred to the destination switch. This operation disconnects the entities from the source switch, tears down its host proxy switches, creates new proxies for the destination switch, and reconnects the entities to the destination switch.In summary, this operation does the following:
    * Adds the
    * config
    * .
    * `maxPorts <vim/DistributedVirtualSwitch/ConfigInfo.rst#maxPorts>`_
    * of the source switch to the
    * maxPorts
    * of the destination switch.
    * The host members of the source switch leave the source switch and join the destination switch with the same Physical NIC and VirtualSwitch (if applicable). A set of new uplink ports, compliant with the
    * `uplinkPortPolicy <vim/DistributedVirtualSwitch/ConfigSpec.rst#uplinkPortPolicy>`_
    * , is created as the hosts join the destination switch.
    * The portgroups on the source switch are copied over to destination switch, by calculating the effective default port config and creating a portgroup of the same name in the destination switch. If the name already exists, the copied portgroup uses names following a "Copy of switch-portgroup-name" scheme to avoid conflict. The same number of ports are created inside each copied portgroup.
    * The standalone distributed virtual ports are not copied, unless there is a virtual machine or host virtual NIC connecting to it. In that case, the operation calculates the effective port config and creates a port in the destination switch with the same name. Name conflict is resolved using numbers like "original-port-name(1)". The uplink ports are not copied over.
    * The virtual machine and host virtual NICs are disconnected from the source switch and reconnected with the destination switch, to the copied standalone port or portgroup.
    * If you are using a
    * `VmwareDistributedVirtualSwitch <vim/dvs/VmwareDistributedVirtualSwitch.rst>`_
    * - Unless the PVLAN map contains exactly the same entries between the source and destination VMware distributed virtual switches, the method raises a fault if
    * `pvlanId <vim/dvs/VmwareDistributedVirtualSwitch/PvlanSpec.rst#pvlanId>`_
    * is set in any port, portgroup, or switch that will be copied.


  Privilege:
               DVSwitch.Modify



  Args:
    dvs (`vim.DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_):
       The switch (source) to be merged




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if operation fails on any host or if there are other update failures.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       vim.fault.NotFound

    `vim.fault.ResourceInUse <vim/fault/ResourceInUse.rst>`_: 
       If failed to delete the source switch

    `vim.fault.InvalidHostState <vim/fault/InvalidHostState.rst>`_: 
       vim.fault.InvalidHostState

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       If called directly on a host.

    `vim.fault.DvsNotAuthorized <vim/fault/DvsNotAuthorized.rst>`_: 
       if login-session's extension key does not match the switch's configured `extensionKey <vim/DistributedVirtualSwitch/ConfigInfo.rst#extensionKey>`_ .


AddDVPortgroup(spec):
   Creates one or more `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_ s and adds them to the distributed virtual switch.


  Privilege:
               DVPortgroup.Create



  Args:
    spec (`vim.dvs.DistributedVirtualPortgroup.ConfigSpec <vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst>`_):
       The specification for the portgroup.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if operation fails on any host or if there are other update failures.

    `vim.fault.DuplicateName <vim/fault/DuplicateName.rst>`_: 
       vim.fault.DuplicateName

    `vim.fault.InvalidName <vim/fault/InvalidName.rst>`_: 
       vim.fault.InvalidName

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       If called directly on a host.

    `vim.fault.DvsNotAuthorized <vim/fault/DvsNotAuthorized.rst>`_: 
       if login-session's extension key does not match the switch's configured `extensionKey <vim/DistributedVirtualSwitch/ConfigInfo.rst#extensionKey>`_ .


MoveDVPort(portKey, destinationPortgroupKey):
   Move the ports out of their current portgroup into the specified portgroup. If the moving of any of the ports results in a violation of the portgroup policy, or type of the source or destination portgroup, the operation raises a fault. A conflict port cannot be moved.


  Privilege:
               DVSwitch.Modify



  Args:
    portKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The keys of the ports to be moved into the portgroup.


    destinationPortgroupKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The key of the portgroup to be moved into. If unset, the port will be moved under the switch.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if operation fails on any host or if there are other update failures.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       vim.fault.NotFound

    `vim.fault.ConcurrentAccess <vim/fault/ConcurrentAccess.rst>`_: 
       vim.fault.ConcurrentAccess

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       If called directly on a host.

    `vim.fault.DvsNotAuthorized <vim/fault/DvsNotAuthorized.rst>`_: 
       if login-session's extension key does not match the switch's configured `extensionKey <vim/DistributedVirtualSwitch/ConfigInfo.rst#extensionKey>`_ .


UpdateDvsCapability(capability):
   Set the capability of the switch.


  Privilege:
               DVSwitch.Modify



  Args:
    capability (`vim.DistributedVirtualSwitch.Capability <vim/DistributedVirtualSwitch/Capability.rst>`_):
       The capability of the switch.




  Returns:
    None
         

  Raises:

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if operation fails on any host or if there are other update failures.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       If called directly on a host or if the switch implementation doesn't support this API.

    `vim.fault.DvsNotAuthorized <vim/fault/DvsNotAuthorized.rst>`_: 
       if login-session's extension key does not match the switch's configured `extensionKey <vim/DistributedVirtualSwitch/ConfigInfo.rst#extensionKey>`_ .


ReconfigureDVPort(port):
   Reconfigure individual ports.


  Privilege:
               DVSwitch.PortConfig



  Args:
    port (`vim.dvs.DistributedVirtualPort.ConfigSpec <vim/dvs/DistributedVirtualPort/ConfigSpec.rst>`_):
       The specification of the ports.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if operation fails on any host or if there are other update failures.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       vim.fault.NotFound

    `vim.fault.ResourceInUse <vim/fault/ResourceInUse.rst>`_: 
       vim.fault.ResourceInUse

    `vim.fault.ConcurrentAccess <vim/fault/ConcurrentAccess.rst>`_: 
       vim.fault.ConcurrentAccess

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       If called directly on a host or if the switch implementation doesn't support this API or if the spec includes settings for any vSphere Distributed Switch feature that is not supported on this switch.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       If the array have different elements for the same port.

    `vim.fault.DvsNotAuthorized <vim/fault/DvsNotAuthorized.rst>`_: 
       if login-session's extension key does not match the switch's configured `extensionKey <vim/DistributedVirtualSwitch/ConfigInfo.rst#extensionKey>`_ .


RefreshDVPortState(portKeys):
   Refresh port states.


  Privilege:
               System.Read



  Args:
    portKeys (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The keys of the ports to be refreshed. If not specified, all port states are refreshed.




  Returns:
    None
         

  Raises:

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if operation fails on any host or if there are other update failures.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       vim.fault.NotFound


RectifyDvsHost(hosts):
   Update the switch configuration on the host to bring them in sync with the current configuration in vCenter Server.


  Privilege:
               System.Read



  Args:
    hosts (`vim.HostSystem <vim/HostSystem.rst>`_, optional):
       The hosts to be rectified.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if operation fails on any host or if there are other update failures.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       vim.fault.NotFound


UpdateNetworkResourcePool(configSpec):
   Update the network resource pool configuration.
  since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_


  Privilege:
               DVSwitch.ResourceManagement



  Args:
    configSpec (`vim.dvs.NetworkResourcePool.ConfigSpec <vim/dvs/NetworkResourcePool/ConfigSpec.rst>`_):
       The network resource pool configuration specification.




  Returns:
    None
         

  Raises:

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if operation fails on any host or if there are other update failures.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the resource pool does not exist on the dvs.

    `vim.fault.InvalidName <vim/fault/InvalidName.rst>`_: 
       if the name of the resource pool is invalid.

    `vim.fault.ConcurrentAccess <vim/fault/ConcurrentAccess.rst>`_: 
       if a network resource pool is modified by two or more clients at the same time.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if network I/O control is not supported on the vSphere Distributed Switch.

    `vim.fault.DvsNotAuthorized <vim/fault/DvsNotAuthorized.rst>`_: 
       if login-session's extension key does not match the switch's configured `extensionKey <vim/DistributedVirtualSwitch/ConfigInfo.rst#extensionKey>`_ .


AddNetworkResourcePool(configSpec):
   Add a network resource pool.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               DVSwitch.ResourceManagement



  Args:
    configSpec (`vim.dvs.NetworkResourcePool.ConfigSpec <vim/dvs/NetworkResourcePool/ConfigSpec.rst>`_):
       the network resource pool configuration specification.




  Returns:
    None
         

  Raises:

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if operation fails on any host or if there are other update failures.

    `vim.fault.InvalidName <vim/fault/InvalidName.rst>`_: 
       vim.fault.InvalidName

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if network I/O control is not supported on the vSphere Distributed Switch.

    `vim.fault.DvsNotAuthorized <vim/fault/DvsNotAuthorized.rst>`_: 
       if login-session's extension key does not match the switch's configured `extensionKey <vim/DistributedVirtualSwitch/ConfigInfo.rst#extensionKey>`_ .


RemoveNetworkResourcePool(key):
   Remove a network resource pool.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               DVSwitch.ResourceManagement



  Args:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The network resource pool key.




  Returns:
    None
         

  Raises:

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if operation fails on any host or if there are other update failures.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the resource pool does not exist on the dvs.

    `vim.fault.InvalidName <vim/fault/InvalidName.rst>`_: 
       if the name of the resource pool is invalid.

    `vim.fault.ResourceInUse <vim/fault/ResourceInUse.rst>`_: 
       If network resource pool is associated with a network entity

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if network I/O control is not supported on the vSphere Distributed Switch.

    `vim.fault.DvsNotAuthorized <vim/fault/DvsNotAuthorized.rst>`_: 
       if login-session's extension key does not match the switch's configured `extensionKey <vim/DistributedVirtualSwitch/ConfigInfo.rst#extensionKey>`_ .


EnableNetworkResourceManagement(enable):
   Enable/Disable network I/O control on the vSphere Distributed Switch.
  since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_


  Privilege:
               DVSwitch.ResourceManagement



  Args:
    enable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       If true, enables I/O control. If false, disables network I/O control.




  Returns:
    None
         

  Raises:

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if the enabling/disabling fails.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if network I/O control is not supported on the vSphere Distributed Switch.

    `vim.fault.DvsNotAuthorized <vim/fault/DvsNotAuthorized.rst>`_: 
       if login-session's extension key does not match the switch's configured `extensionKey <vim/DistributedVirtualSwitch/ConfigInfo.rst#extensionKey>`_ .


DVSRollback(entityBackup):
   This method determines if the distributed virtual switch configuration has changed. If it has changed, the method returns a `VMwareDVSConfigSpec <vim/dvs/VmwareDistributedVirtualSwitch/ConfigSpec.rst>`_ . Use the `ReconfigureDvs_Task <vim/DistributedVirtualSwitch.rst#reconfigure>`_ method to apply the rollback configuration to the switch. You can use the rollback method only on a `VmwareDistributedVirtualSwitch <vim/dvs/VmwareDistributedVirtualSwitch.rst>`_ .
    * If you specify the
    * entityBackup
    * parameter, the returned configuration specification represents the exported switch configuration. If the
    * entityBackup
    * matches the current switch configuration, the method does not return a configuration specification.
    * If
    * entityBackup
    * is not specified, the returned configuration specification represents a previous state of the switch, if available. When you use a VMware distributed virtual switch, each time you reconfigure the switch, the Server saves the switch configuration before applying the updates. If the vCenter Server is restarted, the saved configuration is not preserved and the method does not return a configuration specification.To use the rollback method, you must have the DVSwitch.Read privilege.
  since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_


  Privilege:
               dynamic



  Args:
    entityBackup (`vim.dvs.EntityBackup.Config <vim/dvs/EntityBackup/Config.rst>`_, optional):
       Backup of a distributed virtual switch, returned by the `DVSManagerExportEntity_Task <vim/dvs/DistributedVirtualSwitchManager.rst#exportEntity>`_ method.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if operation fails.

    `vim.fault.RollbackFailure <vim/fault/RollbackFailure.rst>`_: 
       if there is no configuration specified in entityBackup and the previous configuration does not exist either.


CreateDVPortgroup(spec):
   Creates a single `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_ and adds it to the distributed virtual switch.
  since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_


  Privilege:
               DVPortgroup.Create



  Args:
    spec (`vim.dvs.DistributedVirtualPortgroup.ConfigSpec <vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst>`_):
       The specification for the portgroup.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if operation fails on any host or if there are other update failures.

    `vim.fault.DuplicateName <vim/fault/DuplicateName.rst>`_: 
       if a portgroup with the same name already exists

    `vim.fault.InvalidName <vim/fault/InvalidName.rst>`_: 
       if name of the portgroup is invalid


UpdateDVSHealthCheckConfig(healthCheckConfig):
   Update health check configuration.
  since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_


  Privilege:
               DVSwitch.Modify



  Args:
    healthCheckConfig (`vim.DistributedVirtualSwitch.HealthCheckConfig <vim/DistributedVirtualSwitch/HealthCheckConfig.rst>`_):
       The health check configuration.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if operation fails on any host or if there are other update failures.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if health check is not supported on the switch.


LookupDvPortGroup(portgroupKey):
   Returns the portgroup identified by the key within this VDS.
  since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_


  Privilege:
               System.Read



  Args:
    portgroupKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The key that identifies a portgroup of this VDS.




  Returns:
    `vim.dvs.DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_:
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       If the portgroup for the specified key is not found.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       If the operation is not supported.


