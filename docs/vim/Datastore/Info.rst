
vim.Datastore.Info
==================
  Detailed information about a datastore. This is a base type for derived types that have more specific details about a datastore.See `HostVmfsVolume <vim/host/VmfsVolume.rst>`_ See `HostNasVolume <vim/host/NasVolume.rst>`_ See `HostLocalFileSystemVolume <vim/host/LocalFileSystemVolume.rst>`_ 
:extends: vmodl.DynamicData_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the datastore.
    url (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The unique locator for the datastore.
    freeSpace (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Free space of this datastore, in bytes. The server periodically updates this value. It can be explicitly refreshed with the Refresh operation.
    maxFileSize (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The maximum size of a file that can reside on this file system volume.
    maxVirtualDiskCapacity (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The maximum capacity of a virtual disk which can be created on this volume.
    timestamp (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Time when the free-space and capacity values in `DatastoreInfo <vim/Datastore/Info.rst>`_ and `DatastoreSummary <vim/Datastore/Summary.rst>`_ were updated.
    containerId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The unique container ID of the datastore, if applicable.
