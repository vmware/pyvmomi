.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _vim.Folder: ../vim/Folder.rst

.. _vim.Network: ../vim/Network.rst

.. _HttpNfcLease: ../vim/HttpNfcLease.rst

.. _vim.Datastore: ../vim/Datastore.rst

.. _VAppCloneSpec: ../vim/vApp/CloneSpec.rst

.. _VAppConfigSpec: ../vim/vApp/VAppConfigSpec.rst

.. _vim.VirtualApp: ../vim/VirtualApp.rst

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _vSphere API 4.1: ../vim/version.rst#vimversionversion6

.. _vim.HttpNfcLease: ../vim/HttpNfcLease.rst

.. _vim.ResourcePool: ../vim/ResourcePool.rst

.. _vim.ManagedEntity: ../vim/ManagedEntity.rst

.. _vim.vApp.CloneSpec: ../vim/vApp/CloneSpec.rst

.. _vim.fault.FileFault: ../vim/fault/FileFault.rst

.. _vim.fault.InvalidName: ../vim/fault/InvalidName.rst

.. _vim.fault.InvalidState: ../vim/fault/InvalidState.rst

.. _vim.vApp.VAppConfigInfo: ../vim/vApp/VAppConfigInfo.rst

.. _vim.VirtualApp.LinkInfo: ../vim/VirtualApp/LinkInfo.rst

.. _vim.vApp.VAppConfigSpec: ../vim/vApp/VAppConfigSpec.rst

.. _vim.fault.VmConfigFault: ../vim/fault/VmConfigFault.rst

.. _vim.fault.DuplicateName: ../vim/fault/DuplicateName.rst

.. _vim.fault.MigrationFault: ../vim/fault/MigrationFault.rst

.. _vim.fault.TaskInProgress: ../vim/fault/TaskInProgress.rst

.. _vmodl.fault.NotSupported: ../vmodl/fault/NotSupported.rst

.. _vim.fault.VAppConfigFault: ../vim/fault/VAppConfigFault.rst

.. _vim.fault.InvalidDatastore: ../vim/fault/InvalidDatastore.rst

.. _vim.fault.ConcurrentAccess: ../vim/fault/ConcurrentAccess.rst

.. _vmodl.fault.InvalidArgument: ../vmodl/fault/InvalidArgument.rst

.. _vim.fault.InvalidPowerState: ../vim/fault/InvalidPowerState.rst

.. _vmodl.fault.NotEnoughLicenses: ../vmodl/fault/NotEnoughLicenses.rst

.. _vim.fault.InvalidIndexArgument: ../vim/fault/InvalidIndexArgument.rst

.. _vim.fault.MissingNetworkIpConfig: ../vim/fault/MissingNetworkIpConfig.rst

.. _vim.fault.InsufficientResourcesFault: ../vim/fault/InsufficientResourcesFault.rst

.. _vim.fault.MissingPowerOffConfiguration: ../vim/fault/MissingPowerOffConfiguration.rst


vim.VirtualApp
==============
  Represents a multi-tiered software solution. A vApp is a collection of virtual machines (and potentially other vApp containers) that are operated and monitored as a unit. From a manage perspective, a multi-tiered vApp acts a lot like a virtual machine object. It has power operations, networks, datastores, and its resource usage can be configured.From a technical perspective, a vApp container is a specialized resource pool that has been extended with the following capabilities:
   * 
   * Product information such as product name, vendor, properties, and licenses.
   * 
   * A power-on/power-off sequence specification
   * 
   * Support for import/export vApps as OVF packages
   * 
   * An OVF environment that allows for application-level customization
   * Destroying a vAppWhen a vApp is destroyed, all of its virtual machines are destroyed, as well as any child vApps.The VApp.Delete privilege must be held on the vApp as well as the parent folder of the vApp. Also, the VApp.Delete privilege must be held on any child vApps that would be destroyed by the operation.


:extends: vim.ResourcePool_
:since: `vSphere API 4.0`_


Attributes
----------
    parentFolder (`vim.Folder`_):
      privilege: System.View
       A reference to the parent folder in the VM and Template folder hierarchy. This is only set for a root vApp. A root vApp is a vApp that is not a child of another vApp.
    datastore ([`vim.Datastore`_]):
      privilege: System.View
       A collection of references to the subset of datastore objects used by this vApp.
    network ([`vim.Network`_]):
      privilege: System.View
       A collection of references to the subset of network objects that is used by this virtual machine.
    vAppConfig (`vim.vApp.VAppConfigInfo`_):
      privilege: System.Read
       Configuration of this package.
    parentVApp (`vim.ManagedEntity`_):
       Reference to the parent vApp.
    childLink ([`vim.VirtualApp.LinkInfo`_]):
       List of linked children.


Methods
-------


