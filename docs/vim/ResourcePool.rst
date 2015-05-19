.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vApp: ../vim/VirtualApp.rst

.. _info: ../vim/HttpNfcLease.rst#info

.. _state: ../vim/HttpNfcLease.rst#state

.. _Folder: ../vim/Folder.rst#createVm

.. _vim.Task: ../vim/Task.rst

.. _vim.Folder: ../vim/Folder.rst

.. _HttpNfcLease: ../vim/HttpNfcLease.rst

.. _UpdateConfig: ../vim/ResourcePool.rst#updateConfig

.. _CreateVM_Task: ../vim/Folder.rst#createVm

.. _RefreshRuntime: ../vim/ResourcePool.rst#refreshRuntime

.. _vim.ImportSpec: ../vim/ImportSpec.rst

.. _vim.HostSystem: ../vim/HostSystem.rst

.. _vim.VirtualApp: ../vim/VirtualApp.rst

.. _RegisterVM_Task: ../vim/Folder.rst#registerVm

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _vSphere API 4.1: ../vim/version.rst#vimversionversion6

.. _vim.HttpNfcLease: ../vim/HttpNfcLease.rst

.. _vim.ResourcePool: ../vim/ResourcePool.rst

.. _HttpNfcLeaseAbort: ../vim/HttpNfcLease.rst#abort

.. _vim.vm.ConfigSpec: ../vim/vm/ConfigSpec.rst

.. _vim.ManagedEntity: ../vim/ManagedEntity.rst

.. _vim.VirtualMachine: ../vim/VirtualMachine.rst

.. _vim.fault.NotFound: ../vim/fault/NotFound.rst

.. _ResourceConfigSpec: ../vim/ResourceConfigSpec.rst

.. _vim.fault.FileFault: ../vim/fault/FileFault.rst

.. _vim.ComputeResource: ../vim/ComputeResource.rst

.. _HttpNfcLeaseProgress: ../vim/HttpNfcLease.rst#progress

.. _HttpNfcLeaseComplete: ../vim/HttpNfcLease.rst#complete

.. _vim.fault.InvalidName: ../vim/fault/InvalidName.rst

.. _vim.fault.OutOfBounds: ../vim/fault/OutOfBounds.rst

.. _vim.fault.InvalidState: ../vim/fault/InvalidState.rst

.. _vim.ResourceConfigSpec: ../vim/ResourceConfigSpec.rst

.. _vim.fault.VmWwnConflict: ../vim/fault/VmWwnConflict.rst

.. _vim.vApp.VAppConfigSpec: ../vim/vApp/VAppConfigSpec.rst

.. _ResourcePoolRuntimeInfo: ../vim/ResourcePool/RuntimeInfo.rst

.. _vim.fault.AlreadyExists: ../vim/fault/AlreadyExists.rst

.. _vim.fault.VmConfigFault: ../vim/fault/VmConfigFault.rst

.. _vim.fault.DuplicateName: ../vim/fault/DuplicateName.rst

.. _vim.ResourceConfigOption: ../vim/ResourceConfigOption.rst

.. _vmodl.fault.NotSupported: ../vmodl/fault/NotSupported.rst

.. _vim.ResourcePool.Summary: ../vim/ResourcePool/Summary.rst

.. _ResourcePoolResourceUsage: ../vim/ResourcePool/ResourceUsage.rst

.. _vim.fault.InvalidDatastore: ../vim/fault/InvalidDatastore.rst

.. _vim.fault.ConcurrentAccess: ../vim/fault/ConcurrentAccess.rst

.. _vmodl.fault.InvalidArgument: ../vmodl/fault/InvalidArgument.rst

.. _vim.fault.FileAlreadyExists: ../vim/fault/FileAlreadyExists.rst

.. _vim.ResourcePool.RuntimeInfo: ../vim/ResourcePool/RuntimeInfo.rst

.. _vim.fault.InsufficientResourcesFault: ../vim/fault/InsufficientResourcesFault.rst


