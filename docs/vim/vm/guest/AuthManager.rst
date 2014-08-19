
vim.vm.guest.AuthManager
========================
  AuthManager is the managed object that provides APIs to manipulate the guest operating authentication.


:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


Attributes
----------


Methods
-------


ValidateCredentialsInGuest(vm, auth):
   Validates the `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ credentials.This can be used to check the authentication data, or validate any authetication that has a timeout is still valid. If the authentication is not valid, `GuestPermissionDenied <vim/fault/GuestPermissionDenied.rst>`_ will be thrown.


  Privilege:



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       MoRef of the VM to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_):
       The guest authentication data. See `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ .




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

    `vim.fault.GuestComponentsOutOfDate <vim/fault/GuestComponentsOutOfDate.rst>`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest <vim/fault/OperationNotSupportedByGuest.rst>`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest <vim/fault/OperationDisabledByGuest.rst>`_: 
       if the operation is not enabled due to guest agent configuration.

    `vim.fault.InvalidGuestLogin <vim/fault/InvalidGuestLogin.rst>`_: 
       if the the guest authentication information was not accepted.


AcquireCredentialsInGuest(vm, requestedAuth, sessionID):
   Authenticates in the guest and returns a `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ object with the acquired credentials for use in subsequent guest operation calls.This can be used to authenticate inside the guest and obtain a `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ object for supported authentication types. This operation is not needed for Name and Password Authentication. To use Name and Password Authentication, see `NamePasswordAuthentication <vim/vm/guest/NamePasswordAuthentication.rst>`_ . For SSPI authentication, requestAuth should be of the type `SSPIAuthentication <vim/vm/guest/SSPIAuthentication.rst>`_ .


  Privilege:



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       MoRef of the VM to perform the operation on.


    requestedAuth (`vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_):
       The guest authentication data used to acquire credentials. See `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ .


    sessionID (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The sessionID number should be provided only when responding to a server challenge. The sessionID number to be used with the challenge is found in the `GuestAuthenticationChallenge <vim/fault/GuestAuthenticationChallenge.rst>`_ object.




  Returns:
    `vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_:
         Returns a `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ object that can be used in guest operation calls.

  Raises:

    `vim.fault.GuestOperationsFault <vim/fault/GuestOperationsFault.rst>`_: 
       if there is an error processing a guest operation.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.GuestOperationsUnavailable <vim/fault/GuestOperationsUnavailable.rst>`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the VM is not powered on.

    `vim.fault.GuestAuthenticationChallenge <vim/fault/GuestAuthenticationChallenge.rst>`_: 
       if the credential information provided requires a challenge to authenticate.

    `vim.fault.GuestComponentsOutOfDate <vim/fault/GuestComponentsOutOfDate.rst>`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest <vim/fault/OperationNotSupportedByGuest.rst>`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest <vim/fault/OperationDisabledByGuest.rst>`_: 
       if the operation is not enabled due to guest agent configuration.

    `vim.fault.TooManyGuestLogons <vim/fault/TooManyGuestLogons.rst>`_: 
       if there are too many concurrent login sessions active in the guest.

    `vim.fault.InvalidGuestLogin <vim/fault/InvalidGuestLogin.rst>`_: 
       if the the guest authentication information was not accepted.


ReleaseCredentialsInGuest(vm, auth):
   Releases session data and resources associated with a `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ object returned by `AcquireCredentialsInGuest <vim/vm/guest/AuthManager.rst#acquireCredentials>`_ .This frees any resources and session data associated with a `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ object returned by `AcquireCredentialsInGuest <vim/vm/guest/AuthManager.rst#acquireCredentials>`_ . The `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ object can no longer be used to authenticate in the guest once released. Currently this operation is only valid for `TicketedSessionAuthentication <vim/vm/guest/TicketedSessionAuthentication.rst>`_ objects.


  Privilege:



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       MoRef of the VM to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_):
       The guest authentication data. See `GuestAuthentication <vim/vm/guest/GuestAuthentication.rst>`_ .




  Returns:
    None
         

  Raises:

    `vim.fault.GuestOperationsFault <vim/fault/GuestOperationsFault.rst>`_: 
       if there is an error processing a guest operation.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.GuestOperationsUnavailable <vim/fault/GuestOperationsUnavailable.rst>`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState <vim/fault/InvalidPowerState.rst>`_: 
       if the VM is not powered on.

    `vim.fault.GuestComponentsOutOfDate <vim/fault/GuestComponentsOutOfDate.rst>`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest <vim/fault/OperationNotSupportedByGuest.rst>`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest <vim/fault/OperationDisabledByGuest.rst>`_: 
       if the operation is not enabled due to guest agent configuration.

    `vim.fault.InvalidGuestLogin <vim/fault/InvalidGuestLogin.rst>`_: 
       if the the guest authentication information was not accepted.


