
vim.vm.guest.FileManager
========================
  FileManager is the managed object that provides APIs to manipulate the guest operating system files.


:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


Attributes
----------


Methods
-------


MakeDirectoryInGuest(vm, auth, directoryPath, createParentDirectories):
   Creates a directory in the guest OS


  Privilege:



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_):
       The guest authentication data. See `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ .


    directoryPath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The complete path to the directory to be created.


    createParentDirectories (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       Whether any parent directories are to be created.




  Returns:
    None
         

  Raises:

    `vim.fault.GuestOperationsFault <vim/fault/GuestOperationsFault.rst>`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable <vim/fault/GuestOperationsUnavailable.rst>`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied <vim/fault/GuestPermissionDenied.rst>`_: 
       if the directory cannot be created because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin <vim/fault/InvalidGuestLogin.rst>`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.FileAlreadyExists <vim/fault/FileAlreadyExists.rst>`_: 
       if the specified object already exists.

    `vim.fault.GuestComponentsOutOfDate <vim/fault/GuestComponentsOutOfDate.rst>`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest <vim/fault/OperationNotSupportedByGuest.rst>`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest <vim/fault/OperationDisabledByGuest.rst>`_: 
       if the operation is not enabled due to guest agent configuration.


DeleteFileInGuest(vm, auth, filePath):
   Deletes a file in the guest OS


  Privilege:



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_):
       The guest authentication data. See `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ .


    filePath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The complete path to the file or symbolic link to be deleted.




  Returns:
    None
         

  Raises:

    `vim.fault.GuestOperationsFault <vim/fault/GuestOperationsFault.rst>`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable <vim/fault/GuestOperationsUnavailable.rst>`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied <vim/fault/GuestPermissionDenied.rst>`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin <vim/fault/InvalidGuestLogin.rst>`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.NotAFile <vim/fault/NotAFile.rst>`_: 
       if the specified object is not a file.

    `vim.fault.GuestComponentsOutOfDate <vim/fault/GuestComponentsOutOfDate.rst>`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest <vim/fault/OperationNotSupportedByGuest.rst>`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest <vim/fault/OperationDisabledByGuest.rst>`_: 
       if the operation is not enabled due to guest agent configuration.


DeleteDirectoryInGuest(vm, auth, directoryPath, recursive):
   Deletes a directory in the guest OS.


  Privilege:



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_):
       The guest authentication data. See `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ .


    directoryPath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The complete path to the directory to be deleted.


    recursive (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       If true, all subdirectories are also deleted. If false, the directory must be empty for the operation to succeed.




  Returns:
    None
         

  Raises:

    `vim.fault.GuestOperationsFault <vim/fault/GuestOperationsFault.rst>`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable <vim/fault/GuestOperationsUnavailable.rst>`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied <vim/fault/GuestPermissionDenied.rst>`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin <vim/fault/InvalidGuestLogin.rst>`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.NotADirectory <vim/fault/NotADirectory.rst>`_: 
       if the specified object is not a directory.

    `vim.fault.GuestComponentsOutOfDate <vim/fault/GuestComponentsOutOfDate.rst>`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest <vim/fault/OperationNotSupportedByGuest.rst>`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest <vim/fault/OperationDisabledByGuest.rst>`_: 
       if the operation is not enabled due to guest agent configuration.


MoveDirectoryInGuest(vm, auth, srcDirectoryPath, dstDirectoryPath):
   Moves or renames a directory in the guest.


  Privilege:



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_):
       The guest authentication data. See `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ .


    srcDirectoryPath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The complete path to the directory to be moved.


    dstDirectoryPath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The complete path to the where the directory is moved or its new name. It cannot be a path to an existing directory or an existing file.




  Returns:
    None
         

  Raises:

    `vim.fault.GuestOperationsFault <vim/fault/GuestOperationsFault.rst>`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable <vim/fault/GuestOperationsUnavailable.rst>`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied <vim/fault/GuestPermissionDenied.rst>`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin <vim/fault/InvalidGuestLogin.rst>`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate <vim/fault/GuestComponentsOutOfDate.rst>`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest <vim/fault/OperationNotSupportedByGuest.rst>`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest <vim/fault/OperationDisabledByGuest.rst>`_: 
       if the operation is not enabled due to guest agent configuration.


