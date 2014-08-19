
vim.event.HostLocalPortCreatedEvent
===================================
  This event records when host local port is created to recover from management network connectivity loss.
:extends: vim.event.DvsEvent_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    hostLocalPort (`vim.dvs.DistributedVirtualPort.HostLocalPortInfo <vim/dvs/DistributedVirtualPort/HostLocalPortInfo.rst>`_):

       The configuration of the new host local port.
