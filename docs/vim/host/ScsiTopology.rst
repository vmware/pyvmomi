
vim.host.ScsiTopology
=====================
  This data object type describes the SCSI topology information. The data objects in this data object type model the SCSI storage objects from a topological point of view. The SCSI topological view organizes objects by SCSI interface, which contain targets, which in turn contain logical units.SCSI Topology information is not guaranteed to exhaustively enumerate all storage devices on the system. It only shows storage devices that are actually enumerable form a host bus adapter. This means that only storage devices that are composed from one or more paths, which are in turn provided by a host bus adapter, will appear in this inventory.Storage devices provided by the native multipathing plugin (NMP) will always be represented in this inventory since NMP uses a simple policy to create devices out of the paths it claims.Examples of storage devices that will not appear in this inventory are logical devices that are not formed from directly claiming paths. Specific examples of devices that will not appear in this inventory include a device backed by a ramdisk or formed from a software RAID plugin.Legacy note: In hosts where `HostPlugStoreTopology <vim/host/PlugStoreTopology.rst>`_ is not defined or does not exist on the `HostStorageDeviceInfo <vim/host/StorageDeviceInfo.rst>`_ object, only native multipathing exists. That means for these hosts, the ScsiTopology object contains the complete set of LUNs and targets available on the host.
:extends: vmodl.DynamicData_

Attributes:
    adapter ([`vim.host.ScsiTopology.Interface <vim/host/ScsiTopology/Interface.rst>`_], optional):

       The list of SCSI interfaces.
