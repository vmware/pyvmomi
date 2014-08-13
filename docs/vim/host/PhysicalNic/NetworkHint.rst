.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _PhysicalNicCdpInfo: ../../../vim/host/PhysicalNic/CdpInfo.rst

.. _vim.host.PhysicalNic.CdpInfo: ../../../vim/host/PhysicalNic/CdpInfo.rst

.. _vim.host.PhysicalNic.LldpInfo: ../../../vim/host/PhysicalNic/LldpInfo.rst

.. _vim.host.PhysicalNic.NetworkHint.IpNetwork: ../../../vim/host/PhysicalNic/NetworkHint/IpNetwork.rst

.. _vim.host.PhysicalNic.NetworkHint.NamedNetwork: ../../../vim/host/PhysicalNic/NetworkHint/NamedNetwork.rst


vim.host.PhysicalNic.NetworkHint
================================
  The NetworkHint data object type is some information about the network to which the physical network adapter is attached.
:extends: vmodl.DynamicData_

Attributes:
    device (`str`_):

       The physical network adapter device to which this hint applies.
    subnet ([`vim.host.PhysicalNic.NetworkHint.IpNetwork`_], optional):

       The list of subnets that were detected on this physical network adapter.
    network ([`vim.host.PhysicalNic.NetworkHint.NamedNetwork`_], optional):

       The list of network names that were detected on this physical network adapter.
    connectedSwitchPort (`vim.host.PhysicalNic.CdpInfo`_, optional):

       If the uplink directly connects to a CDP-awared network device and the device's CDP broadcast is enabled, this property will be set to return the CDP information that vmkernel received on this Physical NIC. CDP data contains the device information and port ID that the Physical NIC connects to. If the uplink is not connecting to a CDP-awared device or CDP is not enabled on the device, this property will be unset. `PhysicalNicCdpInfo`_ 
    lldpInfo (`vim.host.PhysicalNic.LldpInfo`_, optional):

       If the uplink directly connects to an LLDP-aware network device and the device's LLDP broadcast is enabled, this property will be set to return the LLDP information that is received on this physical network adapter. If the uplink is not connecting to a LLDP-aware device or LLDP is not enabled on the device, this property will be unset.
