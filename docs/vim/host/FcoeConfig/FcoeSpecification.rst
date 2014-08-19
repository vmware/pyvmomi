
vim.host.FcoeConfig.FcoeSpecification
=====================================
  An FcoeSpecification contains values relevant to issuing FCoE discovery. Non-mandatory values are denoted '@optional'.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    underlyingPnic (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of this FcoeSpecification's underlying PhysicalNic
    priorityClass (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       802.1p priority class to use for FCoE traffic.
    sourceMac (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Source MAC address to use for FCoE traffic. This MAC address is associated with the logical construct that is a physical NIC's associated underlying FCoE Controller, as defined in the FC-BB-5 standard. This MAC address should be of the form "xx:xx:xx:xx:xx:xx", where 'x' is a hexadecimal digit. Valid MAC addresses are unicast addresses.
    vlanRange ([`vim.host.FcoeConfig.VlanRange <vim/host/FcoeConfig/VlanRange.rst>`_], optional):

       VLAN ranges to use for FCoE traffic.
