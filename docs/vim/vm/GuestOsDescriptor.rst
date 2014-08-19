
vim.vm.GuestOsDescriptor
========================
  This data object type contains information to describe a particular guest operating system.
:extends: vmodl.DynamicData_

Attributes:
    id (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Identifier (short name) for the guest operating system.
    family (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Family to which this guest operating system belongs.
    fullName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Full name of the guest operating system. For example, if the value of "id" is "win2000Pro", then the value of "fullName" is "Windows 2000 Professional".
    supportedMaxCPUs (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Maximum number of processors supported for this guest.
    numSupportedPhysicalSockets (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Maximum number of sockets supported for this guest.
    numSupportedCoresPerSocket (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Maximum number of cores per socket for this guest.
    supportedMinMemMB (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Minimum memory requirements supported for this guest, in MB.
    supportedMaxMemMB (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Maximum memory requirements supported for this guest, in MB.
    recommendedMemMB (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Recommended default memory size for this guest, in MB.
    recommendedColorDepth (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Recommended default color depth for this guest.
    supportedDiskControllerList ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       List of supported disk controller types for this guest.
    recommendedSCSIController (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Recommended default SCSI controller type for this guest.
    recommendedDiskController (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Recommended default disk controller type for this guest.
    supportedNumDisks (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Number of disks supported for this guest.
    recommendedDiskSizeMB (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Recommended default disk size for this guest, in MB.
    recommendedCdromController (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Recommended default CD-ROM type for this guest.
    supportedEthernetCard ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       List of supported ethernet cards for this guest.
    recommendedEthernetCard (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Recommended default ethernet controller type for this guest.
    supportsSlaveDisk (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate whether or not this guest can support a disk configured as a slave.
    cpuFeatureMask ([`vim.host.CpuIdInfo <vim/host/CpuIdInfo.rst>`_], optional):

       Specifies the CPU feature compatibility masks.
    smcRequired (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag that indicates wether the guest requires an SMC (Apple hardware). This is logically equivalent to GuestOS = Mac OS
    supportsWakeOnLan (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag to indicate whether or not this guest can support Wake-on-LAN.
    supportsVMI (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether or not this guest supports the virtual machine interface.
    supportsMemoryHotAdd (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether the memory size for this guest can be changed while the virtual machine is running.
    supportsCpuHotAdd (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether virtual CPUs can be added to this guest while the virtual machine is running.
    supportsCpuHotRemove (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether virtual CPUs can be removed from this guest while the virtual machine is running.
    supportedFirmware ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       Supported firmware types for this guest. Possible values are described in `GuestOsDescriptorFirmwareType <vim/vm/GuestOsDescriptor/FirmwareType.rst>`_ 
    recommendedFirmware (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Recommended firmware type for this guest. Possible values are described in `GuestOsDescriptorFirmwareType <vim/vm/GuestOsDescriptor/FirmwareType.rst>`_ 
    supportedUSBControllerList ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       List of supported USB controllers for this guest.
    recommendedUSBController (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Recommended default USB controller type for this guest.
    supports3D (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether this guest supports 3D graphics.
    recommended3D (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Recommended 3D graphics for this guest.
    smcRecommended (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether SMC (Apple hardware) is recommended for this guest.
    ich7mRecommended (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether I/O Controller Hub is recommended for this guest.
    usbRecommended (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether USB controller is recommended for this guest.
    supportLevel (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Support level of this Guest Possible values are described in `GuestOsDescriptorSupportLevel <vim/vm/GuestOsDescriptor/SupportLevel.rst>`_ 
    supportedForCreate (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether or not this guest should be allowed for selection during virtual machine creation.
    vRAMSizeInKB (`vim.option.IntOption <vim/option/IntOption.rst>`_):

       Video RAM size limits supported by this guest, in KB.
