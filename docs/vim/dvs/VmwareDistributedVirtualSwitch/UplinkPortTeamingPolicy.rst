.. _rollingOrder: ../../../vim/host/NetworkPolicy/NicTeamingPolicy.rst#rollingOrder

.. _reversePolicy: ../../../vim/host/NetworkPolicy/NicTeamingPolicy.rst#reversePolicy

.. _notifySwitches: ../../../vim/host/NetworkPolicy/NicTeamingPolicy.rst#notifySwitches

.. _vim.BoolPolicy: ../../../vim/BoolPolicy.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.StringPolicy: ../../../vim/StringPolicy.rst

.. _nicTeamingPolicy: ../../../vim/DistributedVirtualSwitch/FeatureCapability.rst#nicTeamingPolicy

.. _vim.InheritablePolicy: ../../../vim/InheritablePolicy.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.FailureCriteria: ../../../vim/dvs/VmwareDistributedVirtualSwitch/FailureCriteria.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortOrderPolicy: ../../../vim/dvs/VmwareDistributedVirtualSwitch/UplinkPortOrderPolicy.rst


vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortTeamingPolicy
==============================================================
  Policy for a uplink port team.
:extends: vim.InheritablePolicy_
:since: `vSphere API 4.0`_

Attributes:
    policy (`vim.StringPolicy`_, optional):

       Network adapter teaming policy. The policy defines the way traffic from the clients of the team is routed through the different uplinks in the team. The policies supported on the VDS platform is one of `nicTeamingPolicy`_ .
    reversePolicy (`vim.BoolPolicy`_, optional):

       The flag to indicate whether or not the teaming policy is applied to inbound frames as well. Also see `reversePolicy`_ 
    notifySwitches (`vim.BoolPolicy`_, optional):

       Flag to specify whether or not to notify the physical switch if a link fails. Also see `notifySwitches`_ 
    rollingOrder (`vim.BoolPolicy`_, optional):

       The flag to indicate whether or not to use a rolling policy when restoring links. Also see `rollingOrder`_ 
    failureCriteria (`vim.dvs.VmwareDistributedVirtualSwitch.FailureCriteria`_, optional):

       Failover detection policy for the uplink port team.
    uplinkPortOrder (`vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortOrderPolicy`_, optional):

       Failover order policy for uplink ports on the hosts.
