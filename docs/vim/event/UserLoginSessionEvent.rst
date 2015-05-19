.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.SessionEvent: ../../vim/event/SessionEvent.rst


vim.event.UserLoginSessionEvent
===============================
  This event records a user logon.
:extends: vim.event.SessionEvent_

Attributes:
    ipAddress (`str`_):

       The IP address of the peer that initiated the connection. This may be the client that originated the session, or it may be an intervening proxy if the binding uses a protocol that supports proxies, such as HTTP.
    userAgent (`str`_, optional):

       The user agent or application
    locale (`str`_):

       The locale of the session.
    sessionId (`str`_):

       The unique identifier for the session.
