.. _GuestInfo: ../../../vim/vm/GuestInfo.rst

.. _vmMonitoring: ../../../vim/cluster/VmToolsMonitoringSettings.rst#vmMonitoring

.. _VirtualMachine: ../../../vim/VirtualMachine.rst

.. _appHeartbeatStatus: ../../../vim/vm/GuestInfo.rst#appHeartbeatStatus

.. _guestHeartbeatStatus: ../../../vim/VirtualMachine.rst#guestHeartbeatStatus

.. _vmToolsMonitoringSettings: ../../../vim/cluster/DasVmSettings.rst#vmToolsMonitoringSettings

.. _vim.cluster.DasConfigInfo: ../../../vim/cluster/DasConfigInfo.rst

.. _ClusterDasConfigInfoVmMonitoringState: ../../../vim/cluster/DasConfigInfo/VmMonitoringState.rst

.. _vim.cluster.DasConfigInfo.VmMonitoringState: ../../../vim/cluster/DasConfigInfo/VmMonitoringState.rst

vim.cluster.DasConfigInfo.VmMonitoringState
===========================================
  The `ClusterDasConfigInfoVmMonitoringState`_ enum defines values that indicate the state of Virtual Machine Health Monitoring. Health Monitoring uses the vmTools (guest) and application agent heartbeat modules. You can configure HA to respond to heartbeat failures of either one or both modules. You can also disable the HA response to heartbeat failures.
   * To set the cluster default for health monitoring, use the ClusterConfigSpecEx.dasConfig.
   * `vmMonitoring`_
   * property.
   * To set health monitoring for a virtual machine, use the ClusterConfigSpecEx.dasVmConfigSpec.info.dasSettings.
   * `vmToolsMonitoringSettings`_
   * property.
   * To retrieve the current state of health monitoring (cluster setting), use the ClusterConfigInfoEx.dasConfig.
   * `vmMonitoring`_
   * property.
   * To retrieve the current state of health monitoring for a virtual machine, use the ClusterConfigInfoEx.dasVmConfig[].dasSettings.vmToolsMonitoringSettings.
   * `vmMonitoring`_
   * property.
  :contained by: `vim.cluster.DasConfigInfo`_

  :type: `vim.cluster.DasConfigInfo.VmMonitoringState`_

  :name: vmAndAppMonitoring

values:
--------

vmMonitoringDisabled
   Virtual machine health monitoring is disabled. In this state, HA response to guest and application heartbeat failures are disabled.

vmMonitoringOnly
   HA response to guest heartbeat failure is enabled. To retrieve the guest heartbeat status, use the `VirtualMachine`_ . `guestHeartbeatStatus`_ property.

vmAndAppMonitoring
   HA response to both guest and application heartbeat failure is enabled.
    * To retrieve the guest heartbeat status, use the
    * `VirtualMachine`_
    * .
    * `guestHeartbeatStatus`_
    * property.
    * To retrieve the application heartbeat status, use the
    * `GuestInfo`_
    * .
    * `appHeartbeatStatus`_
    * property.
