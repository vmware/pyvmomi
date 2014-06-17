.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vmodl.ManagedObject: ../../vim.ExtensibleManagedObject.rst


vim.cluster.Action
==================
  Base class for all action recommendations in VirtualCenter.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    type (`str`_):

       Type of the action. This is encoded to differentiate between different types of actions aimed at achieving different goals.
    target (`vmodl.ManagedObject`_, optional):

       The target object on which this action will be applied. For instance, a migration action will have a virtual machine as its target object, while a host power action will have a host as its target action.
