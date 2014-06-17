.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.host.NumaNode: ../../vim/host/NumaNode.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.host.NumaInfo
=================
  Information about NUMA (non-uniform memory access).
:extends: vmodl.DynamicData_

Attributes:
    type (`str`_):

       The type of NUMA technology.
    numNodes (`int`_):

       The number of NUMA nodes on the host. The value is 0 if the host is not NUMA-capable.
    numaNode (`vim.host.NumaNode`_, optional):

       Information about each of the NUMA nodes on the host. The array is empty if the host is not NUMA-capable.
