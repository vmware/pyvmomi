
vim.option.OptionType
=====================
  The base data object type for all options.
:extends: vmodl.DynamicData_

Attributes:
    valueIsReadonly (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The flag to indicate whether or not a user can modify a value belonging to this option type. If the flag is not set, the value can be modified.
