.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.ManagedObject: ../../vim.ExtensibleManagedObject.rst

.. _vim.event.GeneralEvent: ../../vim/event/GeneralEvent.rst

.. _vim.event.ExtendedEvent.Pair: ../../vim/event/ExtendedEvent/Pair.rst


vim.event.ExtendedEvent
=======================
  This event is the base class for extended events.
:extends: vim.event.GeneralEvent_
:since: `VI API 2.5`_

Attributes:
    eventTypeId (`str`_):

       The id of the type of extended event.
    managedObject (`vmodl.ManagedObject`_):

       The object on which the event was logged.
    data ([`vim.event.ExtendedEvent.Pair`_], optional):

       Key/value pairs associated with event.
