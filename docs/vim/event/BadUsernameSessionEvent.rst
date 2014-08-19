
vim.event.BadUsernameSessionEvent
=================================
  This event records a failed user logon. Failed logons are due to no match existing between the provided user name and password combination and the combinations stored for authentication.
:extends: vim.event.SessionEvent_

Attributes:
    ipAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The IP address of the peer that initiated the connection. This may be the client that originated the session, or it may be an intervening proxy if the binding uses a protocol that supports proxies, such as HTTP.
