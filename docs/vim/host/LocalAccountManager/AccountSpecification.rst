
vim.host.LocalAccountManager.AccountSpecification
=================================================
  This data object type contains common parameters for local account creation. The password and description properties are not supported for group accounts on POSIX hosts.
:extends: vmodl.DynamicData_

Attributes:
    id (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The ID of the specified account.
    password (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The password for a user or group.
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The description of the specified account.
