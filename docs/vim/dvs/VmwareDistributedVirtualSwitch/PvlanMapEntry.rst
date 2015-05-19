.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _VmwareDistributedVirtualSwitchPvlanPortType: ../../../vim/dvs/VmwareDistributedVirtualSwitch/PvlanPortType.rst


vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry
====================================================
  The class represents a PVLAN id.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    primaryVlanId (`int`_):

       The primary VLAN ID. The VLAN IDs of 0 and 4095 are reserved and cannot be used in this property.
    secondaryVlanId (`int`_):

       The secondary VLAN ID. The VLAN IDs of 0 and 4095 are reserved and cannot be used in this property.
    pvlanType (`str`_):

       The type of PVLAN. See `VmwareDistributedVirtualSwitchPvlanPortType`_ for valid values.
