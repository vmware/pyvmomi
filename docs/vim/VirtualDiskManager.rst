
vim.VirtualDiskManager
======================
  This managed object type provides a way to manage and manipulate virtual disks on datastores. The source and the destination names are in the form of a URL or a datastore path.A URL has the formscheme://authority/folder/path?dcPath=dcPath=dsNamewhere
   * scheme
   * is
   * http
   * or
   * https
   * .
   * authority
   * specifies the hostname or IP address of the VirtualCenter or ESX server and optionally the port.
   * dcPath
   * is the inventory path to the Datacenter containing the Datastore.
   * dsName
   * is the name of the Datastore.
   * path
   * is a slash-delimited path from the root of the datastore.A datastore path has the form[datastore]pathwhere
   * datastore
   * is the datastore name.
   * path
   * is a slash-delimited path from the root of the datastore.An example datastore path is "[storage] path/to/file.extension". A listing of all the files, disks and folders on a datastore can be obtained from the datastore browser.See `HostDatastoreBrowser <vim/host/DatastoreBrowser.rst>`_ 


:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


Attributes
----------


Methods
-------


CreateVirtualDisk(name, datacenter, spec):
   Create a virtual disk.The datacenter parameter may be omitted if a URL is used to name the disk.Requires Datastore.FileManagement privilege on the datastore where the virtual disk is created.


  Privilege:
               System.View



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the disk, either a datastore path or a URL referring to the virtual disk to be created.


    datacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       Ifnameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,namemust be a URL.


    spec (`vim.VirtualDiskManager.VirtualDiskSpec <vim/VirtualDiskManager/VirtualDiskSpec.rst>`_):
       The specification of the virtual disk to be created.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         a datastore path referring to the created virtual disk.

  Raises:

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if an error occurs creating the virtual disk.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the datastore.


DeleteVirtualDisk(name, datacenter):
   Delete a virtual disk. All files relating to the disk will be deleted.The datacenter parameter may be omitted if a URL is used to name the disk.Requires Datastore.FileManagement privilege on the datastore where the virtual disk is removed.


  Privilege:
               System.View



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the disk, either a datastore path or a URL referring to the virtual disk to be deleted.


    datacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       Ifnameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,namemust be a URL.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if an error occurs deleting the virtual disk.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the datastore.


