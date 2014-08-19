
vim.event.UplinkPortMtuNotSupportEvent
======================================
  Mtu health check status of an uplink port is changed, and in the latest mtu health check, not all the vlans' MTU setting on physical switch allows vSphere Distributed Switch max MTU size packets passing.
:extends: vim.event.DvsHealthStatusChangeEvent_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
