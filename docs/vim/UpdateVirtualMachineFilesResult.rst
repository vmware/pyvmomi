.. _vSphere API 4.1: ../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../vmodl/DynamicData.rst

.. _UpdateVirtualMachineFiles_Task: ../vim/Datastore.rst#updateVirtualMachineFiles

.. _vim.UpdateVirtualMachineFilesResult.FailedVmFileInfo: ../vim/UpdateVirtualMachineFilesResult/FailedVmFileInfo.rst


vim.UpdateVirtualMachineFilesResult
===================================
  UpdateVirtualMachineFilesResult is the result returned to the `UpdateVirtualMachineFiles_Task`_ method.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    failedVmFile (`vim.UpdateVirtualMachineFilesResult.FailedVmFileInfo`_, optional):

       The list of virtual machines files the server has attempted to update but failed to update.
