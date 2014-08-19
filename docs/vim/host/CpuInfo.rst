
vim.host.CpuInfo
================
  Information about the CPUs.
:extends: vmodl.DynamicData_

Attributes:
    numCpuPackages (`short <https://docs.python.org/2/library/stdtypes.html>`_):

       Number of physical CPU packages on the host.
    numCpuCores (`short <https://docs.python.org/2/library/stdtypes.html>`_):

       Number of physical CPU cores on the host.
    numCpuThreads (`short <https://docs.python.org/2/library/stdtypes.html>`_):

       Number of physical CPU threads on the host.
    hz (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       CPU speed per core. This might be an averaged value if the speed is not uniform across all cores. The total CPU speed of the box is defined as hz * numCpuCores
