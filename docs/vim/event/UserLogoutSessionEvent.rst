
vim.event.UserLogoutSessionEvent
================================
  This event records a user logoff, disconnection, or session timeout.
:extends: vim.event.SessionEvent_

Attributes:
    ipAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The IP address of client
    userAgent (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The user agent or application
    callCount (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Number of API invocations made by the session
    sessionId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The unique identifier for the session.
    loginTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Timestamp when the user logged on for this session.
