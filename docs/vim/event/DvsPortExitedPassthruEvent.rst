
vim.event.DvsPortExitedPassthruEvent
====================================
  A port has exited passthrough mode on the distributed virtual switch.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    portKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The port key.
    runtimeInfo (`vim.dvs.DistributedVirtualPort.RuntimeInfo <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst>`_, optional):

       The port runtime information.
