.. _dasSettings: ../../../vim/cluster/DasVmConfigInfo.rst#dasSettings

.. _defaultVmSettings: ../../../vim/cluster/DasConfigInfo.rst#defaultVmSettings

.. _vim.cluster.DasVmSettings: ../../../vim/cluster/DasVmSettings.rst

.. _ClusterDasVmSettingsRestartPriority: ../../../vim/cluster/DasVmSettings/RestartPriority.rst

.. _vim.cluster.DasVmSettings.RestartPriority: ../../../vim/cluster/DasVmSettings/RestartPriority.rst

vim.cluster.DasVmSettings.RestartPriority
=========================================
  The `ClusterDasVmSettingsRestartPriority`_ enum defines virtual machine restart priority values to resolve resource contention. The priority determines the preference that HA gives to a virtual machine if sufficient capacity is not available to power on all failed virtual machines. For example, high priority virtual machines on a host get preference over low priority virtual machines.All priority values are valid for the restart priority specified in a single virtual machine HA configuration ( `dasSettings`_ ). All values except forclusterRestartPriorityare valid for the cluster-wide default HA configuration for virtual machines ( `defaultVmSettings`_ ).
  :contained by: `vim.cluster.DasVmSettings`_

  :type: `vim.cluster.DasVmSettings.RestartPriority`_

  :name: clusterRestartPriority

values:
--------

disabled
   vSphere HA is disabled for this virtual machine.

high
   Virtual machines with this priority have a higher chance of powering on after a failure if there is insufficient capacity on hosts to meet all virtual machine needs.

medium
   Virtual machines with this priority have an intermediate chance of powering on after a failure if there is insufficient capacity on hosts to meet all virtual machine needs.

low
   Virtual machines with this priority have a lower chance of powering on after a failure if there is insufficient capacity on hosts to meet all virtual machine needs.

clusterRestartPriority
   Virtual machines with this priority use the default restart priority defined for the cluster that contains this virtual machine.
