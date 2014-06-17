.. _vim.event.AlarmEvent: ../../vim/event/AlarmEvent.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst

.. _vim.event.ManagedEntityEventArgument: ../../vim/event/ManagedEntityEventArgument.rst


vim.event.AlarmSnmpFailedEvent
==============================
  This event records a failure to complete an alarm SNMP notification.
:extends: vim.event.AlarmEvent_

Attributes:
    entity (`vim.event.ManagedEntityEventArgument`_):

       The entity with which the alarm is registered.
    reason (`vmodl.LocalizedMethodFault`_):

       The reason for the failure.
