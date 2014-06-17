.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.AuthorizationManager.Permission: ../../vim/AuthorizationManager/Permission.rst


vim.host.SecuritySpec
=====================
  DataObject used for configuring the Security settings
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    adminPassword (`str`_, optional):

       Administrator password to configure
    removePermission (`vim.AuthorizationManager.Permission`_, optional):

       Permissions to remove
    addPermission (`vim.AuthorizationManager.Permission`_, optional):

       Permissions to add
