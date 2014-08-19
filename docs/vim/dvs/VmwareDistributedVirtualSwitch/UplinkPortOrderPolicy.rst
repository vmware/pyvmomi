
vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortOrderPolicy
============================================================
  This data object type describes uplink port ordering policy for a distributed virtual port. A uplink port can be in the active list, the standby list, or neither. It cannot be in both lists.
:extends: vim.InheritablePolicy_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    activeUplinkPort ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       List of active uplink ports used for load balancing.
    standbyUplinkPort ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Standby uplink ports used for failover.
