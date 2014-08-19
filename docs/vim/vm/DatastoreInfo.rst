
vim.vm.DatastoreInfo
====================
  DatastoreInfo describes a datastore that a virtual disk can be stored on.
:extends: vim.vm.TargetInfo_

Attributes:
    datastore (`vim.Datastore.Summary <vim/Datastore/Summary.rst>`_):

       Information about the datastore
    capability (`vim.Datastore.Capability <vim/Datastore/Capability.rst>`_):

       Information about the datastore capabilities
    maxFileSize (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The maximum size of a file that can reside on this datastore.
    maxVirtualDiskCapacity (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The maximum capacity of a virtual disk which can be created on this volume
    mode (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Access mode for this datastore. This is either readOnly or readWrite. A virtual disk needs to be stored on readWrite datastore. ISOs can be read from a readOnly datastore.See `HostMountMode <vim/host/MountInfo/AccessMode.rst>`_ 
    vStorageSupport (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicate the states of vStorage hardware acceleration support for this datastore.See `FileSystemMountInfoVStorageSupportStatus <vim/host/FileSystemMountInfo/VStorageSupportStatus.rst>`_ 
