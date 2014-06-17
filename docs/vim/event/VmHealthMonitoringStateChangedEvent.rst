.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.ClusterEvent: ../../vim/event/ClusterEvent.rst

.. _ClusterDasConfigInfoVmMonitoringState: ../../vim/cluster/DasConfigInfo/VmMonitoringState.rst


vim.event.VmHealthMonitoringStateChangedEvent
=============================================
  This event records when host monitoring state has changed.
:extends: vim.event.ClusterEvent_
:since: `vSphere API 4.0`_

Attributes:
    state (`str`_):

       The service state in `ClusterDasConfigInfoVmMonitoringState`_ 
