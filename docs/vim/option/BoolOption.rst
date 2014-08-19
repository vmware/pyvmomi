
vim.option.BoolOption
=====================
  The BoolOption data object type describes if an option is supported ("true") and if the option is set to "true" or "false" by default.
:extends: vim.option.OptionType_

Attributes:
    supported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether or not the option is supported.
    defaultValue (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The default value for the option.
