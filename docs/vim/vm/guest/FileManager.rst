.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../../vim/Task.rst

.. _HostSystem: ../../../vim/HostSystem.rst

.. _VirtualMachine: ../../../vim/VirtualMachine.rst

.. _HostConfigInfo: ../../../vim/host/ConfigInfo.rst

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vim.VirtualMachine: ../../../vim/VirtualMachine.rst

.. _vim.fault.NotAFile: ../../../vim/fault/NotAFile.rst

.. _vim.fault.FileFault: ../../../vim/fault/FileFault.rst

.. _vim.fault.InvalidState: ../../../vim/fault/InvalidState.rst

.. _vim.fault.NotADirectory: ../../../vim/fault/NotADirectory.rst

.. _FileTransferInformation: ../../../vim/vm/guest/FileManager/FileTransferInformation.rst

.. _vim.fault.TaskInProgress: ../../../vim/fault/TaskInProgress.rst

.. _VirtualMachineRuntimeInfo: ../../../vim/vm/RuntimeInfo.rst

.. _vim.fault.InvalidGuestLogin: ../../../vim/fault/InvalidGuestLogin.rst

.. _vmodl.fault.InvalidArgument: ../../../vmodl/fault/InvalidArgument.rst

.. _vim.fault.FileAlreadyExists: ../../../vim/fault/FileAlreadyExists.rst

.. _vim.fault.InvalidPowerState: ../../../vim/fault/InvalidPowerState.rst

.. _vim.fault.GuestOperationsFault: ../../../vim/fault/GuestOperationsFault.rst

.. _vim.fault.GuestPermissionDenied: ../../../vim/fault/GuestPermissionDenied.rst

.. _vim.vm.guest.GuestAuthentication: ../../../vim/vm/guest/GuestAuthentication.rst

.. _vim.fault.GuestComponentsOutOfDate: ../../../vim/fault/GuestComponentsOutOfDate.rst

.. _vim.fault.OperationDisabledByGuest: ../../../vim/fault/OperationDisabledByGuest.rst

.. _vim.fault.GuestOperationsUnavailable: ../../../vim/fault/GuestOperationsUnavailable.rst

.. _vim.vm.guest.FileManager.ListFileInfo: ../../../vim/vm/guest/FileManager/ListFileInfo.rst

.. _vim.fault.OperationNotSupportedByGuest: ../../../vim/fault/OperationNotSupportedByGuest.rst

.. _vim.vm.guest.FileManager.FileAttributes: ../../../vim/vm/guest/FileManager/FileAttributes.rst

.. _vim.vm.guest.FileManager.FileTransferInformation: ../../../vim/vm/guest/FileManager/FileTransferInformation.rst


vim.vm.guest.FileManager
========================
  FileManager is the managed object that provides APIs to manipulate the guest operating system files.


:since: `vSphere API 5.0`_


Attributes
----------


Methods
-------


