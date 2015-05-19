.. _int: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.event.LicenseEvent: ../../vim/event/LicenseEvent.rst


vim.event.UnlicensedVirtualMachinesEvent
========================================
  This event records that we have unlicensed virtual machines on the specified host. This can be both a (@link vim.ManagedEntity.configIssue configIssue) and an entry in the event log.
:extends: vim.event.LicenseEvent_
:since: `VI API 2.5`_

Attributes:
    unlicensed (`int`_):

    available (`int`_):

