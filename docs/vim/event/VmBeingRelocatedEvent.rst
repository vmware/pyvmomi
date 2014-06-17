.. _vim.event.HostEventArgument: ../../vim/event/HostEventArgument.rst

.. _vim.event.VmRelocateSpecEvent: ../../vim/event/VmRelocateSpecEvent.rst

.. _vim.event.DatastoreEventArgument: ../../vim/event/DatastoreEventArgument.rst

.. _vim.event.DatacenterEventArgument: ../../vim/event/DatacenterEventArgument.rst


vim.event.VmBeingRelocatedEvent
===============================
  This event records that a virtual machine is being relocated.
:extends: vim.event.VmRelocateSpecEvent_

Attributes:
    destHost (`vim.event.HostEventArgument`_):

       The destination host to which the virtual machine is being relocated.
    destDatacenter (`vim.event.DatacenterEventArgument`_, optional):

       The destination datacenter to which the virtual machine is being relocated
    destDatastore (`vim.event.DatastoreEventArgument`_, optional):

       The destination primary datastore to which the virtual machine is being relocated
