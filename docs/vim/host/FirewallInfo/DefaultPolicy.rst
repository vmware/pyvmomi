
vim.host.FirewallInfo.DefaultPolicy
===================================
  Default settings for the firewall, used for ports that are not explicitly opened.
:extends: vmodl.DynamicData_

Attributes:
    incomingBlocked (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag indicating whether incoming traffic should be blocked by default.
    outgoingBlocked (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag indicating whether outgoing traffic should be blocked by default.
