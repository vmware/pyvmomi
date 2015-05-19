.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _defaultVmSettings: ../../vim/cluster/DasConfigInfo.rst#defaultVmSettings

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.VirtualMachine: ../../vim/VirtualMachine.rst

.. _ClusterDasVmConfigInfo: ../../vim/cluster/DasVmConfigInfo.rst

.. _vim.cluster.DasVmSettings: ../../vim/cluster/DasVmSettings.rst

.. _ReconfigureComputeResource_Task: ../../vim/ComputeResource.rst#reconfigureEx

.. _vim.cluster.DasVmConfigInfo.Priority: ../../vim/cluster/DasVmConfigInfo/Priority.rst


vim.cluster.DasVmConfigInfo
===========================
  The `ClusterDasVmConfigInfo`_ data object contains the HA configuration for a single virtual machine.All fields are optional. If you set themodifyparameter totruewhen you call `ReconfigureComputeResource_Task`_ , an unset property has no effect on the existing property value in the cluster configuration on the Server. If you set themodifyparameter tofalsewhen you reconfigure a cluster, the cluster configuration is reverted to the default values, then the new configuration values are applied.
:extends: vmodl.DynamicData_

Attributes:
    key (`vim.VirtualMachine`_):

       Reference to the virtual machine.
    restartPriority (`vim.cluster.DasVmConfigInfo.Priority`_, optional):

       Restart priority for a virtual machine.If there is nothing specified here, then the defaults are picked up from `defaultVmSettings`_ .
    powerOffOnIsolation (`bool`_, optional):

       Flag to indicate whether or not the virtual machine should be powered off if a host determines that it is isolated from the rest of the compute resource.If there is nothing specified here, then the defaults are picked up from `defaultVmSettings`_ .
    dasSettings (`vim.cluster.DasVmSettings`_, optional):

       HA settings that apply to this virtual machine.Values specified in this object override the cluster-wide defaults for virtual machines ( `defaultVmSettings`_ ).
