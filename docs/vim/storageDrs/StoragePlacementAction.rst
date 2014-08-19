
vim.storageDrs.StoragePlacementAction
=====================================
  Describes a single storage initial placement action for placing a virtual machine or a set of virtual disks on a datastore.
:extends: vim.cluster.Action_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_, optional):

       Virtual machine reference. It is possible that the VM has not been created, in which case, this property is left unset.
    relocateSpec (`vim.vm.RelocateSpec <vim/vm/RelocateSpec.rst>`_):

       Specification for placing a virtual machine or a set of virtual disks to a datastore.
    destination (`vim.Datastore <vim/Datastore.rst>`_):

       Target datastore.
    spaceUtilBefore (`float <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Current space utilization on the target datastore. Unit: percentage. For example, if set to 70.0, space utilization is 70%. If not set, the value is not available.
    spaceUtilAfter (`float <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Expected space utilization on the target datastore after placing the virtual disk. Unit: percentage. For example, if set to 70.0, space utilization is 70%. If not set, the value is not available.
    ioLatencyBefore (`float <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Current I/O latency on the target datastore. Unit: millisecond. If not set, the value is not available.
