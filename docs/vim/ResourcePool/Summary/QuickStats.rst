
vim.ResourcePool.Summary.QuickStats
===================================
  A set of statistics that are typically updated with near real-time regularity. These statistics are aggregates of the corresponding statistics of all virtual machines in the given resource pool, and unless otherwise noted, only make sense when at least one virtual machine in the given resource pool is powered on. This data object type does not support notification, for scalability reasons. Therefore, changes in QuickStats do not generate property collector updates. To monitor statistics values, use the statistics and alarms modules instead.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    overallCpuUsage (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Basic CPU performance statistics, in MHz.
    overallCpuDemand (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Basic CPU performance statistics, in MHz.
    guestMemoryUsage (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Guest memory utilization statistics, in MB. This is also known as active guest memory. The number can be between 0 and the configured memory size of a virtual machine.
    hostMemoryUsage (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Host memory utilization statistics, in MB. This is also known as consummed host memory. This is between 0 and the configured resource limit. Valid while a virtual machine is running. This includes the overhead memory of a virtual machine.
    distributedCpuEntitlement (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       This is the amount of CPU resource, in MHz, that this VM is entitled to, as calculated by DRS. Valid only for a VM managed by DRS.
    distributedMemoryEntitlement (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       This is the amount of memory, in MB, that this VM is entitled to, as calculated by DRS. Valid only for a VM managed by DRS.
    staticCpuEntitlement (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The static CPU resource entitlement for a virtual machine. This value is calculated based on this virtual machine's resource reservations, shares and limit, and doesn't take into account current usage. This is the worst case CPU allocation for this virtual machine, that is, the amount of CPU resource this virtual machine would receive if all virtual machines running in the cluster went to maximum consumption. Units are MHz.
    staticMemoryEntitlement (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The static memory resource entitlement for a virtual machine. This value is calculated based on this virtual machine's resource reservations, shares and limit, and doesn't take into account current usage. This is the worst case memory allocation for this virtual machine, that is, the amount of memory this virtual machine would receive if all virtual machines running in the cluster went to maximum consumption. Units are MB.
    privateMemory (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The portion of memory, in MB, that is granted to a virtual machine from non-shared host memory.
    sharedMemory (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The portion of memory, in MB, that is granted to a virtual machine from host memory that is shared between VMs.
    swappedMemory (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The portion of memory, in MB, that is granted to a virtual machine from the host's swap space. This is a sign that there is memory pressure on the host.
    balloonedMemory (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The size of the balloon driver in a virtual machine, in MB. The host will inflate the balloon driver to reclaim physical memory from a virtual machine. This is a sign that there is memory pressure on the host.
    overheadMemory (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The amount of memory resource (in MB) that will be used by a virtual machine above its guest memory requirements. This value is set if and only if a virtual machine is registered on a host that supports memory resource allocation features. For powered off VMs, this is the minimum overhead required to power on the VM on the registered host. For powered on VMs, this is the current overhead reservation, a value which is almost always larger than the minimum overhead, and which grows with time.See `QueryMemoryOverheadEx <vim/HostSystem.rst#queryOverheadEx>`_ 
    consumedOverheadMemory (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The amount of overhead memory, in MB, currently being consumed to run a VM. This value is limited by the overhead memory reservation for a VM, stored in `overheadMemory <vim/ResourcePool/Summary/QuickStats.rst#overheadMemory>`_ .
    compressedMemory (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The amount of compressed memory currently consumed by VM, in KB.
