
vim.event.DvsPortConnectedEvent
===============================
  A port is connected in the distributed virtual switch.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    portKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The port key.
    connectee (`vim.dvs.PortConnectee <vim/dvs/PortConnectee.rst>`_, optional):

       The port's connectee.
