.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vim.Datastore: ../../../vim/Datastore.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _VirtualMachineFileLayoutEx: ../../../vim/vm/FileLayoutEx.rst


vim.vm.StorageInfo.UsageOnDatastore
===================================
  Storage space used by this virtual machine on a particular datastore.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    datastore (`vim.Datastore`_):

       Reference to datastore for which information is being provided.
    committed (`long`_):

       Storage space, in bytes, on this datastore that is actually being used by the virtual machine.It includes space actually occupied by disks, logs, snapshots, configuration files etc. Files of the virtual machine which are present on a different datastore (e.g. a virtual disk on another datastore) are not included here. `VirtualMachineFileLayoutEx`_ provides a detailed break-up of the committed space.
    uncommitted (`long`_):

       Additional storage space, in bytes, potentially used by the virtual machine on this datastore.Additional space may be needed for example when lazily allocated disks grow, or storage for swap is allocated when powering on the virtual machine.If the virtual machine is running off delta disks (for example because a snapshot was taken), then only the potential growth of the currently used delta-disks is considered.
    unshared (`long`_):

       Storage space, in bytes, occupied by the virtual machine on this datastore that is not shared with any other virtual machine.
