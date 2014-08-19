
vim.cluster.DasAamNodeState
===========================
  The `ClusterDasAamNodeState <vim/cluster/DasAamNodeState.rst>`_ data object represents the state of the HA service on an ESX host. (AAM is a component of this service.)
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_
**deprecated**


Attributes:
    host (`vim.HostSystem <vim/HostSystem.rst>`_):

       Reference to the host.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the host ( `HostSystem <vim/HostSystem.rst>`_ . `name <vim/ManagedEntity.rst#name>`_ ).
    configState (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Configuration state of the HA agent on the host. The property can be one of the following values:configuringerrorunconfiguringrunningconfigStaterepresents setting or resetting the HA configuration on the host. If the configuration operation is successful, the value ofconfigStatechanges torunning. See `ClusterDasAamNodeStateDasState <vim/cluster/DasAamNodeState/DasState.rst>`_ .
    runtimeState (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The runtime state of the HA agent on the node. The property can be one of the following values:uninitializedinitializedrunningerroragentShutdownnodeFailedSee `ClusterDasAamNodeStateDasState <vim/cluster/DasAamNodeState/DasState.rst>`_ .
