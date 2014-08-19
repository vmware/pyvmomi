
vim.vm.NetworkShaperInfo
========================
  Network traffic shaping specification.Traffic shaping is used to configure the network utilization characteristics of a virtual machine.
:extends: vmodl.DynamicData_

Attributes:
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Is the shaper enabled?
    peakBps (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Peak bandwidth, in bits per second.
    averageBps (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Average bandwidth, in bits per second.
    burstSize (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Burst size, in bytes.
