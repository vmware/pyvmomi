.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.VffsVolume: ../../vim/host/VffsVolume.rst

.. _vim.host.DiskConfigurationResult: ../../vim/host/DiskConfigurationResult.rst


vim.host.VFlashResourceConfigurationResult
==========================================
  vFlash resource configuration result returns the newly-configured backend VFFS volume and operation result for each passed-in SSD device.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    devicePath ([`str`_], optional):

       The original array of device path which user had specified
    vffs (`vim.host.VffsVolume`_, optional):

       Newly configured VffsVolume
    diskConfigurationResult ([`vim.host.DiskConfigurationResult`_], optional):

       Array of device operation results.
