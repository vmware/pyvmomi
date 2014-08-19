
vim.vm.RuntimeInfo
==================
  The RuntimeInfo data object type provides information about the execution state and history of a virtual machine.
:extends: vmodl.DynamicData_

Attributes:
    device ([`vim.vm.DeviceRuntimeInfo <vim/vm/DeviceRuntimeInfo.rst>`_], optional):

       Per-device runtime info. This array will be empty if the host software does not provide runtime info for any of the device types currently in use by the virtual machine. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.
    host (`vim.HostSystem <vim/HostSystem.rst>`_, optional):

       The host that is responsible for running a virtual machine. This property is null if the virtual machine is not running and is not assigned to run on a particular host.
    connectionState (`vim.VirtualMachine.ConnectionState <vim/VirtualMachine/ConnectionState.rst>`_):

       Indicates whether or not the virtual machine is available for management.
    powerState (`vim.VirtualMachine.PowerState <vim/VirtualMachine/PowerState.rst>`_):

       The current power state of the virtual machine.
    faultToleranceState (`vim.VirtualMachine.FaultToleranceState <vim/VirtualMachine/FaultToleranceState.rst>`_):

       The fault tolerance state of the virtual machine.
    dasVmProtection (`vim.vm.RuntimeInfo.DasProtectionState <vim/vm/RuntimeInfo/DasProtectionState.rst>`_, optional):

       The vSphere HA protection state for a virtual machine. Property is unset if vSphere HA is not enabled.
    toolsInstallerMounted (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag to indicate whether or not the VMware Tools installer is mounted as a CD-ROM.
    suspendTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The timestamp when the virtual machine was most recently suspended.This property is updated every time the virtual machine is suspended.
    bootTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The timestamp when the virtual machine was most recently powered on.This property is updated when the virtual machine is powered on from the poweredOff state, and is cleared when the virtual machine is powered off. This property is not updated when a virtual machine is resumed from a suspended state.
    suspendInterval (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The total time the virtual machine has been suspended since it was initially powered on. This time excludes the current period, if the virtual machine is currently suspended. This property is updated when the virtual machine resumes, and is reset to zero when the virtual machine is powered off.
    question (`vim.vm.QuestionInfo <vim/vm/QuestionInfo.rst>`_, optional):

       The current question, if any, that is blocking the virtual machine's execution.
    memoryOverhead (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The amount of memory resource (in bytes) that will be used by the virtual machine above its guest memory requirements. This value is set if and only if the virtual machine is registered on a host that supports memory resource allocation features.For powered off VMs, this is the minimum overhead required to power on the VM on the registered host.For powered on VMs, this is the current overhead reservation, a value which is almost always larger than the minimum overhead, and which grows with time.See `QueryMemoryOverheadEx <vim/HostSystem.rst#queryOverheadEx>`_ 
    maxCpuUsage (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Current upper-bound on CPU usage. The upper-bound is based on the host the virtual machine is current running on, as well as limits configured on the virtual machine itself or any parent resource pool. Valid while the virtual machine is running. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.
    maxMemoryUsage (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Current upper-bound on memory usage. The upper-bound is based on memory configuration of the virtual machine, as well as limits configured on the virtual machine itself or any parent resource pool. Valid while the virtual machine is running. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.
    numMksConnections (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Number of active MKS connections to this virtual machine.
    recordReplayState (`vim.VirtualMachine.RecordReplayState <vim/VirtualMachine/RecordReplayState.rst>`_):

       Record / replay state of this virtual machine.
    cleanPowerOff (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       For a powered off virtual machine, indicates whether the virtual machine's last shutdown was an orderly power off or not. Unset if the virtual machine is running or suspended.
    needSecondaryReason (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If set, indicates the reason the virtual machine needs a secondary.
    onlineStandby (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       This property indicates whether the guest has gone into one of the s1, s2 or s3 standby modes, false indicates the guest is awake.
    minRequiredEVCModeKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       For a powered-on or suspended virtual machine in a cluster with Enhanced VMotion Compatibility (EVC) enabled, this identifies the least-featured EVC mode (among those for the appropriate CPU vendor) that could admit the virtual machine. See `EVCMode <vim/EVCMode.rst>`_ . This property will be unset if the virtual machine is powered off or is not in an EVC cluster.This property may be used as a general indicator of the CPU feature baseline currently in use by the virtual machine. However, the virtual machine may be suppressing some of the features present in the CPU feature baseline of the indicated mode, either explicitly (in the virtual machine's configured `cpuFeatureMask <vim/vm/ConfigInfo.rst#cpuFeatureMask>`_ ) or implicitly (in the default masks for the `GuestOsDescriptor <vim/vm/GuestOsDescriptor.rst>`_ appropriate for the virtual machine's configured guest OS).
    consolidationNeeded (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether any disk of the virtual machine requires consolidation. This can happen for example when a snapshot is deleted but its associated disk is not committed back to the base disk. Use `ConsolidateVMDisks_Task <vim/VirtualMachine.rst#consolidateDisks>`_ to consolidate if needed.
    offlineFeatureRequirement ([`vim.vm.FeatureRequirement <vim/vm/FeatureRequirement.rst>`_], optional):

       These requirements must have equivalent host capabilities `featureCapability <vim/host/ConfigInfo.rst#featureCapability>`_ in order to power on.
    featureRequirement ([`vim.vm.FeatureRequirement <vim/vm/FeatureRequirement.rst>`_], optional):

       These requirements must have equivalent host capabilities `featureCapability <vim/host/ConfigInfo.rst#featureCapability>`_ in order to power on, resume, or migrate to the host.
    featureMask ([`vim.host.FeatureMask <vim/host/FeatureMask.rst>`_], optional):

       The masks applied to an individual virtual machine as a result of its configuration.
    vFlashCacheAllocation (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Specifies the total allocated vFlash resource for the vFlash caches associated with VM's VMDKs when VM is powered on, in bytes.
