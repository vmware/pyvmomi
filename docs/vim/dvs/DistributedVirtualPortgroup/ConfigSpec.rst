.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _scope: ../../../vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#scope

.. _configVersion: ../../../vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#configVersion

.. _portNameFormat: ../../../vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#portNameFormat

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.ManagedEntity: ../../../vim/ManagedEntity.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _DVPortgroupConfigSpec: ../../../vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst

.. _DVPortgroupConfigInfo: ../../../vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst

.. _vim.dvs.KeyedOpaqueBlob: ../../../vim/dvs/KeyedOpaqueBlob.rst

.. _DistributedVirtualPortgroup: ../../../vim/dvs/DistributedVirtualPortgroup.rst

.. _ReconfigureDVPortgroup_Task: ../../../vim/dvs/DistributedVirtualPortgroup.rst#reconfigure

.. _vim.dvs.DistributedVirtualPort.Setting: ../../../vim/dvs/DistributedVirtualPort/Setting.rst

.. _DistributedVirtualPortgroupPortgroupType: ../../../vim/dvs/DistributedVirtualPortgroup/PortgroupType.rst

.. _vim.dvs.DistributedVirtualPortgroup.PortgroupPolicy: ../../../vim/dvs/DistributedVirtualPortgroup/PortgroupPolicy.rst


vim.dvs.DistributedVirtualPortgroup.ConfigSpec
==============================================
  The `DVPortgroupConfigSpec`_ data object contains configuration data for a `DistributedVirtualPortgroup`_ . Use the `ReconfigureDVPortgroup_Task`_ method to apply the configuration to the portgroup.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    configVersion (`str`_, optional):

       Version string of the configuration that this spec is trying to change. This property is required in reconfiguring a portgroup and should be set to the same value as the `configVersion`_ . This property is ignored in creating a portgroup if set.
    name (`str`_, optional):

       Name of the portgroup.
    numPorts (`int`_, optional):

       Number of ports in the portgroup. Setting this number larger than the number of existing ports in the portgroup causes new ports to be added to the portgroup to meet the number. Setting this property smaller than the number of existing ports deletes the free ports from the portgroup. If the number cannot be met by deleting free ports, a fault is raised. If new ports are added to the portgroup, they are also added to the switch. For portgroups of type ephemeral this property is ignored.
    portNameFormat (`str`_, optional):

       Format of the name of the ports when ports are created in the portgroup. For details see `portNameFormat`_ .
    defaultPortConfig (`vim.dvs.DistributedVirtualPort.Setting`_, optional):

       Default network setting for all the ports in the portgroup.
    description (`str`_, optional):

       Description of the portgroup.
    type (`str`_, optional):

       Type of portgroup. See `DistributedVirtualPortgroup`_ . `DistributedVirtualPortgroupPortgroupType`_ for possible values.
    scope (`vim.ManagedEntity`_, optional):

       Eligible entities that can connect to the port. See `DVPortgroupConfigInfo`_ . `scope`_ .
    policy (`vim.dvs.DistributedVirtualPortgroup.PortgroupPolicy`_, optional):

       Portgroup policy.
    vendorSpecificConfig (`vim.dvs.KeyedOpaqueBlob`_, optional):

       Opaque binary blob that stores vendor specific configuration.
    autoExpand (`bool`_, optional):

       If set to true, this property ignores the limit on the number of ports in the portgroup. When a Virtual Machine/Host tries to connect to the portgroup and there are no free ports available in the portgroup, new ports will be automatically added to the portgroup. The flag is currently supported only for static portgroups.Setting this property to true makes the portgroup a potential candidate for auto-shrink. Once the portgroup has auto-expanded then its disconnected ports are likely to be deleted automatically, as a part of auto-shrink step, if there are more than certain number of free ports. If the portgroup never auto-expanded, then it will never lose any free ports.
