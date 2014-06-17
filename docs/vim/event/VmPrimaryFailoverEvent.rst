.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _VirtualMachineNeedSecondaryReason: ../../vim/VirtualMachine/NeedSecondaryReason.rst


vim.event.VmPrimaryFailoverEvent
================================
  This event records a fault tolerance failover. The reason could be : lost connection to primary, partial hardware failure of primary or by user.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0`_

Attributes:
    reason (`str`_, optional):

       The reason for the failure. see `VirtualMachineNeedSecondaryReason`_ 
