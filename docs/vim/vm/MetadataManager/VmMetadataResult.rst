.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vmodl.LocalizedMethodFault: ../../../vmodl/LocalizedMethodFault.rst

.. _vim.vm.MetadataManager.VmMetadata: ../../../vim/vm/MetadataManager/VmMetadata.rst


vim.vm.MetadataManager.VmMetadataResult
=======================================
  A list of VmMetadataResults are returned for successful and non-successful results of an update or retrieve operation.See MetadataManager#updateMetadata(VmMetadataOwner,See MetadataManager#retrieveMetadata(VmMetadataOwner,See MetadataManager#retrieveAllMetadata(VmMetadataOwner,See MetadataManager#clearMetadata(VmMetadataOwner,
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    vmMetadata (`vim.vm.MetadataManager.VmMetadata`_):

       The VM-specific metadata
    error (`vmodl.LocalizedMethodFault`_, optional):

       MethodFault set for errors in getting or setting the VmMetadata.
