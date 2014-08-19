
vim.SessionManager
==================
  This managed object type includes methods for logging on and logging off clients, determining which clients are currently logged on, and forcing clients to log off.




Attributes
----------
    sessionList ([`vim.UserSession <vim/UserSession.rst>`_]):
      privilege: Sessions.TerminateSession
       The list of currently active sessions.
    currentSession (`vim.UserSession <vim/UserSession.rst>`_):
      privilege: System.Anonymous
       This property contains information about the client's current session. If the client is not logged on, the value is null.
    message (`str <https://docs.python.org/2/library/stdtypes.html>`_):
      privilege: System.View
       The system global message from the server.
    messageLocaleList ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):
      privilege: System.Anonymous
       Provides the list of locales for which the server has localized messages.
    supportedLocaleList ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):
      privilege: System.Anonymous
       Provides the list of locales that the server supports. Listing a locale ensures that some standardized information such as dates appear in the appropriate format. Other localized information, such as error messages, are displayed, if available. If localized information is not available, the message is returned using the system locale.
    defaultLocale (`str <https://docs.python.org/2/library/stdtypes.html>`_):
      privilege: System.Anonymous
       This is the default server locale.


Methods
-------


UpdateServiceMessage(message):
   Updates the system global message. If not blank, the message is immediately displayed to currently logged-on users. When set, the message is shown by new clients upon logging in.


  Privilege:
               Sessions.GlobalMessage



  Args:
    message (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The message to send. Newline characters may be included.




  Returns:
    None
         


LoginByToken(locale):
   Log on to the server through token representing principal identity. The token is obtained from SSO (single sign-on) service. This method fails if the token is not valid, or the principal has no permissions granted. Two type of sso tokens are supported by this method: Bearer and Holder-of-Key (HoK). If the token type obliges the method caller to prove his rights to present this token (HoK), then a signature is supplied as well. The token and the security signature if available are provided in a transport specific way.If the communication with the VirtualCenter is SOAP based read the WS-Security specification (SAML Token profile) to understand how to transport the SSO token and signature.Usual login scenario:
    * Acquire HoK token from the SSO service. Different authentication mechanisms are available for acquiring token (user/password, certificate, SSPI and so on). For more details consult the SSO documentation. To find the location of your SSO service consult the Virtual Infrastructure documentation.
    * Once SSO token is acquired successfully
    * `LoginByToken <vim/SessionManager.rst#loginByToken>`_
    * could be invoked.
  since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_


  Privilege:
               System.Anonymous



  Args:
    locale (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       A two-character ISO-639 language ID (like "en") optionally followed by an underscore and a two-character ISO 3166 country ID (like "US").Examples are "de", "fr_CA", "zh", "zh_CN", and "zh_TW". Note: The method uses the server default locale when a locale is not provided. This default can be configured in the server configuration file. If unspecified, it defaults to the locale of the server environment or English ("en") if unsupported.




  Returns:
    `vim.UserSession <vim/UserSession.rst>`_:
         The UserSession object.

  Raises:

    `vim.fault.InvalidLogin <vim/fault/InvalidLogin.rst>`_: 
       if there is no token provided or the token could not be validated.

    `vim.fault.InvalidLocale <vim/fault/InvalidLocale.rst>`_: 
       if the locale is invalid or unknown to the server.

    `vim.fault.NoPermission <vim/fault/NoPermission.rst>`_: 
       if the principal is valid, but has no access granted.


Login(userName, password, locale):
   Log on to the server. This method fails if the user name and password are incorrect, or if the user is valid but has no permissions granted.


  Privilege:
               System.Anonymous



  Args:
    userName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The `ID <vim/host/LocalAccountManager/AccountSpecification.rst#id>`_ of the user who is logging on to the server.


    password (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The `password <vim/host/LocalAccountManager/AccountSpecification.rst#password>`_ of the user who is logging on to the server.


    locale (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       A two-character ISO-639 language ID (like "en") optionally followed by an underscore and a two-character ISO 3166 country ID (like "US").Examples are "de", "fr_CA", "zh", "zh_CN", and "zh_TW". Note: The method uses the server default locale when a locale is not provided. This default can be configured in the server configuration file. If unspecified, it defaults to the locale of the server environment or English ("en") if unsupported.




  Returns:
    `vim.UserSession <vim/UserSession.rst>`_:
         The UserSession object.As of vSphere API 5.1 for VirtualCenter login use SSO style `LoginByToken <vim/SessionManager.rst#loginByToken>`_ 

  Raises:

    `vim.fault.InvalidLogin <vim/fault/InvalidLogin.rst>`_: 
       if the user and password combination is invalid.

    `vim.fault.InvalidLocale <vim/fault/InvalidLocale.rst>`_: 
       if the locale is invalid or unknown to the server.

    `vim.fault.NoPermission <vim/fault/NoPermission.rst>`_: 
       if the user is valid, but has no access granted.


LoginBySSPI(base64Token, locale):
   Log on to the server using SSPI pass-through authentication.This method provides support for passing credentials of the calling process to the server without using a password, by leveraging the Windows Security Support Provider Interface (SSPI) library.If the function is not supported, this throws a NotSupported fault.The client first calls AcquireCredentialsHandle(). If Kerberos is used, this should include the desired credential to pass. The client then calls InitializeSecurityContext(). The resulting partially-formed context is passed in Base-64 encoded form to this method.If the context has been successfully formed, the server proceeds with login and behaves like `Login <vim/SessionManager.rst#login>`_ . If further negotiation is needed, the server throws an SSPIChallenge fault with a challenge token, which the client should again pass to InitializeSecurityContext(), followed by calling this method again.For more information, see the MSDN documentation on SSPI.
  since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


  Privilege:
               System.Anonymous



  Args:
    base64Token (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The partially formed context returned from InitializeSecurityContext().


    locale (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       A two-character ISO-639 language ID (like "en") optionally followed by an underscore and a two-character ISO 3166 country ID (like "US").Examples are "de", "fr_CA", "zh", "zh_CN", and "zh_TW". Note: The method uses the server default locale when a locale is not provided. This default can be configured in the server configuration file. If unspecified, it defaults to the locale of the server environment or English ("en") if unsupported.




  Returns:
    `vim.UserSession <vim/UserSession.rst>`_:
         The UserSession object.As of vSphere API 5.1 for VirtualCenter login use SSO style `LoginByToken <vim/SessionManager.rst#loginByToken>`_ 

  Raises:

    `vim.fault.SSPIChallenge <vim/fault/SSPIChallenge.rst>`_: 
       if further negotiation is required.

    `vim.fault.InvalidLogin <vim/fault/InvalidLogin.rst>`_: 
       if the user context could not be passed successfully, or the context is not valid on the server.

    `vim.fault.InvalidLocale <vim/fault/InvalidLocale.rst>`_: 
       if the locale is invalid or unknown to the server.

    `vim.fault.NoPermission <vim/fault/NoPermission.rst>`_: 
       if the user is valid, but has no access granted.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the service does not support SSPI authentication.


Logout():
   Log out and terminate the current session.


  Privilege:
               System.View



  Args:


  Returns:
    None
         


AcquireLocalTicket(userName):
   Acquires a one-time ticket for mutual authentication between a server and client.The caller of this operation can use the user name and file content of the returned object as the userName and password arguments for login operation. The local ticket that is returned becomes invalid either after it is used or after a server-determined ticket expiration time passes. This operation can be used by servers and clients to avoid re-entering user credentials after authentication by the operating system has already happened.For example, service console utilities that connect to a host agent should not require users to re-enter their passwords every time the utilities run. Since the one-time password file is readable only by the given user, the identity of the one-time password user is protected by the operating system file permission.Only local clients are allowed to call this operation. Remote clients receive an InvalidRequest fault upon calling this operation.


  Privilege:
               System.Anonymous



  Args:
    userName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       User requesting one-time password.




  Returns:
    `vim.SessionManager.LocalTicket <vim/SessionManager/LocalTicket.rst>`_:
         LocalTicket object containing userName and path to file containing one-time password for use in login operation.

  Raises:

    `vim.fault.InvalidLogin <vim/fault/InvalidLogin.rst>`_: 
       if the userName is invalid.

    `vim.fault.NoPermission <vim/fault/NoPermission.rst>`_: 
       if the user and password are valid, but the user has no access granted.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the server does not support this operation.


AcquireGenericServiceTicket(spec):
   Creates and returns a one-time credential that may be used to make the specified request.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               System.Anonymous



  Args:
    spec (`vim.SessionManager.ServiceRequestSpec <vim/SessionManager/ServiceRequestSpec.rst>`_):
       specification for the service request which will be invoked with the ticket.




  Returns:
    `vim.SessionManager.GenericServiceTicket <vim/SessionManager/GenericServiceTicket.rst>`_:
         a ticket that may be used to invoke the specified request.

  Raises:

    `vim.fault.NoPermission <vim/fault/NoPermission.rst>`_: 
       if the client does not have enough privileges to be granted a ticket.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the spec is not supported or not valid.

    `vim.fault.NotAuthenticated <vim/fault/NotAuthenticated.rst>`_: 
       if the current session is not authenticated for clone session request


TerminateSession(sessionId):
   Log off and terminate the provided list of sessions.This method is only transactional for each session ID. The set of sessions are terminated sequentially, as specified in the list. If a failure occurs, for example, because of an unknown sessionID, the method aborts with an exception. When the method aborts, any sessions that have not yet been terminated are left in their unterminated state.


  Privilege:
               Sessions.TerminateSession



  Args:
    sessionId (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       A list of sessions to terminate.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if a sessionId could not be found as a valid logged-on session.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if a sessionId matches the current session. Use the logout method to terminate the current session.


SetLocale(locale):
   Sets the session locale.


  Privilege:
               System.View



  Args:
    locale (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       A two-character ISO-639 language ID (like "en") optionally followed by an underscore and a two-character ISO 3166 country ID (like "US").Examples are "de", "fr_CA", "zh", "zh_CN", and "zh_TW". Note: The method uses the server default locale when a locale is not provided. This default can be configured in the server configuration file. If unspecified, it defaults to the locale of the server environment or English ("en") if unsupported.




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidLocale <vim/fault/InvalidLocale.rst>`_: 
       if the locale is invalid or unknown to the server.


LoginExtensionBySubjectName(extensionKey, locale):
   Creates a special privileged session that includes the Sessions.ImpersonateUser privilege. Requires that the extension connected using SSL, with a certificate that has a subject name that matches the subject name registered for the extension.As of vSphere API 4.0, the NotFound fault is no longer thrown. Instead, InvalidLogin is thrown if the specified extension is not registered.
  since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


  Privilege:
               System.Anonymous



  Args:
    extensionKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Key of extension that is logging in.


    locale (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       A two-character ISO-639 language ID (like "en") optionally followed by an underscore and a two-character ISO 3166 country ID (like "US").Examples are "de", "fr_CA", "zh", "zh_CN", and "zh_TW". Note: The method uses the server default locale when a locale is not provided. This default can be configured in the server configuration file. If unspecified, it defaults to the locale of the server environment or English ("en") if unsupported.




  Returns:
    `vim.UserSession <vim/UserSession.rst>`_:
         

  Raises:

    `vim.fault.InvalidLogin <vim/fault/InvalidLogin.rst>`_: 
       if the extension is not registered, or the subject name doesn't match the subject name of the extension.

    `vim.fault.InvalidLocale <vim/fault/InvalidLocale.rst>`_: 
       if the supplied locale is not valid

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if no extension is associated with the given key

    `vim.fault.NoClientCertificate <vim/fault/NoClientCertificate.rst>`_: 
       if no certificate was used by the client to connect

    `vim.fault.NoSubjectName <vim/fault/NoSubjectName.rst>`_: 
       if the extension was registered without a subject name

    `vim.fault.InvalidClientCertificate <vim/fault/InvalidClientCertificate.rst>`_: 
       if the client cerificate fails the verification at the server


LoginExtensionByCertificate(extensionKey, locale):
   Creates a special privileged session that includes the Sessions.ImpersonateUser privilege. Requires that the client connect over SSL and provide an X.509 certificate for which they hold the private key. The certificate must match the certificate used in an earlier call to `SetExtensionCertificate <vim/ExtensionManager.rst#setCertificate>`_ .NOTE: Verification of the received certificate (such as expiry, revocation, and trust chain) is not required for successful authentication using this method. If certificate verification is desired, use the `LoginExtensionBySubjectName <vim/SessionManager.rst#loginExtensionBySubjectName>`_ method instead.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               System.Anonymous



  Args:
    extensionKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Key of extension that is logging in.


    locale (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       A two-character ISO-639 language ID (like "en") optionally followed by an underscore and a two-character ISO 3166 country ID (like "US").Examples are "de", "fr_CA", "zh", "zh_CN", and "zh_TW". Note: The method uses the server default locale when a locale is not provided. This default can be configured in the server configuration file. If unspecified, it defaults to the locale of the server environment or English ("en") if unsupported.




  Returns:
    `vim.UserSession <vim/UserSession.rst>`_:
         

  Raises:

    `vim.fault.InvalidLogin <vim/fault/InvalidLogin.rst>`_: 
       if the extension is not registered, or the certificate does not match the expected value.

    `vim.fault.InvalidLocale <vim/fault/InvalidLocale.rst>`_: 
       if the supplied locale is not valid

    `vim.fault.NoClientCertificate <vim/fault/NoClientCertificate.rst>`_: 
       if no certificate was used by the client to connect


ImpersonateUser(userName, locale):
   Converts current session to impersonate the specified user. The current session will take on the identity and authorization level of the user. That user must have a currently-active session. If the given userName is an extension key and this key does not overlap with a user name of any currently-active session, it will take on the identity and authorization level of that extension provided the current session has the same authorization level of that extension.
  since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


  Privilege:
               Sessions.ImpersonateUser



  Args:
    userName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The user or extension key to impersonate.


    locale (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       A two-character ISO-639 language ID (like "en") optionally followed by an underscore and a two-character ISO 3166 country ID (like "US").Examples are "de", "fr_CA", "zh", "zh_CN", and "zh_TW". Note: The method uses the server default locale when a locale is not provided. This default can be configured in the server configuration file. If unspecified, it defaults to the locale of the server environment or English ("en") if unsupported.




  Returns:
    `vim.UserSession <vim/UserSession.rst>`_:
         

  Raises:

    `vim.fault.InvalidLogin <vim/fault/InvalidLogin.rst>`_: 
       vim.fault.InvalidLogin

    `vim.fault.InvalidLocale <vim/fault/InvalidLocale.rst>`_: 
       vim.fault.InvalidLocale


SessionIsActive(sessionID, userName):
   Validates that a currently-active session exists with the specified sessionID and userName associated with it. Returns true if session exists.
  since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


  Privilege:
               Sessions.ValidateSession



  Args:
    sessionID (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Session ID to validate.


    userName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       User name to validate.




  Returns:
    `bool <https://docs.python.org/2/library/stdtypes.html>`_:
         


AcquireCloneTicket():
   Acquire a session-specific ticket string which can be used to clone the current session. The caller of this operation can pass the ticket value to another entity on the client. The recipient can then call `CloneSession <vim/SessionManager.rst#cloneSession>`_ with the ticket string on an unauthenticated session and avoid having to re-enter credentials.The ticket may only be used once and becomes invalid after use. The ticket is also invalidated when the corresponding session is closed or expires. The ticket is only valid on the server which issued it.This sequence of operations is conceptually similar to the functionality provided by `AcquireLocalTicket <vim/SessionManager.rst#acquireLocalTicket>`_ , however the methods can be used by remote clients and do not require a shared filesystem for transport.See `CloneSession <vim/SessionManager.rst#cloneSession>`_ 
  since: `VI API 2.5u2 <vim/version.rst#vimversionversion3>`_


  Privilege:
               System.View



  Args:


  Returns:
    `str <https://docs.python.org/2/library/stdtypes.html>`_:
         one-time secret ticket string.

  Raises:

    `vim.fault.NotAuthenticated <vim/fault/NotAuthenticated.rst>`_: 
       if the current session is not authenticatedSee `CloneSession <vim/SessionManager.rst#cloneSession>`_ 


CloneSession(cloneTicket):
   Clone the session specified by the clone ticket and associate it with the current connection. The current session will take on the identity and authorization level of the UserSession associated with the specified cloning ticket.See `AcquireCloneTicket <vim/SessionManager.rst#acquireCloneTicket>`_ See `AcquireGenericServiceTicket <vim/SessionManager.rst#acquireGenericServiceTicket>`_ 
  since: `VI API 2.5u2 <vim/version.rst#vimversionversion3>`_


  Privilege:
               System.Anonymous



  Args:
    cloneTicket (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       ticket string acquired via `AcquireCloneTicket <vim/SessionManager.rst#acquireCloneTicket>`_ .See `AcquireCloneTicket <vim/SessionManager.rst#acquireCloneTicket>`_ See `AcquireGenericServiceTicket <vim/SessionManager.rst#acquireGenericServiceTicket>`_ 




  Returns:
    `vim.UserSession <vim/UserSession.rst>`_:
         The new/cloned UserSession object.

  Raises:

    `vim.fault.InvalidLogin <vim/fault/InvalidLogin.rst>`_: 
       if the specified ticket value is not valid.See `AcquireCloneTicket <vim/SessionManager.rst#acquireCloneTicket>`_ See `AcquireGenericServiceTicket <vim/SessionManager.rst#acquireGenericServiceTicket>`_ 

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the server does not support this operation.See `AcquireCloneTicket <vim/SessionManager.rst#acquireCloneTicket>`_ See `AcquireGenericServiceTicket <vim/SessionManager.rst#acquireGenericServiceTicket>`_ 


