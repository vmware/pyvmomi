.. _vSphere API 5.1: ../../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _DVSManagerImportEntity_Task: ../../../vim/dvs/DistributedVirtualSwitchManager.rst#importEntity

.. _vim.DistributedVirtualSwitch: ../../../vim/DistributedVirtualSwitch.rst

.. _vim.dvs.DistributedVirtualPortgroup: ../../../vim/dvs/DistributedVirtualPortgroup.rst

.. _DistributedVirtualSwitchManagerImportResult: ../../../vim/dvs/DistributedVirtualSwitchManager/ImportResult.rst

.. _vim.fault.ImportOperationBulkFault.FaultOnImport: ../../../vim/fault/ImportOperationBulkFault/FaultOnImport.rst


vim.dvs.DistributedVirtualSwitchManager.ImportResult
====================================================
  The `DistributedVirtualSwitchManagerImportResult`_ data object represents the results of a `DVSManagerImportEntity_Task`_ operation. It contains lists of the switches and portgroups that were created. It also contains a list of faults that occurred during the operation.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    distributedVirtualSwitch (`vim.DistributedVirtualSwitch`_, optional):

       List of distributed virtual switches.
    distributedVirtualPortgroup (`vim.dvs.DistributedVirtualPortgroup`_, optional):

       List of distributed virtual portgroups.
    importFault (`vim.fault.ImportOperationBulkFault.FaultOnImport`_, optional):

       Faults that occurred on the entities during the import operation.
