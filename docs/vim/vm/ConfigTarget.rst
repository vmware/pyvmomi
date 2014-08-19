
vim.vm.ConfigTarget
===================
  The ConfigTarget class contains information about "physical" devices that can be used to back virtual devices.
:extends: vmodl.DynamicData_

Attributes:
    numCpus (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Number of logical CPUs that can be used to run virtual machines.
    numCpuCores (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Number of physical CPU cores that are available to run virtual machines.
    numNumaNodes (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Number of NUMA nodes.
    smcPresent (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Presence of System Management Controller, indicates the host is Apple hardware, and thus capable of running Mac OS guest as VM.
    datastore ([`vim.vm.DatastoreInfo <vim/vm/DatastoreInfo.rst>`_], optional):

       List of datastores available for virtual disks and associated storage.
    network ([`vim.vm.NetworkInfo <vim/vm/NetworkInfo.rst>`_], optional):

       List of networks available for virtual network adapters.
    opaqueNetwork ([`vim.vm.OpaqueNetworkInfo <vim/vm/OpaqueNetworkInfo.rst>`_], optional):

       List of opaque networks available for virtual network adapters.
    distributedVirtualPortgroup ([`vim.dvs.DistributedVirtualPortgroupInfo <vim/dvs/DistributedVirtualPortgroupInfo.rst>`_], optional):

       List of networks available from DistributedVirtualSwitch for virtual network adapters.
    distributedVirtualSwitch ([`vim.dvs.DistributedVirtualSwitchInfo <vim/dvs/DistributedVirtualSwitchInfo.rst>`_], optional):

       List of distributed virtual switch available for virtual network adapters.
    cdRom ([`vim.vm.CdromInfo <vim/vm/CdromInfo.rst>`_], optional):

       List of CD-ROM devices available for use by virtual CD-ROMs. Used for `VirtualCdromAtapiBackingInfo <vim/vm/device/VirtualCdrom/AtapiBackingInfo.rst>`_ .
    serial ([`vim.vm.SerialInfo <vim/vm/SerialInfo.rst>`_], optional):

       List of serial devices available to support virtualization. Used for `VirtualSerialPortDeviceBackingInfo <vim/vm/device/VirtualSerialPort/DeviceBackingInfo.rst>`_ .
    parallel ([`vim.vm.ParallelInfo <vim/vm/ParallelInfo.rst>`_], optional):

       List of parallel devices available to support virtualization. Used for `VirtualParallelPortDeviceBackingInfo <vim/vm/device/VirtualParallelPort/DeviceBackingInfo.rst>`_ .
    sound ([`vim.vm.SoundInfo <vim/vm/SoundInfo.rst>`_], optional):

       List of sound devices available to support virtualization. Used for `VirtualSoundCardDeviceBackingInfo <vim/vm/device/VirtualSoundCard/DeviceBackingInfo.rst>`_ .
    usb ([`vim.vm.UsbInfo <vim/vm/UsbInfo.rst>`_], optional):

       List of USB devices on the host that are available to support virtualization. Used for `VirtualUSBUSBBackingInfo <vim/vm/device/VirtualUSB/USBBackingInfo.rst>`_ .
    floppy ([`vim.vm.FloppyInfo <vim/vm/FloppyInfo.rst>`_], optional):

       List of floppy devices available for use by virtual floppies. Used for `VirtualFloppyDeviceBackingInfo <vim/vm/device/VirtualFloppy/DeviceBackingInfo.rst>`_ .
    legacyNetworkInfo ([`vim.vm.LegacyNetworkSwitchInfo <vim/vm/LegacyNetworkSwitchInfo.rst>`_], optional):

       Legacy switch names when using the LegacyNetworkBacking types.
    scsiPassthrough ([`vim.vm.ScsiPassthroughInfo <vim/vm/ScsiPassthroughInfo.rst>`_], optional):

       List of generic SCSI devices.
    scsiDisk ([`vim.vm.ScsiDiskDeviceInfo <vim/vm/ScsiDiskDeviceInfo.rst>`_], optional):

       List of physical SCSI disks that can be used as targets for raw disk mapping backings.
    ideDisk ([`vim.vm.IdeDiskDeviceInfo <vim/vm/IdeDiskDeviceInfo.rst>`_], optional):

       List of physical IDE disks that can be used as targets for raw disk backings.
    maxMemMBOptimalPerf (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Maximum recommended memory size, in MB, for creating a new virtual machine.
    resourcePool (`vim.ResourcePool.RuntimeInfo <vim/ResourcePool/RuntimeInfo.rst>`_, optional):

       Information about the current available resources on the current resource pool for a virtual machine. This field is only populated from an Environment browser obtained from a virtual machine.
    autoVmotion (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Information whether a virtual machine with this ConfigTarget can auto vmotion. This field is only populated from an Environment browser obtained from a virtual machine.
    pciPassthrough ([`vim.vm.PciPassthroughInfo <vim/vm/PciPassthroughInfo.rst>`_], optional):

       List of generic PCI devices.
    sriov ([`vim.vm.SriovInfo <vim/vm/SriovInfo.rst>`_], optional):

       List of SRIOV devices.
    vFlashModule ([`vim.vm.VFlashModuleInfo <vim/vm/VFlashModuleInfo.rst>`_], optional):

       List of vFlash modules.
