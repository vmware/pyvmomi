.. _vim.event.HostEventArgument: ../../vim/event/HostEventArgument.rst

.. _vim.event.VmRelocateSpecEvent: ../../vim/event/VmRelocateSpecEvent.rst

.. _vim.event.DatastoreEventArgument: ../../vim/event/DatastoreEventArgument.rst

.. _vim.event.DatacenterEventArgument: ../../vim/event/DatacenterEventArgument.rst


vim.event.VmRelocatedEvent
==========================
  This event records the completion of a virtual machine relocation.
:extends: vim.event.VmRelocateSpecEvent_

Attributes:
    sourceHost (`vim.event.HostEventArgument`_):

       The source host from which the virtual machine was relocated.
    sourceDatacenter (`vim.event.DatacenterEventArgument`_, optional):

       The source datacenter from which the virtual machine relocated
    sourceDatastore (`vim.event.DatastoreEventArgument`_, optional):

       The source primary datastore from which the virtual machine relocated
