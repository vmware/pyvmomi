.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../../vim/Task.rst

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _SSPIAuthentication: ../../../vim/vm/guest/SSPIAuthentication.rst

.. _vim.VirtualMachine: ../../../vim/VirtualMachine.rst

.. _GuestAuthentication: ../../../vim/vm/guest/GuestAuthentication.rst

.. _GuestPermissionDenied: ../../../vim/fault/GuestPermissionDenied.rst

.. _vim.fault.InvalidState: ../../../vim/fault/InvalidState.rst

.. _vim.fault.TaskInProgress: ../../../vim/fault/TaskInProgress.rst

.. _AcquireCredentialsInGuest: ../../../vim/vm/guest/AuthManager.rst#acquireCredentials

.. _NamePasswordAuthentication: ../../../vim/vm/guest/NamePasswordAuthentication.rst

.. _vim.fault.InvalidGuestLogin: ../../../vim/fault/InvalidGuestLogin.rst

.. _vim.fault.InvalidPowerState: ../../../vim/fault/InvalidPowerState.rst

.. _vim.fault.TooManyGuestLogons: ../../../vim/fault/TooManyGuestLogons.rst

.. _TicketedSessionAuthentication: ../../../vim/vm/guest/TicketedSessionAuthentication.rst

.. _vim.fault.GuestOperationsFault: ../../../vim/fault/GuestOperationsFault.rst

.. _vim.vm.guest.GuestAuthentication: ../../../vim/vm/guest/GuestAuthentication.rst

.. _vim.fault.GuestComponentsOutOfDate: ../../../vim/fault/GuestComponentsOutOfDate.rst

.. _vim.fault.OperationDisabledByGuest: ../../../vim/fault/OperationDisabledByGuest.rst

.. _vim.fault.GuestOperationsUnavailable: ../../../vim/fault/GuestOperationsUnavailable.rst

.. _vim.fault.OperationNotSupportedByGuest: ../../../vim/fault/OperationNotSupportedByGuest.rst

.. _vim.fault.GuestAuthenticationChallenge: ../../../vim/fault/GuestAuthenticationChallenge.rst


vim.vm.guest.AuthManager
========================
  AuthManager is the managed object that provides APIs to manipulate the guest operating authentication.


:since: `vSphere API 5.0`_


Attributes
----------


Methods
-------


ValidateCredentialsInGuest(vm, auth):
   Validates the `GuestAuthentication`_ credentials.This can be used to check the authentication data, or validate any authetication that has a timeout is still valid. If the authentication is not valid, `GuestPermissionDenied`_ will be thrown.


  Privilege:



  Args:
    vm (`vim.VirtualMachine`_):
       MoRef of the VM to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication`_):
       The guest authentication data. See `GuestAuthentication`_ .




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

    `vim.fault.GuestComponentsOutOfDate`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest`_: 
       if the operation is not enabled due to guest agent configuration.

    `vim.fault.InvalidGuestLogin`_: 
       if the the guest authentication information was not accepted.


AcquireCredentialsInGuest(vm, requestedAuth, sessionID):
   Authenticates in the guest and returns a `GuestAuthentication`_ object with the acquired credentials for use in subsequent guest operation calls.This can be used to authenticate inside the guest and obtain a `GuestAuthentication`_ object for supported authentication types. This operation is not needed for Name and Password Authentication. To use Name and Password Authentication, see `NamePasswordAuthentication`_ . For SSPI authentication, requestAuth should be of the type `SSPIAuthentication`_ .


  Privilege:



  Args:
    vm (`vim.VirtualMachine`_):
       MoRef of the VM to perform the operation on.


    requestedAuth (`vim.vm.guest.GuestAuthentication`_):
       The guest authentication data used to acquire credentials. See `GuestAuthentication`_ .


    sessionID (`long`_, optional):
       The sessionID number should be provided only when responding to a server challenge. The sessionID number to be used with the challenge is found in the `GuestAuthenticationChallenge`_ object.




  Returns:
    `vim.vm.guest.GuestAuthentication`_:
         Returns a `GuestAuthentication`_ object that can be used in guest operation calls.

  Raises:

    `vim.fault.GuestOperationsFault`_: 
       if there is an error processing a guest operation.

    `vim.fault.TaskInProgress`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.GuestOperationsUnavailable`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState`_: 
       if the VM is not powered on.

    `vim.fault.GuestAuthenticationChallenge`_: 
       if the credential information provided requires a challenge to authenticate.

    `vim.fault.GuestComponentsOutOfDate`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest`_: 
       if the operation is not enabled due to guest agent configuration.

    `vim.fault.TooManyGuestLogons`_: 
       if there are too many concurrent login sessions active in the guest.

    `vim.fault.InvalidGuestLogin`_: 
       if the the guest authentication information was not accepted.


ReleaseCredentialsInGuest(vm, auth):
   Releases session data and resources associated with a `GuestAuthentication`_ object returned by `AcquireCredentialsInGuest`_ .This frees any resources and session data associated with a `GuestAuthentication`_ object returned by `AcquireCredentialsInGuest`_ . The `GuestAuthentication`_ object can no longer be used to authenticate in the guest once released. Currently this operation is only valid for `TicketedSessionAuthentication`_ objects.


  Privilege:



  Args:
    vm (`vim.VirtualMachine`_):
       MoRef of the VM to perform the operation on.


    auth (`vim.vm.guest.GuestAuthentication`_):
       The guest authentication data. See `GuestAuthentication`_ .




  Returns:
    None
         

  Raises:

    `vim.fault.GuestOperationsFault`_: 
       if there is an error processing a guest operation.

    `vim.fault.TaskInProgress`_: 
       if the virtual machine is busy.

    `vim.fault.InvalidState`_: 
       if the operation cannot be performed because of the virtual machine's current state.

    `vim.fault.GuestOperationsUnavailable`_: 
       if the VM agent for guest operations is not running.

    `vim.fault.InvalidPowerState`_: 
       if the VM is not powered on.

    `vim.fault.GuestComponentsOutOfDate`_: 
       if the guest agent is too old to support the operation.

    `vim.fault.OperationNotSupportedByGuest`_: 
       if the operation is not supported by the guest OS.

    `vim.fault.OperationDisabledByGuest`_: 
       if the operation is not enabled due to guest agent configuration.

    `vim.fault.InvalidGuestLogin`_: 
       if the the guest authentication information was not accepted.


