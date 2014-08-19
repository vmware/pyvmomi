
vim.host.VFlashManager.VFlashCacheConfigSpec
============================================
  Specification to configure vFlash cache on the host.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    defaultVFlashModule (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the default vFlash module for the read-write caches associated with the VMs of this host. This setting can be overridden by `vFlashModule <vim/vm/device/VirtualDisk/VFlashCacheConfigInfo.rst#vFlashModule>`_ per VMDK.
    swapCacheReservationInGB (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Amount of vFlash resource is allocated to the host swap cache. As long as set, reservation will be permanent and retain regardless of host power state. The host swap cache will be disabled if the reservation is set to zero.
