.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.VmInstanceUuidAssignedEvent
=====================================
  This event records the assignment of a new instance UUID to a virtual machine.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0`_

Attributes:
    instanceUuid (`str`_):

       The new instance UUID.
