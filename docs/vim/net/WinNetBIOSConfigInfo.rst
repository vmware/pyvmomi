
vim.net.WinNetBIOSConfigInfo
============================
  This data object type describes the Windows-specific NetBIOS configuration.
:extends: vim.net.NetBIOSConfigInfo_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    primaryWINS (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The IP address of the primary WINS server.
    secondaryWINS (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The IP address of the secondary WINS server.
