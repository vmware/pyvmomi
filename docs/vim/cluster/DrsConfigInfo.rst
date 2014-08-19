
vim.cluster.DrsConfigInfo
=========================
  The `ClusterDrsConfigInfo <vim/cluster/DrsConfigInfo.rst>`_ data object contains configuration information for the VMware DRS service.All fields are optional. If you set themodifyparameter totruewhen you call `ReconfigureComputeResource_Task <vim/ComputeResource.rst#reconfigureEx>`_ , an unset property has no effect on the existing property value in the cluster configuration on the Server. If you set themodifyparameter tofalsewhen you reconfigure a cluster, the cluster configuration is reverted to the default values, then the new configuration values are applied.
:extends: vmodl.DynamicData_

Attributes:
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag indicating whether or not the service is enabled.
    enableVmBehaviorOverrides (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag that dictates whether DRS Behavior overrides for individual virtual machines ( `ClusterDrsVmConfigInfo <vim/cluster/DrsVmConfigInfo.rst>`_ ) are enabled. The default value istrue.When this flag istrue, the `ClusterConfigSpecEx <vim/cluster/ConfigSpecEx.rst>`_ . `drsVmConfigSpec <vim/cluster/ConfigSpecEx.rst#drsVmConfigSpec>`_ values override the `defaultVmBehavior <vim/cluster/DrsConfigInfo.rst#defaultVmBehavior>`_ .When this flag isfalse, the `defaultVmBehavior <vim/cluster/DrsConfigInfo.rst#defaultVmBehavior>`_ value applies to all virtual machines, with the following exception: in a cluster that has EVC disabled, you cannot override the virtual machine setting ( `drsVmConfigSpec <vim/cluster/ConfigSpecEx.rst#drsVmConfigSpec>`_ ) for Fault Tolerance virtual machines.
    defaultVmBehavior (`vim.cluster.DrsConfigInfo.DrsBehavior <vim/cluster/DrsConfigInfo/DrsBehavior.rst>`_, optional):

       Specifies the cluster-wide default DRS behavior for virtual machines. You can override the default behavior for a virtual machine by using the `ClusterDrsVmConfigInfo <vim/cluster/DrsVmConfigInfo.rst>`_ object.
    vmotionRate (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Threshold for generated `ClusterRecommendation <vim/cluster/Recommendation.rst>`_ s. DRS generates only those recommendations that are above the specified vmotionRate. Ratings vary from 1 to 5. This setting applies to manual, partiallyAutomated, and fullyAutomated DRS clusters. See `DrsBehavior <vim/cluster/DrsConfigInfo/DrsBehavior.rst>`_ .
    option ([`vim.option.OptionValue <vim/option/OptionValue.rst>`_], optional):

       Advanced settings.
