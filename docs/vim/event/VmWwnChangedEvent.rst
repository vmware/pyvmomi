.. _long: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.VmWwnChangedEvent
===========================
  This event records a change in a virtual machine's WWN (World Wide Name).
:extends: vim.event.VmEvent_
:since: `VI API 2.5`_

Attributes:
    oldNodeWwns (`long`_, optional):

       The old node WWN.
    oldPortWwns (`long`_, optional):

       The old port WWN.
    newNodeWwns (`long`_, optional):

       The new node WWN.
    newPortWwns (`long`_, optional):

       The new port WWN.
