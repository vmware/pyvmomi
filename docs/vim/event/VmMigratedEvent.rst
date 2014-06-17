.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vim.event.HostEventArgument: ../../vim/event/HostEventArgument.rst

.. _vim.event.DatastoreEventArgument: ../../vim/event/DatastoreEventArgument.rst

.. _vim.event.DatacenterEventArgument: ../../vim/event/DatacenterEventArgument.rst


vim.event.VmMigratedEvent
=========================
  This event records a virtual machine migration.
:extends: vim.event.VmEvent_

Attributes:
    sourceHost (`vim.event.HostEventArgument`_):

       The source host. (Because this is after a successful migration, the destination host is recorded in the inherited "host" property.)
    sourceDatacenter (`vim.event.DatacenterEventArgument`_, optional):

       The source datacenter
    sourceDatastore (`vim.event.DatastoreEventArgument`_, optional):

       The source primary datastore
