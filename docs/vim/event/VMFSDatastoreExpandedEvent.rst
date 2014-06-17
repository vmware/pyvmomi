.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.HostEvent: ../../vim/event/HostEvent.rst

.. _vim.event.DatastoreEventArgument: ../../vim/event/DatastoreEventArgument.rst


vim.event.VMFSDatastoreExpandedEvent
====================================
  This event records when a datastore is expanded.
:extends: vim.event.HostEvent_
:since: `vSphere API 4.0`_

Attributes:
    datastore (`vim.event.DatastoreEventArgument`_):

       The associated datastore.
