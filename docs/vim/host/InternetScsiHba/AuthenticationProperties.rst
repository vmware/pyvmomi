.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.InternetScsiHba.AuthenticationProperties
=================================================
  The authentication settings for this host bus adapter or target.
:extends: vmodl.DynamicData_

Attributes:
    chapAuthEnabled (`bool`_):

       True if CHAP is currently enabled
    chapName (`str`_, optional):

       The CHAP user name if enabled
    chapSecret (`str`_, optional):

       The CHAP secret if enabled
    chapAuthenticationType (`str`_, optional):

       The preference for CHAP or non-CHAP protocol if CHAP is enabled
    chapInherited (`bool`_, optional):

       CHAP settings are inherited
    mutualChapName (`str`_, optional):

       When Mutual-CHAP is enabled, the user name that target needs to use to authenticate with the initiator
    mutualChapSecret (`str`_, optional):

       When Mutual-CHAP is enabled, the secret that target needs to use to authenticate with the initiator
    mutualChapAuthenticationType (`str`_, optional):

       The preference for CHAP or non-CHAP protocol if CHAP is enabled
    mutualChapInherited (`bool`_, optional):

       Mutual-CHAP settings are inherited
