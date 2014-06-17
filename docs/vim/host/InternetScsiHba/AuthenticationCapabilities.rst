.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.InternetScsiHba.AuthenticationCapabilities
===================================================
  The authentication capabilities for this host bus adapter.
:extends: vmodl.DynamicData_

Attributes:
    chapAuthSettable (`bool`_):

       True if this host bus adapter supports changing the configuration state of CHAP authentication. CHAP is mandatory, however some adapter may not allow disabling this authentication method.
    krb5AuthSettable (`bool`_):

       Always false in this version of the API.
    srpAuthSettable (`bool`_):

       Always false in this version of the API.
    spkmAuthSettable (`bool`_):

       Always false in this version of the API.
    mutualChapSettable (`bool`_, optional):

       When chapAuthSettable is TRUE, this describes if Mutual CHAP configuration is allowed as well.
    targetChapSettable (`bool`_, optional):

       When targetChapSettable is TRUE, this describes if CHAP configuration is allowed on targets associated with the adapter.
    targetMutualChapSettable (`bool`_, optional):

       When targetMutualChapSettable is TRUE, this describes if Mutual CHAP configuration is allowed on targets associated with the adapter.
