.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.AutoStartManager.AutoPowerInfo: ../../../vim/host/AutoStartManager/AutoPowerInfo.rst

.. _vim.host.AutoStartManager.SystemDefaults: ../../../vim/host/AutoStartManager/SystemDefaults.rst


vim.host.AutoStartManager.Config
================================
  Contains the entire auto-start/auto-stop configuration.
:extends: vmodl.DynamicData_

Attributes:
    defaults (`vim.host.AutoStartManager.SystemDefaults`_, optional):

       System defaults for auto-start/auto-stop.
    powerInfo (`vim.host.AutoStartManager.AutoPowerInfo`_, optional):

       Lists the auto-start/auto-stop configuration. If a virtual machine is not mentioned in this array, it does not participate in auto-start/auto-stop operations.
