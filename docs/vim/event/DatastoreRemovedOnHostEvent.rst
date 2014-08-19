
vim.event.DatastoreRemovedOnHostEvent
=====================================
  This event records when a datastore is removed from a host but not from VirtualCenter.
:extends: vim.event.HostEvent_

Attributes:
    datastore (`vim.event.DatastoreEventArgument <vim/event/DatastoreEventArgument.rst>`_):

       The associated datastore.
