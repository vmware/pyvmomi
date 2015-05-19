.. _vim.LongPolicy: ../../../vim/LongPolicy.rst

.. _vim.BoolPolicy: ../../../vim/BoolPolicy.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.InheritablePolicy: ../../../vim/InheritablePolicy.rst


vim.dvs.DistributedVirtualPort.TrafficShapingPolicy
===================================================
  This data object type describes traffic shaping policy.
:extends: vim.InheritablePolicy_
:since: `vSphere API 4.0`_

Attributes:
    enabled (`vim.BoolPolicy`_, optional):

       The flag to indicate whether or not traffic shaper is enabled on the port.
    averageBandwidth (`vim.LongPolicy`_, optional):

       The average bandwidth in bits per second if shaping is enabled on the port.
    peakBandwidth (`vim.LongPolicy`_, optional):

       The peak bandwidth during bursts in bits per second if traffic shaping is enabled on the port.
    burstSize (`vim.LongPolicy`_, optional):

       The maximum burst size allowed in bytes if shaping is enabled on the port.
