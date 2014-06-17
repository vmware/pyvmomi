.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.VFlashManager.VFlashResourceRunTimeInfo
================================================
  Data object provides vFlash resource runtime usage.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    usage (`long`_):

       Overall usage of vFlash resource, in bytes.
    capacity (`long`_):

       Overall capacity of vFlash resource, in bytes.
    accessible (`bool`_):

       True if all the included the VFFS volumes are accessible. False if one or multiple included VFFS volumes are inaccessible.
    capacityForVmCache (`long`_):

       vFlash resource capacity can be allocated for VM caches
    freeForVmCache (`long`_):

       Free vFlash resource can be allocated for VM caches
