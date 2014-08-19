vim.DistributedVirtualSwitch.NicTeamingPolicyMode
=================================================
  List of possible teaming modes supported by the vNetwork Distributed Switch. The different policy modes define the way traffic is routed through the different uplink ports in a team.
  :contained by: `vim.DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_

  :type: `vim.DistributedVirtualSwitch.NicTeamingPolicyMode <vim/DistributedVirtualSwitch/NicTeamingPolicyMode.rst>`_

  :name: loadbalance_loadbased

values:
--------

failover_explicit
   Use explicit failover order

loadbalance_ip
   Routing based on IP hash

loadbalance_srcid
   Route based on the source of the port ID

loadbalance_srcmac
   Route based on source MAC hash

loadbalance_loadbased
   Routing based by dynamically balancing traffic through the NICs in a team. This is the recommended teaming policy when the network I/O control feature is enabled for the vNetwork Distributed Switch.
