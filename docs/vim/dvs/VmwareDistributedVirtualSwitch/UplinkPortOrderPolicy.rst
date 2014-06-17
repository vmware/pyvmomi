.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.InheritablePolicy: ../../../vim/InheritablePolicy.rst


vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortOrderPolicy
============================================================
  This data object type describes uplink port ordering policy for a distributed virtual port. A uplink port can be in the active list, the standby list, or neither. It cannot be in both lists.
:extends: vim.InheritablePolicy_
:since: `vSphere API 4.0`_

Attributes:
    activeUplinkPort (`str`_, optional):

       List of active uplink ports used for load balancing.
    standbyUplinkPort (`str`_, optional):

       Standby uplink ports used for failover.
