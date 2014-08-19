
vim.host.SecuritySpec
=====================
  DataObject used for configuring the Security settings
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    adminPassword (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Administrator password to configure
    removePermission ([`vim.AuthorizationManager.Permission <vim/AuthorizationManager/Permission.rst>`_], optional):

       Permissions to remove
    addPermission ([`vim.AuthorizationManager.Permission <vim/AuthorizationManager/Permission.rst>`_], optional):

       Permissions to add
