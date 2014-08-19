
vim.DistributedVirtualSwitch.NameArrayUplinkPortPolicy
======================================================
  The uplink port policy specifies an array of uniform names for the uplink ports across the hosts. The size of the array indicates the number of uplink ports that will be created for each host in the switch.When the names in this array change, the uplink ports on all the hosts are automatically renamed accordingly. Increasing the number of names in the array automatically creates additional uplink ports bearing the added name on each host. Decreasing the number of name automatically deletes the unused uplink ports on each host. Decreasing beyond the number of unused uplink port raises a fault.This policy overrides the portgroup port naming format ( `DVPortgroupConfigSpec <vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst>`_ . `portNameFormat <vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst#portNameFormat>`_ ), if both are defined and the uplink ports are created in a uplink portgroup.
:extends: vim.DistributedVirtualSwitch.UplinkPortPolicy_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    uplinkPortName ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       The uniform name of uplink ports on each host.
