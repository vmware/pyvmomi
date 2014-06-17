.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst

.. _vim.event.HostEventArgument: ../../vim/event/HostEventArgument.rst

.. _vim.event.DatastoreEventArgument: ../../vim/event/DatastoreEventArgument.rst

.. _vim.event.DatacenterEventArgument: ../../vim/event/DatacenterEventArgument.rst


vim.event.VmFailedMigrateEvent
==============================
  This event records a failure to migrate a virtual machine.
:extends: vim.event.VmEvent_

Attributes:
    destHost (`vim.event.HostEventArgument`_):

       The destination host.
    reason (`vmodl.LocalizedMethodFault`_):

       The reason for the failure.
    destDatacenter (`vim.event.DatacenterEventArgument`_, optional):

       The destination datacenter
    destDatastore (`vim.event.DatastoreEventArgument`_, optional):

       The destination primary datastore
