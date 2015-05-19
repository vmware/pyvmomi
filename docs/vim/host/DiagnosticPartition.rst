.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _DiagnosticPartitionType: ../../vim/host/DiagnosticPartition/DiagnosticType.rst

.. _vim.host.ScsiDisk.Partition: ../../vim/host/ScsiDisk/Partition.rst

.. _DiagnosticPartitionStorageType: ../../vim/host/DiagnosticPartition/StorageType.rst


vim.host.DiagnosticPartition
============================
  This data object type contains information about an available or active diagnostic partition.
:extends: vmodl.DynamicData_

Attributes:
    storageType (`str`_):

       Indicates the storage type of the diagnostic partition.See `DiagnosticPartitionStorageType`_ 
    diagnosticType (`str`_):

       Indicates the type of the diagnostic partition.See `DiagnosticPartitionType`_ 
    slots (`int`_):

       The number of slots in the diagnostic partition.
    id (`vim.host.ScsiDisk.Partition`_):

       Diagnostic partition identification information.
