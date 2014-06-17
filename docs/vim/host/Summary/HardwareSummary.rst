.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _short: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.SystemIdentificationInfo: ../../../vim/host/SystemIdentificationInfo.rst


vim.host.Summary.HardwareSummary
================================
  This data object type summarizes hardware used by the host.
:extends: vmodl.DynamicData_

Attributes:
    vendor (`str`_):

       The hardware vendor identification.
    model (`str`_):

       The system model identification.
    uuid (`str`_):

       The hardware BIOS identification.
    otherIdentifyingInfo (`vim.host.SystemIdentificationInfo`_, optional):

       Other identification information. This information may be vendor specific.
    memorySize (`long`_):

       The physical memory size in bytes.
    cpuModel (`str`_):

       The CPU model.
    cpuMhz (`int`_):

       The speed of the CPU cores. This is an average value if there are multiple speeds. The product of cpuMhz and numCpuCores is approximately equal to the sum of the MHz for all the individual cores on the host.
    numCpuPkgs (`short`_):

       Number of physical CPU packages on the host. Physical CPU packages are chips that contain one or more processors. Processors contained by a package are also known as CPU cores. For example, one dual-core package is comprised of one chip that contains two CPU cores.
    numCpuCores (`short`_):

       Number of physical CPU cores on the host. Physical CPU cores are the processors contained by a CPU package.
    numCpuThreads (`short`_):

       Number of physical CPU threads on the host.
    numNics (`int`_):

       The number of network adapters.
    numHBAs (`int`_):

       The number of host bus adapters (HBAs).
