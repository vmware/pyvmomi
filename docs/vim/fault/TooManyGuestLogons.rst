.. _ReleaseCredentialsInGuest: ../../vim/vm/guest/AuthManager.rst#releaseCredentials

.. _vim.fault.GuestOperationsFault: ../../vim/fault/GuestOperationsFault.rst


vim.fault.TooManyGuestLogons
============================
    :extends:

        `vim.fault.GuestOperationsFault`_

  A TooManyGuestLogons exception is thrown when there are too many concurrent login sessions active in the guest. `ReleaseCredentialsInGuest`_ can be called on ticketed sessions that are no longer needed. This will decrease the number of concurrent sessions active in the guest.

Attributes:




