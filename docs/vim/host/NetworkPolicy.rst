
vim.host.NetworkPolicy
======================
  This data object type describes network policies that can be configured for both virtual switches and port groups. The policy settings on the port group can inherit policy settings from their containing virtual switch. These policy settings are inherited if the settings on the port group are not set. Since every policy setting on a port group is optional, every individual policy setting can be inherited.By contrast, if a host is capable of implementing a policy setting, every virtual switch has some value assigned to the policy setting. In this case, although all of the policy settings are optional, they always have some value either by inheritance or by direct setting.Policy settings are organized into policy groups such as SecurityPolicy. Policy groups are optional since it is possible that a host may not implement such policies. If a host does not support a policy group, the policy group is not set on both the virtual switches and the port groups.See `HostNetCapabilities <vim/host/NetCapabilities.rst>`_ 
:extends: vmodl.DynamicData_

Attributes:
    security (`vim.host.NetworkPolicy.SecurityPolicy <vim/host/NetworkPolicy/SecurityPolicy.rst>`_, optional):

       The security policy governing ports on this virtual switch.
    nicTeaming (`vim.host.NetworkPolicy.NicTeamingPolicy <vim/host/NetworkPolicy/NicTeamingPolicy.rst>`_, optional):

       The network adapter teaming policy. The bridge must be BondBridge for this property to be valid.
    offloadPolicy (`vim.host.NetOffloadCapabilities <vim/host/NetOffloadCapabilities.rst>`_, optional):

       Offload capabilities are used to optimize virtual machine network performance. When a virtual machine is transmitting on a network, some operations can be offloaded to either the host or the physical hardware. This policy indicates what networking related operations should be offloaded.All virtual machines using this PortGroup are subject to this policy. There is no setting for an individual virtual machine to determine if an operation should be offloaded.
    shapingPolicy (`vim.host.NetworkPolicy.TrafficShapingPolicy <vim/host/NetworkPolicy/TrafficShapingPolicy.rst>`_, optional):

       The traffic shaping policy.
