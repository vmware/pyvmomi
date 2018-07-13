.. _vim.HostSystem: ../../../vim/HostSystem.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vmodl.LocalizedMethodFault: ../../../vmodl/LocalizedMethodFault.rst


vim.fault.DvsOperationBulkFault.FaultOnHost
===========================================
  The fault occurred on the host during an operation.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    host (`vim.HostSystem`_):

    fault (`vmodl.LocalizedMethodFault`_):

       The fault that occurred.
