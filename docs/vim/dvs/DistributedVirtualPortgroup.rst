
vim.dvs.DistributedVirtualPortgroup
===================================
  The `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_ managed object defines how hosts and virtual machines connect to a network. A distributed virtual portgroup specifies `DistributedVirtualPort <vim/dvs/DistributedVirtualPort.rst>`_ configuration options for the ports on a `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ . A portgroup also represents a `Network <vim/Network.rst>`_ entity in the datacenter.
   * To configure host access by portgroup, set the portgroup in the host virtual NIC specification (
   * `HostVirtualNicSpec <vim/host/VirtualNic/Specification.rst>`_
   * .
   * `portgroup <vim/host/VirtualNic/Specification.rst#portgroup>`_
   * ).
   * To configure virtual machine access by portgroup, set the portgroup in the virtual Ethernet card backing (
   * `VirtualEthernetCard <vim/vm/device/VirtualEthernetCard.rst>`_
   * .
   * `backing <vim/vm/device/VirtualDevice.rst#backing>`_
   * .
   * `port <vim/vm/device/VirtualEthernetCard/DistributedVirtualPortBackingInfo.rst#port>`_
   * .
   * `portgroupKey <vim/dvs/PortConnection.rst#portgroupKey>`_
   * ).When you use a portgroup for network access, the Server will create a port according to `config <vim/dvs/DistributedVirtualPortgroup.rst#config>`_ . `type <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#type>`_ .


:extends: vim.Network_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


Attributes
----------
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Generated UUID of the portgroup.
    config (`vim.dvs.DistributedVirtualPortgroup.ConfigInfo <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst>`_):
       Configuration of the portgroup.
    portKeys ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):
       Port keys for the set of ports in the portgroup.


Methods
-------


ReconfigureDVPortgroup(spec):
   Reconfigures one or more distributed virtual portgroups. You can use this method to set portgroup properties or to reset the portgroup to a previous state.Reconfiguring a Standard Distributed Virtual PortgroupTo reconfigure a `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_ , use a `DVPortgroupConfigSpec <vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst>`_ to set the portgroup properties.Reconfiguring a Portgroup Associated With a VMware Distributed Virtual SwitchIf you use a `VmwareDistributedVirtualSwitch <vim/dvs/VmwareDistributedVirtualSwitch.rst>`_ , you can perform the following portgroup reconfiguration:
    * Use a
    * `DVPortgroupConfigSpec <vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst>`_
    * to set the portgroup properties.
    * Use the
    * `DVPortgroupConfigSpec <vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst>`_
    * returned by
    * `DVPortgroupRollback_Task <vim/dvs/DistributedVirtualPortgroup.rst#rollback>`_
    * to reset the portgroup to a previous state.The following privileges are required to reconfigure a portgroup.
    * DVPortgroup.PolicyOp if you are changing the policy of the portgroup.
    * DVPortgroup.ScopeOp if you are changing the scope of the portgroup.
    * DVPortgroup.Modify for anything else.


  Privilege:
               dynamic



  Args:
    spec (`vim.dvs.DistributedVirtualPortgroup.ConfigSpec <vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst>`_):
       Configuration data for the portgroup.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if spec is not valid.

    `vim.fault.ConcurrentAccess <vim/fault/ConcurrentAccess.rst>`_: 
       vim.fault.ConcurrentAccess

    `vim.fault.DuplicateName <vim/fault/DuplicateName.rst>`_: 
       vim.fault.DuplicateName

    `vim.fault.InvalidName <vim/fault/InvalidName.rst>`_: 
       vim.fault.InvalidName

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the spec includes settings for any VDS feature that is not supported on this switch.

    `vim.fault.DvsNotAuthorized <vim/fault/DvsNotAuthorized.rst>`_: 
       if login-session's extension key does not match the switch's configured `extensionKey <vim/DistributedVirtualSwitch/ConfigInfo.rst#extensionKey>`_ .


DVPortgroupRollback(entityBackup):
   This method determines if the portgroup configuration has changed. If it has changed, the method returns a `DVPortgroupConfigSpec <vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst>`_ . Use the `ReconfigureDVPortgroup_Task <vim/dvs/DistributedVirtualPortgroup.rst#reconfigure>`_ method to apply the rollback configuration to the portgroup. You can use the rollback method only on a portgroup that is associated with a `VmwareDistributedVirtualSwitch <vim/dvs/VmwareDistributedVirtualSwitch.rst>`_ .
    * If you specify the
    * entityBackup
    * parameter, the returned configuration specification represents the exported portgroup configuration. If the
    * entityBackup
    * matches the current portgroup configuration, the method does not return a configuration specification.
    * If
    * entityBackup
    * is not specified, the returned configuration specification represents a previous state of the portgroup, if available. When you use a VMware distributed virtual switch, each time you reconfigure the switch, the Server saves the switch configuration before applying the updates. If the vCenter Server is restarted, the saved configuration is not preserved and the method does not return a configuration specification.To use the rollback method, you must have the DVPortgroup.Read privilege.
  since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_


  Privilege:
               dynamic



  Args:
    entityBackup (`vim.dvs.EntityBackup.Config <vim/dvs/EntityBackup/Config.rst>`_, optional):
       The backup of Distributed Virtual PortGroup entity.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if operation fails.

    `vim.fault.RollbackFailure <vim/fault/RollbackFailure.rst>`_: 
       if there is no configuration specified in entityBackup and the previous configuration does not exist either