vim.ResourcePool
================
  Represents a set of physical resources: a single host, a subset of a host's resources, or resources spanning multiple hosts. Resource pools can be subdivided by creating child resource pools. In order to run, a virtual machine must be associated as a child of a resource pool.In a parent/child hierarchy of resource pools and virtual machines, the single resource pool that has no parent pool is known as theroot resource pool.ConfigurationA resource pool is configured with a set of CPU (in MHz) and memory (in MB) resources. These resources are specified in absolute terms with a resource reservation and a resource limit, along with a shares setting. The shares are used during resource contention, to ensure graceful degradation.For the root resource pool, the values of the reservation and the limit are set by the system and are not configurable. The reservation and limit are set to the same value, indicating the total amount of resources the system has available to run virtual machines. This is computed as the aggregated CPU and memory resources provided by the set of current available hosts in the parent compute resource minus the overhead of the virtualization layer.Since the resource pool configuration is absolute (in MHz or MB), the configuration can become invalid when resources are removed. This can happen if a host is removed from the cluster, if a host becomes unavailable, or if a host is placed in maintenance mode. When this happens, the system flags misconfigured resource pools and displays the reservations and limits that are in effect. Further, in a DRS enabled cluster, the tree can be misconfigured if the user bypasses VirtualCenter and powers on VMs directly on the host.A General Discussion of Resource pool states and admission controlThere are three states that the resource pool tree can be in: undercommited (green), overcommited (yellow), and inconsistent (red). Depending on the state, different resource pool configuration policies are enforced. The states are described in more detail below:
   * 
   * GREEN (aka undercommitted)
   * : We have a tree that is in a
   * good
   * state. Every node has a reservation greater than the sum of the reservations for its children. We have enough capacity at the root to satisfy all the resources reserved by the children. All operations performed on the tree, such as powering on virtual machines, creating new resource pools, or reconfiguring resource settings, will ensure that the above constraints are maintained.
   * 
   * RED (aka. inconsistent)
   * : One or more nodes in the tree has children whose reservations are greater than the node is configured to support. For example, i) a resource pool with a fixed reservation has a running virtual machine with a reservation that is higher than the reservation on resource pool itself., or ii) the child reservations are greater than the limit.
   * In this state, the DRS algorithm is disabled until the resource pool tree's configuration has been brought back into a consistent state. We also restrict the resources that such invalid nodes request from their parents to the configured reservation/limit, in an attempt to isolate the problem to a small subtree. For the rest of the tree, we determine whether the cluster is undercommitted or overcommitted according to the existing rules and perform admission control accordingly.
   * Note that since all changes to the resource settings are validated on the VirtualCenter server, the system cannot be brought into this state by simply manipulating a cluster resource pool tree through VirtualCenter. It can only happen if a virtual machine gets powered on directly on a host that is part of a DRS cluster.
   * 
   * YELLOW (aka overcommitted)
   * : In this state, the tree is consistent internally, but the root resource pool does not have the capacity at to meet the reservation of its children. We can only go from GREEN -
   * YELLOW if we lose resources at the root. For example, hosts becomes unavailable or is put into maintenance mode. Note that we will always have enough capacity at the root to run all currently powered on VMs. However, we may not be able to satisfy all resource pool reservations in the tree. In this state, the reservation configured for a resource pool is no longer guaranteed, but the limits are still enforced. This provides additional flexibility for bringing the tree back into a consistent state, without risking bringing the tree into a RED state. In more detail:
   * 
   * 
   * Resource Pool
   * The root is considered to have unlimited capacity. You can reserve resources without any check except the requirement that the tree remains consistent. This means that nodes whose parents are all configured with expandable reservations and no limit will have unlimited available resources. However, if there is an ancestor with a fixed reservation or an expandable reservation with a limit somewhere, then the node will be limited by the reservation/limit of the ancestor.
   * 
   * Virtual Machine
   * Virtual machines are limited by ancestors with a fixed reservation and the capacity at the root.Destroying a ResourcePoolWhen a ResourcePool is destroyed, all the virtual machines are reassigned to its parent pool. The root resource pool cannot be destroyed, and invoking destroy on it will throw an InvalidType fault.Any vApps in the ResourcePool will be moved to the ResourcePool's parent before the pool is destroyed.The Resource.DeletePool privilege must be held on the pool as well as the parent of the resource pool. Also, the Resource.AssignVMToPool privilege must be held on the resource pool's parent pool and any virtual machines that are reassigned.


