.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _enabled: ../../vim/cluster/DasConfigInfo/ServiceState.rst#enabled

.. _disabled: ../../vim/cluster/DasConfigInfo/ServiceState.rst#disabled

.. _vmMonitoring: ../../vim/cluster/VmToolsMonitoringSettings.rst#vmMonitoring

.. _vim.Datastore: ../../vim/Datastore.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vmMonitoringDisabled: ../../vim/cluster/DasConfigInfo/VmMonitoringState.rst#vmMonitoringDisabled

.. _ClusterDasConfigInfo: ../../vim/cluster/DasConfigInfo.rst

.. _admissionControlPolicy: ../../vim/cluster/DasConfigInfo.rst#admissionControlPolicy

.. _vim.option.OptionValue: ../../vim/option/OptionValue.rst

.. _ClusterDasVmConfigSpec: ../../vim/cluster/DasVmConfigSpec.rst

.. _heartbeatDatastoreInfo: ../../vim/cluster/DasAdvancedRuntimeInfo.rst#heartbeatDatastoreInfo

.. _vim.cluster.DasVmSettings: ../../vim/cluster/DasVmSettings.rst

.. _hBDatastoreCandidatePolicy: ../../vim/cluster/DasConfigInfo.rst#hBDatastoreCandidatePolicy

.. _RetrieveDasAdvancedRuntimeInfo: ../../vim/ClusterComputeResource.rst#retrieveDasAdvancedRuntimeInfo

.. _allFeasibleDsWithUserPreference: ../../vim/cluster/DasConfigInfo/HBDatastoreCandidate.rst#allFeasibleDsWithUserPreference

.. _ReconfigureComputeResource_Task: ../../vim/ComputeResource.rst#reconfigureEx

.. _ClusterVmToolsMonitoringSettings: ../../vim/cluster/VmToolsMonitoringSettings.rst

.. _ClusterDasConfigInfoServiceState: ../../vim/cluster/DasConfigInfo/ServiceState.rst

.. _ClusterDasConfigInfoVmMonitoringState: ../../vim/cluster/DasConfigInfo/VmMonitoringState.rst

.. _vim.cluster.DasAdmissionControlPolicy: ../../vim/cluster/DasAdmissionControlPolicy.rst

.. _ClusterDasConfigInfoHBDatastoreCandidate: ../../vim/cluster/DasConfigInfo/HBDatastoreCandidate.rst

.. _ClusterFailoverHostAdmissionControlPolicy: ../../vim/cluster/FailoverHostAdmissionControlPolicy.rst

.. _ClusterFailoverLevelAdmissionControlPolicy: ../../vim/cluster/FailoverLevelAdmissionControlPolicy.rst

.. _ClusterFailoverResourcesAdmissionControlPolicy: ../../vim/cluster/FailoverResourcesAdmissionControlPolicy.rst


vim.cluster.DasConfigInfo
=========================
  The `ClusterDasConfigInfo`_ data object contains configuration data about the HA service on a cluster.All fields are optional. If you set themodifyparameter totruewhen you call `ReconfigureComputeResource_Task`_ , an unset property has no effect on the existing property value in the cluster configuration on the Server. If you set themodifyparameter tofalsewhen you reconfigure a cluster, the cluster configuration is reverted to the default values, then the new configuration values are applied.
:extends: vmodl.DynamicData_

