
vim.AuthorizationManager
========================
  This managed object provides operations to query and update roles and permissions.Privilegesare the basic individual rights required to perform operations. They are statically defined and never change for a single version of a product. Examples of privileges arePower on a virtual machineorConfigure a host.Rolesare aggregations of privileges, used for convenience. For user-defined roles, the system-defined privileges, "System.Anonymous", "System.View", and "System.Read" are always present.Permissionsare the actual access-control rules. A permission is defined on a ManagedEntity and specifies the user or group (principal) to which the rule applies. The role specifies the privileges to apply, and the propagate flag specifies whether or not the rule applies to sub-objects of the managed entity.A ManagedEntity may have multiple permissions, but may have only one permission per user or group. If, when logging in, a user has both a user permission and a group permission (as a group member) for the same entity, then the user-specific permission takes precedent. If there is no user-specific permission, but two or more group permissions are present, and the user is a member of the groups, then the privileges are the union of the specified roles.Managed entities may be collected together into acomplex entityfor the purpose of applying permissions consistently. Complex entities may have a Datacenter, ComputeResource, or ClusterComputeResource as a parent, with other child managed objects as additional parts of the complex entity:
   * A Datacenter's child objects are the root virtual machine and host Folders.
   * A ComputeResource's child objects are the root ResourcePool and HostSystem.
   * A ClusterComputeResource has only the root ResourcePool as a child object.
   * Child objects in a complex entity are forced to inherit permissions from the parent object. When query operations are used to discover permissions on child objects of complex entities, different results may be returned for the owner of the permission. In some cases, the child object of the complex entity is returned as the object that defines the permission, and in other cases, the parent from which the permission is propagated is returned as the object that defines the permission. In both cases, the information about the owner of the permission is correct, since the entities within a complex entity are considered equivalent. Permissions defined on complex entities are always applicable on the child entities, regardless of the propagation flag, but may only be defined or modified on the parent object.
   * In a group of fault-tolerance (FT) protected VirtualMachines, the secondary VirtualMachines are forced to inherit permissions from the primary VirtualMachine. Queries to discover permissions on FT secondary VMs always return the primary VM as the object that defines the permissions. Permissions defined on an FT primary VM are always applicable on its secondary VMs, but can only be defined or modified on the primary VM.




Attributes
----------
    privilegeList ([`vim.AuthorizationManager.Privilege <vim/AuthorizationManager/Privilege.rst>`_]):
      privilege: System.View
       The list of system-defined privileges.
    roleList ([`vim.AuthorizationManager.Role <vim/AuthorizationManager/Role.rst>`_]):
      privilege: System.View
       The currently defined roles in the system, including static system-defined roles.
    description (`vim.AuthorizationDescription <vim/AuthorizationDescription.rst>`_):
      privilege: System.View
       Static, descriptive strings for system roles and privileges.


Methods
-------


