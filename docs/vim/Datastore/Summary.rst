.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _type: ../../vim/host/FileSystemVolume.rst#type

.. _accessible: ../../vim/Datastore/Summary.rst#accessible

.. _DatastoreInfo: ../../vim/Datastore/Info.rst

.. _vim.Datastore: ../../vim/Datastore.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _inaccessibleReason: ../../vim/host/MountInfo.rst#inaccessibleReason

.. _RefreshDatastoreStorageInfo: ../../vim/Datastore.rst#refreshStorageInfo

.. _DatastoreSummaryMaintenanceModeState: ../../vim/Datastore/Summary/MaintenanceModeState.rst


vim.Datastore.Summary
=====================
  Summary information about the datastore. The status fields and managed object reference is not set when an object of this type is created. These fields and references are typically set later when these objects are associated with a host.
:extends: vmodl.DynamicData_

Attributes:
    datastore (`vim.Datastore`_, optional):

       The reference to the managed object.
    name (`str`_):

       The name of the datastore.
    url (`str`_):

       The unique locator for the datastore. This property is guaranteed to be valid only if `accessible`_ is true.
    capacity (`long`_):

       Maximum capacity of this datastore, in bytes. This value is updated periodically by the server. It can be explicitly refreshed with the Refresh operation. This property is guaranteed to be valid only if `accessible`_ is true.
    freeSpace (`long`_):

       Available space of this datastore, in bytes. The server periodically updates this value. It can be explicitly refreshed with the Refresh operation. This property is guaranteed to be valid only if `accessible`_ is true.
    uncommitted (`long`_, optional):

       Total additional storage space, in bytes, potentially used by all virtual machines on this datastore. The server periodically updates this value. It can be explicitly refreshed with the `RefreshDatastoreStorageInfo`_ operation. This property is valid only if `accessible`_ is true.
    accessible (`bool`_):

       The connectivity status of this datastore. If this is set to false, meaning the datastore is not accessible, this datastore's capacity and freespace properties cannot be validated. Furthermore, if this property is set to false, some of the properties in this summary and in `DatastoreInfo`_ should not be used. Refer to the documentation for the property of your interest. For datastores accessed from multiple hosts, vCenter Server reports `accessible`_ as an aggregated value of the properties reported in MountInfo. For instance, if a datastore is accessible through a subset of hosts, then the value of `accessible`_ will be reported as true by vCenter Server. And the reason for a daastore being inaccessible from a host will be reported in `inaccessibleReason`_ 
    multipleHostAccess (`bool`_, optional):

       More than one host in the datacenter has been configured with access to the datastore. This is only provided by VirtualCenter.
    type (`str`_):

       Type of file system volume, such as VMFS or NFS.See `type`_ 
    maintenanceMode (`str`_, optional):

       The current maintenance mode state of the datastore. The set of possible values is described in `DatastoreSummaryMaintenanceModeState`_ .
