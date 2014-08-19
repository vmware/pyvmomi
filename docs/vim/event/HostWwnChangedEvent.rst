
vim.event.HostWwnChangedEvent
=============================
  This event records a change in a host's WWN (World Wide Name).
:extends: vim.event.HostEvent_
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
