.. _powerOff: ../../../vim/cluster/DasVmSettings/IsolationResponse.rst#powerOff

.. _defaultVmSettings: ../../../vim/cluster/DasConfigInfo.rst#defaultVmSettings

.. _isolationResponse: ../../../vim/cluster/DasVmSettings.rst#isolationResponse

.. _vim.cluster.DasVmSettings: ../../../vim/cluster/DasVmSettings.rst

.. _ClusterDasVmSettingsIsolationResponse: ../../../vim/cluster/DasVmSettings/IsolationResponse.rst

.. _vim.cluster.DasVmSettings.IsolationResponse: ../../../vim/cluster/DasVmSettings/IsolationResponse.rst

vim.cluster.DasVmSettings.IsolationResponse
===========================================
  The `ClusterDasVmSettingsIsolationResponse`_ enum defines values that indicate whether or not the virtual machine should be powered off if a host determines that it is isolated from the rest of the cluster.Host network isolation occurs when a host is still running but it can no longer communicate with other hosts in the cluster and it cannot ping the configured isolation address(es). When the HA agent on a host loses contact with the other hosts, it will ping the isolation addresses. If the pings fail, the host will declare itself isolated.Once the HA agent declares the host isolated, it will initiate the isolation response workflow after a 30 second delay. You can use the FDM advanced option fdm.isolationPolicyDelaySec to increase the delay. For each virtual machine, the HA agent attempts to determine if a master is responsible for restarting the virtual machine. If it cannot make the determination, or there is a master that is responsible, the agent will apply the configured isolation response. This workflow will continue until the configuration policy, has been applied to all virtual machines, the agent reconnects to another HA agent in the cluster, or the isolation address pings start succeeding. If there is a master agent in the cluster, it will attempt to restart the virtual machines that were powered off during isolation.By default, the isolated host leaves its virtual machines powered on. You can override the isolation response default with a cluster-wide setting ( `defaultVmSettings`_ ) or a virtual machine setting ( `isolationResponse`_ ).
   * All isolation response values are valid for the
   * `isolationResponse`_
   * property specified in a single virtual machine HA configuration.
   * All values except for
   * clusterIsolationResponse
   * are valid for the cluster-wide default HA configuration for virtual machines (
   * `defaultVmSettings`_
   * ).
   *
   * If you ensure that your network infrastructure is sufficiently redundant and that at least one network path is available at all times, host network isolation should be a rare occurrence.
  :contained by: `vim.cluster.DasVmSettings`_

  :type: `vim.cluster.DasVmSettings.IsolationResponse`_

  :name: clusterIsolationResponse

values:
--------

none
   Do not power off the virtual machine in the event of a host network isolation.

clusterIsolationResponse
   Use the default isolation response defined for the cluster that contains this virtual machine.

powerOff
   Power off the virtual machine in the event of a host network isolation.

shutdown
   Shut down the virtual machine guest operating system in the event of a host network isolation. If the guest operating system fails to shutdown within five minutes, HA will initiate a forced power off.When you use the shutdown isolation response, failover can take longer (compared to the `powerOff`_ response) because the virtual machine cannot fail over until it is shutdown.
