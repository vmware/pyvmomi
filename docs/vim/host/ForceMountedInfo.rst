
vim.host.ForceMountedInfo
=========================
  When the system detects a copy of a VmfsVolume, it will not be auto-mounted on the host and it will be detected as 'UnresolvedVmfsVolume'. If user decides to keep the original Uuid and mount it on the host, it will have 'forceMounted' flag and 'forceMountedInfo' set. 'ForceMountedInfo' provides additional information specific to user-mounted VmfsVolume.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    persist (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates if the vmfsExtent information persistent across host reboots.
    mounted (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates if the volume is currently mounted on the host
