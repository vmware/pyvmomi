.. _str: https://docs.python.org/2/library/stdtypes.html

.. _DrsBehavior: ../../vim/cluster/DrsConfigInfo/DrsBehavior.rst

.. _vim.event.ClusterEvent: ../../vim/event/ClusterEvent.rst


vim.event.DrsEnabledEvent
=========================
  This event records when DRS is enabled on a cluster.
:extends: vim.event.ClusterEvent_

Attributes:
    behavior (`str`_):

       The DRS automation level in ( `DrsBehavior`_ )
