
vim.dvs.NetworkResourcePool
===========================
  The `DVSNetworkResourcePool <vim/dvs/NetworkResourcePool.rst>`_ data object describes the resource configuration and management of network resource pools.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Key of the network resource pool.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Name of the network resource pool.
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Description of the network resource pool.
    configVersion (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Configuration version for the network resource pool.
    allocationInfo (`vim.dvs.NetworkResourcePool.AllocationInfo <vim/dvs/NetworkResourcePool/AllocationInfo.rst>`_):

       Resource settings of the resource pool.
