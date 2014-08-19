
vim.host.VsanSystem
===================
  The VsanSystem managed object type exposes VSAN configuration primitives and serves as a host-level access point for relevant VSAN data objects.


:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_


Attributes
----------
    config (`vim.vsan.host.ConfigInfo <vim/vsan/host/ConfigInfo.rst>`_):
      privilege: System.Read
       The current VSAN service configuration information for this host.


Methods
-------


QueryDisksForVsan(canonicalName):
   Queries disks on this host for suitability to use with the VSAN service, and returns the result.See vim.host.ScsiDisk#canonicalName


  Privilege:
               System.Read



  Args:
    canonicalName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       may be set to restrict the query to the list of `HostScsiDisk <vim/host/ScsiDisk.rst>`_ objects named by the given pathsSee vim.host.ScsiDisk#canonicalName




  Returns:
    [`vim.vsan.host.DiskResult <vim/vsan/host/DiskResult.rst>`_]:
         a list of populated `VsanHostDiskResult <vim/vsan/host/DiskResult.rst>`_ entries


AddDisks(disk):
   Add the set of given disks for use by the VSAN service on this host. Users may use this API to manually add disks for use by VSAN, without specifying an explicit DiskMapping, when the VSAN service not configured to automatically claim storage. Any ineligible disk in the set of given disks and disks which would have exceeded the capacity will be ignored and will not be published in returned `result <vim/TaskInfo.rst#result>`_ .Upon successful completion of the returned `Task <vim/Task.rst>`_ , its `result <vim/TaskInfo.rst#result>`_ field will be populated with a `VsanHostDiskMapResult <vim/vsan/host/DiskMapResult.rst>`_ [] and caller must inspect `VsanHostDiskMapResult <vim/vsan/host/DiskMapResult.rst>`_ [] to check result for individual DiskMapping.See `QueryDisksForVsan <vim/host/VsanSystem.rst#queryDisksForVsan>`_ See `autoClaimStorage <vim/vsan/host/ConfigInfo/StorageInfo.rst#autoClaimStorage>`_ 


  Privilege:
               Host.Config.Storage



  Args:
    disk (`vim.host.ScsiDisk <vim/host/ScsiDisk.rst>`_):
       list of disks to add for use by the VSAN serviceSee `QueryDisksForVsan <vim/host/VsanSystem.rst#queryDisksForVsan>`_ See `autoClaimStorage <vim/vsan/host/ConfigInfo/StorageInfo.rst#autoClaimStorage>`_ 




  Returns:
     `vim.Task <vim/Task.rst>`_:
         


InitializeDisks(mapping):
   Initialize and use the sets of disks in the given DiskMapping list for the VSAN service on this host. Users may use this API to specify or change disk mappings when the VSAN service is not configured to automatically claim storage. For appending new non-SSDs to an existing DiskMapping, users need to specify only the new non-SSDs with its DiskMapping#ssd.Upon successful completion of the returned `Task <vim/Task.rst>`_ , its `result <vim/TaskInfo.rst#result>`_ field will be populated with a `VsanHostDiskMapResult <vim/vsan/host/DiskMapResult.rst>`_ [] and caller must inspect `VsanHostDiskMapResult <vim/vsan/host/DiskMapResult.rst>`_ [] to check result for individual DiskMapping.See `QueryDisksForVsan <vim/host/VsanSystem.rst#queryDisksForVsan>`_ See `autoClaimStorage <vim/vsan/host/ConfigInfo/StorageInfo.rst#autoClaimStorage>`_ 


  Privilege:
               Host.Config.Storage



  Args:
    mapping (`vim.vsan.host.DiskMapping <vim/vsan/host/DiskMapping.rst>`_):
       list of disk mappings to initializeSee `QueryDisksForVsan <vim/host/VsanSystem.rst#queryDisksForVsan>`_ See `autoClaimStorage <vim/vsan/host/ConfigInfo/StorageInfo.rst#autoClaimStorage>`_ 




  Returns:
     `vim.Task <vim/Task.rst>`_:
         


