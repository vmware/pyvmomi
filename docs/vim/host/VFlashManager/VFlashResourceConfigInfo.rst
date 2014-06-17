.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.VffsVolume: ../../../vim/host/VffsVolume.rst


vim.host.VFlashManager.VFlashResourceConfigInfo
===============================================
  vFlash resource configuraiton Information.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    vffs (`vim.host.VffsVolume`_, optional):

       The contained VFFS volume
    capacity (`long`_):

       Capacity of the vFlash resource. It is the capacity of the contained VFFS volume.
