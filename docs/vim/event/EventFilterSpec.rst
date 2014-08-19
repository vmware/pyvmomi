
vim.event.EventFilterSpec
=========================
  Event filter used to query events in the history collector database. The client creates an event history collector with a filter specification, then retrieves the events from the event history collector.
:extends: vmodl.DynamicData_

Attributes:
    entity (`vim.event.EventFilterSpec.ByEntity <vim/event/EventFilterSpec/ByEntity.rst>`_, optional):

       The filter specification for retrieving events by managed entity. If the property is not set, then events attached to all managed entities are collected.
    time (`vim.event.EventFilterSpec.ByTime <vim/event/EventFilterSpec/ByTime.rst>`_, optional):

       The filter specification for retrieving tasks by time. If the property is not set, then events with any time stamp are collected.
    userName (`vim.event.EventFilterSpec.ByUsername <vim/event/EventFilterSpec/ByUsername.rst>`_, optional):

       The filter specification for retrieving events by username. If the property is not set, then events belonging to any user are collected.
    eventChainId (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The filter specification for retrieving events by chain ID. If the property is not set, events with any chain ID are collected.
    alarm (`vim.alarm.Alarm <vim/alarm/Alarm.rst>`_, optional):

       This property, if set, limits the set of collected events to those associated with the specified alarm. If the property is not set, events are collected regardless of their association with alarms.
    scheduledTask (`vim.scheduler.ScheduledTask <vim/scheduler/ScheduledTask.rst>`_, optional):

       This property, if set, limits the set of collected events to those associated with the specified scheduled task. If the property is not set, events are collected regardless of their association with any scheduled task.
    disableFullMessage (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to specify whether or not to prepare the full formatted message for each event. If the property is not set, the collected events do not include the full formatted message.
    category ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       This property, if set, limits the set of collected events to those associated with the specified category. If the property is not set, events are collected regardless of their association with any category. "category" here is the same as Event.severity.
    type ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       This property, if set, limits the set of collected events to those specified types. If the property is not set, events are collected regardless of their types.
    tag ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       This property, if set, limits the set of filtered events to those that have it. If not set, or the size of it 0, the tag of an event is disregarded. A blank string indicates events without tags.
    eventTypeId ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       This property, if set, limits the set of collected events to those specified types.Note: if both `eventTypeId <vim/event/EventFilterSpec.rst#eventTypeId>`_ and `type <vim/event/EventFilterSpec.rst#type>`_ are specified, an exception may be thrown by `CreateCollectorForEvents <vim/event/EventManager.rst#createCollector>`_ .The semantics of how eventTypeId matching is done is as follows:
        * If the event being collected is of type
        * `EventEx <vim/event/EventEx.rst>`_
        * or
        * `ExtendedEvent <vim/event/ExtendedEvent.rst>`_
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
