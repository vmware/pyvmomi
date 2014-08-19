
vim.event.EnteringMaintenanceModeEvent
======================================
  This event records that a host has begun the process of entering maintenance mode. All virtual machine operations are blocked, except the following:
   * MigrateVM
   * PowerOffVM
   * SuspendVM
   * ShutdownGuest
   * StandbyGuest
   * 
:extends: vim.event.HostEvent_

Attributes:
