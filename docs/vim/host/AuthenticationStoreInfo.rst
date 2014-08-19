
vim.host.AuthenticationStoreInfo
================================
  The `HostAuthenticationStoreInfo <vim/host/AuthenticationStoreInfo.rst>`_ base class defines status information for local and host Active Directory authentication.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the authentication store is configured.
        * Host Active Directory authentication -
        * enabled
        * is
        * True
        * if the host is a member of a domain.
        * Local authentication -
        * enabled
        * is always
        * True
        * .
