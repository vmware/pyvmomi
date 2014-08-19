
vim.AuthorizationManager.EntityPrivilege
========================================
  This class defines whether a set of privileges are granted for a managed entity.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):

       The entity on which the privileges are checked.
    privAvailability ([`vim.AuthorizationManager.PrivilegeAvailability <vim/AuthorizationManager/PrivilegeAvailability.rst>`_]):

       whether a set of privileges are granted for the managed entity.
