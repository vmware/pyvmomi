.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.DistributedVirtualSwitch.SwitchPolicy
=========================================
  The switch usage policy types
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    autoPreInstallAllowed (`bool`_, optional):

       Whether downloading a new proxy VirtualSwitch module to the host is allowed to be automatically executed by the switch.
    autoUpgradeAllowed (`bool`_, optional):

       Whether upgrading of the switch is allowed to be automatically executed by the switch.
    partialUpgradeAllowed (`bool`_, optional):

       Whether to allow upgrading a switch when some of the hosts failed to install the needed module. The vCenter Server will reattempt the pre-install operation of the host module on those failed hosts, whenever they reconnect to vCenter.
