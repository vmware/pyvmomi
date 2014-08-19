
vim.AuthorizationManager.Role
=============================
  This data object type specifies a collection of privileges used to grant access to users on managed entities.
:extends: vmodl.DynamicData_

Attributes:
    roleId (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Unique role identifier.
    system (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether or not the role is system-defined. System-defined roles cannot be changed.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       System-defined or user-defined role name.
    info (`vim.Description <vim/Description.rst>`_):

       Displayable role information.
    privilege ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Privileges provided by this role, by privilege identifier.
