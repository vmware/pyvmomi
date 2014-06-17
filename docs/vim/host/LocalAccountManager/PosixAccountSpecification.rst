.. _int: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.host.LocalAccountManager.AccountSpecification: ../../../vim/host/LocalAccountManager/AccountSpecification.rst


vim.host.LocalAccountManager.PosixAccountSpecification
======================================================
  This data object type contains a POSIX-specific parameter for local account creation.
:extends: vim.host.LocalAccountManager.AccountSpecification_

Attributes:
    posixId (`int`_, optional):

       The user ID or group ID of a specified account.
    shellAccess (`bool`_, optional):

       Grants shell access if true. By default, shell access is disallowed.As of vSphere API 4.1, this property has effect only on users with Administrator role on one or more VIM objects. For all others the default is applied.
