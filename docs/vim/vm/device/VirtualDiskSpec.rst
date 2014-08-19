
vim.vm.device.VirtualDiskSpec
=============================
  The VirtualDiskSpec data object type encapsulates change specifications for an individual virtual disk device. The virtual disk being added or modified must be fully specified.
:extends: vim.vm.device.VirtualDeviceSpec_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    migrateCache (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Manner in which to transfer the cache associated with the virtual disk to the target host. If left unset then migrate is used when the backing vFlash module version is compatible with the specific vFalsh module on the target host; otherwise flush is used for write back cache, or a no-op for write through cache. This setting can avoid VM migration failure due to incompatibility. If true then migrate is always used. VM migration may fail if the backing vFlash module version is incompatible with the module on the target host. If false then flush is used for write back cache. It is a no-op for write through cache. This setting can avoid VM migration failure due to incompatibility, but cache files have to be rebuilt on the target host. Default is unset.See `HostVFlashManagerVFlashCacheConfigInfoVFlashModuleConfigOption <vim/host/VFlashManager/VFlashCacheConfigInfo/VFlashModuleConfigOption.rst>`_ 
