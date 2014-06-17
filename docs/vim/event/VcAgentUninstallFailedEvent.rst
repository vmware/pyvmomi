.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.HostEvent: ../../vim/event/HostEvent.rst

.. _AgentInstallFailedReason: ../../vim/fault/AgentInstallFailed/Reason.rst


vim.event.VcAgentUninstallFailedEvent
=====================================
  This event records when the VirtualCenter agent on a host failed to uninstall.
:extends: vim.event.HostEvent_
:since: `vSphere API 4.0`_

Attributes:
    reason (`str`_, optional):

       The reason why the uninstall failed, if known. See `AgentInstallFailedReason`_ 
