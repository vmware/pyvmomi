
vim.cluster.DasFailoverLevelAdvancedRuntimeInfo
===============================================
  Advanced runtime information related to the high availability service for a cluster that has been configured with a failover level admission control policy. See `ClusterFailoverLevelAdmissionControlPolicy <vim/cluster/FailoverLevelAdmissionControlPolicy.rst>`_ .
:extends: vim.cluster.DasAdvancedRuntimeInfo_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    slotInfo (`vim.cluster.DasFailoverLevelAdvancedRuntimeInfo.SlotInfo <vim/cluster/DasFailoverLevelAdvancedRuntimeInfo/SlotInfo.rst>`_):

       Slot information for this cluster.
    totalSlots (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The total number of slots available in the cluster.See SlotInfo
    usedSlots (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of slots currently being used.See SlotInfo
    unreservedSlots (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of slots that are not used by currently powered on virtual machines and not reserved to satisfy the configured failover level. This number gives an indication of how many additional virtual machines can be powered on in this cluster without violating the failover level (assuming the new virtual machine's reservations are satisfied by the current slot size). This value is computed as follows (where m is the configured failover level): Remove the m largest hosts (ie. the ones with the most slots) from the list of "good" hosts (see `totalGoodHosts <vim/cluster/DasFailoverLevelAdvancedRuntimeInfo.rst#totalGoodHosts>`_ ). Sum up the number of slots on the remaining hosts and deduct the number of currently used slots (see `usedSlots <vim/cluster/DasFailoverLevelAdvancedRuntimeInfo.rst#usedSlots>`_ ). If this number is negative, use zero instead.See SlotInfo
    totalVms (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The total number of powered on vms in the cluster.
    totalHosts (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The total number of hosts in the cluster.
    totalGoodHosts (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The total number of connected hosts that are not in maintance mode and that do not have any DAS-related config issues on them.
    hostSlots ([`vim.cluster.DasFailoverLevelAdvancedRuntimeInfo.HostSlots <vim/cluster/DasFailoverLevelAdvancedRuntimeInfo/HostSlots.rst>`_], optional):

    vmsRequiringMultipleSlots ([`vim.cluster.DasFailoverLevelAdvancedRuntimeInfo.VmSlots <vim/cluster/DasFailoverLevelAdvancedRuntimeInfo/VmSlots.rst>`_], optional):

       The list of virtual machines whose reservations and memory overhead are not satisfied by a single slot.
