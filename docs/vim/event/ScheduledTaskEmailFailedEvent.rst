.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst

.. _vim.event.ScheduledTaskEvent: ../../vim/event/ScheduledTaskEvent.rst


vim.event.ScheduledTaskEmailFailedEvent
=======================================
  This event records the failure of an attempt to send a notification via email for a scheduled task.
:extends: vim.event.ScheduledTaskEvent_

Attributes:
    to (`str`_):

       The destination email address.
    reason (`vmodl.LocalizedMethodFault`_):

       The reason for the failure.
