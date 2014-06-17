.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vim.event.HostEventArgument: ../../vim/event/HostEventArgument.rst

.. _vim.event.DatastoreEventArgument: ../../vim/event/DatastoreEventArgument.rst

.. _vim.event.DatacenterEventArgument: ../../vim/event/DatacenterEventArgument.rst


vim.event.VmBeingMigratedEvent
==============================
  This event records that a virtual machine is being migrated.
:extends: vim.event.VmEvent_

Attributes:
    destHost (`vim.event.HostEventArgument`_):

       The destination host.
    destDatacenter (`vim.event.DatacenterEventArgument`_, optional):

       The destination datacenter
    destDatastore (`vim.event.DatastoreEventArgument`_, optional):

       The destination primary datastore
