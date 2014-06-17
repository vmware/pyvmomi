.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vim.option.OptionType: ../../vim/option/OptionType.rst

.. _vim.ElementDescription: ../../vim/ElementDescription.rst


vim.option.ChoiceOption
=======================
  The ChoiceOption data object type defines a set of supported string values, a localizable description for each value, and the default value.
:extends: vim.option.OptionType_

Attributes:
    choiceInfo (`vim.ElementDescription`_):

       The set of possible selections and descriptions.
    defaultIndex (`int`_, optional):

       The index in ChoiceOption.value that serves as the default value.
