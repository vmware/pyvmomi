.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.event.LicenseEvent: ../../vim/event/LicenseEvent.rst


vim.event.AllVirtualMachinesLicensedEvent
=========================================
  This event records that the previously unlicensed virtual machines on the specified host are now licensed. After this event is entered into the event log, we expect to see that the (@link vim.event.Event.UnlicensedVirtualMachinesEvent UnlicensedVirtualMachinesEvent) (@link vim.ManagedEntity.configIssue configIssue) is removed from the host.
:extends: vim.event.LicenseEvent_
:since: `VI API 2.5`_

Attributes:
