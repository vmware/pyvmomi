.. _int: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _guestHeartbeatStatus: ../../../vim/VirtualMachine.rst#guestHeartbeatStatus

.. _vim.ManagedEntity.Status: ../../../vim/ManagedEntity/Status.rst


vim.vm.Summary.QuickStats
=========================
  A set of statistics that are typically updated with near real-time regularity. This data object type does not support notification, for scalability reasons. Therefore, changes in QuickStats do not generate property collector updates. To monitor statistics values, use the statistics and alarms modules instead.
:extends: vmodl.DynamicData_

Attributes:
    overallCpuUsage (`int`_, optional):

       Basic CPU performance statistics, in MHz. Valid while the virtual machine is running.
    overallCpuDemand (`int`_, optional):

       Basic CPU performance statistics, in MHz. Valid while the virtual machine is running.
    guestMemoryUsage (`int`_, optional):

       Guest memory utilization statistics, in MB. This is also known as active guest memory. The number can be between 0 and the configured memory size of the virtual machine. Valid while the virtual machine is running.
    hostMemoryUsage (`int`_, optional):

       Host memory utilization statistics, in MB. This is also known as consumed host memory. This is between 0 and the configured resource limit. Valid while the virtual machine is running. This includes the overhead memory of the VM.
    guestHeartbeatStatus (`vim.ManagedEntity.Status`_):

       Guest operating system heartbeat metric. See `guestHeartbeatStatus`_ for a description.
    distributedCpuEntitlement (`int`_, optional):

       This is the amount of CPU resource, in MHz, that this VM is entitled to, as calculated by DRS. Valid only for a VM managed by DRS.
    distributedMemoryEntitlement (`int`_, optional):

       This is the amount of memory, in MB, that this VM is entitled to, as calculated by DRS. Valid only for a VM managed by DRS.
    staticCpuEntitlement (`int`_, optional):

       The static CPU resource entitlement for a virtual machine. This value is calculated based on this virtual machine's resource reservations, shares and limit, and doesn't take into account current usage. This is the worst case CPU allocation for this virtual machine, that is, the amount of CPU resource this virtual machine would receive if all virtual machines running in the cluster went to maximum consumption. Units are MHz.
    staticMemoryEntitlement (`int`_, optional):

       The static memory resource entitlement for a virtual machine. This value is calculated based on this virtual machine's resource reservations, shares and limit, and doesn't take into account current usage. This is the worst case memory allocation for this virtual machine, that is, the amount of memory this virtual machine would receive if all virtual machines running in the cluster went to maximum consumption. Units are MB.
    privateMemory (`int`_, optional):

       The portion of memory, in MB, that is granted to this VM from non-shared host memory.
    sharedMemory (`int`_, optional):

       The portion of memory, in MB, that is granted to this VM from host memory that is shared between VMs.
    swappedMemory (`int`_, optional):

       The portion of memory, in MB, that is granted to this VM from the host's swap space. This is a sign that there is memory pressure on the host.
    balloonedMemory (`int`_, optional):

       The size of the balloon driver in the VM, in MB. The host will inflate the balloon driver to reclaim physical memory from the VM. This is a sign that there is memory pressure on the host.
    consumedOverheadMemory (`int`_, optional):

       The amount of consumed overhead memory, in MB, for this VM.
    ftLogBandwidth (`int`_, optional):

       The network bandwidth used for logging between the primary and secondary fault tolerance VMs. The unit is kilobytes per second.
    ftSecondaryLatency (`int`_, optional):

       The amount of time in wallclock that the VCPU of the secondary fault tolerance VM is behind the VCPU of the primary VM. The unit is millisecond.
    ftLatencyStatus (`vim.ManagedEntity.Status`_, optional):

       The latency status of the fault tolerance VM. ftLatencyStatus is determined by the value of ftSecondaryLatency. ftLatencyStatus is: green, if ftSecondaryLatency is less than or equal to 2 seconds; yellow, if ftSecondaryLatency is greater than 2 seconds, and less than or equal to 6 seconds; red, if ftSecondaryLatency is greater than 6 seconds; gray, if ftSecondaryLatency is unknown.
    compressedMemory (`long`_, optional):

       The amount of compressed memory currently consumed by VM, in Kb.
    uptimeSeconds (`int`_, optional):

       The system uptime of the VM in seconds.
    ssdSwappedMemory (`long`_, optional):

       The amount of memory swapped to fast disk device such as SSD, in KB.
