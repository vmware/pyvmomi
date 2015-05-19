.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.VmfsDatastoreSpec: ../../vim/host/VmfsDatastoreSpec.rst

.. _vim.host.VmfsDatastoreOption.Info: ../../vim/host/VmfsDatastoreOption/Info.rst


vim.host.VmfsDatastoreOption
============================
  VMFS datastore provisioning option that can be applied on a disk. VMFS datastores can be created or have their capacity increased using storage from a disk. There are often multiple ways in which extents can be allocated on a disk. Each instance of this structure represents one of the possible options that can be applied to provisiong VMFS datastore storage. Only options that follow ESX Server best practice guidelines will be presented.
:extends: vmodl.DynamicData_

Attributes:
    info (`vim.host.VmfsDatastoreOption.Info`_):

       Information about this VMFS datastore provisioniing option. This structure describes the extent allocation policy represented by this option.
    spec (`vim.host.VmfsDatastoreSpec`_):

       Specification to create or increase the capacity of a VMFS datastore. This property contains a configuration specification that can be applied to effect the creation or capacity increase.
