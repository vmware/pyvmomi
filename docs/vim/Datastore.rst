
vim.Datastore
=============
  Represents a storage location for virtual machine files. A storage location can be a VMFS volume, a directory on Network Attached Storage, or a local file system path.A datastore is platform-independent and host-independent. Therefore, datastores do not change when the virtual machines they contain are moved between hosts. The scope of a datastore is a datacenter; the datastore is uniquely named within the datacenter.Any reference to a virtual machine or file accessed by any host within the datacenter must use a datastore path. A datastore path has the form "[datastore]path", wheredatastoreis the datastore name, andpathis a slash-delimited path from the root of the datastore. An example datastore path is "[storage] path/to/config.vmx".You may use the following characters in a path, but not in a datastore name: slash (/), backslash (\), and percent (%).All references to files in the VIM API are implicitly done using datastore paths.When a client creates a virtual machine, it may specify the name of the datastore, omitting the path; the system, meaning VirtualCenter or the host, automatically assigns filenames and creates directories on the given datastore. For example, specifying My_Datastore as a location for a virtual machine called MyVm results in a datastore location of My_Datastore\MyVm\MyVm.vmx.Datastores are configured per host. As part of host configuration, a HostSystem can be configured to mount a set of network drives. Multiple hosts may be configured to point to the same storage location. There exists only one Datastore object per Datacenter, for each such shared location. Each Datastore object keeps a reference to the set of hosts that have mounted the datastore. A Datastore object can be removed only if no hosts currently have the datastore mounted.Thus, managing datastores is done both at the host level and the datacenter level. Each host is configured explicitly with the set of datastores it can access. At the datacenter, a view of the datastores across the datacenter is shown.


:extends: vim.ManagedEntity_


Attributes
----------
    info (`vim.Datastore.Info <vim/Datastore/Info.rst>`_):
       Specific information about the datastore.
    summary (`vim.Datastore.Summary <vim/Datastore/Summary.rst>`_):
       Global properties of the datastore.
    host ([`vim.Datastore.HostMount <vim/Datastore/HostMount.rst>`_]):
       Hosts attached to this datastore.
    vm ([`vim.VirtualMachine <vim/VirtualMachine.rst>`_]):
       Virtual machines stored on this datastore.
    browser (`vim.host.DatastoreBrowser <vim/host/DatastoreBrowser.rst>`_):
       DatastoreBrowser used to browse this datastore.
    capability (`vim.Datastore.Capability <vim/Datastore/Capability.rst>`_):
       Capabilities of this datastore.
    iormConfiguration (`vim.StorageResourceManager.IORMConfigInfo <vim/StorageResourceManager/IORMConfigInfo.rst>`_):
       Configuration of storage I/O resource management for the datastore. Currently we only support storage I/O resource management on VMFS volumes of a datastore.This configuration may not be available if the datastore is not accessible from any host, or if the datastore does not have VMFS volume. The configuration can be modified using the method `ConfigureDatastoreIORM_Task <vim/StorageResourceManager.rst#ConfigureDatastoreIORM>`_ 


Methods
-------


RefreshDatastore():
   Explicitly refreshes free-space and capacity values in `summary <vim/Datastore.rst#summary>`_ and `info <vim/Datastore.rst#info>`_ .


  Privilege:
               System.Read



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the datastore or its underlying volume is not found.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if unable to get the current system information for the datastore.


RefreshDatastoreStorageInfo():
   Refreshes all storage related information including free-space, capacity, and detailed usage of virtual machines. Updated values are available in `summary <vim/Datastore.rst#summary>`_ and `info <vim/Datastore.rst#info>`_ .
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               System.Read



  Args:


  Returns:
    None
         


