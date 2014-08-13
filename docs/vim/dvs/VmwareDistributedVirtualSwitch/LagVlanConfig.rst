.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vim.NumericRange: ../../../vim/NumericRange.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vlanOverrideAllowed: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VMwarePortgroupPolicy.rst#vlanOverrideAllowed


vim.dvs.VmwareDistributedVirtualSwitch.LagVlanConfig
====================================================
  This class defines the vlan configuration of the Link Aggregation Control Protocol group.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    vlanId ([`vim.NumericRange`_], optional):

       The VlanId range for the Uplink Ports in the Link Aggregation Control Protocol group. The valid VlanId range is from 0 to 4094. Overlapping ranges are allowed. If set, this property will override the VLAN configuration of Uplink Ports in the Link Aggregation Control Protocol group. Thus they are no longer inheriting VLAN configuration from their Uplink Port Group. Setting this property would require `vlanOverrideAllowed`_ of all the Uplink Port Groups to be true, otherwise ConflictingConfiguration fault will be raised.
