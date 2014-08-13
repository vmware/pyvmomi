.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.action.Action: ../../vim/action/Action.rst

.. _vim.action.MethodActionArgument: ../../vim/action/MethodActionArgument.rst


vim.action.MethodAction
=======================
  This data object type defines an operation and its arguments, invoked on a particular entity.
:extends: vim.action.Action_

Attributes:
    name (`str`_):

       Name of the operation.
    argument ([`vim.action.MethodActionArgument`_], optional):

       An array consisting of the arguments for the operation.
