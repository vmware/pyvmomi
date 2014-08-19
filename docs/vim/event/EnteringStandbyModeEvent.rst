
vim.event.EnteringStandbyModeEvent
==================================
  This event records that a host has begun the process of entering standby mode. All virtual machine operations are blocked, except the following:
   * MigrateVM
   * PowerOffVM
   * SuspendVM
   * ShutdownGuest
   * StandbyGuest
   * 
:extends: vim.event.HostEvent_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
