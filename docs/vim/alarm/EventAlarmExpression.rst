.. _str: https://docs.python.org/2/library/stdtypes.html

.. _Network: ../../vim/Network.rst

.. _EventEx: ../../vim/event/EventEx.rst

.. _Datastore: ../../vim/Datastore.rst

.. _Datacenter: ../../vim/Datacenter.rst

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _HostSystem: ../../vim/HostSystem.rst

.. _ResourcePool: ../../vim/ResourcePool.rst

.. _ManagedEntity: ../../vim/ManagedEntity.rst

.. _ExtendedEvent: ../../vim/event/ExtendedEvent.rst

.. _VirtualMachine: ../../vim/VirtualMachine.rst

.. _ClusterComputeResource: ../../vim/ClusterComputeResource.rst

.. _DistributedVirtualSwitch: ../../vim/DistributedVirtualSwitch.rst

.. _vim.ManagedEntity.Status: ../../vim/ManagedEntity/Status.rst

.. _vim.alarm.AlarmExpression: ../../vim/alarm/AlarmExpression.rst

.. _vim.alarm.EventAlarmExpression.Comparison: ../../vim/alarm/EventAlarmExpression/Comparison.rst


vim.alarm.EventAlarmExpression
==============================
  An alarm expression that uses the event stream to trigger the alarm.This alarm is triggered when an event matching this expression gets logged.
:extends: vim.alarm.AlarmExpression_
:since: `VI API 2.5`_

Attributes:
    comparisons ([`vim.alarm.EventAlarmExpression.Comparison`_], optional):

       The attributes/values to compare.
    eventType (`str`_):

       The type of the event to trigger the alarm on.
    eventTypeId (`str`_, optional):

       The eventTypeId of the event to match.The semantics of how eventTypeId matching is done is as follows:
        * If the event being matched is of type
        * `EventEx`_
        * or
        * `ExtendedEvent`_
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
    objectType (`str`_, optional):

       Name of the type of managed object on which the event is logged.An event alarm defined on a `ManagedEntity`_ is propagated to child entities in the VirtualCenter inventory depending on the value of this attribute. If objectType is any of the following, the alarm is propagated down to all children of that type:
        * A datacenter:
        * `Datacenter`_
        * .
        * A cluster of host systems:
        * `ClusterComputeResource`_
        * .
        * A single host system:
        * `HostSystem`_
        * .
        * A resource pool representing a set of physical resources on a single host:
        * `ResourcePool`_
        * .
        * A virtual machine:
        * `VirtualMachine`_
        * .
        * A datastore:
        * `Datastore`_
        * .
        * A network:
        * `Network`_
        * .
        * A distributed virtual switch:
        * `DistributedVirtualSwitch`_
        * .
        * 
        * If objectType is unspecified or not contained in the above list, the event alarm is not propagated down to child entities in the VirtualCenter inventory.
        * It is possible to specify an event alarm containing two (or more) different EventAlarmExpression's which contain different objectTypes. In such a case, the event is propagated to all child entities with specified type(s).
    status (`vim.ManagedEntity.Status`_, optional):

       The alarm's new state when this condition is evaluated and satisfied. If not specified then there is no change to alarm status, and all actions are fired (rather than those for the transition).
