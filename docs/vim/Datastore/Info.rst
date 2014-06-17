.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _DatastoreInfo: ../../vim/Datastore/Info.rst

.. _HostNasVolume: ../../vim/host/NasVolume.rst

.. _HostVmfsVolume: ../../vim/host/VmfsVolume.rst

.. _DatastoreSummary: ../../vim/Datastore/Summary.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _HostLocalFileSystemVolume: ../../vim/host/LocalFileSystemVolume.rst


vim.Datastore.Info
==================
  Detailed information about a datastore. This is a base type for derived types that have more specific details about a datastore.See `HostVmfsVolume`_ See `HostNasVolume`_ See `HostLocalFileSystemVolume`_ 
:extends: vmodl.DynamicData_

Attributes:
    name (`str`_):

       The name of the datastore.
    url (`str`_):

       The unique locator for the datastore.
    freeSpace (`long`_):

       Free space of this datastore, in bytes. The server periodically updates this value. It can be explicitly refreshed with the Refresh operation.
    maxFileSize (`long`_):

       The maximum size of a file that can reside on this file system volume.
    maxVirtualDiskCapacity (`long`_, optional):

       The maximum capacity of a virtual disk which can be created on this volume.
    timestamp (`datetime`_, optional):

       Time when the free-space and capacity values in `DatastoreInfo`_ and `DatastoreSummary`_ were updated.
    containerId (`str`_, optional):

       The unique container ID of the datastore, if applicable.
