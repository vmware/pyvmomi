
vim.event.HostEnableAdminFailedEvent
====================================
  This event records the failure to restore some of the administrator's permissions.
:extends: vim.event.HostEvent_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    permissions ([`vim.AuthorizationManager.Permission <vim/AuthorizationManager/Permission.rst>`_]):

