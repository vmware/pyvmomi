
vim.dvs.EntityBackup.Config
===========================
  The `EntityBackupConfig <vim/dvs/EntityBackup/Config.rst>`_ data object contains `VmwareDistributedVirtualSwitch <vim/dvs/VmwareDistributedVirtualSwitch.rst>`_ or `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_ backup configuration data produced by the `DVSManagerExportEntity_Task <vim/dvs/DistributedVirtualSwitchManager.rst#exportEntity>`_ method. It also contains properties that support `DVSManagerImportEntity_Task <vim/dvs/DistributedVirtualSwitchManager.rst#importEntity>`_ operations.A `DVSManagerExportEntity_Task <vim/dvs/DistributedVirtualSwitchManager.rst#exportEntity>`_ operation sets properties that identify the entity instance ( `entityType <vim/dvs/EntityBackup/Config.rst#entityType>`_ , `key <vim/dvs/EntityBackup/Config.rst#key>`_ , and `name <vim/dvs/EntityBackup/Config.rst#name>`_ ) and inventory location ( `container <vim/dvs/EntityBackup/Config.rst#container>`_ ). When you import a backup configuration, you can set thekey,name, andcontainerproperties in accordance with theimportTypespecified in the call to `DVSManagerImportEntity_Task <vim/dvs/DistributedVirtualSwitchManager.rst#importEntity>`_ . See `EntityImportType <vim/dvs/EntityBackup/ImportType.rst>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    entityType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Type of the exported entity ( `DVSManagerExportEntity_Task <vim/dvs/DistributedVirtualSwitchManager.rst#exportEntity>`_ ). See `EntityType <vim/dvs/EntityBackup/EntityType.rst>`_ for valid values.
    configBlob (`base64 <https://docs.python.org/2/library/stdtypes.html>`_):

       Opaque blob that contains the configuration of the entity.
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Unique identifier of the exported entity or the entity to be restored through an import operation.
        * If you are importing a virtual distributed switch and the import type is
        * `applyToEntitySpecified <vim/dvs/EntityBackup/ImportType.rst#applyToEntitySpecified>`_
        * , set the
        * key
        * to
        * `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_
        * .
        * `uuid <vim/DistributedVirtualSwitch.rst#uuid>`_
        * .
        * If you are importing a virtual distributed portgroup and the import type is
        * `applyToEntitySpecified <vim/dvs/EntityBackup/ImportType.rst#applyToEntitySpecified>`_
        * , set the
        * key
        * to
        * `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_
        * .
        * `key <vim/dvs/DistributedVirtualPortgroup.rst#key>`_
        * .The Server ignores the key value when the import operation creates a new entity.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Name of the exported entity or the entity to be restored with the backup configuration. If you are importing an entity and the import type is `applyToEntitySpecified <vim/dvs/EntityBackup/ImportType.rst#applyToEntitySpecified>`_ , the Server will use this value to rename the existing entity.
    container (`vim.ManagedEntity <vim/ManagedEntity.rst>`_, optional):

       Container for this entity. If `entityType <vim/dvs/EntityBackup/Config.rst#entityType>`_ is "distributedVirtualSwitch", the container type is `Folder <vim/Folder.rst>`_ . If `entityType <vim/dvs/EntityBackup/Config.rst#entityType>`_ is "distributedVirtualPortgroup", the container type is `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ .
    configVersion (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Configuration version.
