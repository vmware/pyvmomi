.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _DatastoreNamespaceManager: ../../vim/DatastoreNamespaceManager.rst


vim.Datastore.Capability
========================
  Information about the capabilities of this datastore.
:extends: vmodl.DynamicData_

Attributes:
    directoryHierarchySupported (`bool`_):

       Indicates whether or not directories can be created on this datastore.
    rawDiskMappingsSupported (`bool`_):

       Indicates whether or not raw disk mappings can be created on this datastore.
    perFileThinProvisioningSupported (`bool`_):

       Indicates whether or not the datastore supports thin provisioning on a per file basis. When thin provisioning is used, backing storage is lazily allocated.This is supported by VMFS3. VMFS2 always allocates storage eagerly. Thus, this value is false for VMFS2. Most NAS systems always use thin provisioning. They do not support configuring this on a per file basis, so for NAS systems this value is also false.
    storageIORMSupported (`bool`_):

       Indicates whether the datastore supports Storage I/O Resource Management.
    nativeSnapshotSupported (`bool`_):

       Indicates whether the datastore supports native snapshot feature which is based on Copy-On-Write.
    topLevelDirectoryCreateSupported (`bool`_, optional):

       Indicates whether the datastore supports traditional top-level directory creation.See `DatastoreNamespaceManager`_ 
    seSparseSupported (`bool`_, optional):

       Indicates whether the datastore supports the Flex-SE(SeSparse) feature.
