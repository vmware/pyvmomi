.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.CustomizationEvent
============================
  Base for customization events.
:extends: vim.event.VmEvent_
:since: `VI API 2.5`_

Attributes:
    logLocation (`str`_, optional):

       The location of the in-guest customization log which will contain details of the customization operation.
