.. _str: https://docs.python.org/2/library/stdtypes.html

.. _state: ../../../vim/vsan/host/DiskResult.rst#state

.. _VsanDiskFault: ../../../vim/fault/VsanDiskFault.rst

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _UpdateVsan_Task: ../../../vim/host/VsanSystem.rst#update

.. _QueryDisksForVsan: ../../../vim/host/VsanSystem.rst#queryDisksForVsan

.. _vim.host.ScsiDisk: ../../../vim/host/ScsiDisk.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _VsanHostDiskResultState: ../../../vim/vsan/host/DiskResult/State.rst

.. _vmodl.LocalizedMethodFault: ../../../vmodl/LocalizedMethodFault.rst


vim.vsan.host.DiskResult
========================
  A DiskResult represents the result of VSAN configuration operation on a ScsiDisk, and its current eligibility state for use by the VSAN service.See `QueryDisksForVsan`_ See `UpdateVsan_Task`_ See `VsanHostDiskResultState`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    disk (`vim.host.ScsiDisk`_):

       Disk for this result.
    state (`str`_):

       State of the disk for this result.See `VsanHostDiskResultState`_ 
    vsanUuid (`str`_, optional):

       VSAN disk UUID in case this disk is a VSAN disk.
    error (`vmodl.LocalizedMethodFault`_, optional):

       Error information for this result: may be populated with additional information about the disk at hand, regardless of the disk's state.See `VsanDiskFault`_ See `state`_ 
