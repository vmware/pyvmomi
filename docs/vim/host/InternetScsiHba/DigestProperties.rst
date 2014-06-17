.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.InternetScsiHba.DigestProperties
=========================================
  The digest settings for this host bus adapter.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    headerDigestType (`str`_, optional):

       The header digest preference if header digest is enabled
    headerDigestInherited (`bool`_, optional):

       Header digest setting is inherited
    dataDigestType (`str`_, optional):

       The data digest preference if data digest is enabled
    dataDigestInherited (`bool`_, optional):

       Data digest setting is inherited
