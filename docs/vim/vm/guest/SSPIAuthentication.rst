.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _StartProgramInGuest: ../../../vim/vm/guest/ProcessManager.rst#startProgram

.. _AcquireCredentialsInGuest: ../../../vim/vm/guest/AuthManager.rst#acquireCredentials

.. _ReleaseCredentialsInGuest: ../../../vim/vm/guest/AuthManager.rst#releaseCredentials

.. _GuestAuthenticationChallenge: ../../../vim/fault/GuestAuthenticationChallenge.rst

.. _TicketedSessionAuthentication: ../../../vim/vm/guest/TicketedSessionAuthentication.rst

.. _vim.vm.guest.GuestAuthentication: ../../../vim/vm/guest/GuestAuthentication.rst


vim.vm.guest.SSPIAuthentication
===============================
  SSPIAuthentication contains the information necessary to initiate a ticketed authentication session in the guest using SSPI credentials. The ticketed session is not stateless and stores state inside of the guest.To use SSPIAuthentication, populate sspiToken with a base64 encoded SSPI token. Then call `AcquireCredentialsInGuest`_ with the SSPIAuthentication object and no sessionID. After issuing the `AcquireCredentialsInGuest`_ call, a `GuestAuthenticationChallenge`_ will be thrown. Use the serverChallenge sspiToken in `GuestAuthenticationChallenge`_ to generate the proper SSPI response token. Populate an SSPIAuthentication object with the base64 encoded SSPI response token, and call `AcquireCredentialsInGuest`_ with the SSPIAuthentication object and the sessionID found in `GuestAuthenticationChallenge`_ .Successful authentication will result in a `TicketedSessionAuthentication`_ object being returned. You can use the `TicketedSessionAuthentication`_ in any guest operations function call. You should NOT attempt to use SSPIAuthentication in any guest operations function call.When you no longer need the `TicketedSessionAuthentication`_ object, you should call `ReleaseCredentialsInGuest`_ to free associated resources and session data.Usage notes: SSPI authentication has the same limitations as a duplicated primary token obtained from the Windows API function LogonUser with the LOGON32_LOGON_NETWORK logon type. This will affect programs started with `StartProgramInGuest`_ . For example, launched programs will be unable to use WMI functions unless the "Remote Enable" privilege is enabled for the user. Similarly, access to network resources may fail due to the limitations of the token.
:extends: vim.vm.guest.GuestAuthentication_
:since: `vSphere API 5.0`_

Attributes:
    sspiToken (`str`_):

       This contains a base64 encoded SSPI Token.
