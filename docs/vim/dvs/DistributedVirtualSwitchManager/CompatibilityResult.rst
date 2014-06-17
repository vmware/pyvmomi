.. _vim.HostSystem: ../../../vim/HostSystem.rst

.. _vSphere API 4.1: ../../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vmodl.LocalizedMethodFault: ../../../vmodl/LocalizedMethodFault.rst


vim.dvs.DistributedVirtualSwitchManager.CompatibilityResult
===========================================================
  This is the return type for the checkCompatibility method. This object has a host property and optionally a fault which would be populated only if that host is not compatible with a given dvsProductSpec. If the host is compatible then the error property would be unset.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    host (`vim.HostSystem`_):

       The host for which results are annotated. The whole object will be filtered out if the caller did not have view permissions on the host entity.
    error (`vmodl.LocalizedMethodFault`_, optional):

       This property contains the faults that makes the host not compatible with a given DvsProductSpec. For example, a host might not be compatible because it's an older version of ESX that doesn't support DVS.
