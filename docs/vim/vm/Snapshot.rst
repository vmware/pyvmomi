
vim.vm.Snapshot
===============
  The Snapshot managed object type specifies the interface to individual snapshots of a virtual machine. Although these are managed objects, they are subordinate to their virtual machine.


:extends: vim.ExtensibleManagedObject_


Attributes
----------
    config (`vim.vm.ConfigInfo <vim/vm/ConfigInfo.rst>`_):
       Information about the configuration of this virtual machine when this snapshot was taken.The datastore paths for the virtual machine disks point to the head of the disk chain that represents the disk at this given snapshot. The fileInfo.fileLayout field is not set.
    childSnapshot ([`vim.vm.Snapshot <vim/vm/Snapshot.rst>`_]):
       All snapshots for which this snapshot is the parent.


Methods
-------


RevertToSnapshot(host, suppressPowerOn):
   Change the execution state of the virtual machine to the state of this snapshot.


  Privilege:
               VirtualMachine.State.RevertToSnapshot



  Args:
    host (`vim.HostSystem <vim/HostSystem.rst>`_, optional):
       (optional) Choice of host for the virtual machine, in case this operation causes the virtual machine to power on.If a snapshot was taken while a virtual machine was powered on, and this operation is invoked after the virtual machine was powered off, the operation causes the virtual machine to power on to reach the snapshot state. This parameter can be used to specify a choice of host where the virtual machine should power on.If this parameter is not set and the vBalance feature is configured for automatic load balancing, a host is automatically selected. Otherwise, the virtual machine keeps its existing host affiliation.


    suppressPowerOn (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional, since `vSphere API 4.0 <vim/version.rst#vimversionversion4>`_ ):
       (optional) If set to true, the virtual machine will not be powered on regardless of the power state when the snapshot was created. Default to false.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.InsufficientResourcesFault <vim/fault/InsufficientResourcesFault.rst>`_: 
       if this operation would violate a resource usage policy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed in the current state of the virtual machine. For example, the virtual machine's configuration is not available.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a problem accessing the virtual machine on the filesystem.

    `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_: 
       if a configuration issue prevents the power-on. Typically, a more specific fault, such as UnsupportedVmxLocation, is thrown.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the host product does not support snapshots.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the operation cannot be performed in the current power state of the virtual machine.


RemoveSnapshot(removeChildren, consolidate):
   Removes this snapshot and deletes any associated storage.


  Privilege:
               VirtualMachine.State.RemoveSnapshot



  Args:
    removeChildren (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       Flag to specify removal of the entire snapshot subtree.


    consolidate (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional, since `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_ ):
       (optional) If set to true, the virtual disk associated with this snapshot will be merged with other disk if possible. Defaults to true.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.


RenameSnapshot(name, description):
   Rename this snapshot with either a new name or a new description or both. At least one of these must be specified when calling the rename method.


  Privilege:
               VirtualMachine.State.RenameSnapshot



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       New name for the snapshot.


    description (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       New description for the snapshot.




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidName <vim/fault/InvalidName.rst>`_: 
       if the specified snapshot name is not valid.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed in the current state of the virtual machine. For example, the virtual machine's configuration is not available.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the host product does not support snapshot rename.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the operation cannot be performed in the current power state of the virtual machine.


ExportSnapshot():
   Obtains an export lease on this snapshot. The export lease contains a list of URLs for the virtual disks for this snapshot, as well as a ticket giving access to the URLs.See `HttpNfcLease <vim/HttpNfcLease.rst>`_ for information on how to use the lease.
  since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_


  Privilege:
               VApp.Export



  Args:


  Returns:
    `vim.HttpNfcLease <vim/HttpNfcLease.rst>`_:
         The export lease on this `VirtualMachineSnapshot <vim/vm/Snapshot.rst>`_ . The export task continues running until the lease is completed by the caller.

  Raises:

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state. For example, if the virtual machine configuration information is not available.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is an error accessing the virtual machine files.


