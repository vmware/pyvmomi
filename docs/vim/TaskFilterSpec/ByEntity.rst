.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst

.. _vim.TaskFilterSpec.RecursionOption: ../../vim/TaskFilterSpec/RecursionOption.rst


vim.TaskFilterSpec.ByEntity
===========================
  This data object type specifies a managed entity used to filter task history.
:extends: vmodl.DynamicData_

Attributes:
    entity (`vim.ManagedEntity`_, privilege: System.View):

       The managed entity to which the task pertains.
    recursion (`vim.TaskFilterSpec.RecursionOption`_):

       Specification of related managed entities in the inventory hierarchy.
