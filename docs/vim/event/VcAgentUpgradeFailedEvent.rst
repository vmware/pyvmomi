.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.HostEvent: ../../vim/event/HostEvent.rst

.. _AgentInstallFailedReason: ../../vim/fault/AgentInstallFailed/Reason.rst


vim.event.VcAgentUpgradeFailedEvent
===================================
  This event records when the VirtualCenter agent on a host failed to upgrade.
:extends: vim.event.HostEvent_

Attributes:
    reason (`str`_, optional):

       The reason why the upgrade failed, if known. See `AgentInstallFailedReason`_ 
