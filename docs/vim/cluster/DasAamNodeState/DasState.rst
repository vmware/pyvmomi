.. _configState: ../../../vim/cluster/DasAamNodeState.rst#configState

.. _runtimeState: ../../../vim/cluster/DasAamNodeState.rst#runtimeState

.. _vim.cluster.DasAamNodeState: ../../../vim/cluster/DasAamNodeState.rst

.. _ClusterDasAamNodeStateDasState: ../../../vim/cluster/DasAamNodeState/DasState.rst

.. _vim.cluster.DasAamNodeState.DasState: ../../../vim/cluster/DasAamNodeState/DasState.rst

vim.cluster.DasAamNodeState.DasState
====================================
  The `ClusterDasAamNodeStateDasState`_ enumerated type defines values for host HA configuration and runtime state properties ( `configState`_ and `runtimeState`_ ).
  :contained by: `vim.cluster.DasAamNodeState`_

  :type: `vim.cluster.DasAamNodeState.DasState`_

  :name: nodeFailed

values:
--------

uninitialized
   HA has never been enabled on the the host.

configuring
   HA configuration is in progress.

unconfiguring
   HA configuration is being removed.

agentShutdown
   The HA agent has been shut down.

nodeFailed
   The host is not reachable. This can represent a host failure or an isolated host.

running
   HA agent is running on this host.

error
   There is an error condition. This can represent a configuration error or a host agent runtime error.

initialized
   HA agents have been installed but are not running on the the host.
