.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vim.HostSystem: ../../vim/HostSystem.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.VirtualMachine: ../../vim/VirtualMachine.rst


vim.cluster.DrsMigration
========================
  Describes a single virtual machine migration.
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_):

       A unique key that identifies this recommendation. This is used as an argument to ComputeResource.applyRecommendation.
    time (`datetime`_):

       The time this recommendation was computed.
    vm (`vim.VirtualMachine`_):

       The virtual machine selected for migration.
    cpuLoad (`int`_, optional):

       Current CPU load for the virtual machine, in MHz. This property is only populated for recommendations.
    memoryLoad (`long`_, optional):

       Current memory load for the virtual machine, in bytes. This field is only populated for recommendations.
    source (`vim.HostSystem`_):

       Source host.
    sourceCpuLoad (`int`_, optional):

       Current CPU load on the source host, in MHz.
    sourceMemoryLoad (`long`_, optional):

       Current memory usage on the source host, in bytes.
    destination (`vim.HostSystem`_):

       Destination host.
    destinationCpuLoad (`int`_, optional):

       Current CPU load on the destination host, in MHz.
    destinationMemoryLoad (`long`_, optional):

       Current memory usage on the destination host, in bytes.
