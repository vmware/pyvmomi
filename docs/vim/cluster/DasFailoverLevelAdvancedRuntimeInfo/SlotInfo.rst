.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.cluster.DasFailoverLevelAdvancedRuntimeInfo.SlotInfo
========================================================
  A slot represents an amount of memory and cpu resources on a physical host for use by a virtual machine. It is used in computing the resources to be reserved for failover.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    numVcpus (`int`_):

       The number of virtual cpus of a slot is defined as the maximum number of virtual cpus any powered on virtual machine has.
    cpuMHz (`int`_):

       The cpu speed of a slot is defined as the maximum cpu reservation of any powered on virtual machine in the cluster, or any otherwise defined minimum, whichever is larger.
    memoryMB (`int`_):

       The memory size of a slot is defined as the maximum memory reservation plus memory overhead of any powered on virtual machine in the cluster, or any otherwise defined minimum, whichever is larger.
