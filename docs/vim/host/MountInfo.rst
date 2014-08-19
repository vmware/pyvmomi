
vim.host.MountInfo
==================
  The `HostMountInfo <vim/host/MountInfo.rst>`_ data object provides information related to a configured mount point. This object does not include information about the mounted file system. (See `HostFileSystemMountInfo <vim/host/FileSystemMountInfo.rst>`_ .)
:extends: vmodl.DynamicData_

Attributes:
    path (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Local file path where file system volume is mounted, if applicable. This path identifies the file system volume from the point of view of the host.
    accessMode (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Access mode to the underlying file system for this host.
    mounted (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The mount state of this mount point. For a discovered volume, which is mounted, this is true. When this value is unset, the default value is true.
    accessible (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag that indicates if the datastore is currently accessible from the host.For the case of a standalone host, this property has the same value as `DatastoreSummary <vim/Datastore/Summary.rst>`_ . `accessible <vim/Datastore/Summary.rst#accessible>`_ . You can use the `DatastoreSummary <vim/Datastore/Summary.rst>`_ property if the `HostMountInfo <vim/host/MountInfo.rst>`_ property is not set. The VirtualCenter Server will always make sure the `DatastoreSummary <vim/Datastore/Summary.rst>`_ property is set correctly.
    inaccessibleReason (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       This optional property for inaccessible reason is reported only if a datastore becomes inaccessible as reported by `accessible <vim/host/MountInfo.rst#accessible>`_ and `DatastoreSummary <vim/Datastore/Summary.rst>`_ . `accessible <vim/Datastore/Summary.rst#accessible>`_ . The values for inaccessible reason are defined in the enum InaccessibleReason This helps to determine host specific reason for datastore inaccessibility. If the datastore becomes accessible following an inaccessible condition, the property `inaccessibleReason <vim/host/MountInfo.rst#inaccessibleReason>`_ will be unset.