:extends: vim.ManagedEntity_


Attributes
----------
    summary (`vim.ResourcePool.Summary`_):
       Basic information about a resource pool. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.
    runtime (`vim.ResourcePool.RuntimeInfo`_):
       Runtime information about a resource pool. The `ResourcePoolResourceUsage`_ information within `ResourcePoolRuntimeInfo`_ can be transiently stale. Use `RefreshRuntime`_ method to update the information. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.
    owner (`vim.ComputeResource`_):
      privilege: System.View
       The ComputeResource to which this set of one or more nested resource pools belong.
    resourcePool ([`vim.ResourcePool`_]):
      privilege: System.View
       The set of child resource pools.
    vm ([`vim.VirtualMachine`_]):
      privilege: System.View
       The set of virtual machines associated with this resource pool.
    config (`vim.ResourceConfigSpec`_):
       Configuration of this resource pool.
    childConfiguration ([`vim.ResourceConfigSpec`_]):
       The resource configuration of all direct children (VirtualMachine and ResourcePool) of this resource group.


Methods
-------


UpdateConfig(name, config):
   Updates the configuration of the resource pool.Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.The privilege checks for this operation are as follows:
    * If this is a resource pool, the privilege Resource.EditPool is required on this and on the parent pool or vApp.
    * If this is a vApp, the privilege VApp.ResourceConfig is required on this and on the parent pool or vApp.


  Privilege:
               dynamic



  Args:
    name (`str`_, optional):
       If set, then the new name of the resource pool.


    config (`vim.ResourceConfigSpec`_, optional):
       If set, then the new resource allocation for this resource pool.




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidName`_: 
       if the name is not a valid entity name.

    `vim.fault.DuplicateName`_: 
       if the name is changed to an already existing name.

    `vim.fault.InsufficientResourcesFault`_: 
       if the pool specification cannot be supported by the parent resource pool or vApp.

    `vim.fault.ConcurrentAccess`_: 
       if the changeVersion does not match the server's changeVersion for the configuration.

    `vmodl.fault.InvalidArgument`_: 
       if the parameters are out of range, or if the reservationLimit field is set.


MoveIntoResourcePool(list):
   Moves a set of resource pools, vApps or virtual machines into this pool. The pools, vApps and virtual machines must be part of the cluster or standalone host that contains this pool.For each entity being moved, the move is subject to the following privilege checks:
    * If the object being moved is a ResourcePool, then Resource.MovePool must be held on the pool being moved and it's former parent pool or vApp. If the target is a vApp, the privilege VApp.AssignResourcePool must be held on it. If the target is a ResourcePool, Resource.MovePool must be held on it.
    * If the object being moved is a VirtualApp, VApp.Move must be held on the vApp being moved and it's former parent pool or vApp. If the target entity is a resource pool, Resource.AssignVAppToPool must be held on the target. If the target is a vApp, the privilege VApp.AssignVApp must be held on the target vApp.
    * If the object being moved is a VirtualMachine, then if the target is a ResourcePool, Resource.AssignVMToPool is required on the VirtualMachine and the target pool. If the target is a vApp, VApp.AssignVM is required on both the VirtualMachine and the target pool.This operation is typically used by clients when they implement a drag-and-drop interface to move a set of objects into a folder.This operation is only transactional with respect to each individual entity. The set of entities is moved sequentially, as specified in the list, and committed one at a time. If a failure is detected, then the method terminates with an exception.The root resource pool cannot be moved.


  Privilege:
               dynamic



  Args:
    list (`vim.ManagedEntity`_):
       A list of ResourcePool and VirtualMachine objects.




  Returns:
    None
         

  Raises:

    `vim.fault.DuplicateName`_: 
       if this pool already contains an object with the given name.

    `vim.fault.InsufficientResourcesFault`_: 
       if the move would violate the resource usage policy. Typically, a more specific subclass, such as InsufficientMemoryResourcesFault.

    `vmodl.fault.InvalidArgument`_: 
       if an ancestor of this pool is in the list.


UpdateChildResourceConfiguration(spec):
   Changes resource configuration of a set of children of this resource pool. The method allows bulk modifications of the set of the direct children (virtual machines and resource pools).Bulk modifications are not transactional. Each modification is made individually. If a failure is encountered while applying the changes, then the processing stops, meaning at least one and as many as all of the changes are not applied.A set can include a subset of the resources. Children that are not mentioned in the list are not changed.For each ResourceConfigSpec, the following privilege checks apply:
    * If the ResourceConfigSpec refers to a child resource pool or a child vApp, the privileges required are the same as would be required for calling
    * `UpdateConfig`_
    * on that entity.
    * If the ResourceConfigSpec refers to a virtual machine, VirtualMachine.Config.Resource must be held on the virtual machine.


  Privilege:
               dynamic



  Args:
    spec (`vim.ResourceConfigSpec`_):




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState`_: 
       vim.fault.InvalidState

    `vim.fault.InsufficientResourcesFault`_: 
       if the operation would violate a resource usage policy. Typically, a more specific subclass, such as InsufficientMemoryResourcesFault will be thrown.

    `vmodl.fault.InvalidArgument`_: 
       if a managed entity that is not a child of this group is included.


