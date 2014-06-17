.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _HostAuthenticationStoreInfo: ../../vim/host/AuthenticationStoreInfo.rst


vim.host.AuthenticationStoreInfo
================================
  The `HostAuthenticationStoreInfo`_ base class defines status information for local and host Active Directory authentication.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    enabled (`bool`_):

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
