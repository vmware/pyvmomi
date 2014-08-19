
vim.event.VmBeingRelocatedEvent
===============================
  This event records that a virtual machine is being relocated.
:extends: vim.event.VmRelocateSpecEvent_

Attributes:
    destHost (`vim.event.HostEventArgument <vim/event/HostEventArgument.rst>`_):

       The destination host to which the virtual machine is being relocated.
    destDatacenter (`vim.event.DatacenterEventArgument <vim/event/DatacenterEventArgument.rst>`_, optional):

       The destination datacenter to which the virtual machine is being relocated
    destDatastore (`vim.event.DatastoreEventArgument <vim/event/DatastoreEventArgument.rst>`_, optional):

       The destination primary datastore to which the virtual machine is being relocated
