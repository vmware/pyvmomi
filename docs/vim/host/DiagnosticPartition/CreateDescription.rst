
vim.host.DiagnosticPartition.CreateDescription
==============================================
  The diagnostic partition create description details what will be done to create a new diagnostic partition on a disk. It contains a CreateSpec that can be submitted to create the partition and information that can be shown to the user.
:extends: vmodl.DynamicData_

Attributes:
    layout (`vim.host.DiskPartitionInfo.Layout <vim/host/DiskPartitionInfo/Layout.rst>`_):

       Layout describing the format of the disk In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.
    diskUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The UUID of the SCSI disk on which to create the diagnostic partition. This disk UUID will match that found in the identification field of the creation spec.See `HostScsiDisk <vim/host/ScsiDisk.rst>`_ See `uuid <vim/host/ScsiLun.rst#uuid>`_ 
    spec (`vim.host.DiagnosticPartition.CreateSpec <vim/host/DiagnosticPartition/CreateSpec.rst>`_):

       Creation specification for diagnostic partition
