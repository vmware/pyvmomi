
vim.event.MigrationEvent
========================
  These are events used to describe migration warning and errors
:extends: vim.event.VmEvent_

Attributes:
    fault (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

       The fault that describes the migration issue. This is typically either a MigrationFault or a VmConfigFault.
