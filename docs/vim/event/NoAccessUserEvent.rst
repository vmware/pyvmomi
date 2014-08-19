
vim.event.NoAccessUserEvent
===========================
  This event records a failed user logon due to insufficient access permission.
:extends: vim.event.SessionEvent_

Attributes:
    ipAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The IP address of the peer that initiated the connection. This may be the client that originated the session, or it may be an intervening proxy if the binding uses a protocol that supports proxies, such as HTTP.
