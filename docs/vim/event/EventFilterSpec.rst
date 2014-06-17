.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _type: ../../vim/event/EventFilterSpec.rst#type

.. _EventEx: ../../vim/event/EventEx.rst

.. _eventTypeId: ../../vim/event/EventFilterSpec.rst#eventTypeId

.. _ExtendedEvent: ../../vim/event/ExtendedEvent.rst

.. _vim.alarm.Alarm: ../../vim/alarm/Alarm.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _CreateCollectorForEvents: ../../vim/event/EventManager.rst#createCollector

.. _vim.scheduler.ScheduledTask: ../../vim/scheduler/ScheduledTask.rst

.. _vim.event.EventFilterSpec.ByTime: ../../vim/event/EventFilterSpec/ByTime.rst

.. _vim.event.EventFilterSpec.ByEntity: ../../vim/event/EventFilterSpec/ByEntity.rst

.. _vim.event.EventFilterSpec.ByUsername: ../../vim/event/EventFilterSpec/ByUsername.rst


vim.event.EventFilterSpec
=========================
  Event filter used to query events in the history collector database. The client creates an event history collector with a filter specification, then retrieves the events from the event history collector.
:extends: vmodl.DynamicData_

Attributes:
    entity (`vim.event.EventFilterSpec.ByEntity`_, optional):

       The filter specification for retrieving events by managed entity. If the property is not set, then events attached to all managed entities are collected.
    time (`vim.event.EventFilterSpec.ByTime`_, optional):

       The filter specification for retrieving tasks by time. If the property is not set, then events with any time stamp are collected.
    userName (`vim.event.EventFilterSpec.ByUsername`_, optional):

       The filter specification for retrieving events by username. If the property is not set, then events belonging to any user are collected.
    eventChainId (`int`_, optional):

       The filter specification for retrieving events by chain ID. If the property is not set, events with any chain ID are collected.
    alarm (`vim.alarm.Alarm`_, optional):

       This property, if set, limits the set of collected events to those associated with the specified alarm. If the property is not set, events are collected regardless of their association with alarms.
    scheduledTask (`vim.scheduler.ScheduledTask`_, optional):

       This property, if set, limits the set of collected events to those associated with the specified scheduled task. If the property is not set, events are collected regardless of their association with any scheduled task.
    disableFullMessage (`bool`_, optional):

       Flag to specify whether or not to prepare the full formatted message for each event. If the property is not set, the collected events do not include the full formatted message.
    category (`str`_, optional):

       This property, if set, limits the set of collected events to those associated with the specified category. If the property is not set, events are collected regardless of their association with any category. "category" here is the same as Event.severity.
    type (`str`_, optional):

       This property, if set, limits the set of collected events to those specified types. If the property is not set, events are collected regardless of their types.
    tag (`str`_, optional):

       This property, if set, limits the set of filtered events to those that have it. If not set, or the size of it 0, the tag of an event is disregarded. A blank string indicates events without tags.
    eventTypeId (`str`_, optional):

       This property, if set, limits the set of collected events to those specified types.Note: if both `eventTypeId`_ and `type`_ are specified, an exception may be thrown by `CreateCollectorForEvents`_ .The semantics of how eventTypeId matching is done is as follows:
        * If the event being collected is of type
        * `EventEx`_
        * or
        * `ExtendedEvent`_
        * , then we match against the
        * eventTypeId
        * (for
        * EventEx
        * ) or
        * eventId
        * (for
        * ExtendedEvent
        * ) member of the Event.
        * Otherwise, we match against the type of the Event itself.
        * If neither this property, nor
        * type
        * , is set, events are collected regardless of their types.
