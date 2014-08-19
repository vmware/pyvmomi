
vim.vm.guest.ProcessManager
===========================
  ProcessManager is the managed object that provides APIs to manipulate the guest operating system processes.


:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


Attributes
----------


Methods
-------


StartProgramInGuest(vm, auth, spec):
   Starts a program in the guest operating system.A process started this way can have its status queried with `ListProcessesInGuest <vim/vm/guest/ProcessManager.rst#listProcesses>`_ . When the process completes, its exit code and end time will be available for 5 minutes after completion.


  Privilege:



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       Virtual machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_):
       The guest authentication data. See `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ .


    spec (`vim.vm.guest.ProcessManager.ProgramSpec <vim/vm/guest/ProcessManager/ProgramSpec.rst>`_):
       The arguments describing the program to be started.




  Returns:
    `long <https://docs.python.org/2/library/stdtypes.html>`_:
         The pid of the program started.

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

    `vim.fault.FileNotFound <vim/fault/FileNotFound.rst>`_: 
       if the program path does not exist.

    `vim.fault.CannotAccessFile <vim/fault/CannotAccessFile.rst>`_: 
       if the program path cannot be accessed.

    `vim.fault.GuestPermissionDenied <vim/fault/GuestPermissionDenied.rst>`_: 
       if the program path cannot be run because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin <vim/fault/InvalidGuestLogin.rst>`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate <vim/fault/GuestComponentsOutOfDate.rst>`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest <vim/fault/OperationNotSupportedByGuest.rst>`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest <vim/fault/OperationDisabledByGuest.rst>`_: 
       if the operation is not enabled due to guest agent configuration.


ListProcessesInGuest(vm, auth, pids):
   List the processes running in the guest operating system, plus those started by `StartProgramInGuest <vim/vm/guest/ProcessManager.rst#startProgram>`_ that have recently completed.


  Privilege:



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       Virtual machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_):
       The guest authentication data. See `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ .


    pids (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       If set, only return information about the specified processes. Otherwise, information about all processes are returned. If a specified processes does not exist, nothing will be returned for that process.




  Returns:
    [`vim.vm.guest.ProcessManager.ProcessInfo <vim/vm/guest/ProcessManager/ProcessInfo.rst>`_]:
         The list running processes is returned in an array of `GuestProcessInfo <vim/vm/guest/ProcessManager/ProcessInfo.rst>`_ structures.

  Raises:

    `vim.fault.GuestOperationsFault <vim/fault/GuestOperationsFault.rst>`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.GuestOperationsUnavailable <vim/fault/GuestOperationsUnavailable.rst>`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied <vim/fault/GuestPermissionDenied.rst>`_: 
       if there are insufficient permissions in the guest OS.

    `vim.fault.InvalidGuestLogin <vim/fault/InvalidGuestLogin.rst>`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate <vim/fault/GuestComponentsOutOfDate.rst>`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest <vim/fault/OperationNotSupportedByGuest.rst>`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest <vim/fault/OperationDisabledByGuest.rst>`_: 
       if the operation is not enabled due to guest agent configuration.


TerminateProcessInGuest(vm, auth, pid):
   Terminates a process in the guest OS.


  Privilege:



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       Virtual machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_):
       The guest authentication data. See `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ .


    pid (`long <https://docs.python.org/2/library/stdtypes.html>`_):
       Process ID of the process to be terminated




  Returns:
    None
         

  Raises:

    `vim.fault.GuestOperationsFault <vim/fault/GuestOperationsFault.rst>`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.GuestOperationsUnavailable <vim/fault/GuestOperationsUnavailable.rst>`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the VM is not powered on.

    `vim.fault.GuestProcessNotFound <vim/fault/GuestProcessNotFound.rst>`_: 
       if the pid does not refer to a valid process.

    `vim.fault.GuestPermissionDenied <vim/fault/GuestPermissionDenied.rst>`_: 
       if the process cannot be terminated because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin <vim/fault/InvalidGuestLogin.rst>`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate <vim/fault/GuestComponentsOutOfDate.rst>`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest <vim/fault/OperationNotSupportedByGuest.rst>`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest <vim/fault/OperationDisabledByGuest.rst>`_: 
       if the operation is not enabled due to guest agent configuration.


ReadEnvironmentVariableInGuest(vm, auth, names):
   Reads an environment variable from the guest OSIf the authentication uses interactiveSession, then the environment being read will be that of the user logged into the desktop. Otherwise it's the environment of the system user.


  Privilege:



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       Virtual machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_):
       The guest authentication data. See `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ .


    names (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The names of the variables to be read. If not set, then all the environment variables are returned.




  Returns:
    [`str <https://docs.python.org/2/library/stdtypes.html>`_]:
         A string array containing the value of the variables, or all environment variables if nothing is specified. The format of each string is "name=value". If any specified environment variable isn't set, then nothing is returned for that variable.

  Raises:

    `vim.fault.GuestOperationsFault <vim/fault/GuestOperationsFault.rst>`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy. accepted by the guest OS.

    `vim.fault.GuestOperationsUnavailable <vim/fault/GuestOperationsUnavailable.rst>`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied <vim/fault/GuestPermissionDenied.rst>`_: 
       if there are insufficient permissions in the guest OS.

    `vim.fault.InvalidGuestLogin <vim/fault/InvalidGuestLogin.rst>`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate <vim/fault/GuestComponentsOutOfDate.rst>`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest <vim/fault/OperationNotSupportedByGuest.rst>`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest <vim/fault/OperationDisabledByGuest.rst>`_: 
       if the operation is not enabled due to guest agent configuration.


