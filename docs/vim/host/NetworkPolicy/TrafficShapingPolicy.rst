
vim.host.NetworkPolicy.TrafficShapingPolicy
===========================================
  This data object type describes traffic shaping policy.
:extends: vmodl.DynamicData_

Attributes:
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The flag to indicate whether or not traffic shaper is enabled on the port.
    averageBandwidth (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The average bandwidth in bits per second if shaping is enabled on the port.
    peakBandwidth (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The peak bandwidth during bursts in bits per second if traffic shaping is enabled on the port.
    burstSize (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The maximum burst size allowed in bytes if shaping is enabled on the port.
