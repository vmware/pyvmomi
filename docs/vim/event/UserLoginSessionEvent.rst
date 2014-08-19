
vim.event.UserLoginSessionEvent
===============================
  This event records a user logon.
:extends: vim.event.SessionEvent_

Attributes:
    ipAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The IP address of the peer that initiated the connection. This may be the client that originated the session, or it may be an intervening proxy if the binding uses a protocol that supports proxies, such as HTTP.
    userAgent (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The user agent or application
    locale (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The locale of the session.
    sessionId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The unique identifier for the session.
