.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../vmodl/DynamicData.rst


vim.UserSession
===============
  Information about a current user session.
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_):

       A unique identifier for this session, also known as the session ID.
    userName (`str`_):

       The user name represented by this session.
    fullName (`str`_):

       The full name of the user, if available.
    loginTime (`datetime`_):

       Timestamp when the user last logged on to the server.
    lastActiveTime (`datetime`_):

       Timestamp when the user last executed a command.
    locale (`str`_):

       The locale for the session used for data formatting and preferred for messages.
    messageLocale (`str`_):

       The locale used for messages for the session. If there are no localized messages for the user-specified locale, then the server determines this locale.
    extensionSession (`bool`_):

       Whether or not this session belongs to a VC Extension.
    ipAddress (`str`_):

       The client identity. It could be IP address, or pipe name depended on client binding
    userAgent (`str`_):

       The name of user agent or application
    callCount (`long`_):

       Number of API invocations since the session started
