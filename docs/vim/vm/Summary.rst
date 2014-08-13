.. _guest: ../../vim/VirtualMachine.rst#guest

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _RefreshStorageInfo: ../../vim/VirtualMachine.rst#refreshStorageInfo

.. _vim.VirtualMachine: ../../vim/VirtualMachine.rst

.. _vim.vm.RuntimeInfo: ../../vim/vm/RuntimeInfo.rst

.. _vim.ManagedEntity.Status: ../../vim/ManagedEntity/Status.rst

.. _vim.vm.Summary.QuickStats: ../../vim/vm/Summary/QuickStats.rst

.. _vim.vm.Summary.GuestSummary: ../../vim/vm/Summary/GuestSummary.rst

.. _vim.vm.Summary.ConfigSummary: ../../vim/vm/Summary/ConfigSummary.rst

.. _vim.vm.Summary.StorageSummary: ../../vim/vm/Summary/StorageSummary.rst

.. _vim.CustomFieldsManager.Value: ../../vim/CustomFieldsManager/Value.rst


vim.vm.Summary
==============
  The summary data object type encapsulates a typical set of virtual machine information that is useful for list views and summary pages.VirtualCenter can retrieve this information very efficiently, even for large sets of virtual machines.
:extends: vmodl.DynamicData_

Attributes:
    vm (`vim.VirtualMachine`_, optional):

       Reference to the virtual machine managed object.
    runtime (`vim.vm.RuntimeInfo`_):

       Runtime and state information of a running virtual machine. Most of this information is also available when a virtual machine is powered off. In that case, it contains information from the last run, if available.
    guest (`vim.vm.Summary.GuestSummary`_, optional):

       Guest operating system and VMware Tools information. See `guest`_ for more information.
    config (`vim.vm.Summary.ConfigSummary`_):

       Basic configuration information about the virtual machine. This information is not available when the virtual machine is unavailable, for instance, when it is being created or deleted.
    storage (`vim.vm.Summary.StorageSummary`_, optional):

       Storage information of the virtual machine. It can be explicitly refreshed with the `RefreshStorageInfo`_ operation. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.
    quickStats (`vim.vm.Summary.QuickStats`_):

       A set of statistics that are typically updated with near real-time regularity. This data object type does not support notification, for scalability reasons. Therefore, changes in QuickStats do not generate property collector updates. To monitor statistics values, use the statistics and alarms modules instead.
    overallStatus (`vim.ManagedEntity.Status`_):

       Overall alarm status on this node. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.
    customValue ([`vim.CustomFieldsManager.Value`_], optional):

       Custom field values.
