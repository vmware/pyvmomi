
vim.cluster.DasVmConfigInfo
===========================
  The `ClusterDasVmConfigInfo <vim/cluster/DasVmConfigInfo.rst>`_ data object contains the HA configuration for a single virtual machine.All fields are optional. If you set themodifyparameter totruewhen you call `ReconfigureComputeResource_Task <vim/ComputeResource.rst#reconfigureEx>`_ , an unset property has no effect on the existing property value in the cluster configuration on the Server. If you set themodifyparameter tofalsewhen you reconfigure a cluster, the cluster configuration is reverted to the default values, then the new configuration values are applied.
:extends: vmodl.DynamicData_

Attributes:
    key (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):

       Reference to the virtual machine.
    restartPriority (`vim.cluster.DasVmConfigInfo.Priority <vim/cluster/DasVmConfigInfo/Priority.rst>`_, optional):

       Restart priority for a virtual machine.If there is nothing specified here, then the defaults are picked up from `defaultVmSettings <vim/cluster/DasConfigInfo.rst#defaultVmSettings>`_ .
    powerOffOnIsolation (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate whether or not the virtual machine should be powered off if a host determines that it is isolated from the rest of the compute resource.If there is nothing specified here, then the defaults are picked up from `defaultVmSettings <vim/cluster/DasConfigInfo.rst#defaultVmSettings>`_ .
    dasSettings (`vim.cluster.DasVmSettings <vim/cluster/DasVmSettings.rst>`_, optional):

       HA settings that apply to this virtual machine.Values specified in this object override the cluster-wide defaults for virtual machines ( `defaultVmSettings <vim/cluster/DasConfigInfo.rst#defaultVmSettings>`_ ).
