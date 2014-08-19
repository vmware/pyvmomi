
vim.event.VmBeingHotMigratedEvent
=================================
  This event records that a virtual machine is being hot-migrated.
:extends: vim.event.VmEvent_

Attributes:
    destHost (`vim.event.HostEventArgument <vim/event/HostEventArgument.rst>`_):

       The destination host to which the virtual machine is to be migrated.
    destDatacenter (`vim.event.DatacenterEventArgument <vim/event/DatacenterEventArgument.rst>`_, optional):

       The destination datacenter to which the virtual machine is being migrated
    destDatastore (`vim.event.DatastoreEventArgument <vim/event/DatastoreEventArgument.rst>`_, optional):

       The destination primary datastore to which the virtual machine is being migrated
