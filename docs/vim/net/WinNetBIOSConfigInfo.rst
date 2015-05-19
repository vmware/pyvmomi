.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vim.net.NetBIOSConfigInfo: ../../vim/net/NetBIOSConfigInfo.rst


vim.net.WinNetBIOSConfigInfo
============================
  This data object type describes the Windows-specific NetBIOS configuration.
:extends: vim.net.NetBIOSConfigInfo_
:since: `vSphere API 4.1`_

Attributes:
    primaryWINS (`str`_):

       The IP address of the primary WINS server.
    secondaryWINS (`str`_, optional):

       The IP address of the secondary WINS server.
