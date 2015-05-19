.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.event.HostEvent: ../../vim/event/HostEvent.rst

.. _vim.AuthorizationManager.Permission: ../../vim/AuthorizationManager/Permission.rst


vim.event.HostEnableAdminFailedEvent
====================================
  This event records the failure to restore some of the administrator's permissions.
:extends: vim.event.HostEvent_
:since: `VI API 2.5`_

Attributes:
    permissions ([`vim.AuthorizationManager.Permission`_]):

