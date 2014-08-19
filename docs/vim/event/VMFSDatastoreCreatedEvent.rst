
vim.event.VMFSDatastoreCreatedEvent
===================================
  This event records when a VMFS datastore is created.
:extends: vim.event.HostEvent_

Attributes:
    datastore (`vim.event.DatastoreEventArgument <vim/event/DatastoreEventArgument.rst>`_):

       The associated datastore.
