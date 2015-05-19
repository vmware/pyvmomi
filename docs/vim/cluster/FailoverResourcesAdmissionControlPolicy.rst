.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _cpuFailoverResourcesPercent: ../../vim/cluster/FailoverResourcesAdmissionControlPolicy.rst#cpuFailoverResourcesPercent

.. _memoryFailoverResourcesPercent: ../../vim/cluster/FailoverResourcesAdmissionControlPolicy.rst#memoryFailoverResourcesPercent

.. _vim.cluster.DasAdmissionControlPolicy: ../../vim/cluster/DasAdmissionControlPolicy.rst

.. _ClusterFailoverLevelAdmissionControlPolicy: ../../vim/cluster/FailoverLevelAdmissionControlPolicy.rst

.. _ClusterFailoverResourcesAdmissionControlPolicy: ../../vim/cluster/FailoverResourcesAdmissionControlPolicy.rst


vim.cluster.FailoverResourcesAdmissionControlPolicy
===================================================
  The `ClusterFailoverResourcesAdmissionControlPolicy`_ reserves a specified percentage of aggregate cluster resources for failover. With the resources failover policy in place, vSphere HA uses the following calculations to control virtual machine migration in the cluster.
   * Calculate the total resource requirements for all powered-on virtual machines in the cluster.
   * Calculate the total host resources available for virtual machines.
   * Calculate the Current CPU failover capacity and current memory failover capacity for the cluster.
   * Compare the current CPU failover capacity and current memory failover capacity with the configured resource percentages (
   * `cpuFailoverResourcesPercent`_
   * and
   * `memoryFailoverResourcesPercent`_
   * ). If either current capacity is less than the corresponding configured capacity, HA does not allow the operation.
   * 
   * HA uses the actual reservations of the virtual machines. If a virtual machine does not have reservations, meaning that the reservation is 0, a default of 0MB memory and 256MHz CPU is applied. This is controlled by the same HA advanced options used for the failover level policy (
   * `ClusterFailoverLevelAdmissionControlPolicy`_
   * ).
:extends: vim.cluster.DasAdmissionControlPolicy_
:since: `vSphere API 4.0`_

Attributes:
    cpuFailoverResourcesPercent (`int`_):

       Percentage of CPU resources in the cluster to reserve for failover. You can specify up to 100% of CPU resources for failover.
    memoryFailoverResourcesPercent (`int`_):

       Percentage of memory resources in the cluster to reserve for failover. You can specify up to 100% of memory resources for failover.
