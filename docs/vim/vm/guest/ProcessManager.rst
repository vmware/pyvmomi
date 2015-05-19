.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../../vim/Task.rst

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vim.VirtualMachine: ../../../vim/VirtualMachine.rst

.. _StartProgramInGuest: ../../../vim/vm/guest/ProcessManager.rst#startProgram

.. _vim.fault.FileFault: ../../../vim/fault/FileFault.rst

.. _ListProcessesInGuest: ../../../vim/vm/guest/ProcessManager.rst#listProcesses

.. _vim.fault.InvalidState: ../../../vim/fault/InvalidState.rst

.. _vim.fault.FileNotFound: ../../../vim/fault/FileNotFound.rst

.. _vim.fault.TaskInProgress: ../../../vim/fault/TaskInProgress.rst

.. _vim.fault.CannotAccessFile: ../../../vim/fault/CannotAccessFile.rst

.. _vim.fault.InvalidGuestLogin: ../../../vim/fault/InvalidGuestLogin.rst

.. _vim.fault.InvalidPowerState: ../../../vim/fault/InvalidPowerState.rst

.. _vim.fault.GuestOperationsFault: ../../../vim/fault/GuestOperationsFault.rst

.. _vim.fault.GuestProcessNotFound: ../../../vim/fault/GuestProcessNotFound.rst

.. _vim.fault.GuestPermissionDenied: ../../../vim/fault/GuestPermissionDenied.rst

.. _vim.vm.guest.GuestAuthentication: ../../../vim/vm/guest/GuestAuthentication.rst

.. _vim.fault.GuestComponentsOutOfDate: ../../../vim/fault/GuestComponentsOutOfDate.rst

.. _vim.fault.OperationDisabledByGuest: ../../../vim/fault/OperationDisabledByGuest.rst

.. _vim.fault.GuestOperationsUnavailable: ../../../vim/fault/GuestOperationsUnavailable.rst

.. _vim.fault.OperationNotSupportedByGuest: ../../../vim/fault/OperationNotSupportedByGuest.rst

.. _vim.vm.guest.ProcessManager.ProcessInfo: ../../../vim/vm/guest/ProcessManager/ProcessInfo.rst

.. _vim.vm.guest.ProcessManager.ProgramSpec: ../../../vim/vm/guest/ProcessManager/ProgramSpec.rst


vim.vm.guest.ProcessManager
===========================
  ProcessManager is the managed object that provides APIs to manipulate the guest operating system processes.


:since: `vSphere API 5.0`_


Attributes
----------


Methods
-------


StartProgramInGuest(vm, auth, spec):
   Starts a program in the guest operating system.A process started this way can have its status queried with `ListProcessesInGuest`_ . When the process completes, its exit code and end time will be available for 5 minutes after completion.


  Privilege:



  Args:
    vm (`vim.VirtualMachine`_):
       Virtual machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication`_):
       The guest authentication data. See `GuestAuthentication`_ .


    spec (`vim.vm.guest.ProcessManager.ProgramSpec`_):
       The arguments describing the program to be started.




  Returns:
    `long`_:
         The pid of the program started.

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

    `vim.fault.FileNotFound`_: 
       if the program path does not exist.

    `vim.fault.CannotAccessFile`_: 
       if the program path cannot be accessed.

    `vim.fault.GuestPermissionDenied`_: 
       if the program path cannot be run because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest`_: 
       if the operation is not enabled due to guest agent configuration.


ListProcessesInGuest(vm, auth, pids):
   List the processes running in the guest operating system, plus those started by `StartProgramInGuest`_ that have recently completed.


  Privilege:



  Args:
    vm (`vim.VirtualMachine`_):
       Virtual machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication`_):
       The guest authentication data. See `GuestAuthentication`_ .


    pids (`long`_, optional):
       If set, only return information about the specified processes. Otherwise, information about all processes are returned. If a specified processes does not exist, nothing will be returned for that process.




  Returns:
    [`vim.vm.guest.ProcessManager.ProcessInfo`_]:
         The list running processes is returned in an array of `GuestProcessInfo`_ structures.

  Raises:

    `vim.fault.GuestOperationsFault`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress`_: 
       if the virtual machine is busy.

    `vim.fault.GuestOperationsUnavailable`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied`_: 
       if there are insufficient permissions in the guest OS.

    `vim.fault.InvalidGuestLogin`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest`_: 
       if the operation is not enabled due to guest agent configuration.


TerminateProcessInGuest(vm, auth, pid):
   Terminates a process in the guest OS.


  Privilege:



  Args:
    vm (`vim.VirtualMachine`_):
       Virtual machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication`_):
       The guest authentication data. See `GuestAuthentication`_ .


    pid (`long`_):
       Process ID of the process to be terminated




  Returns:
    None
         

  Raises:

    `vim.fault.GuestOperationsFault`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress`_: 
       if the virtual machine is busy.

    `vim.fault.GuestOperationsUnavailable`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState`_: 
       if the VM is not powered on.

    `vim.fault.GuestProcessNotFound`_: 
       if the pid does not refer to a valid process.

    `vim.fault.GuestPermissionDenied`_: 
       if the process cannot be terminated because the guest authentication will not allow the operation.

    `vim.fault.InvalidGuestLogin`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest`_: 
       if the operation is not enabled due to guest agent configuration.


ReadEnvironmentVariableInGuest(vm, auth, names):
   Reads an environment variable from the guest OSIf the authentication uses interactiveSession, then the environment being read will be that of the user logged into the desktop. Otherwise it's the environment of the system user.


  Privilege:



  Args:
    vm (`vim.VirtualMachine`_):
       Virtual machine to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication`_):
       The guest authentication data. See `GuestAuthentication`_ .


    names (`str`_, optional):
       The names of the variables to be read. If not set, then all the environment variables are returned.




  Returns:
    [`str`_]:
         A string array containing the value of the variables, or all environment variables if nothing is specified. The format of each string is "name=value". If any specified environment variable isn't set, then nothing is returned for that variable.

  Raises:

    `vim.fault.GuestOperationsFault`_: 
       if there is an error processing a guest operation.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.TaskInProgress`_: 
       if the virtual machine is busy. accepted by the guest OS.

    `vim.fault.GuestOperationsUnavailable`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState`_: 
       if the VM is not powered on.

    `vim.fault.GuestPermissionDenied`_: 
       if there are insufficient permissions in the guest OS.

    `vim.fault.InvalidGuestLogin`_: 
       if the the guest authentication information was not accepted.

    `vim.fault.GuestComponentsOutOfDate`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest`_: 
       if the operation is not enabled due to guest agent configuration.


