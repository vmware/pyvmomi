
vim.dvs.NetworkResourcePool.ConfigSpec
======================================
  The `DVSNetworkResourcePoolConfigSpec <vim/dvs/NetworkResourcePool/ConfigSpec.rst>`_ data object contains properties to create or update a network resource pool for a distributed virtual switch.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Key of the network resource pool. The property is ignored for `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ . `AddNetworkResourcePool <vim/DistributedVirtualSwitch.rst#addNetworkResourcePool>`_ operations.
    configVersion (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Unique identifier for a given version of the configuration. Each change to the configuration will update this value. This is typically implemented as a non-decreasing count or a time-stamp. However, a client should always treat this as an opaque string.If you specify the configuration version when you update the resource configuration, the Server will apply the changes only if the specified identifier matches the current `DVSNetworkResourcePool <vim/dvs/NetworkResourcePool.rst>`_ . `configVersion <vim/dvs/NetworkResourcePool.rst#configVersion>`_ value. You can use this field to guard against updates that may have occurred between the time when the client reads `configVersion <vim/dvs/NetworkResourcePool.rst#configVersion>`_ and when the configuration is applied.
    allocationInfo (`vim.dvs.NetworkResourcePool.AllocationInfo <vim/dvs/NetworkResourcePool/AllocationInfo.rst>`_, optional):

       Network resource allocation for the network resource pool.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       User defined name for the resource pool. The property is required for `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ . `AddNetworkResourcePool <vim/DistributedVirtualSwitch.rst#addNetworkResourcePool>`_ operations.
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       User-defined description for the resource pool.
