.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.HostEvent: ../../vim/event/HostEvent.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst


vim.event.HostSyncFailedEvent
=============================
  This event records a failure to sync up with the VirtualCenter agent on the host
:extends: vim.event.HostEvent_
:since: `vSphere API 4.0`_

Attributes:
    reason (`vmodl.LocalizedMethodFault`_):

       The reason for the failure.
