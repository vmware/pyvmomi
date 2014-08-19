
vim.host.LocalAccountManager
============================
  This managed object type provides an interface through which local accounts on a host are managed. Note that this managed object applies only to applications that use a local account database on the host to provide authentication (ESX Server, for example). POSIX and win32 hosts may impose different restrictions on the password, ID, and description formats. POSIX host implementation may restrict the user or group name to be lower case letters and less than 16 characters in total. It may also disallow characters such as ";", "\n", and so on. In short, all the platform dependent rules and restrictions regarding naming of users/groups and password apply here. An InvalidArgument fault is thrown if any of these rules are not obeyed.




Attributes
----------


Methods
-------


CreateUser(user):
   Creates a local user account using the parameters defined in the `HostLocalAccountManagerAccountSpecification <vim/host/LocalAccountManager/AccountSpecification.rst>`_ data object type. For POSIX hosts, passing `HostLocalAccountManagerPosixAccountSpecification <vim/host/LocalAccountManager/PosixAccountSpecification.rst>`_ data object type allows you to control the format of the user ID of the user account being created.


  Privilege:
               Host.Local.ManageUserGroups



  Args:
    user (`vim.host.LocalAccountManager.AccountSpecification <vim/host/LocalAccountManager/AccountSpecification.rst>`_):
       Specification of user being created.




  Returns:
    None
         

  Raises:

    `vim.fault.AlreadyExists <vim/fault/AlreadyExists.rst>`_: 
       if the specified local user account already exists.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the user name or password has an invalid format.


UpdateUser(user):
   Updates a local user account using the parameters defined in the `HostLocalAccountManagerAccountSpecification <vim/host/LocalAccountManager/AccountSpecification.rst>`_ data object type.


  Privilege:
               Host.Local.ManageUserGroups



  Args:
    user (`vim.host.LocalAccountManager.AccountSpecification <vim/host/LocalAccountManager/AccountSpecification.rst>`_):
       Specification of user being updated.




  Returns:
    None
         

  Raises:

    `vim.fault.UserNotFound <vim/fault/UserNotFound.rst>`_: 
       if user is not found.

    `vim.fault.AlreadyExists <vim/fault/AlreadyExists.rst>`_: 
       if new account specification specifies an existing user's ID.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if new password or description has an invalid format.


CreateGroup(group):
   Creates a local group account using the parameters defined in the `HostLocalAccountManagerAccountSpecification <vim/host/LocalAccountManager/AccountSpecification.rst>`_ data object type. For POSIX hosts, passing the `HostLocalAccountManagerPosixAccountSpecification <vim/host/LocalAccountManager/PosixAccountSpecification.rst>`_ data object type allows you to control the group ID format of the group account being created.


  Privilege:
               Host.Local.ManageUserGroups



  Args:
    group (`vim.host.LocalAccountManager.AccountSpecification <vim/host/LocalAccountManager/AccountSpecification.rst>`_):
       Specification of group being created.




  Returns:
    None
         

  Raises:

    `vim.fault.AlreadyExists <vim/fault/AlreadyExists.rst>`_: 
       if specified local group already exists.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if group name is in invalid format.


RemoveUser(userName):
   Removes a local user account.As of vSphere API 5.1, this operation will first try to remove all permissions associated with the specifed account. The permissions of the user are removed one by one, not atomically, and the operation is not rolled back, if the removal of some permission fails.


  Privilege:
               Host.Local.ManageUserGroups



  Args:
    userName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       User ID of the user account being removed.




  Returns:
    None
         

  Raises:

    `vim.fault.UserNotFound <vim/fault/UserNotFound.rst>`_: 
       if the specified userName does not exist.

    `vmodl.fault.SecurityError <vmodl/fault/SecurityError.rst>`_: 
       if trying to remove the last local user with DCUI access, or if trying to remove the last local user with full administrative privileges, or if the system has encountered an error while trying to remove user's permissions. or if the account cannot be removed due to permission issues.


RemoveGroup(groupName):
   Removes a local group account.


  Privilege:
               Host.Local.ManageUserGroups



  Args:
    groupName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Group ID of the group account being removed.




  Returns:
    None
         

  Raises:

    `vim.fault.UserNotFound <vim/fault/UserNotFound.rst>`_: 
       if the specified groupName does not exist.


AssignUserToGroup(user, group):
   Assigns a user to a group.


  Privilege:
               Host.Local.ManageUserGroups



  Args:
    user (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       User ID of the account whose group membership is being assigned.


    group (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Destination group account to which the user is being assigned.




  Returns:
    None
         

  Raises:

    `vim.fault.UserNotFound <vim/fault/UserNotFound.rst>`_: 
       if the specified user or group does not exist.

    `vim.fault.AlreadyExists <vim/fault/AlreadyExists.rst>`_: 
       if the user is already a member of the target group.


UnassignUserFromGroup(user, group):
   Unassigns a user from a group.


  Privilege:
               Host.Local.ManageUserGroups



  Args:
    user (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       User being unassigned from group.


    group (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Group from which the user is being removed.




  Returns:
    None
         

  Raises:

    `vim.fault.UserNotFound <vim/fault/UserNotFound.rst>`_: 
       if the specified user or group does not exist.

    `vim.fault.NoPermission <vim/fault/NoPermission.rst>`_: 
       if the group is the only group to which the user belongs.


