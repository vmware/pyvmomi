
vim.host.Summary
================
  This data object type encapsulates a typical set of host information that is useful for list views and summary pages.VirtualCenter can retrieve this information very efficiently, even for a large set of hosts.
:extends: vmodl.DynamicData_

Attributes:
    host (`vim.HostSystem <vim/HostSystem.rst>`_, optional):

       The reference to the host-managed object.
    hardware (`vim.host.Summary.HardwareSummary <vim/host/Summary/HardwareSummary.rst>`_, optional):

       Basic hardware information, if known.
    runtime (`vim.host.RuntimeInfo <vim/host/RuntimeInfo.rst>`_, optional):

       Basic runtime information, if known.
    config (`vim.host.Summary.ConfigSummary <vim/host/Summary/ConfigSummary.rst>`_):

       Basic configuration information, if known.
    quickStats (`vim.host.Summary.QuickStats <vim/host/Summary/QuickStats.rst>`_):

       Basic host statistics.
    overallStatus (`vim.ManagedEntity.Status <vim/ManagedEntity/Status.rst>`_):

       The overall alarm status of the host. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.
    rebootRequired (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether or not the host requires a reboot due to a configuration change.
    customValue ([`vim.CustomFieldsManager.Value <vim/CustomFieldsManager/Value.rst>`_], optional):

       The customized field values.
    managementServerIp (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       IP address of the VirtualCenter server managing this host, if any.
    maxEVCModeKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The most capable Enhanced VMotion Compatibility mode supported by the host hardware and software; unset if this host cannot participate in any EVC mode.See `supportedEVCMode <vim/Capability.rst#supportedEVCMode>`_ 
    currentEVCModeKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The Enhanced VMotion Compatibility mode that is currently in effect for this host. If the host is in a cluster where EVC is active, this will match the cluster's EVC mode; otherwise this will be unset.See `supportedEVCMode <vim/Capability.rst#supportedEVCMode>`_ 
