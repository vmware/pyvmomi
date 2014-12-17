.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _childType: ../vim/Folder.rst#childType

.. _vim.Folder: ../vim/Folder.rst

.. _VI API 2.5: ../vim/version.rst#vimversionversion2

.. _DVSCreateSpec: ../vim/DistributedVirtualSwitch/CreateSpec.rst

.. _vim.Datacenter: ../vim/Datacenter.rst

.. _vim.StoragePod: ../vim/StoragePod.rst

.. _vim.HostSystem: ../vim/HostSystem.rst

.. _vSphere API 5.0: ../vim/version.rst#vimversionversion7

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _vim.ResourcePool: ../vim/ResourcePool.rst

.. _vim.fault.NoHost: ../vim/fault/NoHost.rst

.. _vim.vm.ConfigSpec: ../vim/vm/ConfigSpec.rst

.. _vim.ManagedEntity: ../vim/ManagedEntity.rst

.. _vim.fault.DvsFault: ../vim/fault/DvsFault.rst

.. _vim.VirtualMachine: ../vim/VirtualMachine.rst

.. _vim.fault.NotFound: ../vim/fault/NotFound.rst

.. _vim.fault.FileFault: ../vim/fault/FileFault.rst

.. _vim.ComputeResource: ../vim/ComputeResource.rst

.. _MoveIntoFolder_Task: ../vim/Folder.rst#moveInto

.. _vim.host.ConnectSpec: ../vim/host/ConnectSpec.rst

.. _vim.fault.OutOfBounds: ../vim/fault/OutOfBounds.rst

.. _vim.fault.InvalidName: ../vim/fault/InvalidName.rst

.. _vim.fault.InvalidState: ../vim/fault/InvalidState.rst

.. _vim.cluster.ConfigSpec: ../vim/cluster/ConfigSpec.rst

.. _vim.fault.InvalidLogin: ../vim/fault/InvalidLogin.rst

.. _vim.fault.VmWwnConflict: ../vim/fault/VmWwnConflict.rst

.. _vim.fault.AlreadyExists: ../vim/fault/AlreadyExists.rst

.. _vim.fault.InvalidFolder: ../vim/fault/InvalidFolder.rst

.. _vim.fault.VmConfigFault: ../vim/fault/VmConfigFault.rst

.. _vim.fault.DuplicateName: ../vim/fault/DuplicateName.rst

.. _vim.cluster.ConfigSpecEx: ../vim/cluster/ConfigSpecEx.rst

.. _vmodl.fault.NotSupported: ../vmodl/fault/NotSupported.rst

.. _vim.fault.SSLVerifyFault: ../vim/fault/SSLVerifyFault.rst

.. _DistributedVirtualSwitch: ../vim/DistributedVirtualSwitch.rst

.. _vim.fault.InvalidDatastore: ../vim/fault/InvalidDatastore.rst

.. _vim.fault.ConcurrentAccess: ../vim/fault/ConcurrentAccess.rst

.. _vim.ClusterComputeResource: ../vim/ClusterComputeResource.rst

.. _vim.fault.AlreadyConnected: ../vim/fault/AlreadyConnected.rst

.. _vim.fault.NotSupportedHost: ../vim/fault/NotSupportedHost.rst

.. _vim.fault.HostConnectFault: ../vim/fault/HostConnectFault.rst

.. _vim.fault.DvsNotAuthorized: ../vim/fault/DvsNotAuthorized.rst

.. _vmodl.fault.InvalidArgument: ../vmodl/fault/InvalidArgument.rst

.. _vim.fault.FileAlreadyExists: ../vim/fault/FileAlreadyExists.rst

.. _vim.fault.AgentInstallFailed: ../vim/fault/AgentInstallFailed.rst

.. _vim.DistributedVirtualSwitch: ../vim/DistributedVirtualSwitch.rst

.. _vim.fault.AlreadyBeingManaged: ../vim/fault/AlreadyBeingManaged.rst

.. _vmodl.fault.NotEnoughLicenses: ../vmodl/fault/NotEnoughLicenses.rst

.. _vim.ComputeResource.ConfigSpec: ../vim/ComputeResource/ConfigSpec.rst

.. _vim.fault.InsufficientResourcesFault: ../vim/fault/InsufficientResourcesFault.rst

