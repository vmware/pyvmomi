
vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortTeamingPolicy
==============================================================
  Policy for a uplink port team.
:extends: vim.InheritablePolicy_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    policy (`vim.StringPolicy <vim/StringPolicy.rst>`_, optional):

       Network adapter teaming policy. The policy defines the way traffic from the clients of the team is routed through the different uplinks in the team. The policies supported on the VDS platform is one of `nicTeamingPolicy <vim/DistributedVirtualSwitch/FeatureCapability.rst#nicTeamingPolicy>`_ .
    reversePolicy (`vim.BoolPolicy <vim/BoolPolicy.rst>`_, optional):

       The flag to indicate whether or not the teaming policy is applied to inbound frames as well. Also see `reversePolicy <vim/host/NetworkPolicy/NicTeamingPolicy.rst#reversePolicy>`_ 
    notifySwitches (`vim.BoolPolicy <vim/BoolPolicy.rst>`_, optional):

       Flag to specify whether or not to notify the physical switch if a link fails. Also see `notifySwitches <vim/host/NetworkPolicy/NicTeamingPolicy.rst#notifySwitches>`_ 
    rollingOrder (`vim.BoolPolicy <vim/BoolPolicy.rst>`_, optional):

       The flag to indicate whether or not to use a rolling policy when restoring links. Also see `rollingOrder <vim/host/NetworkPolicy/NicTeamingPolicy.rst#rollingOrder>`_ 
    failureCriteria (`vim.dvs.VmwareDistributedVirtualSwitch.FailureCriteria <vim/dvs/VmwareDistributedVirtualSwitch/FailureCriteria.rst>`_, optional):

       Failover detection policy for the uplink port team.
    uplinkPortOrder (`vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortOrderPolicy <vim/dvs/VmwareDistributedVirtualSwitch/UplinkPortOrderPolicy.rst>`_, optional):

       Failover order policy for uplink ports on the hosts.
