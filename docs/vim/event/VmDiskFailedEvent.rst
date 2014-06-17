.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst


vim.event.VmDiskFailedEvent
===========================
  This event records a failure to create a virtual disk in a virtual machine.
:extends: vim.event.VmEvent_

Attributes:
    disk (`str`_):

       The name of the virtual disk.
    reason (`vmodl.LocalizedMethodFault`_):

       The reason for the failure.
