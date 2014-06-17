.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.vm.MetadataManager.VmMetadata
=================================
  VmMetadata is a pair of VM ID and opaque metadata.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    vmId (`str`_):

       Datastore URL-based ID for VM, for example, "[datastore1] SomeVM/SomeVM.vmx".
    metadata (`str`_, optional):

       Opaque metadata for the VM identified by vmId. If no value is supplied, the entry for this VM is removed.
