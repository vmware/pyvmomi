
vim.StorageResourceManager
==========================
  This managed object type provides a way to configure resource usage for storage resources.


:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_


Attributes
----------


Methods
-------


ConfigureDatastoreIORM(datastore, spec):
   Changes configuration of storage I/O resource management for a given datastore. The changes are applied to all the backing storage devices for the datastore. Currently we only support storage I/O resource management on VMFS volumes. In order to enable storage I/O resource management on a datstore, we require that all the hosts that are attached to the datastore support this feature.This method is only supported by vCenter server.


  Privilege:



  Args:
    datastore (`vim.Datastore <vim/Datastore.rst>`_):
       The datastore to be configured.


    spec (`vim.StorageResourceManager.IORMConfigSpec <vim/StorageResourceManager/IORMConfigSpec.rst>`_):
       The configuration spec.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.IORMNotSupportedHostOnDatastore <vim/fault/IORMNotSupportedHostOnDatastore.rst>`_: 
       if called on a datastore that is connected to a host that does not support storage I/O resource management.

    `vim.fault.InaccessibleDatastore <vim/fault/InaccessibleDatastore.rst>`_: 
       if cannot access the datastore from any of the hosts.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if called directly on a host or if called on a datastore that does not have VMFS Volume.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if 1. IORMConfigSpec.congestionThreshold is not within the desired range (5 to 100 milliseconds). 2. IORMConfigSpec.congestionThresholdMode is not specified and IORMConfigSpec.congestionThreshold is specified. To set congestionThreshold, congestionThresholdMode should be set to manual


QueryIORMConfigOption(host):
   Query configuration options for storage I/O resource management.


  Privilege:
               Datastore.Config



  Args:
    host (`vim.HostSystem <vim/HostSystem.rst>`_):
       [in] - The host VC will forward the query to. This parameter is ignored by host if this method is called on a host directly.




  Returns:
    `vim.StorageResourceManager.IORMConfigOption <vim/StorageResourceManager/IORMConfigOption.rst>`_:
         configuration option object.


QueryDatastorePerformanceSummary(datastore):
   Returns datastore summary performance statistics.This is an experimental interface that is not intended for use in production code.
  since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_


  Privilege:
               System.View



  Args:
    datastore (`vim.Datastore <vim/Datastore.rst>`_):
       Datastore for which summary statistics is requested.




  Returns:
    [`vim.StorageResourceManager.StoragePerformanceSummary <vim/StorageResourceManager/StoragePerformanceSummary.rst>`_]:
         Summary performance statistics for the datastore. The summary contains latency, throughput, and SIOC activity.

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if input datastore cannot be found


ApplyStorageDrsRecommendationToPod(pod, key):
   Applies a recommendation from the recommendation list. Each recommendation can be applied only once.Requires Resource.ApplyRecommendation privilege on the storage pod. And requires Resource.ColdMigrate privilege on the virtual machine(s) that are relocated. Additionally requires Resource.HotMigrate privilege if the virtual machine is powered on (for Storage VMotion). Also requires Datastore.AllocateSpace on any datastore the virtual machine or its disks are relocated to.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               System.View



  Args:
    pod (`vim.StoragePod <vim/StoragePod.rst>`_):
       The storage pod.


    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The key field of the Recommendation.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       If the specified key refers to a non-existent or an already executed recommendation.


ApplyStorageDrsRecommendation(key):
   Applies a recommendation from the recommendation list. Each recommendation can be applied only once. In the case of CreateVm and CloneVm a VirtualMachine is returned. Other workflows don't have a return value.Requires Resource.ApplyRecommendation privilege on the storage pod. Additionally, depending on the workflow where this API is called from, it may require the privileges of invoking one of following APIs:
    * CreateVm
    * `CreateVM_Task <vim/Folder.rst#createVm>`_
    * AddDisk
    * `ReconfigVM_Task <vim/VirtualMachine.rst#reconfigure>`_
    * RelocateVm
    * `RelocateVM_Task <vim/VirtualMachine.rst#relocate>`_
    * CloneVm
    * `CloneVM_Task <vim/VirtualMachine.rst#clone>`_
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               System.View



  Args:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The key fields of the Recommendations that are applied.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       If the specified key refers to a non-existent or an already executed recommendation.


CancelStorageDrsRecommendation(key):
   Cancels a recommendation. Currently only initial placement recommendations can be cancelled. Migration recommendations cannot.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               System.View



  Args:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The key field of the Recommendation.




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       If the specified key refers to a non-existent or an already executed recommendation.