AddAuthorizationRole(name, privIds):
   Adds a new role. This method will add a user-defined role with given list of privileges and three system-defined privileges, "System.Anonymous", "System.View", and "System.Read".


  Privilege:
               Authorization.ModifyRoles



  Args:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Name of the new role.


    privIds (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       List of privileges to assign to the role.




  Returns:
    `int <https://docs.python.org/2/library/stdtypes.html>`_:
         The roleId assigned to the new role.

  Raises:

    `vim.fault.AlreadyExists <vim/fault/AlreadyExists.rst>`_: 
       if a role with the given name already exists.

    `vim.fault.InvalidName <vim/fault/InvalidName.rst>`_: 
       if the role name is empty.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if privIds contains an unknown privilege.


RemoveAuthorizationRole(roleId, failIfUsed):
   Removes a role.


  Privilege:
               Authorization.ModifyRoles



  Args:
    roleId (`int <https://docs.python.org/2/library/stdtypes.html>`_):


    failIfUsed (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       If true, prevents the role from being removed if any permissions are using it.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the role does not exist.

    `vim.fault.RemoveFailed <vim/fault/RemoveFailed.rst>`_: 
       if failIfUsed is true and the role has permissions.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the role is a system role, meaning it cannot be changed.


UpdateAuthorizationRole(roleId, newName, privIds):
   Updates a role's name or privileges. If the new set of privileges are assigned to the role, the system-defined privileges, "System.Anonymous", "System.View", and "System.Read" will be assigned to the role too.


  Privilege:
               Authorization.ModifyRoles



  Args:
    roleId (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       The ID of the role that is updated.


    newName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The new name for the role.


    privIds (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The new set of privileges to assign to the role.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the role does not exist, or if a privilege in the list cannot be found.

    `vim.fault.InvalidName <vim/fault/InvalidName.rst>`_: 
       if the new role name is empty.

    `vim.fault.AlreadyExists <vim/fault/AlreadyExists.rst>`_: 
       if another role with the given name already exists.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the role is a system role, meaning it cannot be changed.

    `vim.fault.NoPermission <vim/fault/NoPermission.rst>`_: 
       if current session does not have any privilege that being updated in the new role or "Authorization.ModifyRoles" privilege on the root folder.


MergePermissions(srcRoleId, dstRoleId):
   Reassigns all permissions of a role to another role.


  Privilege:
               Authorization.ReassignRolePermissions



  Args:
    srcRoleId (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       The ID of the source role providing the permissions which are changing.


    dstRoleId (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       The ID of the destination role to which the permissions are reassigned.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if either the source or destination role does not exist.

    `vim.fault.AuthMinimumAdminPermission <vim/fault/AuthMinimumAdminPermission.rst>`_: 
       if srcRoleId is the Administrator role, meaning that applying the change would leave the system with no Administrator permission on the root node.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if dstRoleId is the View or Anonymous role or if both role IDs are the same.

    `vim.fault.NoPermission <vim/fault/NoPermission.rst>`_: 
       if current session does not have any privilege in the source or destination role or "Authorization.ReassignRolePermissions" privilege on the root folder.


RetrieveRolePermissions(roleId):
   Finds all the permissions that use a particular role. The result is restricted to managed entities that are visible to the user making the call.


  Privilege:
               System.View



  Args:
    roleId (`int <https://docs.python.org/2/library/stdtypes.html>`_):




  Returns:
    [`vim.AuthorizationManager.Permission <vim/AuthorizationManager/Permission.rst>`_]:
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the role does not exist.


RetrieveEntityPermissions(entity, inherited):
   Gets permissions defined on or effective on a managed entity. This returns the actual permission objects defined in the system for all users and groups relative to the managed entity. The inherited flag specifies whether or not to include permissions defined by the parents of this entity that propagate to this entity.For complex entities, the entity reported as defining the permission may be either the parent or a child entity belonging to the complex entity.The purpose of this method is to discover permissions for administration purposes, not to determine the current permissions. The current user's permissions are found on the `effectiveRole <vim/ManagedEntity.rst#effectiveRole>`_ property of the user's ManagedEntity.


  Privilege:



  Args:
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):


    inherited (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       Whether or not to include propagating permissions defined by parent entities.




  Returns:
    [`vim.AuthorizationManager.Permission <vim/AuthorizationManager/Permission.rst>`_]:
         

  Raises:

    `vmodl.fault.ManagedObjectNotFound <vmodl/fault/ManagedObjectNotFound.rst>`_: 
       if the entity does not exist.


RetrieveAllPermissions():
   Finds all permissions defined in the system. The result is restricted to the managed entities visible to the user making the call.


  Privilege:
               System.View



  Args:


  Returns:
    [`vim.AuthorizationManager.Permission <vim/AuthorizationManager/Permission.rst>`_]:
         


SetEntityPermissions(entity, permission):
   Defines one or more permission rules on an entity or updates rules if already present for the given user or group on the entity.If a permission is specified multiple times for the same user or group, then the last permission specified takes effect.The operation is applied transactionally per permission and is applied to the entity following the order of the elements in the permission array argument. This means that if a failure occurs, the method terminates at that point in the permission array with an exception, leaving at least one and as many as all permissions unapplied.This will fail with an InvalidArgument fault if called on: the direct child folders of a datacenter managed object, the root resource pool of a ComputeResource or ClusterComputeResource, or a HostSystem that is part of a ComputeResource (Stand-alone Host). These objects always have the same permissions as their parent.This will fail with an InvalidArgument fault if called on a fault-tolerance (FT) secondary VirtualMachine. Such a VirtualMachine always has the same permissions as its FT primary VirtualMachine.


  Privilege:



  Args:
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):
       The entity on which to set permissions.


    permission (`vim.AuthorizationManager.Permission <vim/AuthorizationManager/Permission.rst>`_, optional):
       An array of specifications for permissions on the entity.




  Returns:
    None
         

  Raises:

    `vim.fault.UserNotFound <vim/fault/UserNotFound.rst>`_: 
       if a given user or group does not exist.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if a permission's roleId is not valid.

    `vim.fault.AuthMinimumAdminPermission <vim/fault/AuthMinimumAdminPermission.rst>`_: 
       if this change would leave the system with no Administrator permission on the root node, or it would grant further permission to a user or group who already has Administrator permission on the root node.

    `vmodl.fault.ManagedObjectNotFound <vmodl/fault/ManagedObjectNotFound.rst>`_: 
       if the given entity does not exist.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if one of the new role IDs is the View or Anonymous role, or the entity does not support assigning permissions.

    `vim.fault.NoPermission <vim/fault/NoPermission.rst>`_: 
       if current session does not have any privilege in any permission that being set or "Authorization.ModifyPermissions" privilege on the entity.


ResetEntityPermissions(entity, permission):
   Update the entire set of permissions defined on an entity. Any existing permissions on the entity are removed and replaced with the provided set.If a permission is specified multiple times for the same user or group, the last permission specified takes effect.The operation is transactional per permission and could partially fail. The updates are performed in the order of the permission array argument. The first failed update will abort the operation and throw the appropriate exception. When the operation aborts, any permissions that have not yet been removed are left in their original state.After updates are applied, original permissions that are not in the new set are removed. A failure to remove a permission, such as a violation of the minimum administrator permission rule, will abort the operation and could leave remaining original permissions still effective on the entity.This will fail with an InvalidArgument fault if called on: the direct child folders of a datacenter managed object, the root resource pool of a ComputeResource or ClusterComputeResource, or a HostSystem that is part of a ComputeResource (Stand-alone Host). These objects always have the same permissions as their parent.This will fail with an InvalidArgument fault if called on a fault-tolerance (FT) secondary VirtualMachine. Such a VirtualMachine always has the same permissions as its FT primary VirtualMachine.


  Privilege:



  Args:
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):
       The entity on which permissions are updated.


    permission (`vim.AuthorizationManager.Permission <vim/AuthorizationManager/Permission.rst>`_, optional):
       The list of Permission objects that define the new rules for access to the entity and potentially entities below it. If the list is empty, all permissions on the entity are removed.




  Returns:
    None
         

  Raises:

    `vim.fault.UserNotFound <vim/fault/UserNotFound.rst>`_: 
       if one of the given users or groups does not exist.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if a permission for this entity and user or group does not exist.

    `vim.fault.AuthMinimumAdminPermission <vim/fault/AuthMinimumAdminPermission.rst>`_: 
       if this change would leave the system with no Administrator permission on the root node, or it would grant further permission to a user or group who already has Administrator permission on the root node.

    `vmodl.fault.ManagedObjectNotFound <vmodl/fault/ManagedObjectNotFound.rst>`_: 
       if the given entity does not exist.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if one of the new role IDs is the View or Anonymous role, or the entity does not support assigning permissions.

    `vim.fault.NoPermission <vim/fault/NoPermission.rst>`_: 
       if current session does not have any privilege in the updated permission or "Authorization.ModifyPermissions" privilege on the entity.


RemoveEntityPermission(entity, user, isGroup):
   Removes a permission rule from an entity.This will fail with an InvalidArgument fault if called on: the direct child folders of a datacenter managed object, the root resource pool of a ComputeResource or ClusterComputeResource, or a HostSystem that is part of a ComputeResource (Stand-alone Host). These objects always have the same permissions as their parent.This will fail with an InvalidArgument fault if called on a fault-tolerance (FT) secondary VirtualMachine. Such a VirtualMachine always has the same permissions as its FT primary VirtualMachine.


  Privilege:



  Args:
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):
       Entity on which a permission is removed.


    user (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       User or group for which the permission is defined.


    isGroup (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       True, if user refers to a group name; false, for a user name.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if a permission for this entity and user or group does not exist.

    `vim.fault.AuthMinimumAdminPermission <vim/fault/AuthMinimumAdminPermission.rst>`_: 
       if this change would leave the system with no Administrator permission on the root node.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if one of the new role IDs is the View or Anonymous role, or the entity does not support removing permissions.

    `vim.fault.NoPermission <vim/fault/NoPermission.rst>`_: 
       if current session does not have any privilege in the permission to be removed or "Authorization.ModifyPermissions" privilege on the entity.


HasPrivilegeOnEntity(entity, sessionId, privId):
   Check whether a session holds a set of privileges on a managed entity.If the session does not exist, false is returned for all privileges.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               System.View



  Args:
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):
       The entity on which the privileges are checked.


    sessionId (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The session ID to check privileges for. A sesssion ID can be obtained from `key <vim/UserSession.rst#key>`_ .


    privId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The array of privilege IDs to check.




  Returns:
    [`bool <https://docs.python.org/2/library/stdtypes.html>`_]:
         a boolean value for each privilege indicating whether the session holds the privilege.

  Raises:

    `vmodl.fault.ManagedObjectNotFound <vmodl/fault/ManagedObjectNotFound.rst>`_: 
       if the given entity does not exist.


HasPrivilegeOnEntities(entity, sessionId, privId):
   Check whether a session holds a set of privileges on a set of managed entities.If the session does not exist, false is returned for all privileges of all the entities.
  since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_


  Privilege:
               System.View



  Args:
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):
       The set of entities on which the privileges are checked.


    sessionId (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The session ID to check privileges for. A sesssion ID can be obtained from `key <vim/UserSession.rst#key>`_ .


    privId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The array of privilege IDs to check.




  Returns:
    [`vim.AuthorizationManager.EntityPrivilege <vim/AuthorizationManager/EntityPrivilege.rst>`_]:
         The privilege check result.

  Raises:

    `vmodl.fault.ManagedObjectNotFound <vmodl/fault/ManagedObjectNotFound.rst>`_: 
       if a given entity does not exist.


