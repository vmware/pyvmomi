
vim.event.SessionTerminatedEvent
================================
  This event records the termination of a session.
:extends: vim.event.SessionEvent_

Attributes:
    sessionId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The unique identifier of the terminated session.
    terminatedUsername (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the user owning the terminated session.
