.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.vm.NetworkShaperInfo
========================
  Network traffic shaping specification.Traffic shaping is used to configure the network utilization characteristics of a virtual machine.
:extends: vmodl.DynamicData_

Attributes:
    enabled (`bool`_, optional):

       Is the shaper enabled?
    peakBps (`long`_, optional):

       Peak bandwidth, in bits per second.
    averageBps (`long`_, optional):

       Average bandwidth, in bits per second.
    burstSize (`long`_, optional):

       Burst size, in bytes.
