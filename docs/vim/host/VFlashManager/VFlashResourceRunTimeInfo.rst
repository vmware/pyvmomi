
vim.host.VFlashManager.VFlashResourceRunTimeInfo
================================================
  Data object provides vFlash resource runtime usage.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    usage (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Overall usage of vFlash resource, in bytes.
    capacity (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Overall capacity of vFlash resource, in bytes.
    accessible (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       True if all the included the VFFS volumes are accessible. False if one or multiple included VFFS volumes are inaccessible.
    capacityForVmCache (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       vFlash resource capacity can be allocated for VM caches
    freeForVmCache (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Free vFlash resource can be allocated for VM caches
