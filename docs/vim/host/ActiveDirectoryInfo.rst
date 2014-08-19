
vim.host.ActiveDirectoryInfo
============================
  The `HostActiveDirectoryInfo <vim/host/ActiveDirectoryInfo.rst>`_ data object describes ESX host membership in an Active Directory domain. If the `HostAuthenticationStoreInfo <vim/host/AuthenticationStoreInfo.rst>`_ . `enabled <vim/host/AuthenticationStoreInfo.rst#enabled>`_ property isTrue, the host is a member of a domain and the ESX Server will set the domain information properties.
:extends: vim.host.DirectoryStoreInfo_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    joinedDomain (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The domain that this host joined.
    trustedDomain ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       List of domains with which thejoinedDomainhas a trust. ThejoinedDomainis not included in thetrustedDomainlist.
    domainMembershipStatus (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Health information about the domain membership. See `HostActiveDirectoryInfoDomainMembershipStatus <vim/host/ActiveDirectoryInfo/DomainMembershipStatus.rst>`_ .
