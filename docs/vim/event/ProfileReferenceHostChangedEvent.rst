.. _vim.HostSystem: ../../vim/HostSystem.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.ProfileEvent: ../../vim/event/ProfileEvent.rst


vim.event.ProfileReferenceHostChangedEvent
==========================================
  This event records that the reference host associated with this profile has changed
:extends: vim.event.ProfileEvent_
:since: `vSphere API 4.0`_

Attributes:
    referenceHost (`vim.HostSystem`_, optional):

       The newly associated reference host with this profile
