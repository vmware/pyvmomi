
vim.host.DiagnosticPartition
============================
  This data object type contains information about an available or active diagnostic partition.
:extends: vmodl.DynamicData_

Attributes:
    storageType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates the storage type of the diagnostic partition.See `DiagnosticPartitionStorageType <vim/host/DiagnosticPartition/StorageType.rst>`_ 
    diagnosticType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates the type of the diagnostic partition.See `DiagnosticPartitionType <vim/host/DiagnosticPartition/DiagnosticType.rst>`_ 
    slots (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of slots in the diagnostic partition.
    id (`vim.host.ScsiDisk.Partition <vim/host/ScsiDisk/Partition.rst>`_):

       Diagnostic partition identification information.
