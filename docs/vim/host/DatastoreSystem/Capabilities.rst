.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.DatastoreSystem.Capabilities
=====================================
  Capability vector indicating the available product features.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    nfsMountCreationRequired (`bool`_):

       Indicates whether mounting the NFS volume is required to be done as part of NAS datastore creation. If this is set to true, then NAS datastores cannot be created for currently mounted NFS volumes.
    nfsMountCreationSupported (`bool`_):

       Indicates whether mounting an NFS volume is supported when a NAS datastore is created. If this option is false, then NAS datastores corresponding to NFS volumes can be created only for already mounted NFS volumes.
    localDatastoreSupported (`bool`_):

       Indicates whether local datastores are supported.
    vmfsExtentExpansionSupported (`bool`_):

       Indicates whether vmfs extent expansion is supported.
