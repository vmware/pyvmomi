.. _VsanDiskFault: ../../../vim/fault/VsanDiskFault.rst

.. _UpdateVsan_Task: ../../../vim/host/VsanSystem.rst#update

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _VsanHostDiskMapping: ../../../vim/vsan/host/DiskMapping.rst

.. _InitializeDisks_Task: ../../../vim/host/VsanSystem.rst#initializeDisks

.. _vim.vsan.host.DiskResult: ../../../vim/vsan/host/DiskResult.rst

.. _vim.vsan.host.DiskMapping: ../../../vim/vsan/host/DiskMapping.rst

.. _vmodl.LocalizedMethodFault: ../../../vmodl/LocalizedMethodFault.rst


vim.vsan.host.DiskMapResult
===========================
  A DiskMapResult represents the result of an operation performed on the set of disks in a `VsanHostDiskMapping`_ .See `InitializeDisks_Task`_ See `UpdateVsan_Task`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    mapping (`vim.vsan.host.DiskMapping`_):

       DiskMapping for this result.
    diskResult (`vim.vsan.host.DiskResult`_, optional):

       List of results for each disk in the mapping.
    error (`vmodl.LocalizedMethodFault`_, optional):

       Error information for this result.See `VsanDiskFault`_ 
