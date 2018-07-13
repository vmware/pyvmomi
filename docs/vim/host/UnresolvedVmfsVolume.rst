.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _HostStorageSystem: ../../vim/host/StorageSystem.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.UnresolvedVmfsExtent: ../../vim/host/UnresolvedVmfsExtent.rst

.. _vim.host.UnresolvedVmfsVolume.ResolveStatus: ../../vim/host/UnresolvedVmfsVolume/ResolveStatus.rst


vim.host.UnresolvedVmfsVolume
=============================
  Information about detected unbound, unresolved VMFS volume. An unresolved VMFS volume is reported when one or more device partitions of volume are detected to have copies of extents of the volume. Such copies can be created via replication or snapshots.UnresolvedVmfsVolume are not mounted on the host where they are detected. User may choose to resignature the volume in which case a new Uuid is assigned to the volume and contents of the VMFS volume is kept intact.User may choose to keep the original Uuid and mount the VMFS volume as it is on the given host. In this case, user has chosen to mount the copy of the VMFS volume on that host with no change to the original Uuid. This may fail with VmfsVolumeAlreadyMounted exception if there is an existing VMFS volume with the same Uuid mounted somewhere in the same datacenter.Simple diagram representing the possible operations on UnresolvedVmfsVolumeresignature forceMount VmfsVolume<--------------- Unresolved ------------> VmfsVolume with forceMountedInfo Vmfs Volume forceMountedInfo not set will be setSee `HostStorageSystem`_
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    extent ([`vim.host.UnresolvedVmfsExtent`_]):

       List of detected copies of VMFS extents.
    vmfsLabel (`str`_):

       The detected VMFS label name
    vmfsUuid (`str`_):

       The detected VMFS UUID
    totalBlocks (`int`_):

       Total number of blocks in this volume.
    resolveStatus (`vim.host.UnresolvedVmfsVolume.ResolveStatus`_):

       Information related to how the volume might be resolved.
