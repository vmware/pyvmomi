.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _AcquireCredentialsInGuest: ../../../vim/vm/guest/AuthManager.rst#acquireCredentials

.. _ReleaseCredentialsInGuest: ../../../vim/vm/guest/AuthManager.rst#releaseCredentials

.. _vim.vm.guest.GuestAuthentication: ../../../vim/vm/guest/GuestAuthentication.rst


vim.vm.guest.NamePasswordAuthentication
=======================================
  NamePasswordAuthentication contains the information necessary to authenticate within a guest using a name and password. This is the typical method for authentication within a guest and the one currently used by VIX. This method of authentication is stateless.To use NamePasswordAuthentication, populate username and password with the appropriate login information. You should not use `AcquireCredentialsInGuest`_ or `ReleaseCredentialsInGuest`_ for NamePasswordAuthentication.Once populated, you can use NamePasswordAuthentication in any guest operations function call.
:extends: vim.vm.guest.GuestAuthentication_
:since: `vSphere API 5.0`_

Attributes:
    username (`str`_):

       The user name for Name-Password authentication.
    password (`str`_):

       The password for Name-Password authentication.
