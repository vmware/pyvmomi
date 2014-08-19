
vim.cluster.DrsMigration
========================
  Describes a single virtual machine migration.
:extends: vmodl.DynamicData_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       A unique key that identifies this recommendation. This is used as an argument to ComputeResource.applyRecommendation.
    time (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       The time this recommendation was computed.
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):

       The virtual machine selected for migration.
    cpuLoad (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Current CPU load for the virtual machine, in MHz. This property is only populated for recommendations.
    memoryLoad (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Current memory load for the virtual machine, in bytes. This field is only populated for recommendations.
    source (`vim.HostSystem <vim/HostSystem.rst>`_):

       Source host.
    sourceCpuLoad (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Current CPU load on the source host, in MHz.
    sourceMemoryLoad (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Current memory usage on the source host, in bytes.
    destination (`vim.HostSystem <vim/HostSystem.rst>`_):

       Destination host.
    destinationCpuLoad (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Current CPU load on the destination host, in MHz.
    destinationMemoryLoad (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Current memory usage on the destination host, in bytes.
