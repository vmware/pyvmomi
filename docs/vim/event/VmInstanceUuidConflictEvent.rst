.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vim.event.VmEventArgument: ../../vim/event/VmEventArgument.rst


vim.event.VmInstanceUuidConflictEvent
=====================================
  This event records a conflict of virtual machine instance UUIDs.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0`_

Attributes:
    conflictedVm (`vim.event.VmEventArgument`_):

       The virtual machine whose instance UUID conflicts with the current virtual machine's instance UUID.
    instanceUuid (`str`_):

       The instance UUID in conflict.
