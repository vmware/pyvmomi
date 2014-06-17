.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.AlarmEvent: ../../vim/event/AlarmEvent.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst

.. _vim.event.ManagedEntityEventArgument: ../../vim/event/ManagedEntityEventArgument.rst


vim.event.AlarmEmailFailedEvent
===============================
  This event records a failure to complete an alarm email notification.
:extends: vim.event.AlarmEvent_

Attributes:
    entity (`vim.event.ManagedEntityEventArgument`_):

       The entity with which the alarm is registered.
    to (`str`_):

       The destination email address.
    reason (`vmodl.LocalizedMethodFault`_):

       The reason for the failure.
