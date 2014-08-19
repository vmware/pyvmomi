
vim.host.HardwareStatusInfo
===========================
  Data object representing the status of the hardware components of the host.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    memoryStatusInfo ([`vim.host.HardwareStatusInfo.HardwareElementInfo <vim/host/HardwareStatusInfo/HardwareElementInfo.rst>`_], optional):

       Status of the physical memory
    cpuStatusInfo ([`vim.host.HardwareStatusInfo.HardwareElementInfo <vim/host/HardwareStatusInfo/HardwareElementInfo.rst>`_], optional):

       Status of the CPU packages
    storageStatusInfo ([`vim.host.HardwareStatusInfo.StorageStatusInfo <vim/host/HardwareStatusInfo/StorageStatusInfo.rst>`_], optional):

       Status of the physical storage system
