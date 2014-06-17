.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.BootDeviceSystem.BootDevice: ../../vim/host/BootDeviceSystem/BootDevice.rst


vim.host.BootDeviceInfo
=======================
  This data object represents the boot device information of the host.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    bootDevices (`vim.host.BootDeviceSystem.BootDevice`_, optional):

       The list of boot devices present on the host
    currentBootDeviceKey (`str`_, optional):

       The key of the current boot device that the host is configured to boot. This property is unset if the current boot device is disabled.