UpdateVirtualMachineFiles(mountPathDatastoreMapping):
   Update file paths embedded in virtual machine files on the datastore. This can be called after the file system corresponding to the datastore has been resignatured or remounted. Any MountPathDatastorePairs where the new path is the same as the original file path will be ignored.This method is only supported by vCenter server. Also, this method requires that the datastore is `accessible <vim/host/MountInfo.rst#accessible>`_ from at least one host (ESX version 4.1 or above) in vCenter server.While this operation is in progress, it is important that users do not initiate any operations that might read or write to any files on the datastore, such as registering a virtual machine with files residing on the datastore, or performing any virtual disk operations on any files in the datastore. These operations can potentially cause spurious file update failures, while at the same time they can prevent virtual machine files from being updated correctly.If users intend to update multiple datastores using this method, it is strongly advised that the users do not initiate any operations that might read or write to files on any of the datastores, until all of them have been updated. The files of a single virtual machine can reside on multiple datastores, and thus all the involved datastores should be updated, before the virtual machine is considered updated completely.
  since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_


  Privilege:
               Datastore.UpdateVirtualMachineFiles



  Args:
    mountPathDatastoreMapping (`vim.Datastore.MountPathDatastorePair <vim/Datastore/MountPathDatastorePair.rst>`_):
       Old mount path to datastore mapping.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         Return an array of failed virtual machine file info. When there are too many failed files, only a subset of failed files will be returned.

  Raises:

    `vim.fault.ResourceInUse <vim/fault/ResourceInUse.rst>`_: 
       if there exists a registered virtual machine in the volume.

    `vim.fault.PlatformConfigFault <vim/fault/PlatformConfigFault.rst>`_: 
       if any error related to platform occurs during the operation.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the datastore is busy, for example, while another task is updating the datastore after volume resignaturing or remounting.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed due to some error with the datastore; typically a specific subclass of the fault is reported.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if old mount path is mapped to more than one datastores, or if any of the datastore being mapped can not be found.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if all hosts attached to this datastore do not support updating virtual machine files.


RenameDatastore(newName):
   Renames a datastore.


  Privilege:
               Datastore.Rename



  Args:
    newName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The new name to assign to the datastore.




  Returns:
    None
         

  Raises:

    `vim.fault.DuplicateName <vim/fault/DuplicateName.rst>`_: 
       if another datastore in this datacenter already has the same name.

    `vim.fault.InvalidName <vim/fault/InvalidName.rst>`_: 
       if the name is not a valid datastore name.


DestroyDatastore():
   Removes a datastore. A datastore can be removed only if it is not currently used by any host or virtual machine.


  Privilege:
               Datastore.Delete



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.ResourceInUse <vim/fault/ResourceInUse.rst>`_: 
       if one or more hosts or virtual machines are configured to use the datastore.


DatastoreEnterMaintenanceMode():
   Puts the datastore in maintenance mode. While this task is running and when the datastore is in maintenance mode, no virtual machines can be powered on and no provisioning operations can be performed on the datastore. Once the call completes, it is safe to remove datastore without disrupting any virtual machines.The task completes once there are no virtual machines on the datastore and no provisioning operations in progress on the datastore. The operation does not directly initiate any operations to evacuate or power-down powered-on virtual machines. However, if the datastore is part of a storage pod with VMware Storage DRS enabled, Storage DRS provides migration recommendations to evacuate the virtual machines. If Storage DRS is in fully-automatic mode, these are automatically scheduled. The task is cancellable. This method returns a `StoragePlacementResult <vim/storageDrs/StoragePlacementResult.rst>`_ object, which includes a `Task <vim/Task.rst>`_ object with which to monitor the operation, and a list of recommendations and faults generated by Storage DRS when it tries to evacuate the virtual machines on the datastore. The recommendations and faults fields are set only if the datastore is a part of a storage pod with Storage DRS enabled.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               Datastore.Config



  Args:


  Returns:
    `vim.storageDrs.StoragePlacementResult <vim/storageDrs/StoragePlacementResult.rst>`_:
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the datastore is already in maintenance mode.

    `vmodl.fault.RequestCanceled <vmodl/fault/RequestCanceled.rst>`_: 
       if the operation is canceled.


DatastoreExitMaintenanceMode():
   Takes the datastore out of maintenance mode.The task is cancellable.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               Datastore.Config



  Args:


  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the datastore is not in maintenance mode.


