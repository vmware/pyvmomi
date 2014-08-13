.. _str: https://docs.python.org/2/library/stdtypes.html

.. _enabled: ../../vim/host/AuthenticationStoreInfo.rst#enabled

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _HostActiveDirectoryInfo: ../../vim/host/ActiveDirectoryInfo.rst

.. _vim.host.DirectoryStoreInfo: ../../vim/host/DirectoryStoreInfo.rst

.. _HostAuthenticationStoreInfo: ../../vim/host/AuthenticationStoreInfo.rst

.. _HostActiveDirectoryInfoDomainMembershipStatus: ../../vim/host/ActiveDirectoryInfo/DomainMembershipStatus.rst


vim.host.ActiveDirectoryInfo
============================
  The `HostActiveDirectoryInfo`_ data object describes ESX host membership in an Active Directory domain. If the `HostAuthenticationStoreInfo`_ . `enabled`_ property isTrue, the host is a member of a domain and the ESX Server will set the domain information properties.
:extends: vim.host.DirectoryStoreInfo_
:since: `vSphere API 4.1`_

Attributes:
    joinedDomain (`str`_, optional):

       The domain that this host joined.
    trustedDomain ([`str`_], optional):

       List of domains with which thejoinedDomainhas a trust. ThejoinedDomainis not included in thetrustedDomainlist.
    domainMembershipStatus (`str`_, optional):

       Health information about the domain membership. See `HostActiveDirectoryInfoDomainMembershipStatus`_ .
