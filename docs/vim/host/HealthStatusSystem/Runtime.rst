
vim.host.HealthStatusSystem.Runtime
===================================
  The system health runtime information
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    systemHealthInfo (`vim.host.SystemHealthInfo <vim/host/SystemHealthInfo.rst>`_, optional):

       Available system health information
    hardwareStatusInfo (`vim.host.HardwareStatusInfo <vim/host/HardwareStatusInfo.rst>`_, optional):

       Available hardware health information
