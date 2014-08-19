
vim.event.VmBeingMigratedEvent
==============================
  This event records that a virtual machine is being migrated.
:extends: vim.event.VmEvent_

Attributes:
    destHost (`vim.event.HostEventArgument <vim/event/HostEventArgument.rst>`_):

       The destination host.
    destDatacenter (`vim.event.DatacenterEventArgument <vim/event/DatacenterEventArgument.rst>`_, optional):

       The destination datacenter
    destDatastore (`vim.event.DatastoreEventArgument <vim/event/DatastoreEventArgument.rst>`_, optional):

       The destination primary datastore
