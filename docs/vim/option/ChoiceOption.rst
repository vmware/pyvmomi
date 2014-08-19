
vim.option.ChoiceOption
=======================
  The ChoiceOption data object type defines a set of supported string values, a localizable description for each value, and the default value.
:extends: vim.option.OptionType_

Attributes:
    choiceInfo ([`vim.ElementDescription <vim/ElementDescription.rst>`_]):

       The set of possible selections and descriptions.
    defaultIndex (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The index in ChoiceOption.value that serves as the default value.
