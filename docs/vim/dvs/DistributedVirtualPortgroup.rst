.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _vim.Network: ../../vim/Network.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vim.fault.DvsFault: ../../vim/fault/DvsFault.rst

.. _DVPortgroupConfigSpec: ../../vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst

.. _vim.fault.InvalidName: ../../vim/fault/InvalidName.rst

.. _vim.fault.DuplicateName: ../../vim/fault/DuplicateName.rst

.. _vmodl.fault.NotSupported: ../../vmodl/fault/NotSupported.rst

.. _DVPortgroupRollback_Task: ../../vim/dvs/DistributedVirtualPortgroup.rst#rollback

.. _vim.fault.RollbackFailure: ../../vim/fault/RollbackFailure.rst

.. _vim.fault.ConcurrentAccess: ../../vim/fault/ConcurrentAccess.rst

.. _vim.fault.DvsNotAuthorized: ../../vim/fault/DvsNotAuthorized.rst

.. _DistributedVirtualPortgroup: ../../vim/dvs/DistributedVirtualPortgroup.rst

.. _ReconfigureDVPortgroup_Task: ../../vim/dvs/DistributedVirtualPortgroup.rst#reconfigure

.. _vim.dvs.EntityBackup.Config: ../../vim/dvs/EntityBackup/Config.rst

.. _VmwareDistributedVirtualSwitch: ../../vim/dvs/VmwareDistributedVirtualSwitch.rst

.. _vim.dvs.DistributedVirtualPortgroup.ConfigInfo: ../../vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst

.. _vim.dvs.DistributedVirtualPortgroup.ConfigSpec: ../../vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst


vim.dvs.DistributedVirtualPortgroup
===================================
  The `DistributedVirtualPortgroup`_ managed object defines how hosts and virtual machines connect to a network. A distributed virtual portgroup specifies `DistributedVirtualPort`_ configuration options for the ports on a `DistributedVirtualSwitch`_ . A portgroup also represents a `Network`_ entity in the datacenter.
   * To configure host access by portgroup, set the portgroup in the host virtual NIC specification (
   * `HostVirtualNicSpec`_
   * .
   * `portgroup`_
   * ).
   * To configure virtual machine access by portgroup, set the portgroup in the virtual Ethernet card backing (
   * `VirtualEthernetCard`_
   * .
   * `backing`_
   * .
   * `port`_
   * .
   * `portgroupKey`_
   * ).When you use a portgroup for network access, the Server will create a port according to `config`_ . `type`_ .


:extends: vim.Network_
:since: `vSphere API 4.0`_


Attributes
----------
    key (`str`_):
       Generated UUID of the portgroup.
    config (`vim.dvs.DistributedVirtualPortgroup.ConfigInfo`_):
       Configuration of the portgroup.
    portKeys ([`str`_]):
       Port keys for the set of ports in the portgroup.


Methods
-------


ReconfigureDVPortgroup(spec):
   Reconfigures one or more distributed virtual portgroups. You can use this method to set portgroup properties or to reset the portgroup to a previous state.Reconfiguring a Standard Distributed Virtual PortgroupTo reconfigure a `DistributedVirtualPortgroup`_ , use a `DVPortgroupConfigSpec`_ to set the portgroup properties.Reconfiguring a Portgroup Associated With a VMware Distributed Virtual SwitchIf you use a `VmwareDistributedVirtualSwitch`_ , you can perform the following portgroup reconfiguration:
    * Use a
    * `DVPortgroupConfigSpec`_
    * to set the portgroup properties.
    * Use the
    * `DVPortgroupConfigSpec`_
    * returned by
    * `DVPortgroupRollback_Task`_
    * to reset the portgroup to a previous state.The following privileges are required to reconfigure a portgroup.
    * DVPortgroup.PolicyOp if you are changing the policy of the portgroup.
    * DVPortgroup.ScopeOp if you are changing the scope of the portgroup.
    * DVPortgroup.Modify for anything else.


  Privilege:
               dynamic



  Args:
    spec (`vim.dvs.DistributedVirtualPortgroup.ConfigSpec`_):
       Configuration data for the portgroup.




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.DvsFault`_: 
       if spec is not valid.

    `vim.fault.ConcurrentAccess`_: 
       vim.fault.ConcurrentAccess

    `vim.fault.DuplicateName`_: 
       vim.fault.DuplicateName

    `vim.fault.InvalidName`_: 
       vim.fault.InvalidName

    `vmodl.fault.NotSupported`_: 
       if the spec includes settings for any VDS feature that is not supported on this switch.

    `vim.fault.DvsNotAuthorized`_: 
       if login-session's extension key does not match the switch's configured `extensionKey`_ .


DVPortgroupRollback(entityBackup):
   This method determines if the portgroup configuration has changed. If it has changed, the method returns a `DVPortgroupConfigSpec`_ . Use the `ReconfigureDVPortgroup_Task`_ method to apply the rollback configuration to the portgroup. You can use the rollback method only on a portgroup that is associated with a `VmwareDistributedVirtualSwitch`_ .
    * If you specify the
    * entityBackup
    * parameter, the returned configuration specification represents the exported portgroup configuration. If the
    * entityBackup
    * matches the current portgroup configuration, the method does not return a configuration specification.
    * If
    * entityBackup
    * is not specified, the returned configuration specification represents a previous state of the portgroup, if available. When you use a VMware distributed virtual switch, each time you reconfigure the switch, the Server saves the switch configuration before applying the updates. If the vCenter Server is restarted, the saved configuration is not preserved and the method does not return a configuration specification.To use the rollback method, you must have the DVPortgroup.Read privilege.
  since: `vSphere API 5.1`_


  Privilege:
               dynamic



  Args:
    entityBackup (`vim.dvs.EntityBackup.Config`_, optional):
       The backup of Distributed Virtual PortGroup entity.




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.DvsFault`_: 
       if operation fails.

    `vim.fault.RollbackFailure`_: 
       if there is no configuration specified in entityBackup and the previous configuration does not exist either


