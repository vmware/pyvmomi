.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _vim.HostSystem: ../../vim/HostSystem.rst

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _EntityImportType: ../../vim/dvs/EntityBackup/ImportType.rst

.. _vim.SelectionSet: ../../vim/SelectionSet.rst

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst

.. _EntityBackupConfig: ../../vim/dvs/EntityBackup/Config.rst

.. _vim.fault.NotFound: ../../vim/fault/NotFound.rst

.. _vim.fault.DvsFault: ../../vim/fault/DvsFault.rst

.. _vim.dvs.ProductSpec: ../../vim/dvs/ProductSpec.rst

.. _vim.dvs.HostProductSpec: ../../vim/dvs/HostProductSpec.rst

.. _vmodl.fault.NotSupported: ../../vmodl/fault/NotSupported.rst

.. _DistributedVirtualPortgroup: ../../vim/dvs/DistributedVirtualPortgroup.rst

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vim.dvs.EntityBackup.Config: ../../vim/dvs/EntityBackup/Config.rst

.. _DVSManagerImportEntity_Task: ../../vim/dvs/DistributedVirtualSwitchManager.rst#importEntity

.. _vim.DistributedVirtualSwitch: ../../vim/DistributedVirtualSwitch.rst

.. _VmwareDistributedVirtualSwitch: ../../vim/dvs/VmwareDistributedVirtualSwitch.rst

.. _vim.fault.BackupBlobWriteFailure: ../../vim/fault/BackupBlobWriteFailure.rst

.. _vim.dvs.DistributedVirtualPortgroup: ../../vim/dvs/DistributedVirtualPortgroup.rst

.. _vim.DistributedVirtualSwitch.FeatureCapability: ../../vim/DistributedVirtualSwitch/FeatureCapability.rst

.. _vim.dvs.DistributedVirtualSwitchManager.ImportResult: ../../vim/dvs/DistributedVirtualSwitchManager/ImportResult.rst

.. _vim.dvs.DistributedVirtualSwitchManager.HostContainer: ../../vim/dvs/DistributedVirtualSwitchManager/HostContainer.rst

.. _vim.dvs.DistributedVirtualSwitchManager.DvsProductSpec: ../../vim/dvs/DistributedVirtualSwitchManager/DvsProductSpec.rst

.. _vim.dvs.DistributedVirtualSwitchManager.DvsConfigTarget: ../../vim/dvs/DistributedVirtualSwitchManager/DvsConfigTarget.rst

.. _vim.dvs.DistributedVirtualSwitchManager.HostDvsFilterSpec: ../../vim/dvs/DistributedVirtualSwitchManager/HostDvsFilterSpec.rst

.. _vim.dvs.DistributedVirtualSwitchManager.CompatibilityResult: ../../vim/dvs/DistributedVirtualSwitchManager/CompatibilityResult.rst


vim.dvs.DistributedVirtualSwitchManager
=======================================
  The `DistributedVirtualSwitchManager`_ provides methods that support the following operations:
   * Backup and restore operations for
   * `VmwareDistributedVirtualSwitch`_
   * and associated
   * `DistributedVirtualPortgroup`_
   * managed objects.
   * Query operations for information about portgroups and distributed virtual switches.
   * Distributed virtual switch configuration update operations.
   * 


:since: `vSphere API 4.0`_


Attributes
----------


Methods
-------


QueryAvailableDvsSpec():
   This operation returns a list of switch product specifications that are supported by the vCenter Server.


  Privilege:
               System.View



  Args:


  Returns:
    [`vim.dvs.ProductSpec`_]:
         


QueryCompatibleHostForNewDvs(container, recursive, switchProductSpec):
   This operation returns a list of hosts that are compatible with the given DistributedVirtualSwitch product specification.


  Privilege:
               System.View



  Args:
    container (`vim.ManagedEntity`_):
       Where to look for hosts. Supported types of objects for this parameter are `Datacenter`_ , `ComputeResource`_ and `Folder`_ .


    recursive (`bool`_):
       Whether to search for hosts in the subfolders, if applicable. In the case when container is a `Datacenter`_ , the recursive flag is applied to its HostFolder.


    switchProductSpec (`vim.dvs.ProductSpec`_, optional):
       The productSpec of a `DistributedVirtualSwitch`_ . If not set, it is assumed to be the default one used for DistributedVirtualSwitch creation.




  Returns:
    [`vim.HostSystem`_]:
         

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       If the productSpec value is not valid or recognized.


