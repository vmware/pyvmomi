
vim.event.DatastoreDiscoveredEvent
==================================
  This event records when a host is added to VirtualCenter and datastores are discovered.
:extends: vim.event.HostEvent_

Attributes:
    datastore (`vim.event.DatastoreEventArgument <vim/event/DatastoreEventArgument.rst>`_):

       The associated datastore.
