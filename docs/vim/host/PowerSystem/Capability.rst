.. _vSphere API 4.1: ../../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.PowerSystem.PowerPolicy: ../../../vim/host/PowerSystem/PowerPolicy.rst


vim.host.PowerSystem.Capability
===============================
  Power System Capability data object. Exposes policies available in power management system.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    availablePolicy (`vim.host.PowerSystem.PowerPolicy`_):

       List of available host power policies.
