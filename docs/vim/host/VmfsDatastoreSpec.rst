.. _str: https://docs.python.org/2/library/stdtypes.html

.. _uuid: ../../vim/host/ScsiLun.rst#uuid

.. _HostScsiDisk: ../../vim/host/ScsiDisk.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.host.VmfsDatastoreSpec
==========================
  Base class for VMFS datastore addition specification. Used as a generic way to point to one of the creation specifications that can be used to apply a specification to effect the creation or extension of a VMFS datastore.
:extends: vmodl.DynamicData_

Attributes:
    diskUuid (`str`_):

       The UUID of the SCSI disk on which the VMFS datastore is located.See `HostScsiDisk`_ See `uuid`_ 
