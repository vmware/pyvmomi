vim.cluster.Recommendation.ReasonCode
=====================================
  List of defined migration reason codes:
  :contained by: `vim.cluster.Recommendation <vim/cluster/Recommendation.rst>`_

  :type: `vim.cluster.Recommendation.ReasonCode <vim/cluster/Recommendation/ReasonCode.rst>`_

  :name: iolbDisabledInternal

values:
--------

virtualDiskJointAffin
   Fix virtual disk affinity rule violation.

datastoreSpaceOutage
   Fix the issue that a datastore run out of space.

increaseCapacity
   Power on host to increase cluster capacity

balanceDatastoreSpaceUsage
   Balance datastore space usage.

storagePlacement
   Satisfy storage initial placement requests.

unreservedCapacity
   Maintain unreserved capacity

antiAffin
   Fulfill anti-affinity rule.

vmHostHardAffinity
   Fix hard VM/host affinity rule violation

iolbDisabledInternal
   IO load balancing was disabled internally.

jointAffin
   Fulfill affinity rule.

virtualDiskAntiAffin
   Fix virtual disk anti-affinity rule violation.

reservationCpu
   balance CPU reservations

checkResource
   Sanity-check resource pool hierarchy

enterStandby
   Host entering standby mode.

powerOnVm
   Power on virtual machine

balanceDatastoreIOLoad
   Balance datastore I/O workload.

fairnessMemAvg
   Balance average memory utilization.

powerSaving
   Power off host for power savings

reservationMem
   balance memory reservations

hostMaint
   Host entering maintenance mode.

fairnessCpuAvg
   Balance average CPU utilization.

datastoreMaint
   Datastore entering maintenance mode.

vmHostSoftAffinity
   Fix soft VM/host affinity rule violation
