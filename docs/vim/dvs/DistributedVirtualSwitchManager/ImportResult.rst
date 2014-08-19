
vim.dvs.DistributedVirtualSwitchManager.ImportResult
====================================================
  The `DistributedVirtualSwitchManagerImportResult <vim/dvs/DistributedVirtualSwitchManager/ImportResult.rst>`_ data object represents the results of a `DVSManagerImportEntity_Task <vim/dvs/DistributedVirtualSwitchManager.rst#importEntity>`_ operation. It contains lists of the switches and portgroups that were created. It also contains a list of faults that occurred during the operation.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    distributedVirtualSwitch ([`vim.DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_], optional):

       List of distributed virtual switches.
    distributedVirtualPortgroup ([`vim.dvs.DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_], optional):

       List of distributed virtual portgroups.
    importFault ([`vim.fault.ImportOperationBulkFault.FaultOnImport <vim/fault/ImportOperationBulkFault/FaultOnImport.rst>`_], optional):

       Faults that occurred on the entities during the import operation.
