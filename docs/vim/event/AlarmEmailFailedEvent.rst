
vim.event.AlarmEmailFailedEvent
===============================
  This event records a failure to complete an alarm email notification.
:extends: vim.event.AlarmEvent_

Attributes:
    entity (`vim.event.ManagedEntityEventArgument <vim/event/ManagedEntityEventArgument.rst>`_):

       The entity with which the alarm is registered.
    to (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The destination email address.
    reason (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

       The reason for the failure.
