.. _str: https://docs.python.org/2/library/stdtypes.html

.. _int: https://docs.python.org/2/library/stdtypes.html

.. _ipfixEnabled: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VmwarePortConfigPolicy.rst#ipfixEnabled

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _LinkDiscoveryProtocolConfig: ../../../vim/host/LinkDiscoveryProtocolConfig.rst

.. _vim.host.LinkDiscoveryProtocolConfig: ../../../vim/host/LinkDiscoveryProtocolConfig.rst

.. _vim.DistributedVirtualSwitch.ConfigInfo: ../../../vim/DistributedVirtualSwitch/ConfigInfo.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.IpfixConfig: ../../../vim/dvs/VmwareDistributedVirtualSwitch/IpfixConfig.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.VspanSession: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VspanSession.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry: ../../../vim/dvs/VmwareDistributedVirtualSwitch/PvlanMapEntry.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupConfig: ../../../vim/dvs/VmwareDistributedVirtualSwitch/LacpGroupConfig.rst


vim.dvs.VmwareDistributedVirtualSwitch.ConfigInfo
=================================================
  This class defines the VMware specific configuration for DistributedVirtualSwitch.
:extends: vim.DistributedVirtualSwitch.ConfigInfo_
:since: `vSphere API 4.0`_

Attributes:
    vspanSession ([`vim.dvs.VmwareDistributedVirtualSwitch.VspanSession`_], optional):

       The Distributed Port Mirroring sessions in the switch.
    pvlanConfig ([`vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry`_], optional):

       The PVLAN configured in the switch.
    maxMtu (`int`_):

       The maximum MTU in the switch.
    linkDiscoveryProtocolConfig (`vim.host.LinkDiscoveryProtocolConfig`_, optional):

       See `LinkDiscoveryProtocolConfig`_ .
    ipfixConfig (`vim.dvs.VmwareDistributedVirtualSwitch.IpfixConfig`_, optional):

       Configuration for ipfix monitoring of the switch traffic. This must be set before ipfix monitoring can be enabled for the switch, or for any portgroup or port of the switch.See `ipfixEnabled`_ 
    lacpGroupConfig ([`vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupConfig`_], optional):

       The Link Aggregation Control Protocol groups in the switch.
    lacpApiVersion (`str`_, optional):

       The Link Aggregation Control Protocol group version in the switch. See LacpApiVersion for valid values.
