
vim.fault.TooManyGuestLogons
============================
    :extends:

        `vim.fault.GuestOperationsFault <vim/fault/GuestOperationsFault.rst>`_

  A TooManyGuestLogons exception is thrown when there are too many concurrent login sessions active in the guest. `ReleaseCredentialsInGuest <vim/vm/guest/AuthManager.rst#releaseCredentials>`_ can be called on ticketed sessions that are no longer needed. This will decrease the number of concurrent sessions active in the guest.

Attributes:




