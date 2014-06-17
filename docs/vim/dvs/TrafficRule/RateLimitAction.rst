.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vim.dvs.TrafficRule.Action: ../../../vim/dvs/TrafficRule/Action.rst


vim.dvs.TrafficRule.RateLimitAction
===================================
  This class defines network rule action to ratelimit packets.
:extends: vim.dvs.TrafficRule.Action_
:since: `vSphere API 5.5`_

Attributes:
    packetsPerSecond (`int`_):

       Rate limit value specified in packets per second.
