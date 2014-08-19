
vim.event.VmFailedStartingSecondaryEvent
========================================
  This event records vmotion failure when starting a secondary VM.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    reason (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The reason for the failure. See `VmFailedStartingSecondaryEventFailureReason <vim/event/VmFailedStartingSecondaryEvent/FailureReason.rst>`_ 
