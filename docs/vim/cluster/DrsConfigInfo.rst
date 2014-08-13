.. _int: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _DrsBehavior: ../../vim/cluster/DrsConfigInfo/DrsBehavior.rst

.. _drsVmConfigSpec: ../../vim/cluster/ConfigSpecEx.rst#drsVmConfigSpec

.. _defaultVmBehavior: ../../vim/cluster/DrsConfigInfo.rst#defaultVmBehavior

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _ClusterConfigSpecEx: ../../vim/cluster/ConfigSpecEx.rst

.. _ClusterDrsConfigInfo: ../../vim/cluster/DrsConfigInfo.rst

.. _ClusterRecommendation: ../../vim/cluster/Recommendation.rst

.. _vim.option.OptionValue: ../../vim/option/OptionValue.rst

.. _ClusterDrsVmConfigInfo: ../../vim/cluster/DrsVmConfigInfo.rst

.. _ReconfigureComputeResource_Task: ../../vim/ComputeResource.rst#reconfigureEx

.. _vim.cluster.DrsConfigInfo.DrsBehavior: ../../vim/cluster/DrsConfigInfo/DrsBehavior.rst


vim.cluster.DrsConfigInfo
=========================
  The `ClusterDrsConfigInfo`_ data object contains configuration information for the VMware DRS service.All fields are optional. If you set themodifyparameter totruewhen you call `ReconfigureComputeResource_Task`_ , an unset property has no effect on the existing property value in the cluster configuration on the Server. If you set themodifyparameter tofalsewhen you reconfigure a cluster, the cluster configuration is reverted to the default values, then the new configuration values are applied.
:extends: vmodl.DynamicData_

Attributes:
    enabled (`bool`_, optional):

       Flag indicating whether or not the service is enabled.
    enableVmBehaviorOverrides (`bool`_, optional):

       Flag that dictates whether DRS Behavior overrides for individual virtual machines ( `ClusterDrsVmConfigInfo`_ ) are enabled. The default value istrue.When this flag istrue, the `ClusterConfigSpecEx`_ . `drsVmConfigSpec`_ values override the `defaultVmBehavior`_ .When this flag isfalse, the `defaultVmBehavior`_ value applies to all virtual machines, with the following exception: in a cluster that has EVC disabled, you cannot override the virtual machine setting ( `drsVmConfigSpec`_ ) for Fault Tolerance virtual machines.
    defaultVmBehavior (`vim.cluster.DrsConfigInfo.DrsBehavior`_, optional):

       Specifies the cluster-wide default DRS behavior for virtual machines. You can override the default behavior for a virtual machine by using the `ClusterDrsVmConfigInfo`_ object.
    vmotionRate (`int`_, optional):

       Threshold for generated `ClusterRecommendation`_ s. DRS generates only those recommendations that are above the specified vmotionRate. Ratings vary from 1 to 5. This setting applies to manual, partiallyAutomated, and fullyAutomated DRS clusters. See `DrsBehavior`_ .
    option ([`vim.option.OptionValue`_], optional):

       Advanced settings.
