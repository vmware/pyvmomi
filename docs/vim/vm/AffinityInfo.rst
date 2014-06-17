.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.vm.AffinityInfo
===================
  Specification of scheduling affinity.Scheduling affinity is used for explicitly specifying which processors or NUMA nodes may be used by a virtual machine.
:extends: vmodl.DynamicData_

Attributes:
    affinitySet (`int`_, optional):

       List of nodes (processors for CPU, NUMA nodes for memory) that may be used by the virtual machine. If the array is empty when modifying the affinity setting, then any existing affinity is removed.
