.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vlanId: ../../../vim/dvs/VmwareDistributedVirtualSwitch/TrunkVlanSpec.rst#vlanId

.. _pvlanId: ../../../vim/dvs/VmwareDistributedVirtualSwitch/PvlanSpec.rst#pvlanId

.. _ipfixEnabled: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VmwarePortConfigPolicy.rst#ipfixEnabled

.. _securityPolicy: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VmwarePortConfigPolicy.rst#securityPolicy

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _defaultPortConfig: ../../../vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#defaultPortConfig

.. _uplinkTeamingPolicy: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VmwarePortConfigPolicy.rst#uplinkTeamingPolicy

.. _vim.dvs.DistributedVirtualPortgroup.PortgroupPolicy: ../../../vim/dvs/DistributedVirtualPortgroup/PortgroupPolicy.rst


vim.dvs.VmwareDistributedVirtualSwitch.VMwarePortgroupPolicy
============================================================
  This class defines the VMware specific configuration for DistributedVirtualPort.
:extends: vim.dvs.DistributedVirtualPortgroup.PortgroupPolicy_
:since: `vSphere API 4.0`_

Attributes:
    vlanOverrideAllowed (`bool`_):

       Allow the setting of `vlanId`_ , trunk `vlanId`_ , or `pvlanId`_ for an individual port to override the setting in `defaultPortConfig`_ of a portgroup.
    uplinkTeamingOverrideAllowed (`bool`_):

       Allow the setting of `uplinkTeamingPolicy`_ for an individual port to override the setting in `defaultPortConfig`_ of a portgroup.
    securityPolicyOverrideAllowed (`bool`_):

       Allow the setting of `securityPolicy`_ for an individual port to override the setting in `defaultPortConfig`_ of a portgroup.
    ipfixOverrideAllowed (`bool`_, optional):

       Allow the setting of `ipfixEnabled`_ for an individual port to override the setting in `defaultPortConfig`_ of a portgroup.
