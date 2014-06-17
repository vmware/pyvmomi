.. _IP address: ../../../vim/DistributedVirtualSwitch/ConfigInfo.rst#switchIpAddress

.. _vim.IntPolicy: ../../../vim/IntPolicy.rst

.. _vim.BoolPolicy: ../../../vim/BoolPolicy.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _ipfix configuration: ../../../vim/dvs/VmwareDistributedVirtualSwitch/ConfigInfo.rst#ipfixConfig

.. _vim.dvs.DistributedVirtualPort.Setting: ../../../vim/dvs/DistributedVirtualPort/Setting.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.VlanSpec: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VlanSpec.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.SecurityPolicy: ../../../vim/dvs/VmwareDistributedVirtualSwitch/SecurityPolicy.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.UplinkLacpPolicy: ../../../vim/dvs/VmwareDistributedVirtualSwitch/UplinkLacpPolicy.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortTeamingPolicy: ../../../vim/dvs/VmwareDistributedVirtualSwitch/UplinkPortTeamingPolicy.rst


vim.dvs.VmwareDistributedVirtualSwitch.VmwarePortConfigPolicy
=============================================================
  This class defines the VMware specific configuration for DistributedVirtualPort.
:extends: vim.dvs.DistributedVirtualPort.Setting_
:since: `vSphere API 4.0`_

Attributes:
    vlan (`vim.dvs.VmwareDistributedVirtualSwitch.VlanSpec`_, optional):

       The VLAN Specification of the port.
    qosTag (`vim.IntPolicy`_, optional):

       deprecated As of vSphere API 5.0
    uplinkTeamingPolicy (`vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortTeamingPolicy`_, optional):

       The uplink teaming policy. This property is ignored for uplink ports.
    securityPolicy (`vim.dvs.VmwareDistributedVirtualSwitch.SecurityPolicy`_, optional):

       The security policy.
    ipfixEnabled (`vim.BoolPolicy`_, optional):

       True if ipfix monitoring is enabled. To successfully enable ipfix monitoring, the switch must have an assigned `IP address`_ and an appropriately populated `ipfix configuration`_ that specifies a collector IP address and port.
    txUplink (`vim.BoolPolicy`_, optional):

       If true, a copy of packets sent to the switch will always be forwarded to an uplink in addition to the regular packet forwarded done by the switch.
    lacpPolicy (`vim.dvs.VmwareDistributedVirtualSwitch.UplinkLacpPolicy`_, optional):

       Link Aggregation Control Protocol policy. This policy is ignored on non-uplink portgroups. Setting this policy at port level is not supported.
