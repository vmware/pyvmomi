# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim



class TenantManager(pyVmomi.VmomiSupport.ManagedObject):
   """A singleton managed object for managing vCenter tenants."""
   def MarkServiceProviderEntities(self, entity: list[pyVmomi.vim.ManagedEntity]) -> None:
      """
      Define a set of ManagedEntity objects as used for tenant management.
      
      Those entities are a starting point of an inventory hierarchy
      (sub-tree) that functionally exists in the tenant's inventory but are
      owned by the system user of the vCenter Server.
      The operations which the tenant may perform on these objects depend
      on the permissions granted to the tenant by the SaaS provisioning
      layer.
      Permissions that the tenant may create on the parent objects of the
      management entities do not propagate to the hierarchies of
      management entities and thus have no effect on them.
      This operation will fail for all the entities if any of them does
      not exist.
      The method behaviour is transactional - either all entities are
      marked or none if an error occurs while processing them.
      The user calling this method should hold TenantManager.Update on the
      root folder and TenantManager.Update on each entity currently
      being marked as a service provider one. These are strict privilege
      requirements allowing only administrators to call the method.
      
      Args:
          entity: an array of management entities.
      
      Raises:
          pyVmomi.vmodl.fault.ManagedObjectNotFound: if any of the entities doesn't exist.
          pyVmomi.vim.fault.AuthMinimumAdminPermission: if this change will leave the
              system with no Administrator permission on the root folder
              of the service provider inventory.
      """
      ...
   def UnmarkServiceProviderEntities(self, entity: list[pyVmomi.vim.ManagedEntity]) -> None:
      """
      Resets the management type of an array of ManagedEntity objects.
      
      This operation will fail if any of the entities does not exist.
      The method behaviour is transactional - either all entities are
      unmarked or none if an error occurs while processing them.
      The user calling this method should hold TenantManager.Update on the
      root folder and TenantManager.Update on each entity currently
      being unmarked as a service provider one. These are strict privilege
      requirements allowing only administrators to call the method.
      
      Args:
          entity: an array of management entities.
      
      Raises:
          pyVmomi.vmodl.fault.ManagedObjectNotFound: if any of the entities doesn't exist.
      """
      ...
   def RetrieveServiceProviderEntities(self) -> list[pyVmomi.vim.ManagedEntity]:
      """
      Retrieves the list of tenant management entities.
      
      Returns:
          the array of tenant management resources.
      """
      ...
