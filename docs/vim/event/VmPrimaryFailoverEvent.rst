
vim.event.VmPrimaryFailoverEvent
================================
  This event records a fault tolerance failover. The reason could be : lost connection to primary, partial hardware failure of primary or by user.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    reason (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The reason for the failure. see `VirtualMachineNeedSecondaryReason <vim/VirtualMachine/NeedSecondaryReason.rst>`_ 
