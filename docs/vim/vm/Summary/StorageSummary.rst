.. _long: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _committed: ../../../vim/vm/StorageInfo/UsageOnDatastore.rst#committed

.. _uncommitted: ../../../vim/vm/StorageInfo/UsageOnDatastore.rst#uncommitted

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _VirtualMachineStorageInfo: ../../../vim/vm/StorageInfo.rst


vim.vm.Summary.StorageSummary
=============================
  A subset of the storage information of this virtual machine.See `VirtualMachineStorageInfo`_ for a detailed storage break-up.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    committed (`long`_):

       Total storage space, in bytes, committed to this virtual machine across all datastores.Essentially an aggregate of the property `committed`_ across all datastores that this virtual machine is located on.
    uncommitted (`long`_):

       Additional storage space, in bytes, potentially used by this virtual machine on all datastores.Essentially an aggregate of the property `uncommitted`_ across all datastores that this virtual machine is located on.
    unshared (`long`_):

       Total storage space, in bytes, occupied by the virtual machine across all datastores, that is not shared with any other virtual machine.
    timestamp (`datetime`_):

       Time when values in this structure were last updated.
