.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.option.OptionType: ../../vim/option/OptionType.rst


vim.option.StringOption
=======================
  The StringOption data object type is used to define an open-ended string value based on an optional subset of valid characters.
:extends: vim.option.OptionType_

Attributes:
    defaultValue (`str`_):

       The default value.
    validCharacters (`str`_, optional):

       The string containing the set of valid characters. If a string option is not specified, all strings are allowed.
