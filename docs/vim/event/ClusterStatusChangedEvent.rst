
vim.event.ClusterStatusChangedEvent
===================================
  This event records when a cluster's overall status changed.
:extends: vim.event.ClusterEvent_

Attributes:
    oldStatus (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The old ( `status <vim/ComputeResource/Summary.rst#overallStatus>`_ ).
    newStatus (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The new ( `status <vim/ComputeResource/Summary.rst#overallStatus>`_ ).