Attributes:
    enabled (`bool`_, optional):

       Flag to indicate whether or not vSphere HA feature is enabled.
    vmMonitoring (`str`_, optional):

       Level of HA Virtual Machine Health Monitoring Service. You can monitor both guest and application heartbeats, guest heartbeats only, or you can disable the service. See `ClusterDasConfigInfoVmMonitoringState`_ . The default value is `vmMonitoringDisabled`_ .The Service level specified for the cluster determines the possible monitoring settings that you can use for individual virtual machines. See `ClusterVmToolsMonitoringSettings`_ . `vmMonitoring`_ .
    hostMonitoring (`str`_, optional):

       Determines whether HA restarts virtual machines after a host fails. The default value is `ClusterDasConfigInfoServiceState`_ . `enabled`_ . This property is meaningful only when `ClusterDasConfigInfo`_ . `enabled`_ istrue.WhenhostMonitoringis `enabled`_ , HA restarts virtual machines after a host fails.WhenhostMonitoringis `disabled`_ , HA does not restart virtual machines after a host fails. The status of Host Monitoring does not affect other services such as virtual machine Health Monitoring or Fault Tolerance. The rest of the cluster operations follow normal processing. No configuration information is lost and re-enabling the service is a quick operation.
    failoverLevel (`int`_, optional):

       Configured failover level. This is the number of physical host failures that can be tolerated without impacting the ability to satisfy the minimums for all running virtual machines. Acceptable values range from one to four.
    admissionControlPolicy (`vim.cluster.DasAdmissionControlPolicy`_, optional):

       Virtual machine admission control policy for vSphere HA. The policies specify resource availability for failover support.
        * Failover host admission policy
        * `ClusterFailoverHostAdmissionControlPolicy`_
        * - currently you can specify only one failover host.
        * Failover level policy
        * `ClusterFailoverLevelAdmissionControlPolicy`_
        * - the limit of host failures for which resources are reserved. When you use the failover level policy, HA partitions resources into slots. A slot represents the minimum CPU and memory resources that are required to support any powered on virtual machine in the cluster. To retrieve information about partitioned resources, use the
        * `RetrieveDasAdvancedRuntimeInfo`_
        * method.
        * Resources admission policy
        * `ClusterFailoverResourcesAdmissionControlPolicy`_
        * - CPU and memory resources reserved for failover support. When you use the resources policy, you can reserve a percentage of the aggregate cluster resource for failover.
    admissionControlEnabled (`bool`_, optional):

       Flag that determines whether strict admission control is enabled. When you use admission control, the following operations are prevented, if doing so would violate the `admissionControlPolicy`_ .
        * Powering on a virtual machine in the cluster.
        * Migrating a virtual machine into the cluster.
        * Increasing the CPU or memory reservation of powered-on virtual machines in the cluster.With admission control disabled, there is no assurance that all virtual machines in the HA cluster can be restarted after a host failure. VMware recommends that you do not disable admission control, but you might need to do so temporarily, for the following reasons:
        * If you need to violate the failover constraints when there are not enough resources to support them (for example, if you are placing hosts in standby mode to test them for use with DPM).
        * If an automated process needs to take actions that might temporarily violate the failover constraints (for example, as part of an upgrade directed by VMware Update Manager).
        * If you need to perform testing or maintenance operations.
    defaultVmSettings (`vim.cluster.DasVmSettings`_, optional):

       Cluster-wide defaults for virtual machine HA settings. When a virtual machine has no HA configuration ( `ClusterDasVmConfigSpec`_ ), it uses the values specified here.
    option ([`vim.option.OptionValue`_], optional):

       Advanced settings.
    heartbeatDatastore ([`vim.Datastore`_], optional):

       The list of preferred datastores to use for storage heartbeating. Each of the specified datastores should be active and mounted by more than one host. There is no limit on the number of specified datastores and no priority among them. The specified datastores will replace those previously specified and an empty list will delete all such earlier specified ones.vCenter Server chooses the heartbeat datastores for a host from the set specified by `hBDatastoreCandidatePolicy`_ . The choice is made based on datastore connectivity and storage array redundancy (in case of VMFS).The final set of selected heartbeat datastores is reported via `heartbeatDatastoreInfo`_ .
    hBDatastoreCandidatePolicy (`str`_, optional):

       The policy on what datastores will be used by vCenter Server to choose heartbeat datastores. See `ClusterDasConfigInfoHBDatastoreCandidate`_ for all options. The default value is `allFeasibleDsWithUserPreference`_ .
