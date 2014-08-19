vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm
=========================================================================================
  :contained by: `vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState <vim/vm/DeviceRuntimeInfo/VirtualEthernetCardRuntimeState.rst>`_

  :type: `vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm <vim/vm/DeviceRuntimeInfo/VirtualEthernetCardRuntimeState/VmDirectPathGen2InactiveReasonVm.rst>`_

  :name: vmNptVMCIActive

values:
--------

vmNptIncompatibleBackingType
   The device backing is not a DistributedVirtualPortBacking.

vmNptInsufficientMemoryReservation
   The virtual machine does not have full memory reservation required to activate VMDirectPath Gen 2.

vmNptDisabledOrDisconnectedAdapter
   The virtual machine's network adapter is disabled or disconnected, and thus is not participating in VMDirectPath Gen 2.

vmNptConflictingOperationInProgress
   VMDirectPath Gen 2 is temporarily suspended while the virtual machine executes an operation such as suspend.

vmNptVMCIActive
   VMDirectPath Gen 2 is unavailable due to Incompatibe feature VMCI is active in the current VM. Kill the relevant VMCI application(s) and restart the VM will allow the vNIC(s) to enter passthrough mode.

vmNptIncompatibleAdapterFeatures
   The virtual machine's network adapter has features enabled which preclude it participating in VMDirectPath Gen 2 such as INT-x or PXE booting.

vmNptIncompatibleAdapterType
   The device type does not support VMDirectPath Gen 2.See `vmDirectPathGen2Supported <vim/vm/device/VirtualEthernetCardOption.rst#vmDirectPathGen2Supported>`_ 

vmNptConflictingIOChainConfigured
   Some networking feature has placed a conflicting IOChain on the network adapter, which prevents VMDirectPath Gen 2. Examples include DVFilter.

vmNptFaultToleranceOrRecordReplayConfigured
   The virtual machine is configured for Fault Tolerance or Record&Replay, which prevents VMDirectPath Gen 2.

vmNptIncompatibleGuest
   The virtual machine's guest OS does not support VMDirectPath Gen 2.

vmNptMonitorBlocks
   The virtual machine monitor is exercising functionality which which prevents VMDirectPath Gen 2.

vmNptRuntimeError
   VMDirectPath Gen 2 is unavailable due to an unforeseen runtime error in the virtualization platform (typically resource constraints.)

vmNptOutOfIntrVector
   VMDirectPath Gen 2 is unavailable due to host run out of intr vector in host. Guest can configure the vNIC to use less rx/tx queues or use MSI instead of MSIX.

vmNptIncompatibleGuestDriver
   The virtual machine's guest network driver does not support VMDirectPath Gen 2.
