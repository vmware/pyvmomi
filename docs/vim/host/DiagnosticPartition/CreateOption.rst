.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.host.ScsiDisk: ../../../vim/host/ScsiDisk.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _DiagnosticPartitionType: ../../../vim/host/DiagnosticPartition/DiagnosticType.rst

.. _DiagnosticPartitionStorageType: ../../../vim/host/DiagnosticPartition/StorageType.rst


vim.host.DiagnosticPartition.CreateOption
=========================================
  This data object describes a disk that can be used to create a diagnostic partition.
:extends: vmodl.DynamicData_

Attributes:
    storageType (`str`_):

       Indicates the storage type of diagnostic partition to be created.See `DiagnosticPartitionStorageType`_ 
    diagnosticType (`str`_):

       Indicates the type of the diagnostic partition to be created.See `DiagnosticPartitionType`_ 
    disk (`vim.host.ScsiDisk`_):

       The disk which has sufficient free space to contain a diagnostic partition.
