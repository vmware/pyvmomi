.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vFlashModule: ../../../vim/vm/device/VirtualDisk/VFlashCacheConfigInfo.rst#vFlashModule

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.VFlashManager.VFlashCacheConfigInfo.VFlashModuleConfigOption: ../../../vim/host/VFlashManager/VFlashCacheConfigInfo/VFlashModuleConfigOption.rst


vim.host.VFlashManager.VFlashCacheConfigInfo
============================================
  Data object describes host vFlash cache configuration information.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    vFlashModuleConfigOption (`vim.host.VFlashManager.VFlashCacheConfigInfo.VFlashModuleConfigOption`_, optional):

       Cache configuration options for the supported vFlash modules.
    defaultVFlashModule (`str`_, optional):

       Name of the default vFlash module for the read-write cache associated with the VMs of this host. This setting can be overridden by `vFlashModule`_ per VMDK.
    swapCacheReservationInGB (`long`_, optional):

       Amount of vFlash resource is allocated to the host swap cache. As long as set, reservation will be permanent and retain regardless of host power state. The host swap cache will be disabled if reservation is set to zero.
