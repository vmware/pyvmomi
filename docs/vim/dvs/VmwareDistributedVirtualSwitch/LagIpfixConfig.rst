
vim.dvs.VmwareDistributedVirtualSwitch.LagIpfixConfig
=====================================================
  This class defines the ipfix configuration of the Link Aggregation Control Protocol group.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    ipfixEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       True if ipfix monitoring is enabled in the Link Aggregation Control Protocol group. If set, this property will override the ipfix configuration of Uplink Ports in the Link Aggregation Control Protocol group. Thus they are no longer inheriting ipfix configuration from their Uplink Port Group. Setting this property would require `ipfixOverrideAllowed <vim/dvs/VmwareDistributedVirtualSwitch/VMwarePortgroupPolicy.rst#ipfixOverrideAllowed>`_ of all the Uplink Port Groups to be true, otherwise ConflictingConfiguration fault will be raised.
