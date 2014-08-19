
vim.vsan.host.DiskResult
========================
  A DiskResult represents the result of VSAN configuration operation on a ScsiDisk, and its current eligibility state for use by the VSAN service.See `QueryDisksForVsan <vim/host/VsanSystem.rst#queryDisksForVsan>`_ See `UpdateVsan_Task <vim/host/VsanSystem.rst#update>`_ See `VsanHostDiskResultState <vim/vsan/host/DiskResult/State.rst>`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    disk (`vim.host.ScsiDisk <vim/host/ScsiDisk.rst>`_):

       Disk for this result.
    state (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       State of the disk for this result.See `VsanHostDiskResultState <vim/vsan/host/DiskResult/State.rst>`_ 
    vsanUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       VSAN disk UUID in case this disk is a VSAN disk.
    error (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_, optional):

       Error information for this result: may be populated with additional information about the disk at hand, regardless of the disk's state.See `VsanDiskFault <vim/fault/VsanDiskFault.rst>`_ See `state <vim/vsan/host/DiskResult.rst#state>`_ 
