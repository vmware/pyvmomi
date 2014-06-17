.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.SessionManager.LocalTicket
==============================
  This data object type contains the user name and location of the file containing the password that clients can use for one-time logon to a server.
:extends: vmodl.DynamicData_

Attributes:
    userName (`str`_):

       User name to be used for logon.
    passwordFilePath (`str`_):

       Absolute local path to the file containing a one-time password.
