
vim.event.DvsPortBlockedEvent
=============================
  A port is blocked in the distributed virtual switch.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    portKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The port key.
    statusDetail (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Reason for port's current status
    runtimeInfo (`vim.dvs.DistributedVirtualPort.RuntimeInfo <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst>`_, optional):

       The port runtime information.
