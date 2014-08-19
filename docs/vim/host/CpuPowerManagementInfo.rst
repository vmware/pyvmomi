
vim.host.CpuPowerManagementInfo
===============================
  The CpuPowerManagementInfo data object type describes supported power management and current policy.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    currentPolicy (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Information about current CPU power management policy.
    hardwareSupport (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Information about supported CPU power management.
