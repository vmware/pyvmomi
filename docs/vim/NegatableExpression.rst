
vim.NegatableExpression
=======================
  The base class for any type of setting or configuration to which negation can be applied. When used in a configuration information object: if `negate <vim/NegatableExpression.rst#negate>`_ is true, then ~(objectValue) will be used for the configuration. If false, then objectValue will be used as it is.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    negate (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Whether the configuration needs to be negated or not.
