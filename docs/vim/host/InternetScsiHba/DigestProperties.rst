
vim.host.InternetScsiHba.DigestProperties
=========================================
  The digest settings for this host bus adapter.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    headerDigestType (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The header digest preference if header digest is enabled
    headerDigestInherited (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Header digest setting is inherited
    dataDigestType (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The data digest preference if data digest is enabled
    dataDigestInherited (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Data digest setting is inherited
