
vim.event.VmInstanceUuidChangedEvent
====================================
  This event records a change in a virtual machine's instance UUID.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    oldInstanceUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The old instance UUID.
    newInstanceUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The new instance UUID.
