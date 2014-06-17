.. _vim.event.HostEvent: ../../vim/event/HostEvent.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst


vim.event.DrsResourceConfigureFailedEvent
=========================================
  This event records when resource configuration specification synchronization fails on a host.
:extends: vim.event.HostEvent_

Attributes:
    reason (`vmodl.LocalizedMethodFault`_):

       The reason for the failure.
