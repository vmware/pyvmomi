.. _VsanHostNodeState: ../../../vim/vsan/host/NodeState.rst

.. _VsanHostClusterStatus: ../../../vim/vsan/host/ClusterStatus.rst

.. _vim.vsan.host.NodeState: ../../../vim/vsan/host/NodeState.rst

.. _ExitMaintenanceMode_Task: ../../../vim/HostSystem.rst#exitMaintenanceMode

.. _EnterMaintenanceMode_Task: ../../../vim/HostSystem.rst#enterMaintenanceMode

.. _VsanHostClusterStatusState: ../../../vim/vsan/host/ClusterStatus/State.rst

vim.vsan.host.NodeState
=======================
  A `VsanHostNodeState`_ represents the state of participation of a host in the VSAN service.See `VsanHostClusterStatus`_ See `VsanHostClusterStatusState`_ 

  :type: `vim.vsan.host.NodeState`_

  :name: decommissioning

values:
--------

decommissioning
   The node is being decommissioned from the VSAN service; this state is considered transitory.

starting
   The node is starting the VSAN service; this state is considered transitory.

enteringMaintenanceMode
   The node is entering maintenance mode; this state is considered transitory.See `EnterMaintenanceMode_Task`_ 

agent
   The node is enabled for the VSAN service and is serving as an agent.

disabled
   The node is disabled for the VSAN service.

master
   The node is enabled for the VSAN service and is serving as the master.

exitingMaintenanceMode
   The node is exiting maintenance mode; this state is considered transitory.See `ExitMaintenanceMode_Task`_ 

error
   The node is enabled for the VSAN service but has some configuration error which prevents participation.

stopping
   The node is stopping the VSAN service; this state is considered transitory.

backup
   The node is enabled for the VSAN service and is serving as the backup.
