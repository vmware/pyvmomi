.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.option.OptionType: ../../vim/option/OptionType.rst


vim.option.BoolOption
=====================
  The BoolOption data object type describes if an option is supported ("true") and if the option is set to "true" or "false" by default.
:extends: vim.option.OptionType_

Attributes:
    supported (`bool`_):

       The flag to indicate whether or not the option is supported.
    defaultValue (`bool`_):

       The default value for the option.
