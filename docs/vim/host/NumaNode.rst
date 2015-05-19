.. _int: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _short: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.host.NumaNode
=================
  Information about a single NUMA node.NOTE: This data object is not modeled correctly if the NUMA node contains multiple disjoint memory ranges. If there are multiple memory ranges, the client will see one memory ranges from this NumaNode object, and the memory range may or may not belong to this NUMA node.
:extends: vmodl.DynamicData_

Attributes:
    typeId (`int`_):

       Zero-based NUMA ID for the node.
    cpuID ([`short`_]):

       Information about each of the CPUs associated with the node.
    memoryRangeBegin (`long`_):

       Beginning memory range for this NUMA node.
    memoryRangeLength (`long`_):

       Length of the memory range for this node in bytes, that is, the amount of memory on the node.
