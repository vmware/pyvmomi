.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.ManagedEntity: ../../../vim/ManagedEntity.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _DVPortgroupConfigInfo: ../../../vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst

.. _vim.dvs.KeyedOpaqueBlob: ../../../vim/dvs/KeyedOpaqueBlob.rst

.. _DistributedVirtualPortgroup: ../../../vim/dvs/DistributedVirtualPortgroup.rst

.. _vim.DistributedVirtualSwitch: ../../../vim/DistributedVirtualSwitch.rst

.. _DistributedVirtualPortgroupMetaTagName: ../../../vim/dvs/DistributedVirtualPortgroup/MetaTagName.rst

.. _vim.dvs.DistributedVirtualPort.Setting: ../../../vim/dvs/DistributedVirtualPort/Setting.rst

.. _DistributedVirtualPortgroupPortgroupType: ../../../vim/dvs/DistributedVirtualPortgroup/PortgroupType.rst

.. _vim.dvs.DistributedVirtualPortgroup.PortgroupPolicy: ../../../vim/dvs/DistributedVirtualPortgroup/PortgroupPolicy.rst


vim.dvs.DistributedVirtualPortgroup.ConfigInfo
==============================================
  The `DVPortgroupConfigInfo`_ data object defines the configuration of a `DistributedVirtualPortgroup`_ . .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    key (`str`_):

       Key of the portgroup.
    name (`str`_):

       Name of the portgroup.
    numPorts (`int`_):

       Number of ports in the portgroup.
    distributedVirtualSwitch (`vim.DistributedVirtualSwitch`_, optional):

       Distributed virtual switch that the portgroup is defined on. This property should always be set unless the user's setting does not have System.Read privilege on the object referred to by this property.
    defaultPortConfig (`vim.dvs.DistributedVirtualPort.Setting`_, optional):

       Common network setting for all the ports in the portgroup.
    description (`str`_, optional):

       Description of the portgroup.
    type (`str`_):

       Type of portgroup. See `DistributedVirtualPortgroup`_ . `DistributedVirtualPortgroupPortgroupType`_ for possible values.
    policy (`vim.dvs.DistributedVirtualPortgroup.PortgroupPolicy`_):

       Portgroup policy.
    portNameFormat (`str`_, optional):

       If set, a name will be automatically generated based on this format string for a port when it is created in or moved into the portgroup. The format string can contain meta tags that will be resolved to the corresponding values in generating a name, if applicable for the port at the time of name generation.To insert a meta tag in the format string, enclose the names defined as meta tag names inside angle brackets. See `DistributedVirtualPortgroupMetaTagName`_ for a list of currently available meta tags. For example, "redNetwork-portIndex" and "dvsName-pnicportIndex" result in generated port names like "redNetwork-2" and "switch-pnic3".If a meta tag is recognized, but there is no applicable value, the tag will be expanded to empty string. If an arbitrary name appears inside a "" pair and is not recognized as one of the defined meta tags, the substring is treated as-is and appear unchanged in the generated name.To prevent a meta tag from being expanded, prefix the meta tag with a '\' (backslash). For example, the format string "abc\portIndexdef" results in the generated port name "abcportIndexdef".
    scope ([`vim.ManagedEntity`_], optional):

       Eligible entities that can connect to the portgroup. If unset, there is no restriction on which entity can connect to the portgroup. If set, only the entities in the specified list or their child entities are allowed to connect to the portgroup. If scopes are defined at both port and portgroup level, they are taken as an "AND" relationship. If such a relationship doesn't make sense, the reconfigure operation will raise an exception.
    vendorSpecificConfig ([`vim.dvs.KeyedOpaqueBlob`_], optional):

       Opaque binary blob that stores vendor specific configuration.
    configVersion (`str`_, optional):

       Configuration version number.
    autoExpand (`bool`_, optional):

       If set to true, this property ignores the limit on the number of ports in the portgroup. When a Virtual Machine/Host tries to connect to the portgroup and there are no free ports available in the portgroup, new ports will be automatically added to the portgroup. The flag is currently supported only for static portgroups.When this property is set to true, the portgroup becomes a potential candidate for auto-shrink. Once the portgroup has auto-expanded then its disconnected ports are likely to be deleted automatically, as a part of auto-shrink step, if there are more than certain number of free ports. If the portgroup never auto-expanded, then it will never lose any free ports.