CreateResourcePool(name, spec):
   Creates a new resource pool.In the ResourceConfigSpec, all values in ResourceAllocationInfo must be supplied; they are not optional.Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.


  Privilege:
               Resource.CreatePool



  Args:
    name (`str`_):


    spec (`vim.ResourceConfigSpec`_):




  Returns:
    `vim.ResourcePool`_:
         

  Raises:

    `vim.fault.InvalidName`_: 
       if the name is not a valid entity name.

    `vim.fault.DuplicateName`_: 
       if this pool already contains an object with the given name.

    `vim.fault.InsufficientResourcesFault`_: 
       if the operation would violate a resource usage policy. Typically, a more specific subclass, such as InsufficientCpuResourcesFault will be thrown.

    `vmodl.fault.NotSupported`_: 
       if the ComputeResource does not support nested resource pools.

    `vmodl.fault.InvalidArgument`_: 
       if the pool specification is invalid.


DestroyChildren():
   Removes all child resource pools recursively. All virtual machines and vApps associated with the child resource pools get associated with this resource pool.Note that resource pools contained in child vApps are not affected.The privilege checks performed are the following.
    * Resource.DeletePool privilege must be held on this object and each of it's immediate children to be destroyed.
    * If VMs are being moved, the privilege Resource.AssignVMToPool must be held on this resource pool as well as on any virtual machines being moved.
    * If vApps are being moved, the privilege Resource.AssignVAppToPool must be held on this resource pool as well as on any vApps being moved.


  Privilege:
               dynamic



  Args:


  Returns:
    None
         


CreateVApp(name, resSpec, configSpec, vmFolder):
   Creates a new vApp container.Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.
  since: `vSphere API 4.0`_


  Privilege:
               VApp.Create



  Args:
    name (`str`_):
       The name of the vApp container in the inventory


    resSpec (`vim.ResourceConfigSpec`_):
       The resource configuration for the vApp container (same as for a regular resource pool).


    configSpec (`vim.vApp.VAppConfigSpec`_):
       The specification of the vApp specific meta-data.


    vmFolder (`vim.Folder`_, optional):
       The parent folder for the vApp. This must be null if this is a child vApp.




  Returns:
    `vim.VirtualApp`_:
         The created vApp object.

  Raises:

    `vim.fault.InvalidName`_: 
       if the name is not a valid entity name.

    `vim.fault.DuplicateName`_: 
       if this pool already contains an object with the given name.

    `vim.fault.InsufficientResourcesFault`_: 
       if the operation would violate a resource usage policy. Typically, a more specific subclass, such as InsufficientCpuResourcesFault will be thrown.

    `vim.fault.InvalidState`_: 
       if the resource pool does not support the operation in its current state. This will typically be a subclass such as `NoActiveHostInCluster`_ .

    `vim.fault.VmConfigFault`_: 
       or a more specific subclass, if errors are found in the supplied in VApp configuration.

    `vmodl.fault.NotSupported`_: 
       if the ComputeResource does not support nested resource pools.

    `vmodl.fault.InvalidArgument`_: 
       if the pool specification is invalid.


