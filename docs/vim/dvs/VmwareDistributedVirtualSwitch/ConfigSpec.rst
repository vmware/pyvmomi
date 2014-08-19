
vim.dvs.VmwareDistributedVirtualSwitch.ConfigSpec
=================================================
  This class defines the VMware specific configuration for DistributedVirtualSwitch.
:extends: vim.DistributedVirtualSwitch.ConfigSpec_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    pvlanConfigSpec ([`vim.dvs.VmwareDistributedVirtualSwitch.PvlanConfigSpec <vim/dvs/VmwareDistributedVirtualSwitch/PvlanConfigSpec.rst>`_], optional):

       The PVLAN configuration specification.A `VMwareDVSPvlanMapEntry <vim/dvs/VmwareDistributedVirtualSwitch/PvlanMapEntry.rst>`_ that has the same value for `primaryVlanId <vim/dvs/VmwareDistributedVirtualSwitch/PvlanMapEntry.rst#primaryVlanId>`_ and `secondaryVlanId <vim/dvs/VmwareDistributedVirtualSwitch/PvlanMapEntry.rst#secondaryVlanId>`_ is referred to as a primary PVLAN entry. Otherwise, the `VMwareDVSPvlanMapEntry <vim/dvs/VmwareDistributedVirtualSwitch/PvlanMapEntry.rst>`_ is referred to as a secondary PVLAN entry.The `pvlanType <vim/dvs/VmwareDistributedVirtualSwitch/PvlanMapEntry.rst#pvlanType>`_ of a primary PVLAN entry must be `promiscuous <vim/dvs/VmwareDistributedVirtualSwitch/PvlanPortType.rst#promiscuous>`_ . A secondary PVLAN entry can have a `pvlanType <vim/dvs/VmwareDistributedVirtualSwitch/PvlanMapEntry.rst#pvlanType>`_ of either `community <vim/dvs/VmwareDistributedVirtualSwitch/PvlanPortType.rst#community>`_ or `isolated <vim/dvs/VmwareDistributedVirtualSwitch/PvlanPortType.rst#isolated>`_ .Primary PVLAN entries must be explicitly added. If there is no primary PVLAN entry corresponding to the `primaryVlanId <vim/dvs/VmwareDistributedVirtualSwitch/PvlanMapEntry.rst#primaryVlanId>`_ of a secondary PVLAN entry, a fault is thrown.While deleting a primary PVLAN entry, any associated secondary PVLAN entries must be explicitly deleted.
    vspanConfigSpec ([`vim.dvs.VmwareDistributedVirtualSwitch.VspanConfigSpec <vim/dvs/VmwareDistributedVirtualSwitch/VspanConfigSpec.rst>`_], optional):

       The Distributed Port Mirroring configuration specification. The VSPAN sessions in the array cannot be of the same key.
    maxMtu (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The maximum MTU in the switch.
    linkDiscoveryProtocolConfig (`vim.host.LinkDiscoveryProtocolConfig <vim/host/LinkDiscoveryProtocolConfig.rst>`_, optional):

       See `LinkDiscoveryProtocolConfig <vim/host/LinkDiscoveryProtocolConfig.rst>`_ .
    ipfixConfig (`vim.dvs.VmwareDistributedVirtualSwitch.IpfixConfig <vim/dvs/VmwareDistributedVirtualSwitch/IpfixConfig.rst>`_, optional):

       Configuration for ipfix monitoring of the switch traffic. This must be set before ipfix monitoring can be enabled for the switch, or for any portgroup or port of the switch.See `ipfixEnabled <vim/dvs/VmwareDistributedVirtualSwitch/VmwarePortConfigPolicy.rst#ipfixEnabled>`_ 
    lacpApiVersion (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The Link Aggregation Control Protocol group version in the switch. See LacpApiVersion for valid values.
