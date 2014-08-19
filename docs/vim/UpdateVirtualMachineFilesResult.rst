
vim.UpdateVirtualMachineFilesResult
===================================
  UpdateVirtualMachineFilesResult is the result returned to the `UpdateVirtualMachineFiles_Task <vim/Datastore.rst#updateVirtualMachineFiles>`_ method.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    failedVmFile ([`vim.UpdateVirtualMachineFilesResult.FailedVmFileInfo <vim/UpdateVirtualMachineFilesResult/FailedVmFileInfo.rst>`_], optional):

       The list of virtual machines files the server has attempted to update but failed to update.