CreateChildVM(config, host):
   Creates a new virtual machine in a vApp container.This method supports creating a virtual machine directly in a vApp. A virtual machine in a vApp is not associated with a VM folder and therefore cannot be created using the method on a `Folder`_ .This method can only be called directly on a `vApp`_ or on a resource pool that is a child of a vApp.The privilege VirtualMachine.Inventory.Create is required on this entity. Further, if this is a resource pool, the privilege Resource.AssignVMToPool is required. If this is a vApp, the privilege VApp.AssignVM is required.Depending on the properties of the virtual machine bring created, additional privileges may be required. See `CreateVM_Task`_ for a description of these privileges.
  since: `vSphere API 4.0`_


  Privilege:
               VirtualMachine.Inventory.Create



  Args:
    config (`vim.vm.ConfigSpec`_):
       The configuration of the virtual machine hardware.


    host (`vim.HostSystem`_, optional):
       The target host on which the virtual machine will run. This must specify a host that is a member of the ComputeResource indirectly specified by the pool. For a stand-alone host or a cluster with DRS, host can be omitted, and the system selects a default.




  Returns:
     `vim.Task`_:
         the newly created VirtualMachine.

  Raises:

    `vim.fault.VmConfigFault`_: 
       if the configSpec has incorrect values. Typically, a more specific subclass is thrown.

    `vim.fault.FileFault`_: 
       if there is a problem creating the virtual machine on disk. Typically, a more specific subclass, such as NoDiskSpace, will be thrown.

    `vim.fault.OutOfBounds`_: 
       if Host.capability.maxSupportedVMs is exceeded.

    `vim.fault.InvalidName`_: 
       if the name is not a valid entity name.

    `vim.fault.InvalidDatastore`_: 
       if the operation cannot be performed on the target datastores.

    `vim.fault.InsufficientResourcesFault`_: 
       if this operation would violate a resource usage policy.

    `vim.fault.FileAlreadyExists`_: 
       if the requested cfgPath for the virtual machine's configuration file already exists.

    `vim.fault.VmWwnConflict`_: 
       if the WWN of the virtual machine has been used by other virtual machines.

    `vmodl.fault.NotSupported`_: 
       if this resource pool is not a vApp or is a child of a vApp.


RegisterChildVM(path, name, host):
   Adds an existing virtual machine to this resource pool or vApp.This operation only works for vApps or resource pools that are children of vApps. To register a VM in a folder, see `RegisterVM_Task`_ .Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter. In addition to the VirtualMachine.Inventory.Register privilege, it requires System.Read privilege on the datastore that the existing virtual machine resides on.
  since: `vSphere API 4.0`_


  Privilege:
               VirtualMachine.Inventory.Register



  Args:
    path (`str`_):
       A datastore path to the virtual machine. If the path ends with ".vmtx", indicating that it refers to a VM template, an InvalidArgument fault is thrown.


    name (`str`_, optional):
       The name to be assigned to the virtual machine. If this parameter is not set, the displayName configuration parameter of the virtual machine is used. An entity name must be a non-empty string of less than 80 characters. The slash (/), backslash (\) and percent (%) will be escaped using the URL syntax. For example, %2F.


    host (`vim.HostSystem`_, optional):
       The target host on which the virtual machine will run. This parameter must specify a host that is a member of the ComputeResource to which this resource pool belongs. For a stand-alone host or a cluster with DRS, the parameter can be omitted, and the system selects a default.




  Returns:
     `vim.Task`_:
         the newly registered VirtualMachine.

  Raises:

    `vim.fault.OutOfBounds`_: 
       if the maximum number of VMs has been exceeded.

    `vim.fault.AlreadyExists`_: 
       if the virtual machine is already registered.

    `vim.fault.InvalidDatastore`_: 
       if the operation cannot be performed on the target datastores.

    `vim.fault.NotFound`_: 
       if the configuration file is not found on the system.

    `vim.fault.InvalidName`_: 
       if the entity name is invalid.

    `vim.fault.VmConfigFault`_: 
       if the format / configuration of the virtual machine is invalid. Typically, a more specific fault is thrown such as InvalidFormat if the configuration file cannot be read, or InvalidDiskFormat if the disks cannot be read.

    `vim.fault.InsufficientResourcesFault`_: 
       if this operation would violate a resource usage policy.

    `vim.fault.FileFault`_: 
       if there is an error accessing the files on disk.

    `vmodl.fault.NotSupported`_: 
       if the operation is not supported. For example, if the operation is invoked on a resource pool that is unrelated to a vApp.

    `vmodl.fault.InvalidArgument`_: 
       if any of the arguments are invalid and a more specific fault type does not apply.


