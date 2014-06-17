.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst

.. _vim.event.HostEventArgument: ../../vim/event/HostEventArgument.rst

.. _vim.event.VmRelocateSpecEvent: ../../vim/event/VmRelocateSpecEvent.rst

.. _vim.event.DatastoreEventArgument: ../../vim/event/DatastoreEventArgument.rst

.. _vim.event.DatacenterEventArgument: ../../vim/event/DatacenterEventArgument.rst


vim.event.VmRelocateFailedEvent
===============================
  This event records a failure to relocate a virtual machine.
:extends: vim.event.VmRelocateSpecEvent_

Attributes:
    destHost (`vim.event.HostEventArgument`_):

       The destination host to which the virtual machine is being relocated.
    reason (`vmodl.LocalizedMethodFault`_):

       The reason why this relocate operation failed.
    destDatacenter (`vim.event.DatacenterEventArgument`_, optional):

       The destination datacenter to which the virtual machine was being relocated
    destDatastore (`vim.event.DatastoreEventArgument`_, optional):

       The destination primary datastore to which the virtual machine was being relocated
