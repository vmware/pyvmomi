.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _cpuPkg: ../../vim/host/HardwareInfo.rst#cpuPkg

.. _cpuFeature: ../../vim/host/HardwareInfo.rst#cpuFeature

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _supportedCpuFeature: ../../vim/host/Capability.rst#supportedCpuFeature


vim.host.CpuIdInfo
==================
  The CpuIdInfo data object type is used to represent the CPU features of a particular host or product, or to specify what the CPU feature requirements are for a particular virtual machine or guest operating system.For each register (eax,ebx,ecx,edx), the string is a bit mask of the form:????:????:????:????:????:????:????:????When used to represent the features of a specific processor package ( `cpuPkg`_ ), the features common to all processors on a host ( `cpuFeature`_ ), or the features supported by a virtualization platform ( `supportedCpuFeature`_ ), each bit is either '0' or '1', or '-' for unknown/unspecified. In these feature vectors, the vendor field is never set.Optional values in these feature vectors default to '----:----:----:----:----:----:----:----'.When specifying the required feature set for a virtual machine or a guest operating system, the bits can take on the values as described below, and the vendor field may be set. The total feature requirements for a virtual machine are composed by using any requirements listed in the virtual machine's configuration to override the requirements listed in the descriptor for the virtual machine's guest OS.Bits used for specifying requirements:
   * x
   * : Unused by guest software.
   * T
   * : Feature that the guest software requires to be enabled.
   * F
   * : Feature that the guest software requires to be disabled.
   * 1
   * : Feature will be reported as enabled if queried by the guest software.
   * 0
   * : Feature will be reported as disabled if queried by the guest software.
   * R
   * : Feature will be reported as disabled if queried by the guest software; however, for VMotion the actual value of this feature is required to be the same on both hosts.
   * H
   * : Used by guest software. For VMotion the value of this feature is required to be the same on both hosts.
   * -
   * : This bit type is only used in the requirements stored in the virtual machine's configuration. It indicates that, for this bit position, the requirement from the guest OS descriptor should be used instead.
   * The values 'F' and '1' are rarely used but included for completeness. The '0' and '1' values do not promise a faithful virtualization of these features; whether the features work when forced to 0 or 1 is highly dependent on the guest software.
   * Optional values in the requirements from the virtual machine's configuration default to '----:----:----:----:----:----:----:----'. Optional values in the requirements from the guest OS descriptor default to 'xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx'.
   * Once the feature requirements for a virtual machine have been composed from the virtual machine's configuration and guest OS descriptor, the bit types above are used to identify whether or not the virtual machine can be powered on or be migrated with VMotion to a particular host. The rules are as follows:
   * 
   * Power-on
   * : Requirements marked as 'T' or 'F' must match bits '1' or '0', respectively, in the features advertised by the HardwareInfo of the power-on host.
   * VMotion
   * : Requirements marked as 'T' or 'F' must match bits '1' or '0', respectively, in the features advertised by the HardwareInfo of the destination host. Also, at the positions where requirements are marked 'H' or 'R', the advertised value of that feature for the source host must match that of the destination host.
   * 
:extends: vmodl.DynamicData_

Attributes:
    level (`int`_):

       Level (EAX input to CPUID).
    vendor (`str`_, optional):

       Used if this mask is for a particular vendor.
    eax (`str`_, optional):

       String representing the required EAX bits.
    ebx (`str`_, optional):

       String representing the required EBX bits.
    ecx (`str`_, optional):

       String representing the required ECX bits.
    edx (`str`_, optional):

       String representing the required EDX bits.
