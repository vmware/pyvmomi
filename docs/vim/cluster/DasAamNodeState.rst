.. _str: https://docs.python.org/2/library/stdtypes.html

.. _name: ../../vim/ManagedEntity.rst#name

.. _HostSystem: ../../vim/HostSystem.rst

.. _vim.HostSystem: ../../vim/HostSystem.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _ClusterDasAamNodeState: ../../vim/cluster/DasAamNodeState.rst

.. _ClusterDasAamNodeStateDasState: ../../vim/cluster/DasAamNodeState/DasState.rst


vim.cluster.DasAamNodeState
===========================
  The `ClusterDasAamNodeState`_ data object represents the state of the HA service on an ESX host. (AAM is a component of this service.)
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_
**deprecated**


Attributes:
    host (`vim.HostSystem`_):

       Reference to the host.
    name (`str`_):

       Name of the host ( `HostSystem`_ . `name`_ ).
    configState (`str`_):

       Configuration state of the HA agent on the host. The property can be one of the following values:configuringerrorunconfiguringrunningconfigStaterepresents setting or resetting the HA configuration on the host. If the configuration operation is successful, the value ofconfigStatechanges torunning. See `ClusterDasAamNodeStateDasState`_ .
    runtimeState (`str`_):

       The runtime state of the HA agent on the node. The property can be one of the following values:uninitializedinitializedrunningerroragentShutdownnodeFailedSee `ClusterDasAamNodeStateDasState`_ .
