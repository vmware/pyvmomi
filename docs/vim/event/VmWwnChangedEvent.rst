
vim.event.VmWwnChangedEvent
===========================
  This event records a change in a virtual machine's WWN (World Wide Name).
:extends: vim.event.VmEvent_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    oldNodeWwns ([`long <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The old node WWN.
    oldPortWwns ([`long <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The old port WWN.
    newNodeWwns ([`long <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The new node WWN.
    newPortWwns ([`long <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The new port WWN.
