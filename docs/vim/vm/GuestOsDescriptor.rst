.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.CpuIdInfo: ../../vim/host/CpuIdInfo.rst

.. _vim.option.IntOption: ../../vim/option/IntOption.rst

.. _GuestOsDescriptorSupportLevel: ../../vim/vm/GuestOsDescriptor/SupportLevel.rst

.. _GuestOsDescriptorFirmwareType: ../../vim/vm/GuestOsDescriptor/FirmwareType.rst


vim.vm.GuestOsDescriptor
========================
  This data object type contains information to describe a particular guest operating system.
:extends: vmodl.DynamicData_

Attributes:
    id (`str`_):

       Identifier (short name) for the guest operating system.
    family (`str`_):

       Family to which this guest operating system belongs.
    fullName (`str`_):

       Full name of the guest operating system. For example, if the value of "id" is "win2000Pro", then the value of "fullName" is "Windows 2000 Professional".
    supportedMaxCPUs (`int`_):

       Maximum number of processors supported for this guest.
    numSupportedPhysicalSockets (`int`_):

       Maximum number of sockets supported for this guest.
    numSupportedCoresPerSocket (`int`_):

       Maximum number of cores per socket for this guest.
    supportedMinMemMB (`int`_):

       Minimum memory requirements supported for this guest, in MB.
    supportedMaxMemMB (`int`_):

       Maximum memory requirements supported for this guest, in MB.
    recommendedMemMB (`int`_):

       Recommended default memory size for this guest, in MB.
    recommendedColorDepth (`int`_):

       Recommended default color depth for this guest.
    supportedDiskControllerList ([`str`_]):

       List of supported disk controller types for this guest.
    recommendedSCSIController (`str`_, optional):

       Recommended default SCSI controller type for this guest.
    recommendedDiskController (`str`_):

       Recommended default disk controller type for this guest.
    supportedNumDisks (`int`_):

       Number of disks supported for this guest.
    recommendedDiskSizeMB (`int`_):

       Recommended default disk size for this guest, in MB.
    recommendedCdromController (`str`_):

       Recommended default CD-ROM type for this guest.
    supportedEthernetCard ([`str`_]):

       List of supported ethernet cards for this guest.
    recommendedEthernetCard (`str`_, optional):

       Recommended default ethernet controller type for this guest.
    supportsSlaveDisk (`bool`_, optional):

       Flag to indicate whether or not this guest can support a disk configured as a slave.
    cpuFeatureMask ([`vim.host.CpuIdInfo`_], optional):

       Specifies the CPU feature compatibility masks.
    smcRequired (`bool`_):

       Flag that indicates wether the guest requires an SMC (Apple hardware). This is logically equivalent to GuestOS = Mac OS
    supportsWakeOnLan (`bool`_):

       Flag to indicate whether or not this guest can support Wake-on-LAN.
    supportsVMI (`bool`_):

       Flag indicating whether or not this guest supports the virtual machine interface.
    supportsMemoryHotAdd (`bool`_):

       Whether the memory size for this guest can be changed while the virtual machine is running.
    supportsCpuHotAdd (`bool`_):

       Whether virtual CPUs can be added to this guest while the virtual machine is running.
    supportsCpuHotRemove (`bool`_):

       Whether virtual CPUs can be removed from this guest while the virtual machine is running.
    supportedFirmware ([`str`_]):

       Supported firmware types for this guest. Possible values are described in `GuestOsDescriptorFirmwareType`_ 
    recommendedFirmware (`str`_):

       Recommended firmware type for this guest. Possible values are described in `GuestOsDescriptorFirmwareType`_ 
    supportedUSBControllerList ([`str`_], optional):

       List of supported USB controllers for this guest.
    recommendedUSBController (`str`_, optional):

       Recommended default USB controller type for this guest.
    supports3D (`bool`_):

       Whether this guest supports 3D graphics.
    recommended3D (`bool`_):

       Recommended 3D graphics for this guest.
    smcRecommended (`bool`_):

       Whether SMC (Apple hardware) is recommended for this guest.
    ich7mRecommended (`bool`_):

       Whether I/O Controller Hub is recommended for this guest.
    usbRecommended (`bool`_):

       Whether USB controller is recommended for this guest.
    supportLevel (`str`_):

       Support level of this Guest Possible values are described in `GuestOsDescriptorSupportLevel`_ 
    supportedForCreate (`bool`_):

       Whether or not this guest should be allowed for selection during virtual machine creation.
    vRAMSizeInKB (`vim.option.IntOption`_):

       Video RAM size limits supported by this guest, in KB.
