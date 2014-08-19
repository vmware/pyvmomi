
vim.event.VmRelocatedEvent
==========================
  This event records the completion of a virtual machine relocation.
:extends: vim.event.VmRelocateSpecEvent_

Attributes:
    sourceHost (`vim.event.HostEventArgument <vim/event/HostEventArgument.rst>`_):

       The source host from which the virtual machine was relocated.
    sourceDatacenter (`vim.event.DatacenterEventArgument <vim/event/DatacenterEventArgument.rst>`_, optional):

       The source datacenter from which the virtual machine relocated
    sourceDatastore (`vim.event.DatastoreEventArgument <vim/event/DatastoreEventArgument.rst>`_, optional):

       The source primary datastore from which the virtual machine relocated
