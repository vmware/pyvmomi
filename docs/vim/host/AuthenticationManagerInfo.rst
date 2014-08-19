
vim.host.AuthenticationManagerInfo
==================================
  The `HostAuthenticationManagerInfo <vim/host/AuthenticationManagerInfo.rst>`_ data object provides access to authentication information for the ESX host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    authConfig ([`vim.host.AuthenticationStoreInfo <vim/host/AuthenticationStoreInfo.rst>`_]):

       An array containing entries for local authentication and host Active Directory authentication.
        * `HostLocalAuthenticationInfo <vim/host/LocalAuthenticationInfo.rst>`_
        * - Local authentication is always enabled.
        * 
        * `HostActiveDirectoryInfo <vim/host/ActiveDirectoryInfo.rst>`_
        * - Host Active Directory authentication information includes the name of the domain, membership status, and a list of other domains trusted by the membership domain.
