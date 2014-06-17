.. _str: https://docs.python.org/2/library/stdtypes.html

.. _status: ../../vim/ComputeResource/Summary.rst#overallStatus

.. _vim.event.ClusterEvent: ../../vim/event/ClusterEvent.rst


vim.event.ClusterStatusChangedEvent
===================================
  This event records when a cluster's overall status changed.
:extends: vim.event.ClusterEvent_

Attributes:
    oldStatus (`str`_):

       The old ( `status`_ ).
    newStatus (`str`_):

       The new ( `status`_ ).