QueryCompatibleHostForExistingDvs(container, recursive, dvs):
   This operation returns a list of hosts that are compatible with the given DistributedVirtualSwitch product specification.


  Privilege:
               System.View



  Args:
    container (`vim.ManagedEntity`_):
       Where to look for hosts. Supported types of objects for this parameter are `Datacenter`_ , `ComputeResource`_ and `Folder`_ .


    recursive (`bool`_):
       Whether to search for hosts in the subfolders, if applicable. In the case when container is a `Datacenter`_ , the recursive flag is applied to its HostFolder.


    dvs (`vim.DistributedVirtualSwitch`_):
       Search the host based on the specification published in the `compatibleHostComponentProductInfo`_ of a `DistributedVirtualSwitch`_ . If not set, it is assumed to be the specification that a DistributedVirtualSwitch would have if it is created with the default `DistributedVirtualSwitchProductSpec`_ .




  Returns:
    [`vim.HostSystem`_]:
         

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       If the switch value is not valid or recognized.


QueryDvsCompatibleHostSpec(switchProductSpec):
   This operation returns a list of host product specifications that are compatible with the given DistributedVirtualSwitch product specification.


  Privilege:
               System.View



  Args:
    switchProductSpec (`vim.dvs.ProductSpec`_, optional):
       The productSpec of a `DistributedVirtualSwitch`_ . If not set, it is assumed to be the default one used for DistributedVirtualSwitch creation.




  Returns:
    [`vim.dvs.HostProductSpec`_]:
         

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       If the switchProductSpec value is not valid or recognized.


QueryDvsFeatureCapability(switchProductSpec):
   This operation indicates which version-specific DVS features are available for the given DistributedVirtualSwitch product specification.
  since: `vSphere API 4.1`_


  Privilege:
               System.View



  Args:
    switchProductSpec (`vim.dvs.ProductSpec`_, optional):
       The productSpec of a `DistributedVirtualSwitch`_ . If not set, it is assumed to be the default one used for DistributedVirtualSwitch creation.




  Returns:
    `vim.DistributedVirtualSwitch.FeatureCapability`_:
         

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       If the switchProductSpec value is not valid or recognized.


QueryDvsByUuid(uuid):
   This operation returns a DistributedVirtualSwitch given a UUID.


  Privilege:
               System.View



  Args:
    uuid (`str`_):




  Returns:
    `vim.DistributedVirtualSwitch`_:
         

  Raises:

    `vim.fault.NotFound`_: 
       If a switch with the UUID doesn't exist.


QueryDvsConfigTarget(host, dvs):
   This operation returns the DistributedVirtualSwitch or DistributedVirtualPortgroup configuration target on a host.


  Privilege:
               System.View



  Args:
    host (`vim.HostSystem`_, optional):
       The host on which the query is to be made. If called directly on the host this parameter need not be specified.


    dvs (`vim.DistributedVirtualSwitch`_, optional):
       The distributed virtual switch on which the query is to be made. If unspecified the config target will encompass all the distributed virtual switches available on the host.




  Returns:
    `vim.dvs.DistributedVirtualSwitchManager.DvsConfigTarget`_:
         


