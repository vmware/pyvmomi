
vim.action.MethodAction
=======================
  This data object type defines an operation and its arguments, invoked on a particular entity.
:extends: vim.action.Action_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the operation.
    argument ([`vim.action.MethodActionArgument <vim/action/MethodActionArgument.rst>`_], optional):

       An array consisting of the arguments for the operation.
