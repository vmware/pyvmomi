
vim.ResourcePlanningManager.InventoryDescription
================================================
  Data object to capture all information needed to describe a sample inventory.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    numHosts (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of hosts.
    numVirtualMachines (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of virtual machines.
    numResourcePools (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The number of resource pools. Default value is equal to numHosts
    numClusters (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The number of clusters. Default value is equal to numHosts/5.
    numCpuDev (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The number cpu devices per host. Default value is 4.
    numNetDev (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The number network devices per host. Default value is 2.
    numDiskDev (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The number disk devices per host. Default value is 10.
    numvCpuDev (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The number cpu devices per vm. Default value is 2.
    numvNetDev (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The number network devices per vm. Default value is 1.
    numvDiskDev (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The number disk devices per vm. Default value is 4.
