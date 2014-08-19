
vim.event.VmDiskFailedEvent
===========================
  This event records a failure to create a virtual disk in a virtual machine.
:extends: vim.event.VmEvent_

Attributes:
    disk (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the virtual disk.
    reason (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

       The reason for the failure.
