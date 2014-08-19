
vim.vm.Capability
=================
  This data object type contains information about the operation/capabilities of a virtual machine
:extends: vmodl.DynamicData_

Attributes:
    snapshotOperationsSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not a virtual machine supports snapshot operations.
    multipleSnapshotsSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not a virtual machine supports multiple snapshots. This value is not set when the virtual machine is unavailable, for instance, when it is being created or deleted.
    snapshotConfigSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not a virtual machine supports snapshot config.
    poweredOffSnapshotsSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not a virtual machine supports snapshot operations in poweredOff state. This flag doesn't affect vim.VirtualMachine.GetSnapshot, which is always supported.
    memorySnapshotsSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not a virtual machine supports memory snapshots.
    revertToSnapshotSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not a virtual machine supports reverting to a snapshot.
    quiescedSnapshotsSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not a virtual machine supports quiesced snapshots.
    disableSnapshotsSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not snapshots can be disabled.
    lockSnapshotsSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not the snapshot tree can be locked.
    consolePreferencesSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether console preferences can be set for this virtual machine.
    cpuFeatureMaskSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether CPU feature requirements masks can be set for this virtual machine.
    s1AcpiManagementSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not a virtual machine supports ACPI S1 settings management.
    settingScreenResolutionSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether of not this virtual machine supports setting the screen resolution of the console window. This capability depends on the guest operating system configured for this virtual machine.
    toolsAutoUpdateSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Supports tools auto-update.
    vmNpivWwnSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Supports virtual machine NPIV WWN.
    npivWwnOnNonRdmVmSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Supports assigning NPIV WWN to virtual machines that don't have RDM disks.
    vmNpivWwnDisableSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the NPIV disabling operation is supported the virtual machine.
    vmNpivWwnUpdateSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the update of NPIV WWNs are supported on the virtual machine.
    swapPlacementSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether the virtual machine has a configurable `swapfile placement policy <vim/vm/ConfigInfo.rst#swapPlacement>`_ .
    toolsSyncTimeSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether asking tools to sync time with the host is supported.
    virtualMmuUsageSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not the use of nested page table hardware support can be explicitly set.
    diskSharesSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether resource settings for disks can be applied to this virtual machine.
    bootOptionsSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether boot options can be configured for this virtual machine.
    bootRetryOptionsSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether automatic boot retry can be configured for this virtual machine.
    settingVideoRamSizeSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether the video ram size of this virtual machine can be configured.
    settingDisplayTopologySupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether of not this virtual machine supports setting the display topology of the console window. This capability depends on the guest operating system configured for this virtual machine.
    recordReplaySupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether record and replay functionality is supported on this virtual machine.
    changeTrackingSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates that change tracking is supported for virtual disks of this virtual machine. However, even if change tracking is supported, it might not be available for all disks of the virtual machine. For example, passthru raw disk mappings or disks backed by any Ver1BackingInfo cannot be tracked.
    multipleCoresPerSocketSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether multiple virtual cores per socket is supported on this VM.
    hostBasedReplicationSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates that host based replication is supported on this virtual machine. However, even if host based replication is supported, it might not be available for all disk types. For example, passthru raw disk mappings can not be replicated.
    guestAutoLockSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

    memoryReservationLockSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether `memoryReservationLockedToMax <vim/vm/ConfigInfo.rst#memoryReservationLockedToMax>`_ may be set to true for this virtual machine.
    featureRequirementSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether featureRequirement feature is supported.
    poweredOnMonitorTypeChangeSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether a monitor type change is supported while this virtual machine is in the poweredOn state.
    seSparseDiskSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether this virtual machine supports the Flex-SE (space-efficent, sparse) format for virtual disks.
    nestedHVSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether this virtual machine supports nested hardware-assisted virtualization.
    vPMCSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether this virtual machine supports virtualized CPU performance counters.
