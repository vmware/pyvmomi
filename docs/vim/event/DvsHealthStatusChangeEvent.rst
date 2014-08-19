
vim.event.DvsHealthStatusChangeEvent
====================================
  Health check status of an switch is changed.
:extends: vim.event.HostEvent_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    switchUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       UUID of the DVS the host is connected to.
    healthResult (`vim.dvs.HostMember.HealthCheckResult <vim/dvs/HostMember/HealthCheckResult.rst>`_, optional):

       Health check status.
