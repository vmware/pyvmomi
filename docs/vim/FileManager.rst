
vim.FileManager
===============
  This managed object type provides a way to manage and manipulate files and folders on datastores. The source and the destination names are in the form of a URL or a datastore path.A URL has the formscheme://authority/folder/path?dcPath=dcPath=dsNamewhere
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


MoveDatastoreFile(sourceName, sourceDatacenter, destinationName, destinationDatacenter, force):
   Moves the source file or folder to the destination.If the destination file does not exist, it is created. If the destination file exists, the force parameter determines whether to overwrite it with the source or not. If the source path is a folder, then the destination path must not exist; the destination cannot be overwritten even with a force flag in that case. Folder moves are recursive, treating all files and disks to move as binary.If source (or destination) name is specified as a URL, then the corresponding datacenter parameter may be omitted.If any intermediate level folder specified by the source and destination does not exist, a `FileNotFound <vim/fault/FileNotFound.rst>`_ fault is thrown.If a file of a virtual machine is moved, it may corrupt that virtual machine. If a file of a virtual machine is overwritten on the destination datastore as a result of the force parameter, it may corrupt that virtual machine.If the source is an extent of a virtual disk, this operation treats the extent as a file.If source and destination resolve to the same file system location, the call has no effect.It is important to note that this operation will provide transactional guarantees only for a file. No guarantees are provided for folder moves. If the intent is to move a virtual machine registered in the inventory, with transactional guarantees, please refer to `RelocateVM_Task <vim/VirtualMachine.rst#relocate>`_ . If the intent is to rename a virtual machine registered in the inventory, please refer to `Rename_Task <vim/ManagedEntity.rst#rename>`_ .Datastore.FileManagement privilege is required on both source and destination datastores.


  Privilege:
               dynamic



  Args:
    sourceName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the source, either a URL or a datastore path referring to the file or folder to be moved.


    sourceDatacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       IfsourceNameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,sourceNamemust be a URL.


    destinationName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the destination, either a URL or a datastore path referring to the destination file or folder.


    destinationDatacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       IfdestinationNameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter, it is assumed that the destination path belongs to the source datacenter.


    force (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       If true, overwrite any identically named file at the destination. If not specified, it is assumed to be false.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the source or destination datastores. Typically, a specific subclass of this exception is thrown.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a generic file error

    `vim.fault.FileNotFound <vim/fault/FileNotFound.rst>`_: 
       if the file or folder specified by sourceName is not found, or, any intermediate level folder specified by the destinationName is not found.

    `vim.fault.CannotAccessFile <vim/fault/CannotAccessFile.rst>`_: 
       if the source file or folder cannot be moved because of insufficient permissions.

    `vim.fault.FileLocked <vim/fault/FileLocked.rst>`_: 
       if the source file or folder is currently locked or in use.

    `vim.fault.FileAlreadyExists <vim/fault/FileAlreadyExists.rst>`_: 
       if a file with the given name already exists at the destination, and the force flag is false. For folders, if the destination exists, this fault is thrown regardless.

    `vim.fault.NoDiskSpace <vim/fault/NoDiskSpace.rst>`_: 
       if there is not enough space available on the destination datastore.


CopyDatastoreFile(sourceName, sourceDatacenter, destinationName, destinationDatacenter, force):
   Copies the source file or folder to the destination.If the destination file does not exist, it is created. If the destination file exists, the force parameter determines whether to overwrite it with the source or not. Folders can be copied recursively. In this case, the destination, if it exists, must be a folder, else one will be created. Existing files on the destination that conflict with source files can be overwritten using the force parameter. Files and disks are always copied in binary format during recursive copy.If source (or destination) name is specified as a URL, then the corresponding datacenter parameter may be omitted.If any intermediate level folder specified by the source and destination does not exist, a `FileNotFound <vim/fault/FileNotFound.rst>`_ fault is thrown.If a file of a virtual machine is overwritten on the destination datastore as a result of the force parameter, it may corrupt that virtual machine.If the source is an extent of a virtual disk, this operation treats the extent as a file.If source and destination resolve to the same file system location, the call has no effect.It is important to note that this operation will provide transactional guarantees only for a file. No guarantees are provided when copying a folder. If the intent is to clone a virtual machine registered in the inventory, with transactional guarantees, please refer to `CloneVM_Task <vim/VirtualMachine.rst#clone>`_ .Datastore.FileManagement privilege is required on both source and destination datastores.


  Privilege:
               dynamic



  Args:
    sourceName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the source, either a URL or a datastore path referring to the file or folder to be copied.


    sourceDatacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       IfsourceNameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,sourceNamemust be a URL.


    destinationName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the destination, either a URL or a datastore path referring to the destination file or folder.


    destinationDatacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       IfdestinationNameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter, it is assumed that the destination path belongs to the source datacenter.


    force (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       If true, overwrite any identically named file at the destination. If not specified, it is assumed to be false.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the source or destination datastores. Typically, a specific subclass of this exception is thrown.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a generic file error

    `vim.fault.FileNotFound <vim/fault/FileNotFound.rst>`_: 
       if the file or folder specified by sourceName is not found, or, any intermediate level folder specified by the destinationName is not found.

    `vim.fault.CannotAccessFile <vim/fault/CannotAccessFile.rst>`_: 
       if the source cannot be accessed because of insufficient permissions.

    `vim.fault.FileLocked <vim/fault/FileLocked.rst>`_: 
       if the source file or folder is currently locked or in use.

    `vim.fault.FileAlreadyExists <vim/fault/FileAlreadyExists.rst>`_: 
       if a file with the given name already exists at the destination, and the force flag is false.

    `vim.fault.NoDiskSpace <vim/fault/NoDiskSpace.rst>`_: 
       if there is not enough space available at the destination datastore.


DeleteDatastoreFile(name, datacenter):
   Deletes the specified file or folder from the datastore. If a file of a virtual machine is deleted, it may corrupt that virtual machine. Folder deletes are always recursive. The datacenter parameter may be omitted if a URL is used to name the file or folder.If the source is an extent of a virtual disk, this operation treats the extent as a file.It is important to note that this operation will provide transactional guarantees only for a file. No guarantees are provided when deleting folders. If the intent is to delete a virtual machine registered in the inventory, please refer to `Destroy_Task <vim/ManagedEntity.rst#destroy>`_ .Requires Datastore.FileManagement privilege on the datastore.


  Privilege:
               dynamic



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the file or folder, either a URL or a datastore path referring to the file or folder to be deleted.


    datacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       Ifnameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,namemust be a URL.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the datastore. Typically, a specific subclass of this exception is thrown.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a generic file error

    `vim.fault.FileNotFound <vim/fault/FileNotFound.rst>`_: 
       if the file or folder specified by name is not found.

    `vim.fault.CannotDeleteFile <vim/fault/CannotDeleteFile.rst>`_: 
       if the delete operation on the file or folder fails.

    `vim.fault.FileLocked <vim/fault/FileLocked.rst>`_: 
       if the source file or folder is currently locked or in use.


MakeDirectory(name, datacenter, createParentDirectories):
   Create a folder using the specified name. If the parent or intermediate level folders do not exist, and the parameter createParentDirectories is false, a `FileNotFound <vim/fault/FileNotFound.rst>`_ fault is thrown. If the intermediate level folders do not exist, and the parameter createParentDirectories is true, all the non-existent folders are created.Requires Datastore.FileManagement privilege on the datastore.


  Privilege:
               dynamic



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the folder, either a URL or a datastore path referring to the folder to be created.


    datacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       Ifnameis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,namemust be a URL.


    createParentDirectories (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       If true, any non-existent intermediate level folders will be created. If not specified, it is assumed to be false.




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the operation cannot be performed on the datastore. Typically, a specific subclass of this exception is thrown.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a generic file error

    `vim.fault.CannotCreateFile <vim/fault/CannotCreateFile.rst>`_: 
       if the create operation on the folder fails.

    `vim.fault.FileAlreadyExists <vim/fault/FileAlreadyExists.rst>`_: 
       if a file or folder with the given name already exists at the destination.

    `vim.fault.FileNotFound <vim/fault/FileNotFound.rst>`_: 
       if the createParentDirectories is false and a intermediate level folder specified by name is not found.


ChangeOwner(name, datacenter, owner):
   Change the owner for a file.This method is currently not supported.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               dynamic



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):


    datacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):


    owner (`str <https://docs.python.org/2/library/stdtypes.html>`_):




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       vim.fault.InvalidDatastore

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       vim.fault.FileFault

    `vim.fault.UserNotFound <vim/fault/UserNotFound.rst>`_: 
       vim.fault.UserNotFound


