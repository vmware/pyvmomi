
vim.event.ExtendedEvent
=======================
  This event is the base class for extended events.
:extends: vim.event.GeneralEvent_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    eventTypeId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The id of the type of extended event.
    managedObject (`vmodl.ManagedObject <vim.ExtensibleManagedObject.rst>`_):

       The object on which the event was logged.
    data ([`vim.event.ExtendedEvent.Pair <vim/event/ExtendedEvent/Pair.rst>`_], optional):

       Key/value pairs associated with event.