MakeDirectoryInGuest(vm, auth, directoryPath, createParentDirectories):
   Creates a directory in the guest OS


  Privilege:



  Args:
    vm (`vim.VirtualMachine`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication`_):
       The guest authentication data. See `GuestAuthentication`_ .


    directoryPath (`str`_):
       The complete path to the directory to be created.


    createParentDirectories (`bool`_):
       Whether any parent directories are to be created.




  Returns:
    None
         

  Raises:

    `vim.fault.GuestOperationsFault`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied`_: 
       if the directory cannot be created because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.FileAlreadyExists`_: 
       if the specified object already exists.

    `vim.fault.GuestComponentsOutOfDate`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest`_: 
       if the operation is not enabled due to guest agent configuration.


DeleteFileInGuest(vm, auth, filePath):
   Deletes a file in the guest OS


  Privilege:



  Args:
    vm (`vim.VirtualMachine`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication`_):
       The guest authentication data. See `GuestAuthentication`_ .


    filePath (`str`_):
       The complete path to the file or symbolic link to be deleted.




  Returns:
    None
         

  Raises:

    `vim.fault.GuestOperationsFault`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.NotAFile`_: 
       if the specified object is not a file.

    `vim.fault.GuestComponentsOutOfDate`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest`_: 
       if the operation is not enabled due to guest agent configuration.


DeleteDirectoryInGuest(vm, auth, directoryPath, recursive):
   Deletes a directory in the guest OS.


  Privilege:



  Args:
    vm (`vim.VirtualMachine`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication`_):
       The guest authentication data. See `GuestAuthentication`_ .


    directoryPath (`str`_):
       The complete path to the directory to be deleted.


    recursive (`bool`_):
       If true, all subdirectories are also deleted. If false, the directory must be empty for the operation to succeed.




  Returns:
    None
         

  Raises:

    `vim.fault.GuestOperationsFault`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.NotADirectory`_: 
       if the specified object is not a directory.

    `vim.fault.GuestComponentsOutOfDate`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest`_: 
       if the operation is not enabled due to guest agent configuration.


MoveDirectoryInGuest(vm, auth, srcDirectoryPath, dstDirectoryPath):
   Moves or renames a directory in the guest.


  Privilege:



  Args:
    vm (`vim.VirtualMachine`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication`_):
       The guest authentication data. See `GuestAuthentication`_ .


    srcDirectoryPath (`str`_):
       The complete path to the directory to be moved.


    dstDirectoryPath (`str`_):
       The complete path to the where the directory is moved or its new name. It cannot be a path to an existing directory or an existing file.




  Returns:
    None
         

  Raises:

    `vim.fault.GuestOperationsFault`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest`_: 
       if the operation is not enabled due to guest agent configuration.


MoveFileInGuest(vm, auth, srcFilePath, dstFilePath, overwrite):
   Renames a file in the guest.


  Privilege:



  Args:
    vm (`vim.VirtualMachine`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication`_):
       The guest authentication data. See `GuestAuthentication`_ .


    srcFilePath (`str`_):
       The complete path to the original file or symbolic link to be moved.


    dstFilePath (`str`_):
       The complete path to the where the file is renamed. It cannot be a path to an existing diectory.


    overwrite (`bool`_):
       If set, the destination file is clobbered.




  Returns:
    None
         

  Raises:

    `vim.fault.GuestOperationsFault`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest`_: 
       if the operation is not enabled due to guest agent configuration.


CreateTemporaryFileInGuest(vm, auth, prefix, suffix, directoryPath):
   Creates a temporary file.Creates a new unique temporary file for the user to use as needed. The user is responsible for removing it when it is no longer needed.


  Privilege:



  Args:
    vm (`vim.VirtualMachine`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication`_):
       The guest authentication data. See `GuestAuthentication`_ .


    prefix (`str`_):
       The prefix to be given to the new temporary file.


    suffix (`str`_):
       The suffix to be given to the new temporary file.


    directoryPath (`str`_, optional):
       The complete path to the directory in which to create the file. If unset, or an empty string, a guest-specific location will be used.




  Returns:
    `str`_:
         The absolute path of the temporary file that is created.

  Raises:

    `vim.fault.GuestOperationsFault`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest`_: 
       if the operation is not enabled due to guest agent configuration.


CreateTemporaryDirectoryInGuest(vm, auth, prefix, suffix, directoryPath):
   Creates a temporary directory.Creates a new unique temporary directory for the user to use as needed. The user is responsible for removing it when it is no longer needed.


  Privilege:



  Args:
    vm (`vim.VirtualMachine`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication`_):
       The guest authentication data. See `GuestAuthentication`_ .


    prefix (`str`_):
       The prefix to be given to the new temporary directory.


    suffix (`str`_):
       The suffix to be given to the new temporary directory.


    directoryPath (`str`_, optional):
       The complete path to the directory in which to create the new directory. If unset or an empty string, a guest-specific location will be used.




  Returns:
    `str`_:
         The absolute path of the temporary directory that is created.

  Raises:

    `vim.fault.GuestOperationsFault`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest`_: 
       if the operation is not enabled due to guest agent configuration.


ListFilesInGuest(vm, auth, filePath, index, maxResults, matchPattern):
   Returns information about files or directories in the guest.The results could be extermely large, so to minimize the size of the return value for cases where a UI only needs to show the first N results, the answer is batched. Files are returned in OS-specific (inode) order. If the directory is modified between queries, missing or duplicate results can occur.


  Privilege:



  Args:
    vm (`vim.VirtualMachine`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication`_):
       The guest authentication data. See `GuestAuthentication`_ .


    filePath (`str`_):
       The complete path to the directory or file to query.


    index (`int`_, optional):
       Which result to start the list with. The default is 0.


    maxResults (`int`_, optional):
       The maximum number of results to return. The default is 50.


    matchPattern (`str`_, optional):
       A filter for the return values. Match patterns are specified using perl-compatible regular expressions. If matchPattern is unset, then the pattern '.*' is used.




  Returns:
    `vim.vm.guest.FileManager.ListFileInfo`_:
         A `GuestListFileInfo`_ object containing information for all the matching files in the filePath and the number of files left to be returned.

  Raises:

    `vim.fault.GuestOperationsFault`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault`_: 
       vim.fault.FileFault

    `vim.fault.GuestOperationsUnavailable`_: 
       if the VM agent for guest operations is not running.

    `vmodl.fault.InvalidArgument`_: 
       If the matchPattern is an invalid regular expression.

    `vim.fault.InvalidPowerState`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest`_: 
       if the operation is not enabled due to guest agent configuration.


ChangeFileAttributesInGuest(vm, auth, guestFilePath, fileAttributes):
   Changes the file attributes of a specified file inside the guest.


  Privilege:



  Args:
    vm (`vim.VirtualMachine`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication`_):
       The guest authentication data. See `GuestAuthentication`_ .


    guestFilePath (`str`_):
       The complete path to the file to be copied in the guest. If the file points to an symbolic link, then the attributes of the target file are changed.


    fileAttributes (`vim.vm.guest.FileManager.FileAttributes`_):
       Specifies the different file attributes of the guest file to be changed. See `GuestFileAttributes`_ . If any property is not specified, then the specific attribute of the file will be unchanged.




  Returns:
    None
         

  Raises:

    `vim.fault.GuestOperationsFault`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest`_: 
       if the operation is not enabled due to guest agent configuration.


InitiateFileTransferFromGuest(vm, auth, guestFilePath):
   Initiates an operation to transfer a file from the guest.Obtains a reference to `FileTransferInformation`_ object for the file transfer operation. The information object contains a URL to the file inside the guest to be transferred to the client.See `FileTransferInformation`_ for information on how to use the information object. If the power state of the Virtual Machine is changed when the file transfer is in progress, or the Virtual Machine is migrated, then the transfer operation is aborted.In order to ensure a secure connection to the host when transferring a file using HTTPS, the X.509 certificate for the host must be used to authenticate the remote end of the connection. The certificate of the host that the virtual machine is running on can be retrieved using the following fields: vm ( `VirtualMachine`_ ) -runtime ( `VirtualMachineRuntimeInfo`_ ) -host ( `HostSystem`_ ) -config ( `HostConfigInfo`_ ) -certificate.


  Privilege:



  Args:
    vm (`vim.VirtualMachine`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication`_):
       The guest authentication data.


    guestFilePath (`str`_):
       The complete path to the file inside the guest that has to be transferred to the client. It cannot be a path to a directory or a symbolic link.




  Returns:
    `vim.vm.guest.FileManager.FileTransferInformation`_:
         A reference to `FileTransferInformation`_ .

  Raises:

    `vim.fault.GuestOperationsFault`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate`_: 
       If the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest`_: 
       If the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest`_: 
       If the operation is not enabled due to guest agent configuration.


InitiateFileTransferToGuest(vm, auth, guestFilePath, fileAttributes, fileSize, overwrite):
   Initiates an operation to transfer a file to the guest.Obtains a URL to the file inside the guest to be transferred from the client. The user should send a HTTP PUT request specifying the file content in the body of the request. Multiple PUT request cannot be sent to the URL simultaneously. URL will be invalidated after a successful PUT request is sent. If the power state of the Virtual Machine is changed when the file transfer is in progress, or the Virtual Machine is migrated, then the transfer operation is aborted.In order to ensure a secure connection to the host when transferring a file using HTTPS, the X.509 certificate for the host must be used to authenticate the remote end of the connection. The certificate of the host that the virtual machine is running on can be retrieved using the following fields: vm ( `VirtualMachine`_ ) -runtime ( `VirtualMachineRuntimeInfo`_ ) -host ( `HostSystem`_ ) -config ( `HostConfigInfo`_ ) -certificate.


  Privilege:



  Args:
    vm (`vim.VirtualMachine`_):
       Virtual Machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication`_):
       The guest authentication data. See `GuestAuthentication`_ .


    guestFilePath (`str`_):
       The complete destination path in the guest to transfer the file from the client. It cannot be a path to a directory or a symbolic link.


    fileAttributes (`vim.vm.guest.FileManager.FileAttributes`_):
       File attributes of the file that has to be created in the guest. See `GuestFileAttributes`_ . If any file attribute is not specified, then the default value of that property will be set for the file.


    fileSize (`long`_):
       Size of the file to transfer to the guest in bytes.


    overwrite (`bool`_):
       If set, the destination file is clobbered.




  Returns:
    `str`_:
         A URL to which the user has to send a PUT request. The host part of the URL is returned as '*' if the hostname to be used is the name of the server to which the call was made. For example, if the call is made to esx-svr-1.domain1.com, and the file can be uploaded to http://esx-svr-1.domain1.com/guestFile?id=1=1234, the URL returned may be http:///guestFile?id=1=1234. The client replaces the asterisk with the server name on which it invoked the call.

  Raises:

    `vim.fault.GuestOperationsFault`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress`_: 
       if the virtual machine is busy.

    `vim.fault.FileFault`_: 
       if there is a file error in the guest operating system.

    `vim.fault.GuestOperationsUnavailable`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied`_: 
       if the operation fails because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate`_: 
       If the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest`_: 
       If the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest`_: 
       If the operation is not enabled due to guest agent configuration.


