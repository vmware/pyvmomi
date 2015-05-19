.. _long: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.host.CpuInfo: ../../vim/host/CpuInfo.rst

.. _vim.host.NumaInfo: ../../vim/host/NumaInfo.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.BIOSInfo: ../../vim/host/BIOSInfo.rst

.. _vim.host.PciDevice: ../../vim/host/PciDevice.rst

.. _vim.host.CpuIdInfo: ../../vim/host/CpuIdInfo.rst

.. _vim.host.SystemInfo: ../../vim/host/SystemInfo.rst

.. _supportedCpuFeature: ../../vim/host/Capability.rst#supportedCpuFeature

.. _vim.host.CpuPackage: ../../vim/host/CpuPackage.rst

.. _vim.host.ReliableMemoryInfo: ../../vim/host/ReliableMemoryInfo.rst

.. _vim.host.CpuPowerManagementInfo: ../../vim/host/CpuPowerManagementInfo.rst


vim.host.HardwareInfo
=====================
  The HardwareInfo data object type describes the hardware configuration of the host.
:extends: vmodl.DynamicData_

Attributes:
    systemInfo (`vim.host.SystemInfo`_):

       Information about the system as a whole.
    cpuPowerManagementInfo (`vim.host.CpuPowerManagementInfo`_, optional):

    cpuInfo (`vim.host.CpuInfo`_):

       Overall CPU information.
    cpuPkg ([`vim.host.CpuPackage`_]):

       Information about each of the physical CPU packages on the host.
    memorySize (`long`_):

       Total amount of physical memory on the host in bytes.
    numaInfo (`vim.host.NumaInfo`_, optional):

       Information about the NUMA (non-uniform memory access).
    smcPresent (`bool`_):

       Presence of System Management Controller, indicates the host is Apple hardware, and thus capable of running Mac OS guest as VM.
    pciDevice ([`vim.host.PciDevice`_], optional):

       The list of Peripheral Component Interconnect (PCI) devices available on this host.
    cpuFeature ([`vim.host.CpuIdInfo`_], optional):

       CPU feature set that is supported by the hardware. This is the intersection of the feature sets supported by the individual CPU packages. This feature set is modified by the `supportedCpuFeature`_ array in the host capabilities to obtain the feature set supported by the virtualization platform.
    biosInfo (`vim.host.BIOSInfo`_, optional):

       Information about the system BIOS
    reliableMemoryInfo (`vim.host.ReliableMemoryInfo`_, optional):

       Information about reliable memory.
