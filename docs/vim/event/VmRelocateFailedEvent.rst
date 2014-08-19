
vim.event.VmRelocateFailedEvent
===============================
  This event records a failure to relocate a virtual machine.
:extends: vim.event.VmRelocateSpecEvent_

Attributes:
    destHost (`vim.event.HostEventArgument <vim/event/HostEventArgument.rst>`_):

       The destination host to which the virtual machine is being relocated.
    reason (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

       The reason why this relocate operation failed.
    destDatacenter (`vim.event.DatacenterEventArgument <vim/event/DatacenterEventArgument.rst>`_, optional):

       The destination datacenter to which the virtual machine was being relocated
    destDatastore (`vim.event.DatastoreEventArgument <vim/event/DatastoreEventArgument.rst>`_, optional):

       The destination primary datastore to which the virtual machine was being relocated
