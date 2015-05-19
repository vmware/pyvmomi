.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.host.UnresolvedVmfsResolutionSpec
=====================================
  An unresolved VMFS volume is reported when one or more device partitions of volume are detected to have copies of extents of the volume. Such copies can be created via replication or snapshots, for example. This data object type describes how to resolve an unbound VMFS volume. The SCSI device path for each of the VMFS volume extent should be specified. For the current release, only head-extent needs to be specified. In future releases, we will allow user to specify explicitly all the extents which makes up a new Vmfs Volume.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    extentDevicePath ([`str`_]):

       List of device paths each specifying a VMFS extent.One extent must be specified. This property is represented as a list to enable future enhancements to the interface.
    uuidResolution (`str`_):

       When set to Resignature, new Uuid is assigned to the VMFS volume. When set to 'forceMount', existing uuid is assigned to the Vmfs volume and Vmfs volumes metadata doesn't change.See VmfsUuidResolution
