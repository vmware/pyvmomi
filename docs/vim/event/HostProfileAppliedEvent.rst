.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.HostEvent: ../../vim/event/HostEvent.rst

.. _vim.event.ProfileEventArgument: ../../vim/event/ProfileEventArgument.rst


vim.event.HostProfileAppliedEvent
=================================
  This event records that a Profile application was done on the host
:extends: vim.event.HostEvent_
:since: `vSphere API 4.0`_

Attributes:
    profile (`vim.event.ProfileEventArgument`_):

       Link to the profile which was applied
