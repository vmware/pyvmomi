
vim.host.VFlashManager.VFlashResourceConfigInfo
===============================================
  vFlash resource configuraiton Information.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    vffs (`vim.host.VffsVolume <vim/host/VffsVolume.rst>`_, optional):

       The contained VFFS volume
    capacity (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Capacity of the vFlash resource. It is the capacity of the contained VFFS volume.
