
vim.host.LowLevelProvisioningManager.VmMigrationStatus
======================================================
  The status of a virtual machine migration operation.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    migrationId (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Unique identifier for this operation, currently it's unique within one virtual center instance.
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Manner in which the migration process is performed. The set of possible values is described in `HostVMotionManagerVMotionType <vim/host/VMotionManager/VMotionType.rst>`_ .
    source (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether the virtual machine is the source of the migration. For disk only migration, the value is always true.
    consideredSuccessful (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether the operation is considered successful. A migration operation is considered successful if its switch over phase has completed successfully.More specifically, for an in-progress migration, it is considered successful if it has had a sucessful switch over, otherwise it is considered unsuccessful. Likewise, the status of a completed migration operation is also based on the switch over completion status.The difference between a completed vs. in-progress migration with the same consideredSuccessful property is that in the former case the server is able to complete the clean up process thus leaves nothing for the recovery process to clean up.
