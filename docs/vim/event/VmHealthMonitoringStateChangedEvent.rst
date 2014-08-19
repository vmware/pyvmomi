
vim.event.VmHealthMonitoringStateChangedEvent
=============================================
  This event records when host monitoring state has changed.
:extends: vim.event.ClusterEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    state (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The service state in `ClusterDasConfigInfoVmMonitoringState <vim/cluster/DasConfigInfo/VmMonitoringState.rst>`_ 
