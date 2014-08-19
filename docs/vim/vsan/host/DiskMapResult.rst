
vim.vsan.host.DiskMapResult
===========================
  A DiskMapResult represents the result of an operation performed on the set of disks in a `VsanHostDiskMapping <vim/vsan/host/DiskMapping.rst>`_ .See `InitializeDisks_Task <vim/host/VsanSystem.rst#initializeDisks>`_ See `UpdateVsan_Task <vim/host/VsanSystem.rst#update>`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    mapping (`vim.vsan.host.DiskMapping <vim/vsan/host/DiskMapping.rst>`_):

       DiskMapping for this result.
    diskResult ([`vim.vsan.host.DiskResult <vim/vsan/host/DiskResult.rst>`_], optional):

       List of results for each disk in the mapping.
    error (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_, optional):

       Error information for this result.See `VsanDiskFault <vim/fault/VsanDiskFault.rst>`_ 
