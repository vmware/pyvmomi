.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _DVSNetworkResourcePool: ../../vim/dvs/NetworkResourcePool.rst

.. _vim.dvs.NetworkResourcePool.AllocationInfo: ../../vim/dvs/NetworkResourcePool/AllocationInfo.rst


vim.dvs.NetworkResourcePool
===========================
  The `DVSNetworkResourcePool`_ data object describes the resource configuration and management of network resource pools.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    key (`str`_):

       Key of the network resource pool.
    name (`str`_, optional):

       Name of the network resource pool.
    description (`str`_, optional):

       Description of the network resource pool.
    configVersion (`str`_):

       Configuration version for the network resource pool.
    allocationInfo (`vim.dvs.NetworkResourcePool.AllocationInfo`_):

       Resource settings of the resource pool.
