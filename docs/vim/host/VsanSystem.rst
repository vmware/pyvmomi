.. _str: https://docs.python.org/2/library/stdtypes.html

.. _Task: ../../vim/Task.rst

.. _result: ../../vim/TaskInfo.rst#result

.. _enabled: ../../vim/vsan/host/ConfigInfo.rst#enabled

.. _vim.Task: ../../vim/Task.rst

.. _clusterInfo: ../../vim/vsan/host/ConfigInfo.rst#clusterInfo

.. _networkInfo: ../../vim/vsan/host/ConfigInfo.rst#networkInfo

.. _storageInfo: ../../vim/vsan/host/ConfigInfo.rst#storageInfo

.. _UpdateVsan_Task: ../../vim/host/VsanSystem.rst#update

.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _RemoveDisk_Task: ../../vim/host/VsanSystem.rst#removeDisk

.. _autoClaimStorage: ../../vim/vsan/host/ConfigInfo/StorageInfo.rst#autoClaimStorage

.. _QueryDisksForVsan: ../../vim/host/VsanSystem.rst#queryDisksForVsan

.. _vim.host.ScsiDisk: ../../vim/host/ScsiDisk.rst

.. _VsanHostConfigInfo: ../../vim/vsan/host/ConfigInfo.rst

.. _VsanHostDiskResult: ../../vim/vsan/host/DiskResult.rst

.. _VsanHostDiskMapResult: ../../vim/vsan/host/DiskMapResult.rst

.. _RemoveDiskMapping_Task: ../../vim/host/VsanSystem.rst#removeDiskMapping

.. _vim.vsan.host.DiskResult: ../../vim/vsan/host/DiskResult.rst

.. _vim.vsan.host.ConfigInfo: ../../vim/vsan/host/ConfigInfo.rst

.. _vim.vsan.host.DiskMapping: ../../vim/vsan/host/DiskMapping.rst

.. _vim.vsan.host.DiskMapResult: ../../vim/vsan/host/DiskMapResult.rst

.. _vim.vsan.host.ClusterStatus: ../../vim/vsan/host/ClusterStatus.rst


vim.host.VsanSystem
===================
  The VsanSystem managed object type exposes VSAN configuration primitives and serves as a host-level access point for relevant VSAN data objects.


:since: `vSphere API 5.5`_


Attributes
----------
    config (`vim.vsan.host.ConfigInfo`_):
      privilege: System.Read
       The current VSAN service configuration information for this host.


Methods
-------


QueryDisksForVsan(canonicalName):
   Queries disks on this host for suitability to use with the VSAN service, and returns the result.See vim.host.ScsiDisk#canonicalName


  Privilege:
               System.Read



  Args:
    canonicalName (`str`_, optional):
       may be set to restrict the query to the list of `HostScsiDisk`_ objects named by the given pathsSee vim.host.ScsiDisk#canonicalName




  Returns:
    [`vim.vsan.host.DiskResult`_]:
         a list of populated `VsanHostDiskResult`_ entries


AddDisks(disk):
   Add the set of given disks for use by the VSAN service on this host. Users may use this API to manually add disks for use by VSAN, without specifying an explicit DiskMapping, when the VSAN service not configured to automatically claim storage. Any ineligible disk in the set of given disks and disks which would have exceeded the capacity will be ignored and will not be published in returned `result`_ .Upon successful completion of the returned `Task`_ , its `result`_ field will be populated with a `VsanHostDiskMapResult`_ [] and caller must inspect `VsanHostDiskMapResult`_ [] to check result for individual DiskMapping.See `QueryDisksForVsan`_ See `autoClaimStorage`_ 


  Privilege:
               Host.Config.Storage



  Args:
    disk (`vim.host.ScsiDisk`_):
       list of disks to add for use by the VSAN serviceSee `QueryDisksForVsan`_ See `autoClaimStorage`_ 




  Returns:
     `vim.Task`_:
         


