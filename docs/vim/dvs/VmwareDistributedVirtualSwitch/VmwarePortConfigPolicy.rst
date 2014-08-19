
vim.dvs.VmwareDistributedVirtualSwitch.VmwarePortConfigPolicy
=============================================================
  This class defines the VMware specific configuration for DistributedVirtualPort.
:extends: vim.dvs.DistributedVirtualPort.Setting_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    vlan (`vim.dvs.VmwareDistributedVirtualSwitch.VlanSpec <vim/dvs/VmwareDistributedVirtualSwitch/VlanSpec.rst>`_, optional):

       The VLAN Specification of the port.
    qosTag (`vim.IntPolicy <vim/IntPolicy.rst>`_, optional):

       deprecated As of vSphere API 5.0
    uplinkTeamingPolicy (`vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortTeamingPolicy <vim/dvs/VmwareDistributedVirtualSwitch/UplinkPortTeamingPolicy.rst>`_, optional):

       The uplink teaming policy. This property is ignored for uplink ports.
    securityPolicy (`vim.dvs.VmwareDistributedVirtualSwitch.SecurityPolicy <vim/dvs/VmwareDistributedVirtualSwitch/SecurityPolicy.rst>`_, optional):

       The security policy.
    ipfixEnabled (`vim.BoolPolicy <vim/BoolPolicy.rst>`_, optional):

       True if ipfix monitoring is enabled. To successfully enable ipfix monitoring, the switch must have an assigned `IP address <vim/DistributedVirtualSwitch/ConfigInfo.rst#switchIpAddress>`_ and an appropriately populated `ipfix configuration <vim/dvs/VmwareDistributedVirtualSwitch/ConfigInfo.rst#ipfixConfig>`_ that specifies a collector IP address and port.
    txUplink (`vim.BoolPolicy <vim/BoolPolicy.rst>`_, optional):

       If true, a copy of packets sent to the switch will always be forwarded to an uplink in addition to the regular packet forwarded done by the switch.
    lacpPolicy (`vim.dvs.VmwareDistributedVirtualSwitch.UplinkLacpPolicy <vim/dvs/VmwareDistributedVirtualSwitch/UplinkLacpPolicy.rst>`_, optional):

       Link Aggregation Control Protocol policy. This policy is ignored on non-uplink portgroups. Setting this policy at port level is not supported.
