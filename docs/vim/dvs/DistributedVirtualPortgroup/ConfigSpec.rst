
vim.dvs.DistributedVirtualPortgroup.ConfigSpec
==============================================
  The `DVPortgroupConfigSpec <vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst>`_ data object contains configuration data for a `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_ . Use the `ReconfigureDVPortgroup_Task <vim/dvs/DistributedVirtualPortgroup.rst#reconfigure>`_ method to apply the configuration to the portgroup.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    configVersion (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Version string of the configuration that this spec is trying to change. This property is required in reconfiguring a portgroup and should be set to the same value as the `configVersion <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#configVersion>`_ . This property is ignored in creating a portgroup if set.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Name of the portgroup.
    numPorts (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Number of ports in the portgroup. Setting this number larger than the number of existing ports in the portgroup causes new ports to be added to the portgroup to meet the number. Setting this property smaller than the number of existing ports deletes the free ports from the portgroup. If the number cannot be met by deleting free ports, a fault is raised. If new ports are added to the portgroup, they are also added to the switch. For portgroups of type ephemeral this property is ignored.
    portNameFormat (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Format of the name of the ports when ports are created in the portgroup. For details see `portNameFormat <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#portNameFormat>`_ .
    defaultPortConfig (`vim.dvs.DistributedVirtualPort.Setting <vim/dvs/DistributedVirtualPort/Setting.rst>`_, optional):

       Default network setting for all the ports in the portgroup.
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Description of the portgroup.
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Type of portgroup. See `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_ . `DistributedVirtualPortgroupPortgroupType <vim/dvs/DistributedVirtualPortgroup/PortgroupType.rst>`_ for possible values.
    scope ([`vim.ManagedEntity <vim/ManagedEntity.rst>`_], optional):

       Eligible entities that can connect to the port. See `DVPortgroupConfigInfo <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst>`_ . `scope <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#scope>`_ .
    policy (`vim.dvs.DistributedVirtualPortgroup.PortgroupPolicy <vim/dvs/DistributedVirtualPortgroup/PortgroupPolicy.rst>`_, optional):

       Portgroup policy.
    vendorSpecificConfig ([`vim.dvs.KeyedOpaqueBlob <vim/dvs/KeyedOpaqueBlob.rst>`_], optional):

       Opaque binary blob that stores vendor specific configuration.
    autoExpand (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If set to true, this property ignores the limit on the number of ports in the portgroup. When a Virtual Machine/Host tries to connect to the portgroup and there are no free ports available in the portgroup, new ports will be automatically added to the portgroup. The flag is currently supported only for static portgroups.Setting this property to true makes the portgroup a potential candidate for auto-shrink. Once the portgroup has auto-expanded then its disconnected ports are likely to be deleted automatically, as a part of auto-shrink step, if there are more than certain number of free ports. If the portgroup never auto-expanded, then it will never lose any free ports.
