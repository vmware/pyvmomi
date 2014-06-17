.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.option.OptionValue: ../../../vim/option/OptionValue.rst


vim.host.InternetScsiHba.ParamValue
===================================
  Describes the the value of an iSCSI parameter, and whether the value is being inherited.
:extends: vim.option.OptionValue_
:since: `vSphere API 4.0`_

Attributes:
    isInherited (`bool`_, optional):

       Indicates if the value is inherited from some other source. If unset, the value is not inheritable. isInherited can be modified only if it has already been set. If value is to being modified, isInherited should be set to true. Setting isInherited to false will result in the value being once again inherited from the source.
