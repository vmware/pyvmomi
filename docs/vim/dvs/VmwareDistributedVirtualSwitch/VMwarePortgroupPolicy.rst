
vim.dvs.VmwareDistributedVirtualSwitch.VMwarePortgroupPolicy
============================================================
  This class defines the VMware specific configuration for DistributedVirtualPort.
:extends: vim.dvs.DistributedVirtualPortgroup.PortgroupPolicy_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    vlanOverrideAllowed (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Allow the setting of `vlanId <vim/dvs/VmwareDistributedVirtualSwitch/VlanIdSpec.rst#vlanId>`_ , trunk `vlanId <vim/dvs/VmwareDistributedVirtualSwitch/TrunkVlanSpec.rst#vlanId>`_ , or `pvlanId <vim/dvs/VmwareDistributedVirtualSwitch/PvlanSpec.rst#pvlanId>`_ for an individual port to override the setting in `defaultPortConfig <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#defaultPortConfig>`_ of a portgroup.
    uplinkTeamingOverrideAllowed (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Allow the setting of `uplinkTeamingPolicy <vim/dvs/VmwareDistributedVirtualSwitch/VmwarePortConfigPolicy.rst#uplinkTeamingPolicy>`_ for an individual port to override the setting in `defaultPortConfig <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#defaultPortConfig>`_ of a portgroup.
    securityPolicyOverrideAllowed (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Allow the setting of `securityPolicy <vim/dvs/VmwareDistributedVirtualSwitch/VmwarePortConfigPolicy.rst#securityPolicy>`_ for an individual port to override the setting in `defaultPortConfig <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#defaultPortConfig>`_ of a portgroup.
    ipfixOverrideAllowed (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Allow the setting of `ipfixEnabled <vim/dvs/VmwareDistributedVirtualSwitch/VmwarePortConfigPolicy.rst#ipfixEnabled>`_ for an individual port to override the setting in `defaultPortConfig <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#defaultPortConfig>`_ of a portgroup.
