.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.FcoeConfig.VlanRange: ../../vim/host/FcoeConfig/VlanRange.rst

.. _vim.host.FcoeConfig.FcoeCapabilities: ../../vim/host/FcoeConfig/FcoeCapabilities.rst


vim.host.FcoeConfig
===================
  This data object type describes an FCoE configuration as it pertains to an underlying physical NIC. Terminology is borrowed from T11's working draft of the Fibre Channel Backbone 5 standard (FC-BB-5). The draft can be found at http://www.t11.org.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    priorityClass (`int`_):

       802.1p priority class used for FCoE traffic.
    sourceMac (`str`_):

       Source MAC address used for FCoE traffic. This MAC address is associated with the logical construct that is a physical NIC's associated underlying FCoE Controller, as defined in the FC-BB-5 standard. This MAC address should be of the form "xx:xx:xx:xx:xx:xx", where 'x' is a hexadecimal digit. Valid MAC addresses are unicast addresses.
    vlanRange (`vim.host.FcoeConfig.VlanRange`_):

       VLAN ranges associated with this FcoeConfig.
    capabilities (`vim.host.FcoeConfig.FcoeCapabilities`_):

       Settable capabilities for this FcoeConfig.
    fcoeActive (`bool`_):

       Indicates whether this FcoeConfig is "active" (has been used in conjunction with a parent physical network adapter for FCoE discovery).
