.. _str: https://docs.python.org/2/library/stdtypes.html

.. _int: https://docs.python.org/2/library/stdtypes.html

.. _isolated: ../../../vim/dvs/VmwareDistributedVirtualSwitch/PvlanPortType.rst#isolated

.. _community: ../../../vim/dvs/VmwareDistributedVirtualSwitch/PvlanPortType.rst#community

.. _pvlanType: ../../../vim/dvs/VmwareDistributedVirtualSwitch/PvlanMapEntry.rst#pvlanType

.. _promiscuous: ../../../vim/dvs/VmwareDistributedVirtualSwitch/PvlanPortType.rst#promiscuous

.. _ipfixEnabled: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VmwarePortConfigPolicy.rst#ipfixEnabled

.. _primaryVlanId: ../../../vim/dvs/VmwareDistributedVirtualSwitch/PvlanMapEntry.rst#primaryVlanId

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _secondaryVlanId: ../../../vim/dvs/VmwareDistributedVirtualSwitch/PvlanMapEntry.rst#secondaryVlanId

.. _VMwareDVSPvlanMapEntry: ../../../vim/dvs/VmwareDistributedVirtualSwitch/PvlanMapEntry.rst

.. _LinkDiscoveryProtocolConfig: ../../../vim/host/LinkDiscoveryProtocolConfig.rst

.. _vim.host.LinkDiscoveryProtocolConfig: ../../../vim/host/LinkDiscoveryProtocolConfig.rst

.. _vim.DistributedVirtualSwitch.ConfigSpec: ../../../vim/DistributedVirtualSwitch/ConfigSpec.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.IpfixConfig: ../../../vim/dvs/VmwareDistributedVirtualSwitch/IpfixConfig.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.PvlanConfigSpec: ../../../vim/dvs/VmwareDistributedVirtualSwitch/PvlanConfigSpec.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.VspanConfigSpec: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VspanConfigSpec.rst


vim.dvs.VmwareDistributedVirtualSwitch.ConfigSpec
=================================================
  This class defines the VMware specific configuration for DistributedVirtualSwitch.
:extends: vim.DistributedVirtualSwitch.ConfigSpec_
:since: `vSphere API 4.0`_

Attributes:
    pvlanConfigSpec (`vim.dvs.VmwareDistributedVirtualSwitch.PvlanConfigSpec`_, optional):

       The PVLAN configuration specification.A `VMwareDVSPvlanMapEntry`_ that has the same value for `primaryVlanId`_ and `secondaryVlanId`_ is referred to as a primary PVLAN entry. Otherwise, the `VMwareDVSPvlanMapEntry`_ is referred to as a secondary PVLAN entry.The `pvlanType`_ of a primary PVLAN entry must be `promiscuous`_ . A secondary PVLAN entry can have a `pvlanType`_ of either `community`_ or `isolated`_ .Primary PVLAN entries must be explicitly added. If there is no primary PVLAN entry corresponding to the `primaryVlanId`_ of a secondary PVLAN entry, a fault is thrown.While deleting a primary PVLAN entry, any associated secondary PVLAN entries must be explicitly deleted.
    vspanConfigSpec (`vim.dvs.VmwareDistributedVirtualSwitch.VspanConfigSpec`_, optional):

       The Distributed Port Mirroring configuration specification. The VSPAN sessions in the array cannot be of the same key.
    maxMtu (`int`_, optional):

       The maximum MTU in the switch.
    linkDiscoveryProtocolConfig (`vim.host.LinkDiscoveryProtocolConfig`_, optional):

       See `LinkDiscoveryProtocolConfig`_ .
    ipfixConfig (`vim.dvs.VmwareDistributedVirtualSwitch.IpfixConfig`_, optional):

       Configuration for ipfix monitoring of the switch traffic. This must be set before ipfix monitoring can be enabled for the switch, or for any portgroup or port of the switch.See `ipfixEnabled`_ 
    lacpApiVersion (`str`_, optional):

       The Link Aggregation Control Protocol group version in the switch. See LacpApiVersion for valid values.
