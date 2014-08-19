
vim.event.VmMigratedEvent
=========================
  This event records a virtual machine migration.
:extends: vim.event.VmEvent_

Attributes:
    sourceHost (`vim.event.HostEventArgument <vim/event/HostEventArgument.rst>`_):

       The source host. (Because this is after a successful migration, the destination host is recorded in the inherited "host" property.)
    sourceDatacenter (`vim.event.DatacenterEventArgument <vim/event/DatacenterEventArgument.rst>`_, optional):

       The source datacenter
    sourceDatastore (`vim.event.DatastoreEventArgument <vim/event/DatastoreEventArgument.rst>`_, optional):

       The source primary datastore
