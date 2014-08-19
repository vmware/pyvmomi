
vim.event.LockerMisconfiguredEvent
==================================
  Locker has not been configured properly. This event is fired when the datastore configured to back the locker does not exist or when connectivity to the datastore is lost.
:extends: vim.event.Event_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    datastore (`vim.event.DatastoreEventArgument <vim/event/DatastoreEventArgument.rst>`_):

       The datastore that has been configured to back the locker
