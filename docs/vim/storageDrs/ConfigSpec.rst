
vim.storageDrs.ConfigSpec
=========================
  The `StorageDrsConfigSpec <vim/storageDrs/ConfigSpec.rst>`_ data object provides a set of update specifications for storage DRS configuration. To support incremental changes, these properties are all optional.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    podConfigSpec (`vim.storageDrs.PodConfigSpec <vim/storageDrs/PodConfigSpec.rst>`_, optional):

       Changes to the configuration of the storage DRS service.
    vmConfigSpec ([`vim.storageDrs.VmConfigSpec <vim/storageDrs/VmConfigSpec.rst>`_], optional):

       Changes to the per-virtual-machine storage DRS settings.
