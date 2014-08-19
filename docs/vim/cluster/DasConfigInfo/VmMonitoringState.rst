vim.cluster.DasConfigInfo.VmMonitoringState
===========================================
  The `ClusterDasConfigInfoVmMonitoringState <vim/cluster/DasConfigInfo/VmMonitoringState.rst>`_ enum defines values that indicate the state of Virtual Machine Health Monitoring. Health Monitoring uses the vmTools (guest) and application agent heartbeat modules. You can configure HA to respond to heartbeat failures of either one or both modules. You can also disable the HA response to heartbeat failures.
   * To set the cluster default for health monitoring, use the ClusterConfigSpecEx.dasConfig.
   * `vmMonitoring <vim/cluster/DasConfigInfo.rst#vmMonitoring>`_
   * property.
   * To set health monitoring for a virtual machine, use the ClusterConfigSpecEx.dasVmConfigSpec.info.dasSettings.
   * `vmToolsMonitoringSettings <vim/cluster/DasVmSettings.rst#vmToolsMonitoringSettings>`_
   * property.
   * To retrieve the current state of health monitoring (cluster setting), use the ClusterConfigInfoEx.dasConfig.
   * `vmMonitoring <vim/cluster/DasConfigInfo.rst#vmMonitoring>`_
   * property.
   * To retrieve the current state of health monitoring for a virtual machine, use the ClusterConfigInfoEx.dasVmConfig[].dasSettings.vmToolsMonitoringSettings.
   * `vmMonitoring <vim/cluster/VmToolsMonitoringSettings.rst#vmMonitoring>`_
   * property.
  :contained by: `vim.cluster.DasConfigInfo <vim/cluster/DasConfigInfo.rst>`_

  :type: `vim.cluster.DasConfigInfo.VmMonitoringState <vim/cluster/DasConfigInfo/VmMonitoringState.rst>`_

  :name: vmAndAppMonitoring

values:
--------

vmMonitoringDisabled
   Virtual machine health monitoring is disabled. In this state, HA response to guest and application heartbeat failures are disabled.

vmMonitoringOnly
   HA response to guest heartbeat failure is enabled. To retrieve the guest heartbeat status, use the `VirtualMachine <vim/VirtualMachine.rst>`_ . `guestHeartbeatStatus <vim/VirtualMachine.rst#guestHeartbeatStatus>`_ property.

vmAndAppMonitoring
   HA response to both guest and application heartbeat failure is enabled.
    * To retrieve the guest heartbeat status, use the
    * `VirtualMachine <vim/VirtualMachine.rst>`_
    * .
    * `guestHeartbeatStatus <vim/VirtualMachine.rst#guestHeartbeatStatus>`_
    * property.
    * To retrieve the application heartbeat status, use the
    * `GuestInfo <vim/vm/GuestInfo.rst>`_
    * .
    * `appHeartbeatStatus <vim/vm/GuestInfo.rst#appHeartbeatStatus>`_
    * property.
