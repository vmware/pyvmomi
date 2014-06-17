.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _VmFailedStartingSecondaryEventFailureReason: ../../vim/event/VmFailedStartingSecondaryEvent/FailureReason.rst


vim.event.VmFailedStartingSecondaryEvent
========================================
  This event records vmotion failure when starting a secondary VM.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0`_

Attributes:
    reason (`str`_, optional):

       The reason for the failure. See `VmFailedStartingSecondaryEventFailureReason`_ 
