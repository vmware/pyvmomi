.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _AcquireCredentialsInGuest: ../../../vim/vm/guest/AuthManager.rst#acquireCredentials

.. _ReleaseCredentialsInGuest: ../../../vim/vm/guest/AuthManager.rst#releaseCredentials

.. _vim.vm.guest.GuestAuthentication: ../../../vim/vm/guest/GuestAuthentication.rst


vim.vm.guest.TicketedSessionAuthentication
==========================================
  TicketedSessionAuthentication contains the information necessary to use previously obtained credentials in the guest. The ticketed session is not stateless and stores state inside of the guest.A TicketedSessionAuthentication object will be returned as the result of a successful call to `AcquireCredentialsInGuest`_ . You can use this object in any guest operations function call.When you no longer need the TicketedSessionAuthentication object, you should call `ReleaseCredentialsInGuest`_ to free associated resources and session data.
:extends: vim.vm.guest.GuestAuthentication_
:since: `vSphere API 5.0`_

Attributes:
    ticket (`str`_):

       This contains a base64 encoded Ticket.