ImportVApp(spec, folder, host):
   Creates a new entity in this resource pool. The import process consists of two steps:
    * Create the VMs and/or vApps that make up the entity.
    * Upload virtual disk contents.In step 1, the client must wait for the server to create all inventory objects. It does that by monitoring the `state`_ property on the `HttpNfcLease`_ object returned from this call. When the server is done creating objects, the lease will change to the ready state, and step 2 begins. If an error occurs while the server is creating inventory objects, the lease will change to the error state, and the import process is aborted.In step 2, the client uploads disk contents using the URLs provided in the `info`_ property of the lease. The client must call `HttpNfcLeaseProgress`_ on the lease periodically to keep the lease alive and report progress to the server. Failure to do so will cause the lease to time out, and the import process will be aborted.When the client is done uploading disks, it completes the lease by calling `HttpNfcLeaseComplete`_ . The client can also abort the import process by calling `HttpNfcLeaseAbort`_ .If the import process fails, is aborted, or times out, all created inventory objects are removed, including all virtual disks.This operation only works if the folder's childType includes VirtualMachine.Depending on the properties of the virtual machine bring imported, additional privileges may be required. See `CreateVM_Task`_ for a description of these privileges.
  since: `vSphere API 4.0`_


  Privilege:
               VApp.Import



  Args:
    spec (`vim.ImportSpec`_):
       An `ImportSpec`_ describing what to import.


    folder (`vim.Folder`_, optional):
       The folder to which the entity will be attached.


    host (`vim.HostSystem`_, optional):
       The target host on which the entity will run. This must specify a host that is a member of the ComputeResource indirectly specified by the pool. For a stand-alone host or a cluster with DRS, host can be omitted, and the system selects a default.




  Returns:
    `vim.HttpNfcLease`_:
         a `HttpNfcLease`_ object which is used to drive the import session.

  Raises:

    `vim.fault.VmConfigFault`_: 
       if a VM configSpec has incorrect values. Typically, a more specific subclass is thrown.

    `vim.fault.FileFault`_: 
       if there is a problem creating the virtual machine on disk. Typically, a more specific subclass, such as NoDiskSpace, will be thrown.

    `vim.fault.OutOfBounds`_: 
       if Host.capability.maxSupportedVMs is exceeded.

    `vim.fault.DuplicateName`_: 
       if another virtual machine in the same folder already has the specified target name.

    `vim.fault.InvalidName`_: 
       if the name is not a valid entity name.

    `vim.fault.InvalidDatastore`_: 
       if the operation cannot be performed on the target datastores.

    `vim.fault.InsufficientResourcesFault`_: 
       if this operation would violate a resource usage policy.

    `vim.fault.FileAlreadyExists`_: 
       if the requested cfgPath for the virtual machine's configuration file already exists.

    `vmodl.fault.NotSupported`_: 
       if the virtual machine is being created within a folder whose `childType`_ property is not set to "VirtualMachine", a vApp is being imported into a resource pool that does not support nested resource pools, or a virtual machine is being imported into a resource pool and no folder is given.

    `vim.fault.VmWwnConflict`_: 
       if the WWN of the virtual machine has been used by other virtual machines.


QueryResourceConfigOption():
   Get a value range and default values for `ResourceConfigSpec`_ .
  since: `vSphere API 4.1`_


  Privilege:
               Resource.EditPool



  Args:


  Returns:
    `vim.ResourceConfigOption`_:
          `ResourceConfigOption`_ object.


RefreshRuntime():
   Refreshes the resource usage data that is available in `ResourcePoolRuntimeInfo`_ . The latest runtime resource usage of this resource pool may not be available immediately after operations that alter resource usage, such as powering on a virtual machine. Invoke this method when resource usage may have recently changed, and the most up-to-date value in the `ResourcePoolRuntimeInfo`_ is needed.
  since: `vSphere API 4.1`_


  Privilege:
               System.View



  Args:


  Returns:
    None
         


