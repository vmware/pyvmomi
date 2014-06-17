.. _vim.event.HostEvent: ../../vim/event/HostEvent.rst

.. _vim.event.DatastoreEventArgument: ../../vim/event/DatastoreEventArgument.rst


vim.event.DatastoreRemovedOnHostEvent
=====================================
  This event records when a datastore is removed from a host but not from VirtualCenter.
:extends: vim.event.HostEvent_

Attributes:
    datastore (`vim.event.DatastoreEventArgument`_):

       The associated datastore.
