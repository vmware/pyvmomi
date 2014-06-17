.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vFlashModule: ../../../vim/vm/device/VirtualDisk/VFlashCacheConfigInfo.rst#vFlashModule

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.VFlashManager.VFlashCacheConfigSpec
============================================
  Specification to configure vFlash cache on the host.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    defaultVFlashModule (`str`_):

       Name of the default vFlash module for the read-write caches associated with the VMs of this host. This setting can be overridden by `vFlashModule`_ per VMDK.
    swapCacheReservationInGB (`long`_):

       Amount of vFlash resource is allocated to the host swap cache. As long as set, reservation will be permanent and retain regardless of host power state. The host swap cache will be disabled if the reservation is set to zero.
