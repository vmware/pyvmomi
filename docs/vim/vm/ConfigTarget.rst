.. _int: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.vm.UsbInfo: ../../vim/vm/UsbInfo.rst

.. _vim.vm.SoundInfo: ../../vim/vm/SoundInfo.rst

.. _vim.vm.CdromInfo: ../../vim/vm/CdromInfo.rst

.. _vim.vm.SriovInfo: ../../vim/vm/SriovInfo.rst

.. _vim.vm.FloppyInfo: ../../vim/vm/FloppyInfo.rst

.. _vim.vm.SerialInfo: ../../vim/vm/SerialInfo.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.vm.NetworkInfo: ../../vim/vm/NetworkInfo.rst

.. _vim.vm.ParallelInfo: ../../vim/vm/ParallelInfo.rst

.. _vim.vm.DatastoreInfo: ../../vim/vm/DatastoreInfo.rst

.. _vim.vm.VFlashModuleInfo: ../../vim/vm/VFlashModuleInfo.rst

.. _vim.vm.IdeDiskDeviceInfo: ../../vim/vm/IdeDiskDeviceInfo.rst

.. _vim.vm.OpaqueNetworkInfo: ../../vim/vm/OpaqueNetworkInfo.rst

.. _VirtualUSBUSBBackingInfo: ../../vim/vm/device/VirtualUSB/USBBackingInfo.rst

.. _vim.vm.ScsiDiskDeviceInfo: ../../vim/vm/ScsiDiskDeviceInfo.rst

.. _vim.vm.PciPassthroughInfo: ../../vim/vm/PciPassthroughInfo.rst

.. _vim.vm.ScsiPassthroughInfo: ../../vim/vm/ScsiPassthroughInfo.rst

.. _VirtualCdromAtapiBackingInfo: ../../vim/vm/device/VirtualCdrom/AtapiBackingInfo.rst

.. _vim.ResourcePool.RuntimeInfo: ../../vim/ResourcePool/RuntimeInfo.rst

.. _vim.vm.LegacyNetworkSwitchInfo: ../../vim/vm/LegacyNetworkSwitchInfo.rst

.. _VirtualFloppyDeviceBackingInfo: ../../vim/vm/device/VirtualFloppy/DeviceBackingInfo.rst

.. _VirtualSoundCardDeviceBackingInfo: ../../vim/vm/device/VirtualSoundCard/DeviceBackingInfo.rst

.. _VirtualSerialPortDeviceBackingInfo: ../../vim/vm/device/VirtualSerialPort/DeviceBackingInfo.rst

.. _vim.dvs.DistributedVirtualSwitchInfo: ../../vim/dvs/DistributedVirtualSwitchInfo.rst

.. _VirtualParallelPortDeviceBackingInfo: ../../vim/vm/device/VirtualParallelPort/DeviceBackingInfo.rst

.. _vim.dvs.DistributedVirtualPortgroupInfo: ../../vim/dvs/DistributedVirtualPortgroupInfo.rst


vim.vm.ConfigTarget
===================
  The ConfigTarget class contains information about "physical" devices that can be used to back virtual devices.
:extends: vmodl.DynamicData_

Attributes:
    numCpus (`int`_):

       Number of logical CPUs that can be used to run virtual machines.
    numCpuCores (`int`_):

       Number of physical CPU cores that are available to run virtual machines.
    numNumaNodes (`int`_):

       Number of NUMA nodes.
    smcPresent (`bool`_):

       Presence of System Management Controller, indicates the host is Apple hardware, and thus capable of running Mac OS guest as VM.
    datastore ([`vim.vm.DatastoreInfo`_], optional):

       List of datastores available for virtual disks and associated storage.
    network ([`vim.vm.NetworkInfo`_], optional):

       List of networks available for virtual network adapters.
    opaqueNetwork ([`vim.vm.OpaqueNetworkInfo`_], optional):

       List of opaque networks available for virtual network adapters.
    distributedVirtualPortgroup ([`vim.dvs.DistributedVirtualPortgroupInfo`_], optional):

       List of networks available from DistributedVirtualSwitch for virtual network adapters.
    distributedVirtualSwitch ([`vim.dvs.DistributedVirtualSwitchInfo`_], optional):

       List of distributed virtual switch available for virtual network adapters.
    cdRom ([`vim.vm.CdromInfo`_], optional):

       List of CD-ROM devices available for use by virtual CD-ROMs. Used for `VirtualCdromAtapiBackingInfo`_ .
    serial ([`vim.vm.SerialInfo`_], optional):

       List of serial devices available to support virtualization. Used for `VirtualSerialPortDeviceBackingInfo`_ .
    parallel ([`vim.vm.ParallelInfo`_], optional):

       List of parallel devices available to support virtualization. Used for `VirtualParallelPortDeviceBackingInfo`_ .
    sound ([`vim.vm.SoundInfo`_], optional):

       List of sound devices available to support virtualization. Used for `VirtualSoundCardDeviceBackingInfo`_ .
    usb ([`vim.vm.UsbInfo`_], optional):

       List of USB devices on the host that are available to support virtualization. Used for `VirtualUSBUSBBackingInfo`_ .
    floppy ([`vim.vm.FloppyInfo`_], optional):

       List of floppy devices available for use by virtual floppies. Used for `VirtualFloppyDeviceBackingInfo`_ .
    legacyNetworkInfo ([`vim.vm.LegacyNetworkSwitchInfo`_], optional):

       Legacy switch names when using the LegacyNetworkBacking types.
    scsiPassthrough ([`vim.vm.ScsiPassthroughInfo`_], optional):

       List of generic SCSI devices.
    scsiDisk ([`vim.vm.ScsiDiskDeviceInfo`_], optional):

       List of physical SCSI disks that can be used as targets for raw disk mapping backings.
    ideDisk ([`vim.vm.IdeDiskDeviceInfo`_], optional):

       List of physical IDE disks that can be used as targets for raw disk backings.
    maxMemMBOptimalPerf (`int`_):

       Maximum recommended memory size, in MB, for creating a new virtual machine.
    resourcePool (`vim.ResourcePool.RuntimeInfo`_, optional):

       Information about the current available resources on the current resource pool for a virtual machine. This field is only populated from an Environment browser obtained from a virtual machine.
    autoVmotion (`bool`_, optional):

       Information whether a virtual machine with this ConfigTarget can auto vmotion. This field is only populated from an Environment browser obtained from a virtual machine.
    pciPassthrough ([`vim.vm.PciPassthroughInfo`_], optional):

       List of generic PCI devices.
    sriov ([`vim.vm.SriovInfo`_], optional):

       List of SRIOV devices.
    vFlashModule ([`vim.vm.VFlashModuleInfo`_], optional):

       List of vFlash modules.
