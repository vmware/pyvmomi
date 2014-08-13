.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.HostSystem: ../../vim/HostSystem.rst

.. _supportedEVCMode: ../../vim/Capability.rst#supportedEVCMode

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.RuntimeInfo: ../../vim/host/RuntimeInfo.rst

.. _vim.ManagedEntity.Status: ../../vim/ManagedEntity/Status.rst

.. _vim.host.Summary.QuickStats: ../../vim/host/Summary/QuickStats.rst

.. _vim.CustomFieldsManager.Value: ../../vim/CustomFieldsManager/Value.rst

.. _vim.host.Summary.ConfigSummary: ../../vim/host/Summary/ConfigSummary.rst

.. _vim.host.Summary.HardwareSummary: ../../vim/host/Summary/HardwareSummary.rst


vim.host.Summary
================
  This data object type encapsulates a typical set of host information that is useful for list views and summary pages.VirtualCenter can retrieve this information very efficiently, even for a large set of hosts.
:extends: vmodl.DynamicData_

Attributes:
    host (`vim.HostSystem`_, optional):

       The reference to the host-managed object.
    hardware (`vim.host.Summary.HardwareSummary`_, optional):

       Basic hardware information, if known.
    runtime (`vim.host.RuntimeInfo`_, optional):

       Basic runtime information, if known.
    config (`vim.host.Summary.ConfigSummary`_):

       Basic configuration information, if known.
    quickStats (`vim.host.Summary.QuickStats`_):

       Basic host statistics.
    overallStatus (`vim.ManagedEntity.Status`_):

       The overall alarm status of the host. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.
    rebootRequired (`bool`_):

       Indicates whether or not the host requires a reboot due to a configuration change.
    customValue ([`vim.CustomFieldsManager.Value`_], optional):

       The customized field values.
    managementServerIp (`str`_, optional):

       IP address of the VirtualCenter server managing this host, if any.
    maxEVCModeKey (`str`_, optional):

       The most capable Enhanced VMotion Compatibility mode supported by the host hardware and software; unset if this host cannot participate in any EVC mode.See `supportedEVCMode`_ 
    currentEVCModeKey (`str`_, optional):

       The Enhanced VMotion Compatibility mode that is currently in effect for this host. If the host is in a cluster where EVC is active, this will match the cluster's EVC mode; otherwise this will be unset.See `supportedEVCMode`_ 
