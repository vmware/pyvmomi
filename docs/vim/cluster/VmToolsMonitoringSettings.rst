.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _dasSettings: ../../vim/cluster/DasVmConfigInfo.rst#dasSettings

.. _maxFailures: ../../vim/cluster/VmToolsMonitoringSettings.rst#maxFailures

.. _vmMonitoring: ../../vim/cluster/DasConfigInfo.rst#vmMonitoring

.. _clusterSettings: ../../vim/cluster/VmToolsMonitoringSettings.rst#clusterSettings

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _maxFailureWindow: ../../vim/cluster/VmToolsMonitoringSettings.rst#maxFailureWindow

.. _defaultVmSettings: ../../vim/cluster/DasConfigInfo.rst#defaultVmSettings

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _ClusterDasConfigInfo: ../../vim/cluster/DasConfigInfo.rst

.. _ClusterDasVmConfigInfo: ../../vim/cluster/DasVmConfigInfo.rst

.. _vmToolsMonitoringSettings: ../../vim/cluster/DasVmSettings.rst#vmToolsMonitoringSettings

.. _ClusterVmToolsMonitoringSettings: ../../vim/cluster/VmToolsMonitoringSettings.rst

.. _ClusterDasConfigInfoVmMonitoringState: ../../vim/cluster/DasConfigInfo/VmMonitoringState.rst


vim.cluster.VmToolsMonitoringSettings
=====================================
  The `ClusterVmToolsMonitoringSettings`_ data object contains virtual machine monitoring settings that are used by the Virtual Machine Health Monitoring Service. The Service checks the VMware Tools heartbeat of a virtual machine. If heartbeats have not been received within a specified time interval, the Service declares the virtual machine as failed and resets the virtual machine.These settings are applied to individual virtual machines during cluster reconfiguration ( `ClusterDasVmConfigInfo`_ . `dasSettings`_ . `vmToolsMonitoringSettings`_ ). You can also specify them as default values ( `ClusterDasConfigInfo`_ . `defaultVmSettings`_ ).All fields are optional. In case of a reconfiguration, fields left unset are not changed.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    enabled (`bool`_, optional):

       Flag indicating whether or not the Virtual Machine Health Monitoring service is enabled.The Server does not use this property.
    vmMonitoring (`str`_, optional):

       Indicates the type of virtual machine monitoring. Specify a string value corresponding to one of the following `ClusterDasConfigInfoVmMonitoringState`_ values:
        * vmMonitoringDisabled
        * (the default value)
        * vmMonitoringOnly
        * vmAndAppMonitoringThe individual VMware Tools setting for virtual machine monitoring depends on the HA Virtual Machine Health Monitoring Service level that is defined for the cluster ( `ClusterDasConfigInfo`_ . `vmMonitoring`_ ). The following list indicates the supported VMware ToolsvmMonitoringvalues according to the cluster configuration.
        * If the cluster configuration specifies
        * vmMonitoringDisabled
        * , the Service is disabled and the HA Service ignores the VMware Tools monitoring setting.
        * If the cluster configuration specifies
        * vmMonitoringOnly
        * , the Service supports
        * vmMonitoringOnly
        * or
        * vmMonitoringDisabled
        * only.
        * If the cluster configuration specifies
        * vmAndAppMonitoring
        * , you can use any of the
        * `ClusterDasConfigInfoVmMonitoringState`_
        * values.The `clusterSettings`_ value has no effect on the constraint imposed by the HA Virtual Machine Health Monitoring Service level that is defined for the cluster ( `ClusterDasConfigInfo`_ . `vmMonitoring`_ ).Application monitoring events are generated regardless of the currently configured type of virtual machine monitoring. You can use these events even if monitoring is being disabled or set tovmMonitoringOnly.
    clusterSettings (`bool`_, optional):

       Flag indicating whether to use the cluster settings or the per VM settings.The default value is true.
    failureInterval (`int`_, optional):

       If no heartbeat has been received for at least the specified number of seconds, the virtual machine is declared as failed.The default value is 30.
    minUpTime (`int`_, optional):

       The number of seconds for the virtual machine's heartbeats to stabilize after the virtual machine has been powered on. This time should include the guest operating system boot-up time. The virtual machine monitoring will begin only after this period.The default value is 120.
    maxFailures (`int`_, optional):

       Maximum number of failures and automated resets allowed during the time that `maxFailureWindow`_ specifies. If `maxFailureWindow`_ is -1 (no window), this represents the absolute number of failures after which automated response is stopped.If a virtual machine exceeds this threshold, in-depth problem analysis is usually needed.The default value is 3.
    maxFailureWindow (`int`_, optional):

       The number of seconds for the window during which up to `maxFailures`_ resets can occur before automated responses stop.If set to -1, no failure window is specified.The default value is -1.
