
vim.dvs.VmwareDistributedVirtualSwitch.ConfigInfo
=================================================
  This class defines the VMware specific configuration for DistributedVirtualSwitch.
:extends: vim.DistributedVirtualSwitch.ConfigInfo_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    vspanSession ([`vim.dvs.VmwareDistributedVirtualSwitch.VspanSession <vim/dvs/VmwareDistributedVirtualSwitch/VspanSession.rst>`_], optional):

       The Distributed Port Mirroring sessions in the switch.
    pvlanConfig ([`vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry <vim/dvs/VmwareDistributedVirtualSwitch/PvlanMapEntry.rst>`_], optional):

       The PVLAN configured in the switch.
    maxMtu (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The maximum MTU in the switch.
    linkDiscoveryProtocolConfig (`vim.host.LinkDiscoveryProtocolConfig <vim/host/LinkDiscoveryProtocolConfig.rst>`_, optional):

       See `LinkDiscoveryProtocolConfig <vim/host/LinkDiscoveryProtocolConfig.rst>`_ .
    ipfixConfig (`vim.dvs.VmwareDistributedVirtualSwitch.IpfixConfig <vim/dvs/VmwareDistributedVirtualSwitch/IpfixConfig.rst>`_, optional):

       Configuration for ipfix monitoring of the switch traffic. This must be set before ipfix monitoring can be enabled for the switch, or for any portgroup or port of the switch.See `ipfixEnabled <vim/dvs/VmwareDistributedVirtualSwitch/VmwarePortConfigPolicy.rst#ipfixEnabled>`_ 
    lacpGroupConfig ([`vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupConfig <vim/dvs/VmwareDistributedVirtualSwitch/LacpGroupConfig.rst>`_], optional):

       The Link Aggregation Control Protocol groups in the switch.
    lacpApiVersion (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The Link Aggregation Control Protocol group version in the switch. See LacpApiVersion for valid values.