RefreshStorageDrsRecommendation(pod):
   Make Storage DRS invoke again on the specified pod `StoragePod <vim/StoragePod.rst>`_ and return a new list of recommendations. Concurrent "refresh" requests may be combined together and trigger only one Storage DRS invocation.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               System.View



  Args:
    pod (`vim.StoragePod <vim/StoragePod.rst>`_):
       The storage pod. The recommendations generated is stored at PodStorageDrsEntry#recommendation.




  Returns:
    None
         


ConfigureStorageDrsForPod(pod, spec, modify):
   Change the storage DRS configuration for a pod `StoragePod <vim/StoragePod.rst>`_ .
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:



  Args:
    pod (`vim.StoragePod <vim/StoragePod.rst>`_):
       The storage pod.


    spec (`vim.storageDrs.ConfigSpec <vim/storageDrs/ConfigSpec.rst>`_):
       A set of storage Drs configuration changes to apply to the storage pod. The specification can be a complete set of changes or a partial set of changes, applied incrementally.


    modify (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       Flag to specify whether the specification ("spec") should be applied incrementally. If "modify" is false and the operation succeeds, then the configuration of the storage pod matches the specification exactly; in this case any unset portions of the specification will result in unset or default portions of the configuration.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         


RecommendDatastores(storageSpec):
   This method returns a `StoragePlacementResult <vim/storageDrs/StoragePlacementResult.rst>`_ object. This API is intended to replace the following existing APIs for SDRS-enabled pods: CreateVm: StoragePlacementSpec::type == create = `CreateVM_Task <vim/Folder.rst#createVm>`_ AddDisk: StoragePlacementSpec::type == reconfigure = `ReconfigVM_Task <vim/VirtualMachine.rst#reconfigure>`_ RelocateVm: StoragePlacementSpec::type == relocate = `RelocateVM_Task <vim/VirtualMachine.rst#relocate>`_ CloneVm: StoragePlacementSpec::type == clone = `CloneVM_Task <vim/VirtualMachine.rst#clone>`_ The PodSelectionSpec parameter in StoragePlacementSpec is required for all workflows. It specifies which SDRS-enabled pod the user has selected for the VM and/or for each disk. For CreateVm, RelocateVm and CloneVm, PodSelectionSpec.storagePod is the user selected SDRS pod for the VM, i.e., its system files. For all workflows, PodSelectionSpec.disk.storagePod is the user selected SDRS pod for the given disk. Note that a DiskLocator must be specified for each disk that the user requests to create, migrate or clone into an SDRS pod, even if it's the same pod as the VM or the user has manually selected a datastore within the pod. If the user has manually selected a datastore, the datastore must be specified in the workflow specific fields as described below. For CreateVm and AddDisk, the manually selected datastore must be specified in ConfigSpec.files or ConfigSpec.deviceChange.device.backing.datastore, the fields should will be unset if the user wants SDRS to recommend the datastore. For RelocateVm, the manually selected datastore must be specified in RelocateSpec.datastore or RelocateSpec.disk.datastore; the fields should be unset iff the user wants SDRS recommendations. For CloneVm, the manually selected datastore must be specified in CloneSpec.location.datastore or CloneSpec.location.disk[].datastore; the fields should be unset iff the user wants SDRS recommendations. The remaining expected input parameters in StoragePlacementSpec will be the same as those for the existing API as determined by StoragePlacementSpec::type. If a parameter is optional in the existing API, it will also be optional in the new API.
    * For CreateVm, the Folder, ConfigSpec, ResourcePool and HostSystem parameters will be expected in StoragePlacementSpec. The disks to be created can be determined by ConfigSpec -
    * VirtualDeviceSpec[] (deviceChange) -
    * VirtualDevice (device) -
    * VirtualDisk (subclass).
    * For AddDisk, the VirtualMachine and ConfigSpec parameters will be expected. The use of the ConfigSpec for determining the disks to add will be the same as that in CreateVm.
    * For RelocateVm, the VirtualMachine, RelocateSpec and MovePriority parameters will be expected.
    * For CloneVm, the VirtualMachine, CloneSpec, Folder and cloneName parameters will be expected.
    * SDRS takes into account constraints such as space usages, (anti-) affinity rules, datastore maintenance mode, etc. when making placement recommendations. Given that the constraints are satisfied, SDRS tries to balance space usages and I/O loads in the placement.
    * 
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               System.View



  Args:
    storageSpec (`vim.storageDrs.StoragePlacementSpec <vim/storageDrs/StoragePlacementSpec.rst>`_):




  Returns:
    `vim.storageDrs.StoragePlacementResult <vim/storageDrs/StoragePlacementResult.rst>`_:
         


