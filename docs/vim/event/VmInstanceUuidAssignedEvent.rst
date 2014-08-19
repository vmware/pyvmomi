
vim.event.VmInstanceUuidAssignedEvent
=====================================
  This event records the assignment of a new instance UUID to a virtual machine.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    instanceUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The new instance UUID.
