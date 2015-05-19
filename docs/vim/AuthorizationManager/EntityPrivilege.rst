.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst

.. _vim.AuthorizationManager.PrivilegeAvailability: ../../vim/AuthorizationManager/PrivilegeAvailability.rst


vim.AuthorizationManager.EntityPrivilege
========================================
  This class defines whether a set of privileges are granted for a managed entity.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    entity (`vim.ManagedEntity`_):

       The entity on which the privileges are checked.
    privAvailability ([`vim.AuthorizationManager.PrivilegeAvailability`_]):

       whether a set of privileges are granted for the managed entity.