QueryDvsCheckCompatibility(hostContainer, dvsProductSpec, hostFilterSpec):
   This operation returns a list of compatibility results. Each compatibility result is an object that has a host property and optionally a fault which would be populated only if that host is not compatible with a given dvsProductSpec. All filters in hostFilerSpecs are ANDed to derive the intersection of hosts against which compatibility is checked. If caller did not have view privileges on the host entity in an element of the CompatibilityResult array, then that entire element would be removed from the CompatibilityResult array. Typical uses:
    * For the createDVS situation, hostFilterSpec is of type HostDvsFilterSpec and DvsProductSpec will have newSwitchProductSpec set.
    * For the Add-Host-To-DVS situation, you can use either HostDvsFilterSpec or HostDvsMembershipFilter with inclusive being false, and pass the DVS in DvsProductSpec.
    * For the Upgrade-DVS situation, you can use either HostDvsFilterSpec or HostDvsMembershipFilter with inclusive being true, and pass the new desired ProductSpec for DVS in newSwitchProductSpec.
  since: `vSphere API 4.1`_


  Privilege:
               System.View



  Args:
    hostContainer (`vim.dvs.DistributedVirtualSwitchManager.HostContainer`_):
       The container of hosts on which we check the compatibility. This container can be a datacenter, folder, or computeResource. We can also include all the hosts in the hierarchy with container as root of the tree.


    dvsProductSpec (`vim.dvs.DistributedVirtualSwitchManager.DvsProductSpec`_, optional):
       The productSpec of a DistributedVirtualSwitch. If not set, it is assumed to be the default one used for DistributedVirtualSwitch creation for current version.


    hostFilterSpec (`vim.dvs.DistributedVirtualSwitchManager.HostDvsFilterSpec`_, optional):
       The hosts against which to check compatibility. This is a filterSpec and users can use this to specify all hosts in a container (datacenter, folder, or computeResource), an array of hosts, or hosts that might or might not be a DVS member.




  Returns:
    [`vim.dvs.DistributedVirtualSwitchManager.CompatibilityResult`_]:
         

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       If the dvsProductSpec value is not valid or recognized.


RectifyDvsOnHost(hosts):
   Update the Distributed Switch configuration on the hosts to bring them in sync with the current configuration in vCenter Server.
  since: `vSphere API 5.0`_


  Privilege:
               System.Read



  Args:
    hosts (`vim.HostSystem`_):
       The hosts to be rectified.




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.DvsFault`_: 
       if operation fails on any host or if there are other update failures.


DVSManagerExportEntity(selectionSet):
   Export the configuration for entities specified in the selectionSet parameter. You can use this method only for a `VmwareDistributedVirtualSwitch`_ and its associated `DistributedVirtualPortgroup`_ objects. Use the `DVSManagerImportEntity_Task`_ method to restore the entity to the state represented by the exported configuration. You can also use the exported configuration to create a new switch or portgroup.
  since: `vSphere API 5.1`_


  Privilege:
               dynamic



  Args:
    selectionSet (`vim.SelectionSet`_):
       The selection criteria for a set of entities to export the configuration.




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.NotFound`_: 
       If entity in selectionSet doesn't exist.

    `vim.fault.BackupBlobWriteFailure`_: 
       if failed to create backup config blob.


DVSManagerImportEntity(entityBackup, importType):
   Import the configuration of entities specified in `EntityBackupConfig`_ . You can restore the existing configuration to the state represented by the backup configuration. You can also use the backup configuration to create a new switch or portgroup. See `EntityImportType`_ .
  since: `vSphere API 5.1`_


  Privilege:
               dynamic



  Args:
    entityBackup (`vim.dvs.EntityBackup.Config`_):
       Configuration of one or more entities to be imported. The entity backup configuration is returned by the `DVSManagerExportEntity_Task`_ method.


    importType (`str`_):
       Specifies whether to create a new configuration or restore a previous configuration. See `EntityImportType`_ for valid values.




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.DvsFault`_: 
       if operation fails on any host.

    `vim.fault.NotFound`_: 
       If entity in `key`_ doesn't exist.


DVSManagerLookupDvPortGroup(switchUuid, portgroupKey):
   Returns the portgroup identified by the key within the specified VDS identified by its UUID.
  since: `vSphere API 5.1`_


  Privilege:
               System.View



  Args:
    switchUuid (`str`_):
       The UUID of the `DistributedVirtualSwitch`_ .


    portgroupKey (`str`_):
       The key that identifies a `DistributedVirtualPortgroup`_ .




  Returns:
    `vim.dvs.DistributedVirtualPortgroup`_:
         

  Raises:

    `vim.fault.NotFound`_: 
       If the portgroup for the specified inputs was not found.

    `vmodl.fault.NotSupported`_: 
       If the operation is not supported.


