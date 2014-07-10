.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst


vim.AuthorizationManager.Permission
===================================
  This data object type provides assignment of some role access to a principal on a specific entity. A ManagedEntity is limited to one permission per principal.
:extends: vmodl.DynamicData_

Attributes:
    entity (`vim.ManagedEntity`_, optional):

       Managed entity the permission is defined on. Left unset when calling setPermissions or resetPermissions, but present for the results of permission queries.
    principal (`str`_):

       User or group receiving access in the form of "login" for local or "DOMAIN\login" for users in a Windows domain.
    group (`bool`_):

       Whether principal refers to a user or a group. True for a group and false for a user.
    roleId (`int`_):

       Reference to the role providing the access.
    propagate (`bool`_):

       Whether or not this permission propagates down the hierarchy to sub-entities.
