.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.vm.MetadataManager.VmMetadata: ../../../vim/vm/MetadataManager/VmMetadata.rst


vim.vm.MetadataManager.VmMetadataInput
======================================
  VmMetadataInput specifies the operation and metadata for a specific VM.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    operation (`str`_):

       The input operation type. The values come from VmMetadataOp
    vmMetadata (`vim.vm.MetadataManager.VmMetadata`_):

       the VM and optional metadata
