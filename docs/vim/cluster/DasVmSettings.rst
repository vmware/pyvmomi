
vim.cluster.DasVmSettings
=========================
  The `ClusterDasVmSettings <vim/cluster/DasVmSettings.rst>`_ data object contains the HA configuration settings specified for a single virtual machine (identified by `ClusterDasVmConfigInfo <vim/cluster/DasVmConfigInfo.rst>`_ . `key <vim/cluster/DasVmConfigInfo.rst#key>`_ ) or as cluster-wide defaults ( `ClusterDasConfigInfo <vim/cluster/DasConfigInfo.rst>`_ . `defaultVmSettings <vim/cluster/DasConfigInfo.rst#defaultVmSettings>`_ ).All fields are optional. If you set themodifyparameter totruewhen you call `ReconfigureComputeResource_Task <vim/ComputeResource.rst#reconfigureEx>`_ , an unset property has no effect on the existing property value in the cluster configuration on the Server. If you set themodifyparameter tofalsewhen you reconfigure a cluster, the cluster configuration is reverted to the default values, then the new configuration values are applied.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    restartPriority (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Restart priority for a virtual machine.If not specified at either the cluster level or the virtual machine level, this will default tomedium.See `ClusterDasVmSettingsRestartPriority <vim/cluster/DasVmSettings/RestartPriority.rst>`_ 
    isolationResponse (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether or not the virtual machine should be powered off if a host determines that it is isolated from the rest of the compute resource.If not specified at either the cluster level or the virtual machine level, this will default topowerOff.See `ClusterDasVmSettingsIsolationResponse <vim/cluster/DasVmSettings/IsolationResponse.rst>`_ 
    vmToolsMonitoringSettings (`vim.cluster.VmToolsMonitoringSettings <vim/cluster/VmToolsMonitoringSettings.rst>`_, optional):

       Configuration for the VM Health Monitoring Service.
