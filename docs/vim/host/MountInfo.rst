.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _accessible: ../../vim/Datastore/Summary.rst#accessible

.. _HostMountInfo: ../../vim/host/MountInfo.rst

.. _DatastoreSummary: ../../vim/Datastore/Summary.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _inaccessibleReason: ../../vim/host/MountInfo.rst#inaccessibleReason

.. _HostFileSystemMountInfo: ../../vim/host/FileSystemMountInfo.rst


vim.host.MountInfo
==================
  The `HostMountInfo`_ data object provides information related to a configured mount point. This object does not include information about the mounted file system. (See `HostFileSystemMountInfo`_ .)
:extends: vmodl.DynamicData_

Attributes:
    path (`str`_, optional):

       Local file path where file system volume is mounted, if applicable. This path identifies the file system volume from the point of view of the host.
    accessMode (`str`_):

       Access mode to the underlying file system for this host.
    mounted (`bool`_, optional):

       The mount state of this mount point. For a discovered volume, which is mounted, this is true. When this value is unset, the default value is true.
    accessible (`bool`_, optional):

       Flag that indicates if the datastore is currently accessible from the host.For the case of a standalone host, this property has the same value as `DatastoreSummary`_ . `accessible`_ . You can use the `DatastoreSummary`_ property if the `HostMountInfo`_ property is not set. The VirtualCenter Server will always make sure the `DatastoreSummary`_ property is set correctly.
    inaccessibleReason (`str`_, optional):

       This optional property for inaccessible reason is reported only if a datastore becomes inaccessible as reported by `accessible`_ and `DatastoreSummary`_ . `accessible`_ . The values for inaccessible reason are defined in the enum InaccessibleReason This helps to determine host specific reason for datastore inaccessibility. If the datastore becomes accessible following an inaccessible condition, the property `inaccessibleReason`_ will be unset.
