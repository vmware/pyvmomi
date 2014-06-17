.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.HttpNfcLease.DeviceUrl
==========================
  Provides a mapping from logical device IDs to upload/download URLs.For export, a single device id is returned based on the object identifiers for the objects.For import, two device ids are returned. One based on the object names used in the ImportSpec, and one based on the object identifiers for the created objects. This is immutable and would match the id if an ExportLease is latter created.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    key (`str`_):

       The immutable identifier for the device. This is set for both import/export leases.
    importKey (`str`_):

       Identifies the device based on the names in an ImportSpec. This is only set for import leases.
    url (`str`_):

    sslThumbprint (`str`_):

       SSL thumbprint for the host the URL refers to. Empty if no SSL thumbprint is available or needed.
    disk (`bool`_, optional):

       Optional value to specify if the attached file is a disk in vmdk format.
    targetId (`str`_, optional):

       Id for this target. This only used for multi-POSTing, where a single HTTP POST is applied to multiple targets.
    datastoreKey (`str`_, optional):

       Key for the datastore this disk is on. This is used to look up hosts which can be used to multi-POST disk contents, in the host map of the lease.
    fileSize (`long`_, optional):

       Specifies the size of the file backing for this device. This property is only set for non-disk file backings.
