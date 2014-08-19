
vim.profile.CompositeExpression
===============================
  DataObject to Compose expressions. It is used to group expressions together. They are similar to a parentheses in an expression.
:extends: vim.profile.Expression_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    operator (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Logical operator to be applied between the expressions in the composite expression. e.g: or, and
    expressionName ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       List of expression names that will be used for this composition. The individual expressions will return a boolean. The return values of the individual expressions will be used to compute the final return value of the CompositeExpression. The expressions specified in the list can themselves be CompositeExpressions.
