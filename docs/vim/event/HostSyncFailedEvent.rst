
vim.event.HostSyncFailedEvent
=============================
  This event records a failure to sync up with the VirtualCenter agent on the host
:extends: vim.event.HostEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    reason (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

       The reason for the failure.
