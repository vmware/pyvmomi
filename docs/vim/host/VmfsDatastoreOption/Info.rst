.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.DiskPartitionInfo.Layout: ../../../vim/host/DiskPartitionInfo/Layout.rst

.. _HostDiskPartitionInfoPartitionFormat: ../../../vim/host/DiskPartitionInfo/PartitionFormat.rst


vim.host.VmfsDatastoreOption.Info
=================================
  Base class that describes a VMFS datastore provisioning option.
:extends: vmodl.DynamicData_

Attributes:
    layout (`vim.host.DiskPartitionInfo.Layout`_):

       The partition table layout that the disk will have if this provisioning option is selected. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.
    partitionFormatChange (`bool`_, optional):

       Indicates whether selecting this option will change the partition format type on the disk.See `HostDiskPartitionInfoPartitionFormat`_ 
