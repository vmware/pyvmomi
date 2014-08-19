
vim.alarm.EventAlarmExpression
==============================
  An alarm expression that uses the event stream to trigger the alarm.This alarm is triggered when an event matching this expression gets logged.
:extends: vim.alarm.AlarmExpression_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    comparisons ([`vim.alarm.EventAlarmExpression.Comparison <vim/alarm/EventAlarmExpression/Comparison.rst>`_], optional):

       The attributes/values to compare.
    eventType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The type of the event to trigger the alarm on.
    eventTypeId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The eventTypeId of the event to match.The semantics of how eventTypeId matching is done is as follows:
        * If the event being matched is of type
        * `EventEx <vim/event/EventEx.rst>`_
        * or
        * `ExtendedEvent <vim/event/ExtendedEvent.rst>`_
        * , then we match this value against the
        * eventTypeId
        * (for
        * EventEx
        * ) or
        * eventId
        * (for
        * ExtendedEvent
        * ) member of the Event.
        * Otherwise, we match it against the type of the Event itself.
        * 
        * Either
        * eventType
        * or
        * eventTypeId
        * 
        * must
        * be set.
    objectType (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Name of the type of managed object on which the event is logged.An event alarm defined on a `ManagedEntity <vim/ManagedEntity.rst>`_ is propagated to child entities in the VirtualCenter inventory depending on the value of this attribute. If objectType is any of the following, the alarm is propagated down to all children of that type:
        * A datacenter:
        * `Datacenter <vim/Datacenter.rst>`_
        * .
        * A cluster of host systems:
        * `ClusterComputeResource <vim/ClusterComputeResource.rst>`_
        * .
        * A single host system:
        * `HostSystem <vim/HostSystem.rst>`_
        * .
        * A resource pool representing a set of physical resources on a single host:
        * `ResourcePool <vim/ResourcePool.rst>`_
        * .
        * A virtual machine:
        * `VirtualMachine <vim/VirtualMachine.rst>`_
        * .
        * A datastore:
        * `Datastore <vim/Datastore.rst>`_
        * .
        * A network:
        * `Network <vim/Network.rst>`_
        * .
        * A distributed virtual switch:
        * `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_
        * .
        * 
        * If objectType is unspecified or not contained in the above list, the event alarm is not propagated down to child entities in the VirtualCenter inventory.
        * It is possible to specify an event alarm containing two (or more) different EventAlarmExpression's which contain different objectTypes. In such a case, the event is propagated to all child entities with specified type(s).
    status (`vim.ManagedEntity.Status <vim/ManagedEntity/Status.rst>`_, optional):

       The alarm's new state when this condition is evaluated and satisfied. If not specified then there is no change to alarm status, and all actions are fired (rather than those for the transition).
