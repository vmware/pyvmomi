.. _HostMultipathInfo: ../../vim/host/MultipathInfo.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _HostStorageDeviceInfo: ../../vim/host/StorageDeviceInfo.rst

.. _HostMultipathStateInfo: ../../vim/host/MultipathStateInfo.rst

.. _vim.host.MultipathInfo.LogicalUnit: ../../vim/host/MultipathInfo/LogicalUnit.rst


vim.host.MultipathInfo
======================
  The `HostMultipathInfo`_ data object describes the multipathing policy configuration to determine the storage failover policies for a SCSI logical unit. The multipathing policy configuration operates on SCSI logical units and the paths to the logical units.Multipath policy configuration is only possible on storage devices provided by the native multipathing plug-store plugin. Storage devices using the native multipathing storage plugin will have an entry in this data object. Storage devices provided by a different storage plugin will not appear in the inventory represented by this data object.Legacy note: In hosts where `HostMultipathStateInfo`_ is not defined or does not exist on the `HostStorageDeviceInfo`_ object, only native multipathing exists. That means for these hosts, the MultipathInfo object contains the complete set of LUNs and paths on the LUNs available on the host.
:extends: vmodl.DynamicData_

Attributes:
    lun ([`vim.host.MultipathInfo.LogicalUnit`_], optional):

       List of logical units that can be configured for multipathing.
