
vim.ResourcePool.ResourceUsage
==============================
  Specifies the resource usage for either memory or CPU. For CPU the unit is MHz, for memory the unit is bytes.In the typical case, where a resourcepool is in a consistent state, unreservedForVm will be equal to unreservedForPool. Hence, we can simply say talk about unreserved resources.If the reservation on the resource pool is not expandable, then the following is true:reservation = reservationUsed + unreservedIf the reservation on the resource pool is expandable, then the following is true:reservation + parent.unreserved = reservationUsed + unreserved
:extends: vmodl.DynamicData_

Attributes:
    reservationUsed (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Total amount of resources that have been used to satisfy the reservation requirements of all descendants of this resource pool (includes both resource pools and virtual machines).
    reservationUsedForVm (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Total amount of resources that have been used to satisfy the reservation requirements of running virtual machines in this resource pool or any of its child resource pools.
    unreservedForPool (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Total amount of resources available to satisfy a reservation for a child resource pool. In the undercommitted state, this is limited by the capacity at the root node. In the overcommitted case, this could be higher since we do not perform the dynamic capacity checks.
    unreservedForVm (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Total amount of resources available to satisfy a reservation for a child virtual machine. In general, this should be the same as `unreservedForPool <vim/ResourcePool/ResourceUsage.rst#unreservedForPool>`_ . However, in the overcommitted case, this is limited by the remaining available resources at the root node.
    overallUsage (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Close to real-time resource usage of all running child virtual machines, including virtual machines in child resource pools.
    maxUsage (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Current upper-bound on usage. The upper-bound is based on the limit configured on this resource pool, as well as limits configured on any parent resource pool.
