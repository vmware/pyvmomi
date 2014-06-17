.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.ResourcePlanningManager.InventoryDescription
================================================
  Data object to capture all information needed to describe a sample inventory.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    numHosts (`int`_):

       The number of hosts.
    numVirtualMachines (`int`_):

       The number of virtual machines.
    numResourcePools (`int`_, optional):

       The number of resource pools. Default value is equal to numHosts
    numClusters (`int`_, optional):

       The number of clusters. Default value is equal to numHosts/5.
    numCpuDev (`int`_, optional):

       The number cpu devices per host. Default value is 4.
    numNetDev (`int`_, optional):

       The number network devices per host. Default value is 2.
    numDiskDev (`int`_, optional):

       The number disk devices per host. Default value is 10.
    numvCpuDev (`int`_, optional):

       The number cpu devices per vm. Default value is 2.
    numvNetDev (`int`_, optional):

       The number network devices per vm. Default value is 1.
    numvDiskDev (`int`_, optional):

       The number disk devices per vm. Default value is 4.
