.. _name: ../../../vim/dvs/EntityBackup/Config.rst#name

.. _Folder: ../../../vim/Folder.rst

.. _container: ../../../vim/dvs/EntityBackup/Config.rst#container

.. _entityType: ../../../vim/dvs/EntityBackup/Config.rst#entityType

.. _configBlob: ../../../vim/dvs/EntityBackup/Config.rst#configBlob

.. _EntityImportType: ../../../vim/dvs/EntityBackup/ImportType.rst

.. _EntityBackupConfig: ../../../vim/dvs/EntityBackup/Config.rst

.. _vim.dvs.EntityBackup: ../../../vim/dvs/EntityBackup.rst

.. _DistributedVirtualSwitch: ../../../vim/DistributedVirtualSwitch.rst

.. _DVSManagerImportEntity_Task: ../../../vim/dvs/DistributedVirtualSwitchManager.rst#importEntity

.. _DistributedVirtualPortgroup: ../../../vim/dvs/DistributedVirtualPortgroup.rst

.. _DistributedVirtualSwitchManager: ../../../vim/dvs/DistributedVirtualSwitchManager.rst

.. _vim.dvs.EntityBackup.ImportType: ../../../vim/dvs/EntityBackup/ImportType.rst

vim.dvs.EntityBackup.ImportType
===============================
  The `EntityImportType`_ enum defines the import type for a `DistributedVirtualSwitchManager`_ . `DVSManagerImportEntity_Task`_ operation.
  :contained by: `vim.dvs.EntityBackup`_

  :type: `vim.dvs.EntityBackup.ImportType`_

  :name: applyToEntitySpecified

values:
--------

createEntityWithNewIdentifier
   Create the entity with new identifiers. Specify the `EntityBackupConfig`_ . `name`_ and `EntityBackupConfig`_ . `container`_ properties.The Server ignores any value for the `EntityBackupConfig`_ . `key`_ property.

applyToEntitySpecified
   Apply the configuration specified in the `EntityBackupConfig`_ . `configBlob`_ property to the entity specified in the `EntityBackupConfig`_ . `entityType`_ and `EntityBackupConfig`_ . `key`_ properties. If you specify `EntityBackupConfig`_ . `name`_ , the Server uses the specified name to rename the entity.The Server ignores any value for the `EntityBackupConfig`_ . `container`_ property.

createEntityWithOriginalIdentifier
   Recreate the entities with the original identifiers of the entity from which backup was created. The Server throws an exception if an entity with the same identifier already exists. This option will also add the host members to the `DistributedVirtualSwitch`_ and will try to get the virtual machine networking back with the same `DistributedVirtualPortgroup`_ . Specify a `Folder`_ as the `EntityBackupConfig`_ . `container`_ for `EntityBackupConfig`_ . `entityType`_ "distributedVirtualSwitch".The Server ignores any values for the `EntityBackupConfig`_ . `key`_ and `EntityBackupConfig`_ . `name`_ properties.
