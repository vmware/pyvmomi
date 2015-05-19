.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _HostActiveDirectoryInfo: ../../vim/host/ActiveDirectoryInfo.rst

.. _HostLocalAuthenticationInfo: ../../vim/host/LocalAuthenticationInfo.rst

.. _HostAuthenticationManagerInfo: ../../vim/host/AuthenticationManagerInfo.rst

.. _vim.host.AuthenticationStoreInfo: ../../vim/host/AuthenticationStoreInfo.rst


vim.host.AuthenticationManagerInfo
==================================
  The `HostAuthenticationManagerInfo`_ data object provides access to authentication information for the ESX host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    authConfig ([`vim.host.AuthenticationStoreInfo`_]):

       An array containing entries for local authentication and host Active Directory authentication.
        * `HostLocalAuthenticationInfo`_
        * - Local authentication is always enabled.
        * 
        * `HostActiveDirectoryInfo`_
        * - Host Active Directory authentication information includes the name of the domain, membership status, and a list of other domains trusted by the membership domain.
