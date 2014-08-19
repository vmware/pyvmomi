
vim.vm.guest.NamePasswordAuthentication
=======================================
  NamePasswordAuthentication contains the information necessary to authenticate within a guest using a name and password. This is the typical method for authentication within a guest and the one currently used by VIX. This method of authentication is stateless.To use NamePasswordAuthentication, populate username and password with the appropriate login information. You should not use `AcquireCredentialsInGuest <vim/vm/guest/AuthManager.rst#acquireCredentials>`_ or `ReleaseCredentialsInGuest <vim/vm/guest/AuthManager.rst#releaseCredentials>`_ for NamePasswordAuthentication.Once populated, you can use NamePasswordAuthentication in any guest operations function call.
:extends: vim.vm.guest.GuestAuthentication_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    username (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The user name for Name-Password authentication.
    password (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The password for Name-Password authentication.
