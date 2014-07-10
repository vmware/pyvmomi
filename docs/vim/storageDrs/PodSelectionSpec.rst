.. _vim.StoragePod: ../../vim/StoragePod.rst

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.storageDrs.PodSelectionSpec.VmPodConfig: ../../vim/storageDrs/PodSelectionSpec/VmPodConfig.rst


vim.storageDrs.PodSelectionSpec
===============================
  Specification for moving or copying a virtual machine to a different Storage Pod.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    initialVmConfig (`vim.storageDrs.PodSelectionSpec.VmPodConfig`_, optional):

       An optional list that allows specifying the storage pod location for each virtual disk and the VM configurations and overrides to be used during placement.
    storagePod (`vim.StoragePod`_, optional):

       The storage pod where the virtual machine should be located.
