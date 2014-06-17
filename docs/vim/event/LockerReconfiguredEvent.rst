.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.event.Event: ../../vim/event/Event.rst

.. _vim.event.DatastoreEventArgument: ../../vim/event/DatastoreEventArgument.rst


vim.event.LockerReconfiguredEvent
=================================
  Locker was reconfigured to a new location.
:extends: vim.event.Event_
:since: `VI API 2.5`_

Attributes:
    oldDatastore (`vim.event.DatastoreEventArgument`_, optional):

       The datastore that was previously backing the locker. This field is not set if a datastore was not backing the locker previously.
    newDatastore (`vim.event.DatastoreEventArgument`_, optional):

       The datastore that is now used to back the locker. This field is not set if no datastore is currently backing the locker.
