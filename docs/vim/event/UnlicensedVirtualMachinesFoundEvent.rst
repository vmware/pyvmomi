
vim.event.UnlicensedVirtualMachinesFoundEvent
=============================================
  This event records that we discovered unlicensed virtual machines on the specified host. After this event is entered into the event log, we expect to see a corresponding (@link vim.event.Event.UnlicensedVirtualMachinesEvent UnlicensedVirtualMachinesEvent) (@link vim.ManagedEntity.configIssue configIssue) on the host.
:extends: vim.event.LicenseEvent_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    available (`int <https://docs.python.org/2/library/stdtypes.html>`_):