RemoveDisk(disk):
   Remove the set of given disks from use by the VSAN service on this host. Users may use this API to manually remove a DiskMapping#nonSsd from a DiskMapping. This operation is only permitted if the VSAN service on this host is not configured to automatically claim storage.This method may not be used to remove the last DiskMapping#nonSsd from any given DiskMapping. Removal of the last DiskMapping#nonSsd can be accomplished by using `RemoveDiskMapping_Task <vim/host/VsanSystem.rst#removeDiskMapping>`_ .Upon successful completion of the returned `Task <vim/Task.rst>`_ , its `result <vim/TaskInfo.rst#result>`_ field will be populated with a `VsanHostDiskResult <vim/vsan/host/DiskResult.rst>`_ []. Sets DiskIsLastRemainingNonSSD fault in returned task if specified disk is the last DiskMapping#nonSsd member of DiskMapping.See `RemoveDiskMapping_Task <vim/host/VsanSystem.rst#removeDiskMapping>`_ See `UpdateVsan_Task <vim/host/VsanSystem.rst#update>`_ See `autoClaimStorage <vim/vsan/host/ConfigInfo/StorageInfo.rst#autoClaimStorage>`_ 


  Privilege:
               Host.Config.Storage



  Args:
    disk (`vim.host.ScsiDisk <vim/host/ScsiDisk.rst>`_):
       list of disks to be removed from use by the VSAN service.See `RemoveDiskMapping_Task <vim/host/VsanSystem.rst#removeDiskMapping>`_ See `UpdateVsan_Task <vim/host/VsanSystem.rst#update>`_ See `autoClaimStorage <vim/vsan/host/ConfigInfo/StorageInfo.rst#autoClaimStorage>`_ 




  Returns:
     `vim.Task <vim/Task.rst>`_:
         


RemoveDiskMapping(mapping):
   Delete given set of disk mappings from use by the VSAN service on this host. This API may be used to remove all disks in a given mapping, including its DiskMapping#ssd. This operation is only permitted if the VSAN service on this host is not configured to automatically claim storage.Upon successful completion of the returned `Task <vim/Task.rst>`_ , its `result <vim/TaskInfo.rst#result>`_ field will be populated with an empty `VsanHostDiskMapResult <vim/vsan/host/DiskMapResult.rst>`_ []. If any errors are encountered, the returned field will instead contain populated error information.See `RemoveDisk_Task <vim/host/VsanSystem.rst#removeDisk>`_ See `UpdateVsan_Task <vim/host/VsanSystem.rst#update>`_ See `autoClaimStorage <vim/vsan/host/ConfigInfo/StorageInfo.rst#autoClaimStorage>`_ 


  Privilege:
               Host.Config.Storage



  Args:
    mapping (`vim.vsan.host.DiskMapping <vim/vsan/host/DiskMapping.rst>`_):
       list of disk mappings to be removed from VSAN usage.See `RemoveDisk_Task <vim/host/VsanSystem.rst#removeDisk>`_ See `UpdateVsan_Task <vim/host/VsanSystem.rst#update>`_ See `autoClaimStorage <vim/vsan/host/ConfigInfo/StorageInfo.rst#autoClaimStorage>`_ 




  Returns:
     `vim.Task <vim/Task.rst>`_:
         


UpdateVsan(config):
   Update the VSAN service on this host according to the given host configuration specification.Enabling and disabling the VSAN service can be achieved by using the `enabled <vim/vsan/host/ConfigInfo.rst#enabled>`_ flag. Host storage settings can be specified through use of `storageInfo <vim/vsan/host/ConfigInfo.rst#storageInfo>`_ . If this value is omitted, changes will not be made to the existing storage configuration. Host cluster settings can be specified through use of `clusterInfo <vim/vsan/host/ConfigInfo.rst#clusterInfo>`_ . If this value is omitted, changes will not be made to the existing cluster configuration. Host network settings can be specified through use of `networkInfo <vim/vsan/host/ConfigInfo.rst#networkInfo>`_ . If this value is omitted, changes will not be made to the existing network configuration.See `VsanHostConfigInfo <vim/vsan/host/ConfigInfo.rst>`_ See `storageInfo <vim/vsan/host/ConfigInfo.rst#storageInfo>`_ See `clusterInfo <vim/vsan/host/ConfigInfo.rst#clusterInfo>`_ See `networkInfo <vim/vsan/host/ConfigInfo.rst#networkInfo>`_ See `QueryDisksForVsan <vim/host/VsanSystem.rst#queryDisksForVsan>`_ 


  Privilege:
               Host.Config.Storage



  Args:
    config (`vim.vsan.host.ConfigInfo <vim/vsan/host/ConfigInfo.rst>`_):
       host configuration settings to use for the VSAN service.See `VsanHostConfigInfo <vim/vsan/host/ConfigInfo.rst>`_ See `storageInfo <vim/vsan/host/ConfigInfo.rst#storageInfo>`_ See `clusterInfo <vim/vsan/host/ConfigInfo.rst#clusterInfo>`_ See `networkInfo <vim/vsan/host/ConfigInfo.rst#networkInfo>`_ See `QueryDisksForVsan <vim/host/VsanSystem.rst#queryDisksForVsan>`_ 




  Returns:
     `vim.Task <vim/Task.rst>`_:
         


QueryHostStatus():
   Queries this host's current runtime status for the VSAN service.


  Privilege:
               System.Read



  Args:


  Returns:
    `vim.vsan.host.ClusterStatus <vim/vsan/host/ClusterStatus.rst>`_:
         a populated `VsanHostClusterStatus <vim/vsan/host/ClusterStatus.rst>`_ entry


