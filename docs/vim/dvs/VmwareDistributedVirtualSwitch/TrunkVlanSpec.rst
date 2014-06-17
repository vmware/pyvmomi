.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.NumericRange: ../../../vim/NumericRange.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.VlanSpec: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VlanSpec.rst


vim.dvs.VmwareDistributedVirtualSwitch.TrunkVlanSpec
====================================================
  This data type specifies that the port uses trunk mode, which allows the guest operating system to manage its own VLAN tags.
:extends: vim.dvs.VmwareDistributedVirtualSwitch.VlanSpec_
:since: `vSphere API 4.0`_

Attributes:
    vlanId (`vim.NumericRange`_):

       The VlanId range for the trunk port. The valid VlanId range is from 0 to 4094. Overlapping ranges are allowed.
