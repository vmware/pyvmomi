
vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry
====================================================
  The class represents a PVLAN id.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    primaryVlanId (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The primary VLAN ID. The VLAN IDs of 0 and 4095 are reserved and cannot be used in this property.
    secondaryVlanId (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The secondary VLAN ID. The VLAN IDs of 0 and 4095 are reserved and cannot be used in this property.
    pvlanType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The type of PVLAN. See `VmwareDistributedVirtualSwitchPvlanPortType <vim/dvs/VmwareDistributedVirtualSwitch/PvlanPortType.rst>`_ for valid values.
