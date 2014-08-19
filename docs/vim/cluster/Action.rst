
vim.cluster.Action
==================
  Base class for all action recommendations in VirtualCenter.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Type of the action. This is encoded to differentiate between different types of actions aimed at achieving different goals.
    target (`vmodl.ManagedObject <vim.ExtensibleManagedObject.rst>`_, optional):

       The target object on which this action will be applied. For instance, a migration action will have a virtual machine as its target object, while a host power action will have a host as its target action.
