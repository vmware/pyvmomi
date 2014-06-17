.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.vm.customization.Password
=============================
  Contains a password string and a flag that specifies whether the string is in plain text or encrypted.
:extends: vmodl.DynamicData_

Attributes:
    value (`str`_):

       The password string. It is encrypted if the associated plainText flag is false.
    plainText (`bool`_):

       Flag to specify whether or not the password is in plain text, rather than encrypted.