UpdateVAppConfig(spec):
   Updates the vApp configuration.Updates in different areas require different privileges. See `VAppConfigSpec`_ for a full description.


  Privilege:
               dynamic



  Args:
    spec (`vim.vApp.VAppConfigSpec`_):
       contains the updates to the current configuration. Any set element, is changed. All values in the spec that is left unset, will not be modified.




  Returns:
    None
         

  Raises:

    `vim.fault.TaskInProgress`_: 
       if the vApp is busy.

    `vim.fault.VmConfigFault`_: 
       for bad configuration, such as invalid property types.

    `vim.fault.ConcurrentAccess`_: 
       if another operation conflicted with this operation.

    `vim.fault.FileFault`_: 
       vim.fault.FileFault

    `vim.fault.InvalidName`_: 
       vim.fault.InvalidName

    `vim.fault.DuplicateName`_: 
       vim.fault.DuplicateName

    `vim.fault.InvalidState`_: 
       vim.fault.InvalidState

    `vim.fault.InsufficientResourcesFault`_: 
       vim.fault.InsufficientResourcesFault

    `vim.fault.InvalidDatastore`_: 
       vim.fault.InvalidDatastore

    `vim.fault.InvalidPowerState`_: 
       if the reconfiguration is not possible given the current powerState of the vApp.

    `vmodl.fault.InvalidArgument`_: 
       for wrong input.

    `vim.fault.InvalidIndexArgument`_: 
       if a wrong key is used in one of the arrays. For example, for duplicated entries in entityConfig.


UpdateLinkedChildren(addChangeSet, removeSet):
   Reconfigure the set of linked children.A VirtualMachine and vApp can be added as a linked child as long as it is not a direct child of another vApp. In case it is a linked child, the existing link is removed and replaced with the new link specified in this call.An InvalidArgument fault is thrown if a link target is a direct child of another vApp, or if the addition of the link will result in a vApp with a cycle. For example, a vApp cannot be linked to itself.The removeSet must refer to managed entities that are currently linked children. Otherwise, an InvalidArgument exception is thrown.For each entity being linked, the operation is subject to the following privilege checks:
    * If the object being linked is a vApp, VApp.Move must be held on the vApp being linked and its former parent vApp (if any). The privilege VApp.AssignVApp must be held on this vApp.
    * If the object being linked is a VirtualMachine, VApp.AssignVM is required on both the target vApp, the VirtualMachine, and its former parent vApp (if any).Privilege checks for each entity in the removeSet are similar to the entities in the addChangeSet, except that there is no target vApp.This operation is only transactional with respect to each individual link change. The changes are processed sequentially and committed one at a time. The addChangeSet is processed first, followed by the removeSet. If a failure is detected, then the method terminates with an exception.
  since: `vSphere API 4.1`_


  Privilege:
               dynamic



  Args:
    addChangeSet (`vim.VirtualApp.LinkInfo`_, optional):
       a set of LinkInfo objects that either add a new link or modify an exisiting link.


    removeSet (`vim.ManagedEntity`_, optional):
       a set of entities that should no longer link to this vApp.




  Returns:
    None
         

  Raises:

    `vim.fault.ConcurrentAccess`_: 
       If a concurrent modification happens while adding the link.

    `vmodl.fault.InvalidArgument`_: 
       See above description.

    `vmodl.fault.NotSupported`_: 
       If the target of the link is not in the same datacenter.


CloneVApp(name, target, spec):
   Creates a clone of this vApp.Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.When invoking this method, the following privilege checks occur:
    * The privilege VApp.Clone is required on this vApp.
    * If the target is a resource pool, the privilege Resource.AssignVAppToPool is required on it.
    * If the target is a vApp, the privileges VApp.Clone and VApp.AssignVApp are required on it.Additional privileges are required by the clone spec provided. See `VAppCloneSpec`_ for details.


  Privilege:
               VApp.Clone



  Args:
    name (`str`_):
       The name of the new vApp.


    target (`vim.ResourcePool`_):
       The parent entity of the new vApp. Must be of type `ResourcePool`_ or `VirtualApp`_ .


    spec (`vim.vApp.CloneSpec`_):
       Specifies how to clone the vApp.




  Returns:
     `vim.Task`_:
         The newly created vApp.

  Raises:

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the vApp's current state. For example, if the virtual machine configuration information is not available, or if the vApp is running.

    `vim.fault.InvalidDatastore`_: 
       if the operation cannot be performed on the target datastores.

    `vim.fault.TaskInProgress`_: 
       if the vApp is busy.

    `vim.fault.VmConfigFault`_: 
       if one of the virtual machines are not compatible with a destination host. Typically, a specific subclass of this exception is thrown, such as IDEDiskNotSupported.

    `vim.fault.FileFault`_: 
       if there was an error accessing one of the virtual machine files.

    `vim.fault.MigrationFault`_: 
       if it is not possible to migrate one of the virtual machines to the destination. This is typically due to hosts being incompatible, such as mismatch in network polices or access to networks and datastores. Typically, a more specific subclass is thrown.

    `vim.fault.InsufficientResourcesFault`_: 
       if this operation would violate a resource usage policy.

    `vim.fault.InvalidPowerState`_: 
       if the vApp is powered on.

    `vmodl.fault.NotSupported`_: 
       if the operation is not supported by the current agent.


