.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.ManagedEntity: ../../../vim/ManagedEntity.rst

.. _vim.event.EventFilterSpec.RecursionOption: ../../../vim/event/EventFilterSpec/RecursionOption.rst


vim.event.EventFilterSpec.ByEntity
==================================
  This option specifies a managed entity used to filter event history. If the specified managed entity is a Folder or a ResourcePool, the query will actually be performed on the entities contained within that Folder or ResourcePool, so you cannot query for events on Folders and ResourcePools themselves this way.
:extends: vmodl.DynamicData_

Attributes:
    entity (`vim.ManagedEntity`_, privilege: System.View):

       The managed entity to which the event pertains.
    recursion (`vim.event.EventFilterSpec.RecursionOption`_):

       Specification of related managed entities in the inventory hierarchy.
