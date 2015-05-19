.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.SessionEvent: ../../vim/event/SessionEvent.rst


vim.event.SessionTerminatedEvent
================================
  This event records the termination of a session.
:extends: vim.event.SessionEvent_

Attributes:
    sessionId (`str`_):

       The unique identifier of the terminated session.
    terminatedUsername (`str`_):

       The name of the user owning the terminated session.
