.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _DiagnosticPartitionType: ../../../vim/host/DiagnosticPartition/DiagnosticType.rst

.. _vim.host.ScsiDisk.Partition: ../../../vim/host/ScsiDisk/Partition.rst

.. _DiagnosticPartitionStorageType: ../../../vim/host/DiagnosticPartition/StorageType.rst

.. _vim.host.DiskPartitionInfo.Specification: ../../../vim/host/DiskPartitionInfo/Specification.rst


vim.host.DiagnosticPartition.CreateSpec
=======================================
  The diagnostic create specification is used by the system to create a new diagnostic partition on a SCSI disk.
:extends: vmodl.DynamicData_

Attributes:
    storageType (`str`_):

       Indicates the storage type where the diagnostic partition will be created.See `DiagnosticPartitionStorageType`_ 
    diagnosticType (`str`_):

       Indicates the type of the diagnostic partition to be created.See `DiagnosticPartitionType`_ 
    id (`vim.host.ScsiDisk.Partition`_):

       Diagnostic partition identification information.
    partition (`vim.host.DiskPartitionInfo.Specification`_):

       Partitioning specification.
    active (`bool`_, optional):

       Indicates if the created diagnostic partition should be made the active diagnostic partition. If not supplied, the system will decide whether or not the created specification is active.
