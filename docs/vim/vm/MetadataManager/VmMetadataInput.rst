
vim.vm.MetadataManager.VmMetadataInput
======================================
  VmMetadataInput specifies the operation and metadata for a specific VM.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    operation (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The input operation type. The values come from VmMetadataOp
    vmMetadata (`vim.vm.MetadataManager.VmMetadata <vim/vm/MetadataManager/VmMetadata.rst>`_):

       the VM and optional metadata
