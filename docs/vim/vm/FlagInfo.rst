.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _virtualMmuUsage: ../../vim/vm/FlagInfo.rst#virtualMmuUsage

.. _virtualExecUsage: ../../vim/vm/FlagInfo.rst#virtualExecUsage

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _VirtualMachineHtSharing: ../../vim/vm/FlagInfo/HtSharing.rst

.. _VirtualMachinePowerOffBehavior: ../../vim/vm/FlagInfo/PowerOffBehavior.rst

.. _VirtualMachineFlagInfoMonitorType: ../../vim/vm/FlagInfo/MonitorType.rst

.. _VirtualMachineFlagInfoVirtualMmuUsage: ../../vim/vm/FlagInfo/VirtualMmuUsage.rst

.. _VirtualMachineFlagInfoVirtualExecUsage: ../../vim/vm/FlagInfo/VirtualExecUsage.rst


vim.vm.FlagInfo
===============
  The FlagInfo data object type encapsulates the flag settings for a virtual machine. These properties are optional since the same structure is used to change the values during an edit or create operation.
:extends: vmodl.DynamicData_

Attributes:
    disableAcceleration (`bool`_, optional):

       Flag to turn off video acceleration for a virtual machine console window.
    enableLogging (`bool`_, optional):

       Flag to enable logging for a virtual machine.
    useToe (`bool`_, optional):

       Flag to specify whether or not to use TOE (TCP/IP Offloading).
    runWithDebugInfo (`bool`_, optional):

       Flag to specify whether or not to run in debug mode.
    monitorType (`str`_, optional):

       vmx process type. See `VirtualMachineFlagInfoMonitorType`_ for possible values for this property.
    htSharing (`str`_, optional):

       Specifies how the VCPUs of a virtual machine are allowed to share physical cores on a hyperthreaded system. Two VCPUs are "sharing" a core if they are both running on logical CPUs of the core at the same time.See `VirtualMachineHtSharing`_ 
    snapshotDisabled (`bool`_, optional):

       Flag to specify whether snapshots are disabled for this virtual machine.
    snapshotLocked (`bool`_, optional):

       Flag to specify whether the snapshot tree is locked for this virtual machine.
    diskUuidEnabled (`bool`_, optional):

       Indicates whether disk UUIDs are being used by this virtual machine. If this flag is set to false, disk UUIDs are not exposed to the guest.Since products before ESX 3.1 do not support disk UUIDs, moving virtual machines from a platform that supports UUID to a platform that does not support UUIDs could result in unspecified guest behavior. For virtual machines where the ability to move to older platforms is important, this flag should be set to false. If the value is unset, the behavior 'false' will be used.
    virtualMmuUsage (`str`_, optional):

       Indicates whether or not the system will try to use nested page table hardware support, if available.By default, VMware software will determine whether or not to use nested page table hardware support based on various factors such as the guest operating system type and the physical hardware. Certain workloads can benefit from explicitly turning nested page table hardware support on or off; this can be set using nptUsage flag. If the value is unset, the value will default to automatic. `VirtualMachineFlagInfoVirtualMmuUsage`_ represents the set of possible values.
    virtualExecUsage (`str`_, optional):

       Indicates whether or not the system will try to use Hardware Virtualization (HV) support for instruction virtualization, if available.By default, VMware software will determine whether or not to use hardware virtualization support based on various factors such as the guest operating system type and the physical hardware. Certain workloads can benefit from explicitly turning hardware virtualization support on or off. If the value is unset, the value will default to hvAuto. `VirtualMachineFlagInfoVirtualExecUsage`_ represents the set of possible values.New processors can enable two hardware acceleration technologies for virtualization, one for instruction virtualization and the other for MMU virtualization. Intel names its hardware-assisted instruction virtualization as VT, and its hardware-assisted MMU virtualization as EPT. AMD calls them as AMD-V and RVI, respectively. For details on these technologies, please refer to documents from the processor vendors. `virtualExecUsage`_ controls instruction virtualization; while `virtualMmuUsage`_ controls MMU virtualization. "On" allows hardware acceleration, while "off" only allows software solution.There are four meaningful combinations.(hvAuto, automatic) - The host chooses which feature to use. (hvOn, on) - Use both VT/AMD-V and EPT/RVI. (hvOn, off) - Use VT/AMD-V but do not use EPT/RVI. (hvOff, off) - Do not use any of these hardware acceleration technologies.
    snapshotPowerOffBehavior (`str`_, optional):

       Specifies the power-off behavior for a virtual machine that has a snapshot. If the value is unset, the behavior 'powerOff' will be used.See `VirtualMachinePowerOffBehavior`_ 
    recordReplayEnabled (`bool`_, optional):

       Flag to specify whether record and replay operations are allowed for this virtual machine. If this flag is set to 'true', instruction virtualization will use hardware virtualization (HV) support. I.e., virtualExecUsage will be set to 'hvOn'. If this flag is set to 'false' for a virtual machine that already has a recording, replay will be disallowed, though the recording will be preserved. If the value is unset, the behavior 'false' will be used.
