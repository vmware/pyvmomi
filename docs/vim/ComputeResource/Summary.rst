.. _int: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _short: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.ManagedEntity.Status: ../../vim/ManagedEntity/Status.rst


vim.ComputeResource.Summary
===========================
  This data object type encapsulates a typical set of ComputeResource information that is useful for list views and summary pages.
:extends: vmodl.DynamicData_

Attributes:
    totalCpu (`int`_):

       Aggregated CPU resources of all hosts, in MHz.
    totalMemory (`long`_):

       Aggregated memory resources of all hosts, in bytes.
    numCpuCores (`short`_):

       Number of physical CPU cores. Physical CPU cores are the processors contained by a CPU package.
    numCpuThreads (`short`_):

       Aggregated number of CPU threads.
    effectiveCpu (`int`_):

       Effective CPU resources (in MHz) available to run virtual machines. This is the aggregated effective resource level from all running hosts. Hosts that are in maintenance mode or are unresponsive are not counted. Resources used by the VMware Service Console are not included in the aggregate. This value represents the amount of resources available for the root resource pool for running virtual machines.
    effectiveMemory (`long`_):

       Effective memory resources (in MB) available to run virtual machines. This is the aggregated effective resource level from all running hosts. Hosts that are in maintenance mode or are unresponsive are not counted. Resources used by the VMware Service Console are not included in the aggregate. This value represents the amount of resources available for the root resource pool for running virtual machines.
    numHosts (`int`_):

       Total number of hosts.
    numEffectiveHosts (`int`_):

       Total number of effective hosts.
    overallStatus (`vim.ManagedEntity.Status`_):

       Overall alarm status. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.
