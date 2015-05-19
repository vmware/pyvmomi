.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.dvs.VmwareDistributedVirtualSwitch.VlanSpec: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VlanSpec.rst


vim.dvs.VmwareDistributedVirtualSwitch.VlanIdSpec
=================================================
  This data type defines the configuration when single vlanId is used for the port.
:extends: vim.dvs.VmwareDistributedVirtualSwitch.VlanSpec_
:since: `vSphere API 4.0`_

Attributes:
    vlanId (`int`_):

       The VLAN ID for ports. Possible values:
        * A value of 0 specifies that you do not want the port associated with a VLAN.
        * A value from 1 to 4094 specifies a VLAN ID for the port.
