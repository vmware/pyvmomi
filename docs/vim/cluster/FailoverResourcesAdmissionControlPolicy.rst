
vim.cluster.FailoverResourcesAdmissionControlPolicy
===================================================
  The `ClusterFailoverResourcesAdmissionControlPolicy <vim/cluster/FailoverResourcesAdmissionControlPolicy.rst>`_ reserves a specified percentage of aggregate cluster resources for failover. With the resources failover policy in place, vSphere HA uses the following calculations to control virtual machine migration in the cluster.
   * Calculate the total resource requirements for all powered-on virtual machines in the cluster.
   * Calculate the total host resources available for virtual machines.
   * Calculate the Current CPU failover capacity and current memory failover capacity for the cluster.
   * Compare the current CPU failover capacity and current memory failover capacity with the configured resource percentages (
   * `cpuFailoverResourcesPercent <vim/cluster/FailoverResourcesAdmissionControlPolicy.rst#cpuFailoverResourcesPercent>`_
   * and
   * `memoryFailoverResourcesPercent <vim/cluster/FailoverResourcesAdmissionControlPolicy.rst#memoryFailoverResourcesPercent>`_
   * ). If either current capacity is less than the corresponding configured capacity, HA does not allow the operation.
   * 
   * HA uses the actual reservations of the virtual machines. If a virtual machine does not have reservations, meaning that the reservation is 0, a default of 0MB memory and 256MHz CPU is applied. This is controlled by the same HA advanced options used for the failover level policy (
   * `ClusterFailoverLevelAdmissionControlPolicy <vim/cluster/FailoverLevelAdmissionControlPolicy.rst>`_
   * ).
:extends: vim.cluster.DasAdmissionControlPolicy_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    cpuFailoverResourcesPercent (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Percentage of CPU resources in the cluster to reserve for failover. You can specify up to 100% of CPU resources for failover.
    memoryFailoverResourcesPercent (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Percentage of memory resources in the cluster to reserve for failover. You can specify up to 100% of memory resources for failover.
