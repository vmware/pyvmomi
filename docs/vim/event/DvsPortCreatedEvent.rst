
vim.event.DvsPortCreatedEvent
=============================
  New ports are created in the distributed virtual switch.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    portKey ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       The key of the ports that are created.
