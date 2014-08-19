
vim.host.DiagnosticPartition.CreateOption
=========================================
  This data object describes a disk that can be used to create a diagnostic partition.
:extends: vmodl.DynamicData_

Attributes:
    storageType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates the storage type of diagnostic partition to be created.See `DiagnosticPartitionStorageType <vim/host/DiagnosticPartition/StorageType.rst>`_ 
    diagnosticType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates the type of the diagnostic partition to be created.See `DiagnosticPartitionType <vim/host/DiagnosticPartition/DiagnosticType.rst>`_ 
    disk (`vim.host.ScsiDisk <vim/host/ScsiDisk.rst>`_):

       The disk which has sufficient free space to contain a diagnostic partition.
