.. _long: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _AcquireCredentialsInGuest: ../../vim/vm/guest/AuthManager.rst#acquireCredentials

.. _vim.fault.GuestOperationsFault: ../../vim/fault/GuestOperationsFault.rst


vim.fault.GuestAuthenticationChallenge
======================================
    :extends:

        `vim.fault.GuestOperationsFault`_

  Fault is thrown when a call to `AcquireCredentialsInGuest`_ requires a challenge response in order to authenticate in the guest. The authToken string in serverChallenge contains a base64 encoded challenge token.

Attributes:

    serverChallenge (`str`_)

    sessionID (`long`_)