.. _vim.fault.VmAlreadyExistsInDatacenter: ../vim/fault/VmAlreadyExistsInDatacenter.rst

.. _vim.DistributedVirtualSwitch.CreateSpec: ../vim/DistributedVirtualSwitch/CreateSpec.rst

.. _vim.fault.DisallowedOperationOnFailoverHost: ../vim/fault/DisallowedOperationOnFailoverHost.rst


vim.Folder
==========
  The `Folder`_ managed object is a container for storing and organizing inventory objects. Folders can contain folders and other objects. The `childType`_ property identifies a folder's type and determines the types of folders and objects the folder can contain.
   * A folder can contain a child folder of the same type as the parent folder.
   * All `Datacenter`_ objects contain dedicated folders for:
     * `VirtualMachine`_, templates, and `VirtualApp`_ objects.
     * `ComputeResource`_ hierarchies.
     * `Network`_, `DistributedVirtualSwitch`_, and `DistributedVirtualPortgroup`_ objects.
     * `Datastore`_ objects.
   * A folder can contain child objects of type `childType`_. Virtual machine and network entity folders can also contain additional object types.
   * The root folder is a data center folder.

  See `ServiceInstance`_ for a representation of the organization of the inventory.

  The Folder`_ managed object also acts as a factory object, meaning it creates new entities in a folder. The object provides methods to create child folders and objects, methods to add existing objects to folders, and methods to remove objects from folders and to delete folders.

  `Folder`_ inherits the `Destroy_Task`_ method. `Destroy_Task`_ is a recursive operation that removes all child objects and folders. When you call `Destroy_Task`_ to destroy a folder, the system uses the specified folder as a root and traverses its descendant hierarchy, calling `Destroy_Task`_ on each object. `Destroy_Task`_ is a single operation that treats each recursive call as a single transaction, committing each call to remove an object individually. If `Destroy_Task`_ fails on an object, the method terminates at that point with an exception, leaving some or all of the objects still in the inventory.

  Notes on the folder destroy method:
   * Calling `Destroy_Task`_ on a virtual machine folder recursively calls `Destroy_Task`_ on all the child virtual machines and vApps, which are then removed from disk. Use `UnregisterAndDestroy_Task`_ to unregister virtual machines or vApps recursively without removing them from the disk.
   * For virtual machine folders, the `Destroy_Task`_ method requires the VirtualMachine.Delete privilege on the folder as well as all virtual machines to be destroyed. It also requires the VirtualApp.Delete privilege on all VirtualApp objects to be destroyed.
   * Destroying a host folder or datacenter folder unregisters all child hosts and virtual machines from vCenter. The hosts are simply removed from the inventory, along with their virtual machines. The virtual machines are not removed from disk nor are their runtime states changed.
   * You can remove network and datastore folders only if they are empty.
   * You cannot destroy, rename, or move the virtual machine, compute resource, network entity, and datastore child folders of a Datacenter.


:extends: vim.ManagedEntity_


Attributes
----------
    childType ([`str`_]):
      privilege: System.View
       Specifies the object types a folder may contain. When you create a folder, it inherits its childType from the parent folder in which it is created. childType is an array of strings. Each array entry identifies a set of object types - Folder and one or more managed object types. The following list shows childType values for the different folders:
        * { "vim.Folder", "vim.Datacenter" } - Identifies the root folder and its descendant folders. Data center folders can contain child data center folders and Datacenter managed objects. Datacenter objects contain virtual machine, compute resource, network entity, and datastore folders.
        * { "vim.Folder", "vim.Virtualmachine", "vim.VirtualApp" } - Identifies a virtual machine folder. A virtual machine folder may contain child virtual machine folders. It also can contain VirtualMachine managed objects, templates, and VirtualApp managed objects.
        * { "vim.Folder", "vim.ComputeResource" } - Identifies a compute resource folder, which contains child compute resource folders and ComputeResource hierarchies.
        * { "vim.Folder", "vim.Network" } - Identifies a network entity folder. Network entity folders on a vCenter Server can contain Network, DistributedVirtualSwitch, and DistributedVirtualPortgroup managed objects. Network entity folders on an ESXi host can contain only Network objects.
        * { "vim.Folder", "vim.Datastore" } - Identifies a datastore folder. Datastore folders can contain child datastore folders and Datastore managed objects.
    childEntity ([`vim.ManagedEntity`_]):
      privilege: System.View
       An array of managed object references. Each entry is a reference to a child entity.


Methods
-------


CreateFolder(name):
   Creates a new sub-folder with the specified name. The `childType`_ property of the new folder is the same as the `childType`_ property of the current folder.Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.


  Privilege:
               Folder.Create



  Args:
    name (`str`_):
       The name to be given the new folder. An entity name must be a non-empty string of less than 80 characters. The slash (/), backslash (\) and percent (%) will be escaped using the URL syntax. For example, %2F.




  Returns:
    `vim.Folder`_:
         A reference to the new folder.

  Raises:

    `vim.fault.DuplicateName`_:
       if another object in the same folder has the target name.

    `vim.fault.InvalidName`_:
       if the name is not a valid entity name.


MoveIntoFolder(list):
   Moves a set of managed entities into this folder.This operation is typically used by clients when they implement a drag-and-drop interface to move a set of objects into a folder.This operation is transactional only with respect to each individual entity. The set of entities is moved sequentially as specified in the list, and committed one at a time. If the `MoveIntoFolder_Task`_ method fails on an object, the method terminates at that point with an exception, leaving the rest of the managed entities in their original location.The objects that can be moved into a folder depends on the folder's type (as defined by the folder's `childType`_ property). For a datacenter folder, only datacenters and datacenter folders can be moved into the folder. For a virtual machine folder, only virtual machines and virtual machine folders can be moved into the folder. For a host folder, ComputeResource objects, host folder objects, and HostSystem objects can be moved into the folder.Moving a HostSystem into a host folder creates a stand-alone host from a host that is currently part of a ClusterComputeResource. The host must be part of a ClusterComputeResource in the same datacenter and the host must be in maintenance mode. Otherwise, the operation fails.A ComputeResource with a single root resource pool is created for each HostSystem. The name of the ComputeResource is the DNS or IP address of the host. This operation moves the (physical) host resources out of a cluster. It does not move or change the ResourcePool configuration that is part of the ClusterComputeResource with which the host was associated.Note that all virtual machines associated with a host are moved with the host into the folder. If there are virtual machines that should not be moved with the host, then migrate them from the host before initiating this operation.For a HostSystem move, the privileges required are Host.Inventory.EditCluster on the source ClusterComputeResource, Host.Inventory.MoveHost on the HostSystem, and Host.Inventory.AddStandaloneHost on the target Folder.Otherwise, the privilege required for this operation varies depending on this folder's type and is checked against the source container, destination container, and the object:
    * Folder.Move if the object is a Folder
    * Datacenter.Move if the object is a Datacenter
    * Host.Inventory.MoveCluster if the object is a ComputeResource
    * VirtualMachine.Inventory.Move if the object is a virtual machine or virtual machine template
    * DVSwitch.Move if the object is a DistributedVirtualSwitch
    * Datastore.Move if the object is a datastore
    * Network.Move if the object is a network
    * If the object is a HostSystem, the privileges required are Host.Inventory.AddStandaloneHost on the folder, Host.Inventory.MoveHost on the HostSystem, and Host.Inventory.EditCluster on the host's original ComputeResource.


  Privilege:
               dynamic



  Args:
    list (`vim.ManagedEntity`_):
       The list of objects to be moved into the folder.




  Returns:
     `vim.Task`_:


  Raises:

    `vim.fault.DuplicateName`_:
       if this folder already contains an object with the specified name.

    `vim.fault.InvalidFolder`_:
       if a Folder that is a parent of this Folder is part of the list of objects.

    `vim.fault.InvalidState`_:
       if a HostSystem is not part of the same datacenter, not part of a ClusterComputeResource, or not in maintenance mode.

    `vmodl.fault.NotSupported`_:
       if the entity is being moved into a folder whose `childType`_ property is not set to the appropriate value. For example, a VirtualMachine entity cannot be moved into a folder whose ChildType property value does not contain "VirtualMachine".

    `vim.fault.DisallowedOperationOnFailoverHost`_:
       if the host is being moved out of a cluster and was configured as a failover host in that cluster. See `ClusterFailoverHostAdmissionControlPolicy`_ .

    `vim.fault.VmAlreadyExistsInDatacenter`_:
       if moving a standalone host between datacenters, and one or more of the host's virtual machines is already registered to a host in the destination datacenter.


CreateVM(config, pool, host):
   Creates a new virtual machine in the current folder and attaches it to the specified resource pool. This operation creates a virtual machine, instead of cloning a virtual machine from an existing one.The server does not support creating templates using this method. Instead, you should create templates by marking existing virtual machines as templates, or by cloning an existing virtual machine or template.This operation only works if the folder's childType includes VirtualMachine. In addition to the VirtualMachine.Inventory.Create privilege, may also require any of the following privileges depending on the properties of the virtual machine bring created:
    * VirtualMachine.Config.AddExistingDisk if including a virtual disk device that refers to an existing virtual disk file (not RDM)
    * VirtualMachine.Config.AddNewDisk if including a virtual disk device that creates a new virtual disk file (not RDM)
    * VirtualMachine.Config.RawDevice if including a raw device mapping (RDM) or SCSI passthrough device
    * VirtualMachine.Config.HostUSBDevice if including a VirtualUSB device backed by a host USB device
    * VirtualMachine.Config.AdvancedConfig if setting values in ConfigSpec.extraConfig
    * VirtualMachine.Config.SwapPlacement if setting swapPlacement
    * VirtualMachine.Config.ChangeTracking if setting changed block tracking for the virtual machine's disks.
    * Datastore.AllocateSpace required on all datastores where the virtual machine and its virtual disks will be created
    * Network.Assign required on the network which is assigned to the new virtual machine that is being created


  Privilege:
               VirtualMachine.Inventory.Create



  Args:
    config (`vim.vm.ConfigSpec`_):
       The configuration of the virtual machine hardware.


    pool (`vim.ResourcePool`_):
       The resource pool to which the virtual machine will be attached.


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

    `vim.fault.DuplicateName`_:
       if another virtual machine in the same folder already has the specified target name.

    `vim.fault.InvalidName`_:
       if the name is not a valid entity name.

    `vim.fault.InvalidDatastore`_:
       if the operation cannot be performed on the target datastores.

    `vim.fault.InsufficientResourcesFault`_:
       if this operation would violate a resource usage policy.

    `vim.fault.AlreadyExists`_:
       if the requested cfgPath (or the default cfgPath) for the virtual machine's configuration file is already loaded in the inventory.

    `vim.fault.InvalidState`_:
       if the operation is not allowed in current state of the entities involved.

    `vim.fault.FileAlreadyExists`_:
       if the requested cfgPath for the virtual machine's configuration file already exists.

    `vmodl.fault.NotSupported`_:
       if the virtual machine is being created within a folder whose `childType`_ property is not set to "VirtualMachine".

    `vim.fault.VmWwnConflict`_:
       if the WWN of the virtual machine has been used by other virtual machines.


RegisterVM(path, name, asTemplate, pool, host):
   Adds an existing virtual machine to the folder.Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.This operation only works if the folder's type is VirtualMachine. In addition to the VirtualMachine.Inventory.Register and Resource.AssignVMToPool privileges, it requires System.Read privilege on the datastore that the existing virtual machine resides on.


  Privilege:
               VirtualMachine.Inventory.Register



  Args:
    path (`str`_):
       A datastore path to the virtual machine.


    name (`str`_, optional):
       The name to be assigned to the virtual machine. If this parameter is not set, the displayName configuration parameter of the virtual machine is used. An entity name must be a non-empty string of less than 80 characters. The slash (/), backslash (\) and percent (%) will be escaped using the URL syntax. For example, %2F.


    asTemplate (`bool`_):
       Flag to specify whether or not the virtual machine should be marked as a template.


    pool (`vim.ResourcePool`_, optional):
       The resource pool to which the virtual machine should be attached. If imported as a template, this parameter is not set.


    host (`vim.HostSystem`_, optional):
       The target host on which the virtual machine will run. This parameter must specify a host that is a member of the ComputeResource indirectly specified by the pool. For a stand-alone host or a cluster with DRS, the parameter can be omitted, and the system selects a default.




  Returns:
     `vim.Task`_:
         the newly registered VirtualMachine.

  Raises:

    `vim.fault.OutOfBounds`_:
       if the maximum number of VMs for this folder has been exceeded. The maximum number is determined by Host.capability.maxSupportedVMs.

    `vim.fault.DuplicateName`_:
       if another virtual machine in the same folder has the target name.

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

    `vim.fault.InvalidState`_:
       if the operation is not allowed in current state of the entities involved.

    `vmodl.fault.NotSupported`_:
       if the operation is not supported. For example, templates are not supported directly on hosts. Also, if the operation is invoked on a folder whose `childType`_ property is not set to "VirtualMachine".

    `vmodl.fault.InvalidArgument`_:
       if any of the arguments such as host or resource pool are not set to valid values.


CreateCluster(name, spec):
   Creates a new cluster compute resource in this folder.Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.


  Privilege:
               Host.Inventory.CreateCluster



  Args:
    name (`str`_):
       Name for the new cluster.


    spec (`vim.cluster.ConfigSpec`_):
       Specification for the cluster.




  Returns:
    `vim.ClusterComputeResource`_:
         A new ClusterComputeResource instance.

  Raises:

    `vim.fault.DuplicateName`_:
       if an entity with that name already exists.

    `vim.fault.InvalidName`_:
       if the name is not a valid entity name.

    `vmodl.fault.InvalidArgument`_:
       if the cluster configuration specification parameter is invalid.

    `vmodl.fault.NotSupported`_:
       if the cluster is being added to a folder whose `childType`_ property value does not contain "ComputeResource" or "ClusterComputeResource".


CreateClusterEx(name, spec):
   Creates a new cluster compute resource in this folder.Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.
  since: `VI API 2.5`_


  Privilege:
               Host.Inventory.CreateCluster



  Args:
    name (`str`_):
       Name for the new cluster.


    spec (`vim.cluster.ConfigSpecEx`_):
       Specification for the cluster.




  Returns:
    `vim.ClusterComputeResource`_:
         A new ClusterComputeResource instance.

  Raises:

    `vim.fault.DuplicateName`_:
       if an entity with that name already exists.

    `vim.fault.InvalidName`_:
       if the name is not a valid entity name.

    `vmodl.fault.InvalidArgument`_:
       if the cluster configuration specification parameter is invalid.

    `vmodl.fault.NotSupported`_:
       if the cluster is being added to a folder whose `childType`_ property value does not contain "ComputeResource" or "ClusterComputeResource".


AddStandaloneHost(spec, compResSpec, addConnected, license):
   Creates a new single-host compute resource. The name provided can be an IP address, such as 192.168.0.120, or a string, such as esx120. If a name is specified, a DNS lookup is used to resolve it to a fully-qualified name, such as esx120.vmware.com. If the DNS lookup fails, the string is stored as specified.Licenses for the host are allocated when making the first connection to the host. This is because the license needed typically depends on the type of host and the number of CPUs.In addition to the Host.Inventory.AddStandaloneHost privilege, it requires System.View privilege on the VM folder that the VMs of the host will be placed on.


  Privilege:
               Host.Inventory.AddStandaloneHost



  Args:
    spec (`vim.host.ConnectSpec`_):
       The host name, port, and passwords for the host to be added.


    compResSpec (`vim.ComputeResource.ConfigSpec`_, optional, since `VI API 2.5`_ ):
       Optionally specify the configuration for the compute resource that will be created to contain the host.


    addConnected (`bool`_):
       Flag to specify whether or not the host should be connected as soon as it is added. The host will not be added if a connection attempt is made and fails.


    license (`str`_, optional, since `vSphere API 4.0`_ ):
       Provide a licenseKey or licenseKeyType. See `LicenseManager`_




  Returns:
     `vim.Task`_:
         the newly added ComputeResource.

  Raises:

    `vim.fault.InvalidLogin`_:
       if authentication with the host fails.

    `vim.fault.HostConnectFault`_:
       if an error occurred when attempting to connect to a host. Typically, a more specific subclass, such as AlreadyBeingManaged, is thrown.

    `vim.fault.DuplicateName`_:
       if another host in the same folder has the name.

    `vmodl.fault.InvalidArgument`_:
       if an argument is specified incorrectly.

    `vim.fault.AlreadyBeingManaged`_:
       if the host is already being managed by a vCenter server. If the host is being managed by a different vCenter server, this can be overridden by the "force" flag in the connection specification.

    `vmodl.fault.NotEnoughLicenses`_:
       if there are not enough licenses to add the host.

    `vim.fault.NoHost`_:
       if the host cannot be contacted.

    `vmodl.fault.NotSupported`_:
       if the host is being added to a folder whose `childType`_ property does not contain "ComputeResource".

    `vim.fault.NotSupportedHost`_:
       if the host is running a software version that is not supported.

    `vim.fault.AgentInstallFailed`_:
       if there is an error installing the vCenter agent on the new host.

    `vim.fault.AlreadyConnected`_:
       if addConnected is true and the host is already connected to vCenter.

    `vim.fault.SSLVerifyFault`_:
       if the host certificate could not be authenticated


CreateDatacenter(name):
   Creates a new datacenter with the given name.Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.


  Privilege:
               Datacenter.Create



  Args:
    name (`str`_):
       Name for the new datacenter. An entity name must be a non-empty string of less than 80 characters. The slash (/), backslash (\) and percent (%) will be escaped using the URL syntax. For example, %2F.




  Returns:
    `vim.Datacenter`_:
         A new Datacenter instance.

  Raises:

    `vim.fault.DuplicateName`_:
       if an entity with that name already exists.

    `vim.fault.InvalidName`_:
       if the new name is not a valid entity name.

    `vmodl.fault.NotSupported`_:
       if the datacenter is being created within a folder whose `childType`_ property value does not contain "Datacenter".


UnregisterAndDestroy():
   Recursively unregisters all virtual machines and vApps, and destroys all child virtual machine folders. This is similar to the Destroy_Task method, but this method calls UnregisterAndDestroy_Task on each virtual machine object instead of calling Destroy_Task. This operation applies only to VirtualMachine folders.UnregisterAndDestroy_Task is a recursive operation that destroys the specified virtual machine folder, unregisters all child virtual machine objects, and destroys all child virtual machine folders. When you call UnregisterAndDestroy_Task to destroy a virtual machine folder, the system uses the specified folder as a root and traverses its descendant hierarchy, calling UnregisterAndDestroy_Task on each virtual machine object and Destroy_Task on each virtual machine folder. UnregisterAndDestroy_Task is a single operation that treats each recursive call as a single transaction, committing each call to remove an object individually. If a failure occurs, the method terminates at that point with an exception, leaving some or all objects unaffected.If you are removing virtual machines, you must hold the VirtualMachine.Delete privilege on all of the virtual machines to be unregistered, and on their parent folders. If you are removing virtual applications, you must hold the VApp.Delete privilege on all of the virtual applications to be unregistered, and on their parent folders.


  Privilege:
               Folder.Delete



  Args:


  Returns:
     `vim.Task`_:


  Raises:

    `vim.fault.ConcurrentAccess`_:
       if another client modifies the folder contents before this operation completes.

    `vim.fault.InvalidState`_:
       if a virtual machine is not powered off or suspended.

    `vmodl.fault.NotSupported`_:
       if the `childType`_ property of the folder is not set to "VirtualMachine".


CreateDVS(spec):
   Create a `DistributedVirtualSwitch`_ in the folder according to the specified `DVSCreateSpec`_ . The specified Folder must be a Network entity folder.
  since: `vSphere API 4.0`_


  Privilege:
               DVSwitch.Create



  Args:
    spec (`vim.DistributedVirtualSwitch.CreateSpec`_):
       The `DVSCreateSpec`_ to create the distributed virtual switch.




  Returns:
     `vim.Task`_:
         A new DistributedVirtualSwitch instance.

  Raises:

    `vim.fault.DvsFault`_:
       vim.fault.DvsFault

    `vim.fault.DuplicateName`_:
       vim.fault.DuplicateName

    `vim.fault.InvalidName`_:
       vim.fault.InvalidName

    `vim.fault.NotFound`_:
       vim.fault.NotFound

    `vim.fault.DvsNotAuthorized`_:
       if login-session's extension key does not match ( `extensionKey`_ ).

    `vmodl.fault.NotSupported`_:
       if called directly on a host.


CreateStoragePod(name):
   Creates a new storage pod in this folder.Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.
  since: `vSphere API 5.0`_


  Privilege:
               Folder.Create



  Args:
    name (`str`_):
       Name for the new storage pod.




  Returns:
    `vim.StoragePod`_:
         A new StoragePod instance.

  Raises:

    `vim.fault.DuplicateName`_:
       if an entity with that name already exists.

    `vim.fault.InvalidName`_:
       if the name is not a valid entity name.

    `vmodl.fault.NotSupported`_:
       if the storage pod is being added to a folder whose `childType`_ property value does not contain "StoragePod".


