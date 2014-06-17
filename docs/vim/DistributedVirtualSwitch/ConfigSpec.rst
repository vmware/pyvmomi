.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _DVSConfigSpec: ../../vim/DistributedVirtualSwitch/ConfigSpec.rst

.. _configVersion: ../../vim/DistributedVirtualSwitch/ConfigInfo.rst#configVersion

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _ReconfigureDvs_Task: ../../vim/DistributedVirtualSwitch.rst#reconfigure

.. _vim.dvs.KeyedOpaqueBlob: ../../vim/dvs/KeyedOpaqueBlob.rst

.. _DistributedVirtualSwitch: ../../vim/DistributedVirtualSwitch.rst

.. _QueryDvsCheckCompatibility: ../../vim/dvs/DistributedVirtualSwitchManager.rst#checkCompatibility

.. _vim.dvs.HostMember.ConfigSpec: ../../vim/dvs/HostMember/ConfigSpec.rst

.. _vim.dvs.DistributedVirtualPortgroup: ../../vim/dvs/DistributedVirtualPortgroup.rst

.. _vim.dvs.DistributedVirtualPort.Setting: ../../vim/dvs/DistributedVirtualPort/Setting.rst

.. _vim.DistributedVirtualSwitch.ContactInfo: ../../vim/DistributedVirtualSwitch/ContactInfo.rst

.. _vim.DistributedVirtualSwitch.SwitchPolicy: ../../vim/DistributedVirtualSwitch/SwitchPolicy.rst

.. _vim.DistributedVirtualSwitch.UplinkPortPolicy: ../../vim/DistributedVirtualSwitch/UplinkPortPolicy.rst


vim.DistributedVirtualSwitch.ConfigSpec
=======================================
  The `DVSConfigSpec`_ data object contains configuration data for a `DistributedVirtualSwitch`_ . Use the `ReconfigureDvs_Task`_ method to apply the configuration to the switch.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    configVersion (`str`_, optional):

       The version string of the configuration that this spec is trying to change. This property is required in reconfiguring a switch and should be set to the same value as `configVersion`_ . This property is ignored during switch creation.
    name (`str`_, optional):

       The name of the switch. Must be unique in the parent folder.
    numStandalonePorts (`int`_, optional):

       The number of standalone ports in the switch. Standalone ports are ports that do not belong to any portgroup. If set to a number larger than number of existing standalone ports in the switch, new ports get created to meet the number. If set to a number smaller than the number of existing standalone ports, free ports (uplink ports excluded) are deleted to meet the number. If the set number cannot be met by deleting free standalone ports, a fault is raised.
    maxPorts (`int`_, optional):

       The maximum number of DistributedVirtualPorts allowed in the switch. If specified in a reconfigure operation, this number cannot be smaller than the number of existing DistributedVirtualPorts.
    uplinkPortPolicy (`vim.DistributedVirtualSwitch.UplinkPortPolicy`_, optional):

       The uplink port policy.
    uplinkPortgroup (`vim.dvs.DistributedVirtualPortgroup`_, optional):

       The uplink portgroups.
    defaultPortConfig (`vim.dvs.DistributedVirtualPort.Setting`_, optional):

       The default configuration for ports.
    host (`vim.dvs.HostMember.ConfigSpec`_, optional):

       The host member specification. A particular host should have only one entry in this array. Duplicate entries for the same host will raise a fault. The host version should be compatible with the version of `DistributedVirtualSwitch`_ . Use `QueryDvsCheckCompatibility`_ to check for compatibility.
    extensionKey (`str`_, optional):

       The key of the extension registered by a remote server that controls the switch.
    description (`str`_, optional):

       Set the description string of the switch.
    policy (`vim.DistributedVirtualSwitch.SwitchPolicy`_, optional):

       The usage policy of the switch.
    vendorSpecificConfig (`vim.dvs.KeyedOpaqueBlob`_, optional):

       Set the opaque blob that stores vendor specific configuration.
    contact (`vim.DistributedVirtualSwitch.ContactInfo`_, optional):

       Set the human operator contact information.
    switchIpAddress (`str`_, optional):

       IP address for the switch, specified using IPv4 dot notation. The utility of this address is defined by other switch features.
    defaultProxySwitchMaxNumPorts (`int`_, optional):

       The default host proxy switch maximum port number
