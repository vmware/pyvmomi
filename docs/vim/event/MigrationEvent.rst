.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst


vim.event.MigrationEvent
========================
  These are events used to describe migration warning and errors
:extends: vim.event.VmEvent_

Attributes:
    fault (`vmodl.LocalizedMethodFault`_):

       The fault that describes the migration issue. This is typically either a MigrationFault or a VmConfigFault.
