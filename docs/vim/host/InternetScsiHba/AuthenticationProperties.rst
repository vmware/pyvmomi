
vim.host.InternetScsiHba.AuthenticationProperties
=================================================
  The authentication settings for this host bus adapter or target.
:extends: vmodl.DynamicData_

Attributes:
    chapAuthEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       True if CHAP is currently enabled
    chapName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The CHAP user name if enabled
    chapSecret (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The CHAP secret if enabled
    chapAuthenticationType (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The preference for CHAP or non-CHAP protocol if CHAP is enabled
    chapInherited (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       CHAP settings are inherited
    mutualChapName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       When Mutual-CHAP is enabled, the user name that target needs to use to authenticate with the initiator
    mutualChapSecret (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       When Mutual-CHAP is enabled, the secret that target needs to use to authenticate with the initiator
    mutualChapAuthenticationType (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The preference for CHAP or non-CHAP protocol if CHAP is enabled
    mutualChapInherited (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Mutual-CHAP settings are inherited
