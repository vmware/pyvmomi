.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _StorageDrsConfigSpec: ../../vim/storageDrs/ConfigSpec.rst

.. _vim.storageDrs.VmConfigSpec: ../../vim/storageDrs/VmConfigSpec.rst

.. _vim.storageDrs.PodConfigSpec: ../../vim/storageDrs/PodConfigSpec.rst


vim.storageDrs.ConfigSpec
=========================
  The `StorageDrsConfigSpec`_ data object provides a set of update specifications for storage DRS configuration. To support incremental changes, these properties are all optional.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    podConfigSpec (`vim.storageDrs.PodConfigSpec`_, optional):

       Changes to the configuration of the storage DRS service.
    vmConfigSpec ([`vim.storageDrs.VmConfigSpec`_], optional):

       Changes to the per-virtual-machine storage DRS settings.
