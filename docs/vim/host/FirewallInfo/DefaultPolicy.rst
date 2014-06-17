.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.FirewallInfo.DefaultPolicy
===================================
  Default settings for the firewall, used for ports that are not explicitly opened.
:extends: vmodl.DynamicData_

Attributes:
    incomingBlocked (`bool`_, optional):

       Flag indicating whether incoming traffic should be blocked by default.
    outgoingBlocked (`bool`_, optional):

       Flag indicating whether outgoing traffic should be blocked by default.
