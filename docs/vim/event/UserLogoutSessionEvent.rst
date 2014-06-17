.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.SessionEvent: ../../vim/event/SessionEvent.rst


vim.event.UserLogoutSessionEvent
================================
  This event records a user logoff, disconnection, or session timeout.
:extends: vim.event.SessionEvent_

Attributes:
    ipAddress (`str`_, optional):

       The IP address of client
    userAgent (`str`_, optional):

       The user agent or application
    callCount (`long`_, optional):

       Number of API invocations made by the session
    sessionId (`str`_, optional):

       The unique identifier for the session.
    loginTime (`datetime`_, optional):

       Timestamp when the user logged on for this session.
