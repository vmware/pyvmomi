
vim.vm.ScsiDiskDeviceInfo
=========================
  The ScsiDiskDeviceInfo class contains detailed information about a specific scsi disk hardware device. These devices are for the vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo.
:extends: vim.vm.DiskDeviceInfo_

Attributes:
    disk (`vim.host.ScsiDisk <vim/host/ScsiDisk.rst>`_, optional):

       Detailed information about the disk.
    transportHint (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Transport identifier hint used to identify the device. To definitively correlate this device with a host physical disk, use the disk property. This identifier is intended as a hint to end users to identify the disk device.
    lunNumber (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       LUN number hint used to identify the SCSI device. To definitively correlate this device with a host physical disk, use the disk property. This identifier is intended as a hint to end users to identify the disk device.
