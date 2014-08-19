
vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupConfig
======================================================
  This class defines VMware specific multiple IEEE 802.3ad Dynamic Link Aggregation Control Protocol groups.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The generated key as the identifier for the Link Aggregation group.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The display name.
    mode (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The mode of Link Aggregation Control Protocol. See UplinkLacpMode for valid values.
    uplinkNum (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The number of uplink ports.
    loadbalanceAlgorithm (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Load balance policy. See LacpLoadBalanceAlgorithm for valid values.
    vlan (`vim.dvs.VmwareDistributedVirtualSwitch.LagVlanConfig <vim/dvs/VmwareDistributedVirtualSwitch/LagVlanConfig.rst>`_, optional):

       The VLAN Specification of the Uplink Ports in the Link Aggregation group.
    ipfix (`vim.dvs.VmwareDistributedVirtualSwitch.LagIpfixConfig <vim/dvs/VmwareDistributedVirtualSwitch/LagIpfixConfig.rst>`_, optional):

       Ipfix configuration of the Link Aggregation Control Protocol group.
    uplinkName ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Names for the Uplink Ports in the group. This property is ignored in an update operation.
    uplinkPortKey ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Keys for the Uplink Ports in the group. This property is ignored in an update operation.
