.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _enableHyperThreading(): ../../../vim/host/CpuSchedulerSystem.rst#enableHyperThreading

.. _disableHyperthreading(): ../../../vim/host/CpuSchedulerSystem.rst#disableHyperThreading


vim.host.CpuSchedulerSystem.HyperThreadScheduleInfo
===================================================
  This data object type describes the CpuSchedulerSystem configuration for optimizing hyperthreading. The primary hyperthreading optimization employed by the CpuSchedulerSystem is to utilize hyperthreads as additional schedulable resources. Although hyperthreads provide limited additional concurrency, certain workloads (such as idling) can take advantage of these hyperthreads. This is particularly useful for SMP virtual machines that use gang scheduling. (Gang scheduling refers to a situation in which all of a parallel program's tasks are grouped into a "gang" and concurrently scheduled on distinct processors of a parallel computer system.)Changes to the hyperthreading optimization can take effect only after a system restart. Therefore, while it is possible to change the configuration at any time, the change will take effect only on the next boot.
:extends: vmodl.DynamicData_

Attributes:
    available (`bool`_):

       The flag to indicate whether or not hyperthreading optimization is available on the system. This property is set by VMware prior to installation.
    active (`bool`_):

       The flag to indicate whether or not the CPU scheduler is currently treating hyperthreads as schedulable resources. Setting this property involves a successful invocation of either the `enableHyperThreading()`_ method ("true") or the `disableHyperthreading()`_ method ("false"). The property is set once the system is rebooted.
    config (`bool`_):

       The flag to indicate whether or not the CPU scheduler should treat hyperthreads as schedulable resources the next time the CPU scheduler starts.
        * This property is set to "true" by successfully invoking the
        * `enableHyperThreading()`_
        * method.
        * This property is set to "false" by successfully invoking the
        * `disableHyperthreading()`_
        * method.
