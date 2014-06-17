.. _float: https://docs.python.org/2/library/stdtypes.html

.. _vim.Datastore: ../../vim/Datastore.rst

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vim.cluster.Action: ../../vim/cluster/Action.rst

.. _vim.VirtualMachine: ../../vim/VirtualMachine.rst

.. _vim.vm.RelocateSpec: ../../vim/vm/RelocateSpec.rst


vim.storageDrs.StoragePlacementAction
=====================================
  Describes a single storage initial placement action for placing a virtual machine or a set of virtual disks on a datastore.
:extends: vim.cluster.Action_
:since: `vSphere API 5.0`_

Attributes:
    vm (`vim.VirtualMachine`_, optional):

       Virtual machine reference. It is possible that the VM has not been created, in which case, this property is left unset.
    relocateSpec (`vim.vm.RelocateSpec`_):

       Specification for placing a virtual machine or a set of virtual disks to a datastore.
    destination (`vim.Datastore`_):

       Target datastore.
    spaceUtilBefore (`float`_, optional):

       Current space utilization on the target datastore. Unit: percentage. For example, if set to 70.0, space utilization is 70%. If not set, the value is not available.
    spaceUtilAfter (`float`_, optional):

       Expected space utilization on the target datastore after placing the virtual disk. Unit: percentage. For example, if set to 70.0, space utilization is 70%. If not set, the value is not available.
    ioLatencyBefore (`float`_, optional):

       Current I/O latency on the target datastore. Unit: millisecond. If not set, the value is not available.
