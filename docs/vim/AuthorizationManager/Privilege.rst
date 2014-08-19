
vim.AuthorizationManager.Privilege
==================================
  This data object type provides access to some aspect of the system. Privileges are generally independent. This means a user with a privilege usually can perform an associated set of actions without needing any additional supporting privileges.Within each product version, privileges do not change. See `AuthorizationDescription <vim/AuthorizationDescription.rst>`_ for detailed information on the privileges defined by the system.
:extends: vmodl.DynamicData_

Attributes:
    privId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Unique identifier.
    onParent (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Determines whether or not the privilege is applied on the parent entity.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Privilege name.
    privGroupName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Group name.
