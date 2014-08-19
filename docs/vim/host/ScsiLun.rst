
vim.host.ScsiLun
================
  The `ScsiLun <vim/host/ScsiLun.rst>`_ data object describes a SCSI logical unit. A SCSI logical unit is a host device that an ESX Server or virtual machine can use for I/O operations.An ESX Server creates SCSI logical unit objects to represent devices in the host configuration. (See the definition of `ScsiLunType <vim/host/ScsiLun/ScsiLunType.rst>`_ for a list of the supported device types.) The vSphere API uses one of two object types to represent a SCSI logical unit, depending on the device type.
   * Disks containing file system volumes or parts of volumes for hosts or raw disks for virtual machines. To represent disks, the ESX Server creates a
   * `HostScsiDisk <vim/host/ScsiDisk.rst>`_
   * object, which inherits properties from the
   * `ScsiLun <vim/host/ScsiLun.rst>`_
   * base class.
   * Other SCSI devices, for example SCSI passthrough devices for virtual machines. To represent one of these devices, the ESX Server creates a
   * `ScsiLun <vim/host/ScsiLun.rst>`_
   * object.When the Server creates a `HostScsiDisk <vim/host/ScsiDisk.rst>`_ or `ScsiLun <vim/host/ScsiLun.rst>`_ object, it specifies a valid device name and type:
   * `deviceName <vim/host/Device.rst#deviceName>`_
   * - A string representing the name of the device that is meaningful to the host. The following are some examples of device names.
   * 
   * /dev/cdrom
   * 
   * /vmkdev/vmhba0:0:1:0
   * 
   * PhysicalDrive0
   * 
   * `deviceType <vim/host/Device.rst#deviceType>`_
   * - A string describing the type of device. The following are some examples of device types.
   * 
   * scsi-cdrom
   * 
   * 
   * scsi-tape
   * 
   * 
   * scsi-disk
   * 
   * 
   * scsi-processor
   * 
   * 
   * scsi-unknown
   * 
:extends: vim.host.Device_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Linkable identifier
    uuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Universally unique identifier for the LUN used to identify ScsiLun across multiple servers.This identifier can be used to identify analogous objects in other views such as `HostMultipathInfoLogicalUnit <vim/host/MultipathInfo/LogicalUnit.rst>`_ and `HostScsiTopologyLun <vim/host/ScsiTopology/Lun.rst>`_ .See `HostMultipathInfoLogicalUnit <vim/host/MultipathInfo/LogicalUnit.rst>`_ See `HostScsiTopologyLun <vim/host/ScsiTopology/Lun.rst>`_ 
    descriptor ([`vim.host.ScsiLun.Descriptor <vim/host/ScsiLun/Descriptor.rst>`_], optional):

       List of descriptors that can be used to identify the LUN object. The uuid will also appear as a descriptor.The id field in the descriptor is a string that can be used to correlate the ScsiLun across multiple servers. A ScsiLun may have multiple descriptors. The choice and order of these descriptors may be different on different servers.Not all descriptors are suitable for correlation. Some descriptors are only sufficient to identify the ScsiLun within a single host. Each descriptor contains a quality property that indicates whether or not the descriptor is suitable for correlation.
    canonicalName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Canonical name of the SCSI logical unit.Disk partition or extent identifiers refer to this name when referring to a disk. Use this property to correlate a partition or extent to a specific SCSI disk.See `diskName <vim/host/ScsiDisk/Partition.rst#diskName>`_ 
    displayName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       User configurable display name of the SCSI logical unit. A default display name will be used if available. If the display name is not supported, it will be unset. The display name does not have to be unique but it is recommended that it be unique.
    lunType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The type of SCSI device. Must be one of the values of `ScsiLunType <vim/host/ScsiLun/ScsiLunType.rst>`_ .
    vendor (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The vendor of the SCSI device.
    model (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The model number of the SCSI device.
    revision (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The revision of the SCSI device.
    scsiLevel (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The SCSI level of the SCSI device.
    serialNumber (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The serial number of the SCSI device. For a device that is SCSI-3 compliant, this property is derived from page 80h of the Vital Product Data (VPD), as defined by the SCSI-3 Primary Commands (SPC-3) spec. Not all SCSI-3 compliant devices provide this information. For devices that are not SCSI-3 compliant, this property is not defined.
    durableName (`vim.host.ScsiLun.DurableName <vim/host/ScsiLun/DurableName.rst>`_, optional):

       The durable name of the SCSI device. For a SCSI-3 compliant device this property is derived from the payloads of pages 80h and 83h of the Vital Product Data (VPD) as defined by the T10 and SMI standards. For devices that do not provide this information, this property is not defined.
    alternateName ([`vim.host.ScsiLun.DurableName <vim/host/ScsiLun/DurableName.rst>`_], optional):

       Alternate durable names. Records all available durable names derived from page 80h of the Vital Product Data (VPD) and the Identification Vital Product Data (VPD) page 83h as defined by the SCSI-3 Primary Commands. For devices that are not SCSI-3 compliant this property is not defined.
    standardInquiry ([`int <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Standard Inquiry payload. For a SCSI-3 compliant device this property is derived from the standard inquiry data. For devices that are not SCSI-3 compliant this property is not defined.
    queueDepth (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The queue depth of SCSI device.
    operationalState ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       The operational states of the LUN. When more than one item is present in the array, the first state should be considered the primary state. For example, a LUN may be "ok" and "degraded" indicating I/O is still possible to the LUN, but it is operating in a degraded mode.See `ScsiLunState <vim/host/ScsiLun/State.rst>`_ 
    capabilities (`vim.host.ScsiLun.Capabilities <vim/host/ScsiLun/Capabilities.rst>`_, optional):

       Capabilities of SCSI device.
    vStorageSupport (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       vStorage hardware acceleration support status. This property represents storage acceleration provided by the SCSI logical unit. See `ScsiLunVStorageSupportStatus <vim/host/ScsiLun/VStorageSupportStatus.rst>`_ for valid values.If a storage device supports hardware acceleration, the ESX host can offload specific virtual machine management operations to the storage device. With hardware assistance, the host performs storage operations faster and consumes less CPU, memory, and storage fabric bandwidth.For vSphere 4.0 or earlier hosts, this value will be unset.
