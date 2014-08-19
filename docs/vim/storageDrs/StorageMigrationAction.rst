
vim.storageDrs.StorageMigrationAction
=====================================
  Describes a single storage migration action. The storage migration action applies either to a virtual machine or a set of virtual disks.
:extends: vim.cluster.Action_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):

       Virtual machine reference.
    relocateSpec (`vim.vm.RelocateSpec <vim/vm/RelocateSpec.rst>`_):

       Specification for moving a virtual machine or a set of virtual disks to a different datastore.
    source (`vim.Datastore <vim/Datastore.rst>`_):

       Source datastore.
    destination (`vim.Datastore <vim/Datastore.rst>`_):

       Destination datastore.
    sizeTransferred (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The amount of data to be transferred. Unit: KB.
    spaceUtilSrcBefore (`float <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Space utilization on the source datastore before storage migration. Unit: percentage. For example, if set to 70.0, space utilization is 70%. If not set, the value is not available.
    spaceUtilDstBefore (`float <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Space utilization on the destination datastore before storage migration. Unit: percentage. For example, if set to 70.0, space utilization is 70%. If not set, the value is not available.
    spaceUtilSrcAfter (`float <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Expected space utilization on the source datastore after storage migration. Unit: percentage. For example, if set to 70.0, space utilization is 70%. If not set, the value is not available.
    spaceUtilDstAfter (`float <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Expected space utilization on the destination datastore after storage migration. Unit: percentage. For example, if set to 70.0, space utilization is 70%. If not set, the value is not available.
    ioLatencySrcBefore (`float <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       I/O latency on the source datastore before storage migration. Unit: millisecond. If not set, the value is not available.
    ioLatencyDstBefore (`float <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       I/O latency on the destination datastore before storage migration. Unit: millisecond. If not set, the value is not available.
