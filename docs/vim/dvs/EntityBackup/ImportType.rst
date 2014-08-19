vim.dvs.EntityBackup.ImportType
===============================
  The `EntityImportType <vim/dvs/EntityBackup/ImportType.rst>`_ enum defines the import type for a `DistributedVirtualSwitchManager <vim/dvs/DistributedVirtualSwitchManager.rst>`_ . `DVSManagerImportEntity_Task <vim/dvs/DistributedVirtualSwitchManager.rst#importEntity>`_ operation.
  :contained by: `vim.dvs.EntityBackup <vim/dvs/EntityBackup.rst>`_

  :type: `vim.dvs.EntityBackup.ImportType <vim/dvs/EntityBackup/ImportType.rst>`_

  :name: applyToEntitySpecified

values:
--------

createEntityWithNewIdentifier
   Create the entity with new identifiers. Specify the `EntityBackupConfig <vim/dvs/EntityBackup/Config.rst>`_ . `name <vim/dvs/EntityBackup/Config.rst#name>`_ and `EntityBackupConfig <vim/dvs/EntityBackup/Config.rst>`_ . `container <vim/dvs/EntityBackup/Config.rst#container>`_ properties.The Server ignores any value for the `EntityBackupConfig <vim/dvs/EntityBackup/Config.rst>`_ . `key <vim/dvs/EntityBackup/Config.rst#key>`_ property.

applyToEntitySpecified
   Apply the configuration specified in the `EntityBackupConfig <vim/dvs/EntityBackup/Config.rst>`_ . `configBlob <vim/dvs/EntityBackup/Config.rst#configBlob>`_ property to the entity specified in the `EntityBackupConfig <vim/dvs/EntityBackup/Config.rst>`_ . `entityType <vim/dvs/EntityBackup/Config.rst#entityType>`_ and `EntityBackupConfig <vim/dvs/EntityBackup/Config.rst>`_ . `key <vim/dvs/EntityBackup/Config.rst#key>`_ properties. If you specify `EntityBackupConfig <vim/dvs/EntityBackup/Config.rst>`_ . `name <vim/dvs/EntityBackup/Config.rst#name>`_ , the Server uses the specified name to rename the entity.The Server ignores any value for the `EntityBackupConfig <vim/dvs/EntityBackup/Config.rst>`_ . `container <vim/dvs/EntityBackup/Config.rst#container>`_ property.

createEntityWithOriginalIdentifier
   Recreate the entities with the original identifiers of the entity from which backup was created. The Server throws an exception if an entity with the same identifier already exists. This option will also add the host members to the `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ and will try to get the virtual machine networking back with the same `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_ . Specify a `Folder <vim/Folder.rst>`_ as the `EntityBackupConfig <vim/dvs/EntityBackup/Config.rst>`_ . `container <vim/dvs/EntityBackup/Config.rst#container>`_ for `EntityBackupConfig <vim/dvs/EntityBackup/Config.rst>`_ . `entityType <vim/dvs/EntityBackup/Config.rst#entityType>`_ "distributedVirtualSwitch".The Server ignores any values for the `EntityBackupConfig <vim/dvs/EntityBackup/Config.rst>`_ . `key <vim/dvs/EntityBackup/Config.rst#key>`_ and `EntityBackupConfig <vim/dvs/EntityBackup/Config.rst>`_ . `name <vim/dvs/EntityBackup/Config.rst#name>`_ properties.
