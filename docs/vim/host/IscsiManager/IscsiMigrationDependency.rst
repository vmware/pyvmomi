.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.IscsiManager.IscsiStatus: ../../../vim/host/IscsiManager/IscsiStatus.rst

.. _vim.host.IscsiManager.IscsiDependencyEntity: ../../../vim/host/IscsiManager/IscsiDependencyEntity.rst


vim.host.IscsiManager.IscsiMigrationDependency
==============================================
  Provides migration dependency information for a given Physical NIC. Lists all the iSCSI and networking resources impacted if migration of a given Physical NIC is to take place.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    migrationAllowed (`bool`_):

       Indicates whether migration can be safely performed If migrationAllowed is False, the disallowReason will contain the specific condition that makes the migration attempt unsafe.
    disallowReason (`vim.host.IscsiManager.IscsiStatus`_, optional):

       Reasons for not allowing migration. Unset if migrationAllowed is true.
    dependency (`vim.host.IscsiManager.IscsiDependencyEntity`_, optional):

       Details of all the resources affected by migration.
