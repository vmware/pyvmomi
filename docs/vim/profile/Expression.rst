
vim.profile.Expression
======================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    id (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Identifier of this expression. The id has to be unique within a Profile. The id can be used as a key while building composite expressions.
    displayName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       User visible display name
    negated (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating if the condition of the expression should be negated. e.g: conditions like VSwitch0 has vmnic0 connected to it can be turned into VSwitch0 doesn't have vmnic0 connected to it.