MoveVirtualDisk(sourceName, sourceDatacenter, destName, destDatacenter, force, profile):
   Move a virtual disk and all related files from the source location specified bysourceNameandsourceDatacenterto the destination location specified bydestNameanddestDatacenter.If source (or destination) name is specified as a URL, then the corresponding datacenter parameter may be omitted.If source and destination resolve to the same file system location, the call has no effect.Requires Datastore.FileManagement privilege on both source and destination datastores.


  Privilege:
               System.View



  Args:
    sourceName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the source, either a datastore path or a URL referring to the virtual disk to be moved.


    sourceDatacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       IfsourceNameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,sourceNamemust be a URL.


    destName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the destination, either a datastore path or a URL referring to the destination virtual disk.


    destDatacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       IfdestNameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter, it is assumed that the destination path belongs to the source datacenter.


    force (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       If true, overwrite any indentically named disk at the destination. If not specified, it is assumed to be false


    profile (`vim.vm.ProfileSpec <vim/vm/ProfileSpec.rst>`_, optional, since `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_ ):
       User can specify new set of profile when moving virtual disk.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         a datastore path referring to the destination virtual disk.

  Raises:

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if an error occurs renaming the virtual disk.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the source or destination datastore.


CopyVirtualDisk(sourceName, sourceDatacenter, destName, destDatacenter, destSpec, force):
   Copy a virtual disk, performing conversions as specified in the spec.If source (or destination) name is specified as a URL, then the corresponding datacenter parameter may be omitted.If source and destination resolve to the same file system location, the call has no effect, regardless of destSpec content.Requires Datastore.FileManagement privilege on both source and destination datastores.


  Privilege:
               System.View



  Args:
    sourceName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the source, either a datastore path or a URL referring to the virtual disk to be copied.


    sourceDatacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       IfsourceNameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,sourceNamemust be a URL.


    destName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the destination, either a datastore path or a URL referring to the virtual disk to be created.


    destDatacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       IfdestNameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter, it is assumed that the destination path belongs to the source datacenter.


    destSpec (`vim.VirtualDiskManager.VirtualDiskSpec <vim/VirtualDiskManager/VirtualDiskSpec.rst>`_, optional):
       The specification of the virtual disk to be created. If not specified, a preallocated format and busLogic adapter type is assumed.


    force (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The force flag is currently ignored. The FileAlreadyExists fault is thrown if the destination file already exists.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         a datastore path referring to the copied virtual disk.

  Raises:

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if an error occurs cloning the virtual disk.

    `vim.fault.InvalidDiskFormat <vim/fault/InvalidDiskFormat.rst>`_: 
       if the destination's format is not supported.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the source or destination datastore.


ExtendVirtualDisk(name, datacenter, newCapacityKb, eagerZero):
   Expand the capacity of a virtual disk to the new capacity. If the eagerZero flag is not specified, - the extended disk region of a zerothick disk will be zeroedthick - the extended disk region of a eagerzerothick disk will be eagerzeroedthick - a thin-provisioned disk will always be extended as a thin-provisioned disk. If the eagerZero flag TRUE, the extended region of the disk will always be eagerly zeroed. If the eagerZero flag FALSE, the extended region of a zeroedthick or eagerzeroedthick the disk will not be eagerly zeroed. This condition has no effect on a thin source disk.The datacenter parameter may be omitted if a URL is used to name the disk.Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.


  Privilege:
               System.View



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the disk, either a datastore path or a URL referring to the virtual disk whose capacity should be expanded.


    datacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       Ifnameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,namemust be a URL.


    newCapacityKb (`long <https://docs.python.org/2/library/stdtypes.html>`_):
       The new capacty of the virtual disk in Kb.


    eagerZero (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional, since `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_ ):
       If true, the extended part of the disk will be explicitly filled with zeroes.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if an error occurs extending the virtual disk.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the datastore.


QueryVirtualDiskFragmentation(name, datacenter):
   Return the percentage of fragmentation of the sparse virtual disk. This is the fragmentation of virtual disk file(s) in the host operating system, not the fragmentation of the guest operating systemS filesystem inside the virtual disk.The datacenter parameter may be omitted if a URL is used to name the disk.Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.


  Privilege:
               System.View



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the disk, either a datastore path or a URL referring to the virtual disk for which to return the percentage of fragmentation.


    datacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       Ifnameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,namemust be a URL.




  Returns:
    `int <https://docs.python.org/2/library/stdtypes.html>`_:
         the percentage of fragmentation (as an integer between 0 and 100) of the sparse virtual disk.

  Raises:

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if an error occurs reading the virtual disk.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the datastore.


DefragmentVirtualDisk(name, datacenter):
   Defragment a sparse virtual disk. This is defragmentation of the virtual disk file(s) in the host operating system, not defragmentation of the guest operating system filesystem inside the virtual disk.The datacenter parameter may be omitted if a URL is used to name the disk.Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.


  Privilege:
               System.View



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the disk, either a datastore path or a URL referring to the virtual disk that should be defragmented.


    datacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       Ifnameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,namemust be a URL.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if an error occurs defragmenting the virtual disk.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the datastore.


ShrinkVirtualDisk(name, datacenter, copy):
   Shrink a sparse virtual disk.The datacenter parameter may be omitted if a URL is used to name the disk.The optional parametercopyspecifies whether to shrink the disk in copy-shrink mode or in-place mode. In copy-shrink mode, additional space is required, but will result in a shrunk disk that is also defragmented. In-place shrink does not require additional space, but will increase fragmentation. The default behavior is to perform copy-shrink if the parameter is not specified.Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.


  Privilege:
               System.View



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the disk, either a datastore path or a URL referring to the virtual disk that should be shrink.


    datacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       Ifnameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,namemust be a URL.


    copy (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       If true or omitted, performs shrink in copy-shrink mode, otherwise shrink in in-place mode.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if an error occurs shrinking the virtual disk.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the datastore.


InflateVirtualDisk(name, datacenter):
   Inflate a sparse or thin-provisioned virtual disk up to the full size. Additional space allocated to the disk as a result of this operation will be filled with zeroes.The datacenter parameter may be omitted if a URL is used to name the disk.Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.


  Privilege:
               System.View



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the disk, either a datastore path or a URL referring to the virtual disk that should be inflated.


    datacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       Ifnameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,namemust be a URL.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if an error occurs inflating the virtual disk.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the datastore.


EagerZeroVirtualDisk(name, datacenter):
   Explicitly zero out unaccessed parts zeroedthick disk. Effectively a no-op if the disk is already eagerZeroedThick. Unlike zeroFillVirtualDisk, which wipes the entire disk, this operation only affects previously unaccessed parts of the disk.The datacenter parameter may be omitted if a URL is used to name the disk.Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               System.View



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the disk, either a datastore path or a URL referring to the virtual disk that should be inflated.


    datacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       Ifnameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,namemust be a URL.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if an error occurs while eager-zeroing the virtual disk.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the datastore.


ZeroFillVirtualDisk(name, datacenter):
   Overwrite all blocks of the virtual disk with zeros. All data will be lost.The datacenter parameter may be omitted if a URL is used to name the disk.Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.


  Privilege:
               System.View



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the disk, either a datastore path or a URL referring to the virtual disk whose blocks should be overwritten with zeroes.


    datacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       Ifnameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,namemust be a URL.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if an error occurs zero filling the virtual disk.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the datastore.


SetVirtualDiskUuid(name, datacenter, uuid):
   Set the virtual disk SCSI inquiry page 0x83 data.The datacenter parameter may be omitted if a URL is used to name the disk.Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.


  Privilege:
               System.View



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the disk, either a datastore path or a URL referring to the virtual disk whose SCSI inquiry page 0x83 data should be set.


    datacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       Ifnameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,namemust be a URL.


    uuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The hex representation of the unique ID for this virtual disk.




  Returns:
    None
         

  Raises:

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if an error occurs updating the virtual disk.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the datastore.


QueryVirtualDiskUuid(name, datacenter):
   Get the virtual disk SCSI inquiry page 0x83 data.The datacenter parameter may be omitted if a URL is used to name the disk.Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.


  Privilege:
               System.View



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the disk, either a datastore path or a URL referring to the virtual disk from which to get SCSI inquiry page 0x83 data.


    datacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       Ifnameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,namemust be a URL.




  Returns:
    `str <https://docs.python.org/2/library/stdtypes.html>`_:
         The hex representation of the unique ID for this virtual disk.

  Raises:

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if an error occurs reading the virtual disk.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the datastore.


QueryVirtualDiskGeometry(name, datacenter):
   Get the disk geometry information for the virtual disk.The datacenter parameter may be omitted if a URL is used to name the disk.Requires Datastore.FileManagement privilege on the datastore where the virtual disk resides.


  Privilege:
               System.View



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the disk, either a datastore path or a URL referring to the virtual disk from which to get geometry information.


    datacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       Ifnameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,namemust be a URL.




  Returns:
    `vim.host.DiskDimensions.Chs <vim/host/DiskDimensions/Chs.rst>`_:
         The geometry information for this virtual disk.

  Raises:

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if an error occurs reading the virtual disk.

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the datastore.


