.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.KeyAnyValue: ../../vmodl/KeyAnyValue.rst

.. _vim.profile.Expression: ../../vim/profile/Expression.rst


vim.profile.SimpleExpression
============================
  DataObject represents a pre-defined expression
:extends: vim.profile.Expression_
:since: `vSphere API 4.0`_

Attributes:
    expressionType (`str`_):

       Type of the simple expression to instantiate. The expressionType should be derived from the available expressions as listed in the metadata.
    parameter (`vmodl.KeyAnyValue`_, optional):

       The parameters for the expressionType. The list of parameters needed for a simple expression can be obtained from the metadata.
