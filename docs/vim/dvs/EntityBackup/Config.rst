.. _str: https://docs.python.org/2/library/stdtypes.html

.. _name: ../../../vim/dvs/EntityBackup/Config.rst#name

.. _uuid: ../../../vim/DistributedVirtualSwitch.rst#uuid

.. _base64: https://docs.python.org/2/library/stdtypes.html

.. _Folder: ../../../vim/Folder.rst

.. _container: ../../../vim/dvs/EntityBackup/Config.rst#container

.. _entityType: ../../../vim/dvs/EntityBackup/Config.rst#entityType

.. _EntityType: ../../../vim/dvs/EntityBackup/EntityType.rst

.. _vSphere API 5.1: ../../../vim/version.rst#vimversionversion8

.. _EntityImportType: ../../../vim/dvs/EntityBackup/ImportType.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.ManagedEntity: ../../../vim/ManagedEntity.rst

.. _EntityBackupConfig: ../../../vim/dvs/EntityBackup/Config.rst

.. _applyToEntitySpecified: ../../../vim/dvs/EntityBackup/ImportType.rst#applyToEntitySpecified

.. _DistributedVirtualSwitch: ../../../vim/DistributedVirtualSwitch.rst

.. _DistributedVirtualPortgroup: ../../../vim/dvs/DistributedVirtualPortgroup.rst

.. _DVSManagerImportEntity_Task: ../../../vim/dvs/DistributedVirtualSwitchManager.rst#importEntity

.. _DVSManagerExportEntity_Task: ../../../vim/dvs/DistributedVirtualSwitchManager.rst#exportEntity

.. _VmwareDistributedVirtualSwitch: ../../../vim/dvs/VmwareDistributedVirtualSwitch.rst


vim.dvs.EntityBackup.Config
===========================
  The `EntityBackupConfig`_ data object contains `VmwareDistributedVirtualSwitch`_ or `DistributedVirtualPortgroup`_ backup configuration data produced by the `DVSManagerExportEntity_Task`_ method. It also contains properties that support `DVSManagerImportEntity_Task`_ operations.A `DVSManagerExportEntity_Task`_ operation sets properties that identify the entity instance ( `entityType`_ , `key`_ , and `name`_ ) and inventory location ( `container`_ ). When you import a backup configuration, you can set thekey,name, andcontainerproperties in accordance with theimportTypespecified in the call to `DVSManagerImportEntity_Task`_ . See `EntityImportType`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    entityType (`str`_):

       Type of the exported entity ( `DVSManagerExportEntity_Task`_ ). See `EntityType`_ for valid values.
    configBlob (`base64`_):

       Opaque blob that contains the configuration of the entity.
    key (`str`_, optional):

       Unique identifier of the exported entity or the entity to be restored through an import operation.
        * If you are importing a virtual distributed switch and the import type is
        * `applyToEntitySpecified`_
        * , set the
        * key
        * to
        * `DistributedVirtualSwitch`_
        * .
        * `uuid`_
        * .
        * If you are importing a virtual distributed portgroup and the import type is
        * `applyToEntitySpecified`_
        * , set the
        * key
        * to
        * `DistributedVirtualPortgroup`_
        * .
        * `key`_
        * .The Server ignores the key value when the import operation creates a new entity.
    name (`str`_, optional):

       Name of the exported entity or the entity to be restored with the backup configuration. If you are importing an entity and the import type is `applyToEntitySpecified`_ , the Server will use this value to rename the existing entity.
    container (`vim.ManagedEntity`_, optional):

       Container for this entity. If `entityType`_ is "distributedVirtualSwitch", the container type is `Folder`_ . If `entityType`_ is "distributedVirtualPortgroup", the container type is `DistributedVirtualSwitch`_ .
    configVersion (`str`_, optional):

       Configuration version.