InitializeDisks(mapping):
   Initialize and use the sets of disks in the given DiskMapping list for the VSAN service on this host. Users may use this API to specify or change disk mappings when the VSAN service is not configured to automatically claim storage. For appending new non-SSDs to an existing DiskMapping, users need to specify only the new non-SSDs with its DiskMapping#ssd.Upon successful completion of the returned `Task`_ , its `result`_ field will be populated with a `VsanHostDiskMapResult`_ [] and caller must inspect `VsanHostDiskMapResult`_ [] to check result for individual DiskMapping.See `QueryDisksForVsan`_ See `autoClaimStorage`_ 


  Privilege:
               Host.Config.Storage



  Args:
    mapping (`vim.vsan.host.DiskMapping`_):
       list of disk mappings to initializeSee `QueryDisksForVsan`_ See `autoClaimStorage`_ 




  Returns:
     `vim.Task`_:
         


RemoveDisk(disk):
   Remove the set of given disks from use by the VSAN service on this host. Users may use this API to manually remove a DiskMapping#nonSsd from a DiskMapping. This operation is only permitted if the VSAN service on this host is not configured to automatically claim storage.This method may not be used to remove the last DiskMapping#nonSsd from any given DiskMapping. Removal of the last DiskMapping#nonSsd can be accomplished by using `RemoveDiskMapping_Task`_ .Upon successful completion of the returned `Task`_ , its `result`_ field will be populated with a `VsanHostDiskResult`_ []. Sets DiskIsLastRemainingNonSSD fault in returned task if specified disk is the last DiskMapping#nonSsd member of DiskMapping.See `RemoveDiskMapping_Task`_ See `UpdateVsan_Task`_ See `autoClaimStorage`_ 


  Privilege:
               Host.Config.Storage



  Args:
    disk (`vim.host.ScsiDisk`_):
       list of disks to be removed from use by the VSAN service.See `RemoveDiskMapping_Task`_ See `UpdateVsan_Task`_ See `autoClaimStorage`_ 




  Returns:
     `vim.Task`_:
         


RemoveDiskMapping(mapping):
   Delete given set of disk mappings from use by the VSAN service on this host. This API may be used to remove all disks in a given mapping, including its DiskMapping#ssd. This operation is only permitted if the VSAN service on this host is not configured to automatically claim storage.Upon successful completion of the returned `Task`_ , its `result`_ field will be populated with an empty `VsanHostDiskMapResult`_ []. If any errors are encountered, the returned field will instead contain populated error information.See `RemoveDisk_Task`_ See `UpdateVsan_Task`_ See `autoClaimStorage`_ 


  Privilege:
               Host.Config.Storage



  Args:
    mapping (`vim.vsan.host.DiskMapping`_):
       list of disk mappings to be removed from VSAN usage.See `RemoveDisk_Task`_ See `UpdateVsan_Task`_ See `autoClaimStorage`_ 




  Returns:
     `vim.Task`_:
         


UpdateVsan_Task(config):
   Update the VSAN service on this host according to the given host configuration specification.Enabling and disabling the VSAN service can be achieved by using the `enabled`_ flag. Host storage settings can be specified through use of `storageInfo`_ . If this value is omitted, changes will not be made to the existing storage configuration. Host cluster settings can be specified through use of `clusterInfo`_ . If this value is omitted, changes will not be made to the existing cluster configuration. Host network settings can be specified through use of `networkInfo`_ . If this value is omitted, changes will not be made to the existing network configuration.See `VsanHostConfigInfo`_ See `storageInfo`_ See `clusterInfo`_ See `networkInfo`_ See `QueryDisksForVsan`_ 


  Privilege:
               Host.Config.Storage



  Args:
    config (`vim.vsan.host.ConfigInfo`_):
       host configuration settings to use for the VSAN service.See `VsanHostConfigInfo`_ See `storageInfo`_ See `clusterInfo`_ See `networkInfo`_ See `QueryDisksForVsan`_ 




  Returns:
     `vim.Task`_:
         


QueryHostStatus():
   Queries this host's current runtime status for the VSAN service.


  Privilege:
               System.Read



  Args:


  Returns:
    `vim.vsan.host.ClusterStatus`_:
         a populated `VsanHostClusterStatus`_ entry


