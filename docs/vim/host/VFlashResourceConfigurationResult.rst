
vim.host.VFlashResourceConfigurationResult
==========================================
  vFlash resource configuration result returns the newly-configured backend VFFS volume and operation result for each passed-in SSD device.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    devicePath ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The original array of device path which user had specified
    vffs (`vim.host.VffsVolume <vim/host/VffsVolume.rst>`_, optional):

       Newly configured VffsVolume
    diskConfigurationResult ([`vim.host.DiskConfigurationResult <vim/host/DiskConfigurationResult.rst>`_], optional):

       Array of device operation results.
