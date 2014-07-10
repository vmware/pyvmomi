.. _vim.Task: ../../vim/Task.rst

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vim.host.AuthenticationStoreInfo: ../../vim/host/AuthenticationStoreInfo.rst


vim.host.AuthenticationStore
============================
  The `HostAuthenticationStore`_ base class represents both local user and host Active Directory authentication for an ESX host.
   * Local user authentication is always enabled. The vSphere API does not support local user configuration for a host.
   * Active Directory authentication for ESX hosts relies on an established Active Directory account that has the authority to add the host to a domain.
   * 


:since: `vSphere API 4.1`_


Attributes
----------
    info (`vim.host.AuthenticationStoreInfo`_):
       Information about the authentication store.


Methods
-------