MoveFileInGuest(vm, auth, srcFilePath, dstFilePath, overwrite):
   Renames a file in the guest.


  Privilege:



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_):
       The guest authentication data. See `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ .


    srcFilePath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The complete path to the original file or symbolic link to be moved.


    dstFilePath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The complete path to the where the file is renamed. It cannot be a path to an existing diectory.


    overwrite (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       If set, the destination file is clobbered.




  Returns:
    None
         

  Raises:

    `vim.fault.GuestOperationsFault <vim/fault/GuestOperationsFault.rst>`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable <vim/fault/GuestOperationsUnavailable.rst>`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied <vim/fault/GuestPermissionDenied.rst>`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin <vim/fault/InvalidGuestLogin.rst>`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate <vim/fault/GuestComponentsOutOfDate.rst>`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest <vim/fault/OperationNotSupportedByGuest.rst>`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest <vim/fault/OperationDisabledByGuest.rst>`_: 
       if the operation is not enabled due to guest agent configuration.


CreateTemporaryFileInGuest(vm, auth, prefix, suffix, directoryPath):
   Creates a temporary file.Creates a new unique temporary file for the user to use as needed. The user is responsible for removing it when it is no longer needed.


  Privilege:



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_):
       The guest authentication data. See `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ .


    prefix (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The prefix to be given to the new temporary file.


    suffix (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The suffix to be given to the new temporary file.


    directoryPath (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The complete path to the directory in which to create the file. If unset, or an empty string, a guest-specific location will be used.




  Returns:
    `str <https://docs.python.org/2/library/stdtypes.html>`_:
         The absolute path of the temporary file that is created.

  Raises:

    `vim.fault.GuestOperationsFault <vim/fault/GuestOperationsFault.rst>`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable <vim/fault/GuestOperationsUnavailable.rst>`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied <vim/fault/GuestPermissionDenied.rst>`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin <vim/fault/InvalidGuestLogin.rst>`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate <vim/fault/GuestComponentsOutOfDate.rst>`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest <vim/fault/OperationNotSupportedByGuest.rst>`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest <vim/fault/OperationDisabledByGuest.rst>`_: 
       if the operation is not enabled due to guest agent configuration.


CreateTemporaryDirectoryInGuest(vm, auth, prefix, suffix, directoryPath):
   Creates a temporary directory.Creates a new unique temporary directory for the user to use as needed. The user is responsible for removing it when it is no longer needed.


  Privilege:



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_):
       The guest authentication data. See `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ .


    prefix (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The prefix to be given to the new temporary directory.


    suffix (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The suffix to be given to the new temporary directory.


    directoryPath (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The complete path to the directory in which to create the new directory. If unset or an empty string, a guest-specific location will be used.




  Returns:
    `str <https://docs.python.org/2/library/stdtypes.html>`_:
         The absolute path of the temporary directory that is created.

  Raises:

    `vim.fault.GuestOperationsFault <vim/fault/GuestOperationsFault.rst>`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable <vim/fault/GuestOperationsUnavailable.rst>`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied <vim/fault/GuestPermissionDenied.rst>`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin <vim/fault/InvalidGuestLogin.rst>`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate <vim/fault/GuestComponentsOutOfDate.rst>`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest <vim/fault/OperationNotSupportedByGuest.rst>`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest <vim/fault/OperationDisabledByGuest.rst>`_: 
       if the operation is not enabled due to guest agent configuration.


ListFilesInGuest(vm, auth, filePath, index, maxResults, matchPattern):
   Returns information about files or directories in the guest.The results could be extermely large, so to minimize the size of the return value for cases where a UI only needs to show the first N results, the answer is batched. Files are returned in OS-specific (inode) order. If the directory is modified between queries, missing or duplicate results can occur.


  Privilege:



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_):
       The guest authentication data. See `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ .


    filePath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The complete path to the directory or file to query.


    index (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       Which result to start the list with. The default is 0.


    maxResults (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The maximum number of results to return. The default is 50.


    matchPattern (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       A filter for the return values. Match patterns are specified using perl-compatible regular expressions. If matchPattern is unset, then the pattern '.*' is used.




  Returns:
    `vim.vm.guest.FileManager.ListFileInfo <vim/vm/guest/FileManager/ListFileInfo.rst>`_:
         A `GuestListFileInfo <vim/vm/guest/FileManager/ListFileInfo.rst>`_ object containing information for all the matching files in the filePath and the number of files left to be returned.

  Raises:

    `vim.fault.GuestOperationsFault <vim/fault/GuestOperationsFault.rst>`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       vim.fault.FileFault

    `vim.fault.GuestOperationsUnavailable <vim/fault/GuestOperationsUnavailable.rst>`_: 
       if the VM agent for guest operations is not running.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       If the matchPattern is an invalid regular expression.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied <vim/fault/GuestPermissionDenied.rst>`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin <vim/fault/InvalidGuestLogin.rst>`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate <vim/fault/GuestComponentsOutOfDate.rst>`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest <vim/fault/OperationNotSupportedByGuest.rst>`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest <vim/fault/OperationDisabledByGuest.rst>`_: 
       if the operation is not enabled due to guest agent configuration.


ChangeFileAttributesInGuest(vm, auth, guestFilePath, fileAttributes):
   Changes the file attributes of a specified file inside the guest.


  Privilege:



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_):
       The guest authentication data. See `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ .


    guestFilePath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The complete path to the file to be copied in the guest. If the file points to an symbolic link, then the attributes of the target file are changed.


    fileAttributes (`vim.vm.guest.FileManager.FileAttributes <vim/vm/guest/FileManager/FileAttributes.rst>`_):
       Specifies the different file attributes of the guest file to be changed. See `GuestFileAttributes <vim/vm/guest/FileManager/FileAttributes.rst>`_ . If any property is not specified, then the specific attribute of the file will be unchanged.




  Returns:
    None
         

  Raises:

    `vim.fault.GuestOperationsFault <vim/fault/GuestOperationsFault.rst>`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable <vim/fault/GuestOperationsUnavailable.rst>`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied <vim/fault/GuestPermissionDenied.rst>`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin <vim/fault/InvalidGuestLogin.rst>`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate <vim/fault/GuestComponentsOutOfDate.rst>`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest <vim/fault/OperationNotSupportedByGuest.rst>`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest <vim/fault/OperationDisabledByGuest.rst>`_: 
       if the operation is not enabled due to guest agent configuration.


InitiateFileTransferFromGuest(vm, auth, guestFilePath):
   Initiates an operation to transfer a file from the guest.Obtains a reference to `FileTransferInformation <vim/vm/guest/FileManager/FileTransferInformation.rst>`_ object for the file transfer operation. The information object contains a URL to the file inside the guest to be transferred to the client.See `FileTransferInformation <vim/vm/guest/FileManager/FileTransferInformation.rst>`_ for information on how to use the information object. If the power state of the Virtual Machine is changed when the file transfer is in progress, or the Virtual Machine is migrated, then the transfer operation is aborted.In order to ensure a secure connection to the host when transferring a file using HTTPS, the X.509 certificate for the host must be used to authenticate the remote end of the connection. The certificate of the host that the virtual machine is running on can be retrieved using the following fields: vm ( `VirtualMachine <vim/VirtualMachine.rst>`_ ) -runtime ( `VirtualMachineRuntimeInfo <vim/vm/RuntimeInfo.rst>`_ ) -host ( `HostSystem <vim/HostSystem.rst>`_ ) -config ( `HostConfigInfo <vim/host/ConfigInfo.rst>`_ ) -certificate.


  Privilege:



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_):
       The guest authentication data.


    guestFilePath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The complete path to the file inside the guest that has to be transferred to the client. It cannot be a path to a directory or a symbolic link.




  Returns:
    `vim.vm.guest.FileManager.FileTransferInformation <vim/vm/guest/FileManager/FileTransferInformation.rst>`_:
         A reference to `FileTransferInformation <vim/vm/guest/FileManager/FileTransferInformation.rst>`_ .

  Raises:

    `vim.fault.GuestOperationsFault <vim/fault/GuestOperationsFault.rst>`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable <vim/fault/GuestOperationsUnavailable.rst>`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied <vim/fault/GuestPermissionDenied.rst>`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin <vim/fault/InvalidGuestLogin.rst>`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate <vim/fault/GuestComponentsOutOfDate.rst>`_: 
       If the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest <vim/fault/OperationNotSupportedByGuest.rst>`_: 
       If the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest <vim/fault/OperationDisabledByGuest.rst>`_: 
       If the operation is not enabled due to guest agent configuration.


InitiateFileTransferToGuest(vm, auth, guestFilePath, fileAttributes, fileSize, overwrite):
   Initiates an operation to transfer a file to the guest.Obtains a URL to the file inside the guest to be transferred from the client. The user should send a HTTP PUT request specifying the file content in the body of the request. Multiple PUT request cannot be sent to the URL simultaneously. URL will be invalidated after a successful PUT request is sent. If the power state of the Virtual Machine is changed when the file transfer is in progress, or the Virtual Machine is migrated, then the transfer operation is aborted.In order to ensure a secure connection to the host when transferring a file using HTTPS, the X.509 certificate for the host must be used to authenticate the remote end of the connection. The certificate of the host that the virtual machine is running on can be retrieved using the following fields: vm ( `VirtualMachine <vim/VirtualMachine.rst>`_ ) -runtime ( `VirtualMachineRuntimeInfo <vim/vm/RuntimeInfo.rst>`_ ) -host ( `HostSystem <vim/HostSystem.rst>`_ ) -config ( `HostConfigInfo <vim/host/ConfigInfo.rst>`_ ) -certificate.


  Privilege:



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_):
       The guest authentication data. See `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ .


    guestFilePath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The complete destination path in the guest to transfer the file from the client. It cannot be a path to a directory or a symbolic link.


    fileAttributes (`vim.vm.guest.FileManager.FileAttributes <vim/vm/guest/FileManager/FileAttributes.rst>`_):
       File attributes of the file that has to be created in the guest. See `GuestFileAttributes <vim/vm/guest/FileManager/FileAttributes.rst>`_ . If any file attribute is not specified, then the default value of that property will be set for the file.


    fileSize (`long <https://docs.python.org/2/library/stdtypes.html>`_):
       Size of the file to transfer to the guest in bytes.


    overwrite (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       If set, the destination file is clobbered.




  Returns:
    `str <https://docs.python.org/2/library/stdtypes.html>`_:
         A URL to which the user has to send a PUT request. The host part of the URL is returned as '*' if the hostname to be used is the name of the server to which the call was made. For example, if the call is made to esx-svr-1.domain1.com, and the file can be uploaded to http://esx-svr-1.domain1.com/guestFile?id=1=1234, the URL returned may be http:///guestFile?id=1=1234. The client replaces the asterisk with the server name on which it invoked the call.

  Raises:

    `vim.fault.GuestOperationsFault <vim/fault/GuestOperationsFault.rst>`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable <vim/fault/GuestOperationsUnavailable.rst>`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied <vim/fault/GuestPermissionDenied.rst>`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin <vim/fault/InvalidGuestLogin.rst>`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate <vim/fault/GuestComponentsOutOfDate.rst>`_: 
       If the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest <vim/fault/OperationNotSupportedByGuest.rst>`_: 
       If the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest <vim/fault/OperationDisabledByGuest.rst>`_: 
       If the operation is not enabled due to guest agent configuration.


