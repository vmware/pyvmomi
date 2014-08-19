
vim.fault.GuestAuthenticationChallenge
======================================
    :extends:

        `vim.fault.GuestOperationsFault <vim/fault/GuestOperationsFault.rst>`_

  Fault is thrown when a call to `AcquireCredentialsInGuest <vim/vm/guest/AuthManager.rst#acquireCredentials>`_ requires a challenge response in order to authenticate in the guest. The authToken string in serverChallenge contains a base64 encoded challenge token.

Attributes:

    serverChallenge (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    sessionID (`long <https://docs.python.org/2/library/stdtypes.html>`_)




