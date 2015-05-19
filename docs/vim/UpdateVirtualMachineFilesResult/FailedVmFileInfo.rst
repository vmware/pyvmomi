.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst


vim.UpdateVirtualMachineFilesResult.FailedVmFileInfo
====================================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    vmFile (`str`_):

       The file path
    fault (`vmodl.LocalizedMethodFault`_):

       The reason why the update failed.
