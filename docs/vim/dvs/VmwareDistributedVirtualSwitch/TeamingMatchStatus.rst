.. _policy: ../../../vim/dvs/VmwareDistributedVirtualSwitch/UplinkPortTeamingPolicy.rst#policy

.. _vim.dvs.VmwareDistributedVirtualSwitch: ../../../vim/dvs/VmwareDistributedVirtualSwitch.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.TeamingMatchStatus: ../../../vim/dvs/VmwareDistributedVirtualSwitch/TeamingMatchStatus.rst

vim.dvs.VmwareDistributedVirtualSwitch.TeamingMatchStatus
=========================================================
  The teaming health check match status.
  :contained by: `vim.dvs.VmwareDistributedVirtualSwitch`_

  :type: `vim.dvs.VmwareDistributedVirtualSwitch.TeamingMatchStatus`_

  :name: nonIphashMismatch

values:
--------

iphashMatch
   The value of 'loadbalance_ip' is used in a uplink teaming policy `policy`_ in the vSphere Distributed Switch, and the external physical switch has the matching EtherChannel configuration.

nonIphashMatch
   The value of 'loadbalance_ip' is not used in a uplink teaming policy `policy`_ in the vSphere Distributed Switch, and the external physical switch does not have EtherChannel configuration.

iphashMismatch
   The value of 'loadbalance_ip' is used in a uplink teaming policy `policy`_ in the vSphere Distributed Switch, but the external physical switch does not have the matching EtherChannel configuration.

nonIphashMismatch
   The value of 'loadbalance_ip' is not used in a uplink teaming policy `policy`_ in the vSphere Distributed Switch, but the external physical switch has EtherChannel configuration.