ExportVApp():
   Obtains an export lease on this vApp. The export lease contains a list of URLs for the disks of the virtual machines in this vApp, as well as a ticket that gives access to these URLs.See `HttpNfcLease`_ for information on how to use the lease.


  Privilege:
               VApp.Export



  Args:


  Returns:
    `vim.HttpNfcLease`_:
         the export lease on this vApp. The export task continues running until the lease is completed or aborted.

  Raises:

    `vim.fault.InvalidPowerState`_: 
       if the vApp is powered on.

    `vim.fault.TaskInProgress`_: 
       if the vApp is busy.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the vApp's current state. For example, if the virtual machine configuration information is not available, or if the vApp is running.

    `vim.fault.FileFault`_: 
       if there was an error accessing one of the virtual machine files.


PowerOnVApp():
   Starts this vApp.The virtual machines (or sub vApps) will be started in the order specified in the vApp configuration. If the vApp is suspended (@see vim.VirtualApp.Summary.suspended), all suspended virtual machines will be powered-on based on the defined start-up order.While a vApp is starting, all power operations performed on sub entities are disabled through the VIM API. They will throw TaskInProgress.In case of a failure to power-on a virtual machine, the exception from the virtual machine power on is returned, and the power-on sequence will be terminated. In case of a failure, virtual machines that are already started will remain powered-on.


  Privilege:
               VApp.PowerOn



  Args:


  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.TaskInProgress`_: 
       if the vApp is busy

    `vim.fault.InvalidState`_: 
       if it fails to power on a virtual machine due to no host availability, or unable to access the configuration file of a VM.

    `vim.fault.InsufficientResourcesFault`_: 
       if this operation would violate a resource usage policy.

    `vim.fault.VmConfigFault`_: 
       if a configuration issue on the vApp or a virtual machine in the vApp prevents the power-on to complete. Typically, a more specific fault, such as InvalidPropertyType is thrown.

    `vim.fault.VAppConfigFault`_: 
       if a configuration issue on a vApp prevents the power-on. Typically, a more specific fault, MissingPowerOnConfiguration, is thrown.

    `vim.fault.FileFault`_: 
       if there is a problem accessing the virtual machine on the filesystem.

    `vim.fault.InvalidPowerState`_: 
       if the vApp is already running

    `vmodl.fault.NotEnoughLicenses`_: 
       if there are not enough licenses to power on one or more virtual machines.

    `vmodl.fault.NotSupported`_: 
       if the vApp is marked as a template.

    `vim.fault.MissingNetworkIpConfig`_: 
       if no network configuration exists for the primary network for the vApp.


PowerOffVApp(force):
   Stops this vApp.The virtual machines (or child vApps) will be stopped in the order specified in the vApp configuration, if force is false. If force is set to true, all virtual machines are powered-off (in no specific order and possibly in parallel) regardless of the vApp auto-start configuration.While a vApp is stopping, all power operations performed on sub entities are disabled through the VIM API. They will throw TaskInProgress.


  Privilege:
               VApp.PowerOff



  Args:
    force (`bool`_):
       If force is false, the shutdown order in the vApp is executed. If force is true, all virtual machines are powered-off (regardless of shutdown order).




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.TaskInProgress`_: 
       if the vApp is busy.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the vApp's current state. For example, if the vApp is in the process of being started.

    `vim.fault.VAppConfigFault`_: 
       vim.fault.VAppConfigFault

    `vim.fault.InvalidPowerState`_: 
       if the vApp is not running

    `vim.fault.MissingPowerOffConfiguration`_: 
       if no vApp powerOff configuration has been specified.


SuspendVApp():
   Suspends this vApp.Suspends all powered-on virtual machines in a vApp, including virtual machines in child vApps. The virtual machines are suspended in the same order as used for a power-off operation (reverse power-on sequence).While a vApp is being suspended, all power operations performed on sub entities are disabled through the VIM API. They will throw TaskInProgress.
  since: `vSphere API 4.1`_


  Privilege:
               VApp.Suspend



  Args:


  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.TaskInProgress`_: 
       if the vApp is busy.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the vApp's current state. For example, if the vApp is in the process of being started.

    `vim.fault.VAppConfigFault`_: 
       vim.fault.VAppConfigFault

    `vim.fault.InvalidPowerState`_: 
       if the vApp is not running


unregisterVApp():
   Removes this vApp from the inventory without removing any of the virtual machine's files on disk. All high-level information stored with the management server (ESX Server or VirtualCenter) is removed, including information such as vApp configuration, statistics, permissions, and alarms.


  Privilege:
               VApp.Unregister



  Args:


  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.ConcurrentAccess`_: 
       vim.fault.ConcurrentAccess

    `vim.fault.InvalidState`_: 
       vim.fault.InvalidState

    `vim.fault.InvalidPowerState`_: 
       if the vApp is running.


