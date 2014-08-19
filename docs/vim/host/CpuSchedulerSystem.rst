
vim.host.CpuSchedulerSystem
===========================
  This managed object provides an interface through which you can gather and configure the host CPU scheduler policies that affect the performance of running virtual machines.Note: This managed object is useful only on platforms where resource management controls are available to optimize the running of virtual machines.


:extends: vim.ExtensibleManagedObject_


Attributes
----------
    hyperthreadInfo (`vim.host.CpuSchedulerSystem.HyperThreadScheduleInfo <vim/host/CpuSchedulerSystem/HyperThreadScheduleInfo.rst>`_):
       The hyperthread configuration for the CpuSchedulerSystem. The existence of this data object type indicates if the CPU scheduler is capable of scheduling hyperthreads as resources.


Methods
-------


EnableHyperThreading():
   Treat hyperthreads as schedulable resources the next time the CPU scheduler starts. If successful, this operation will set the `config <vim/host/CpuSchedulerSystem/HyperThreadScheduleInfo.rst#config>`_ property to "true".


  Privilege:
               Host.Config.HyperThreading



  Args:


  Returns:
    None
         

  Raises:

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the hyperthreading optimization is not available on the host (the boolean `available <vim/host/CpuSchedulerSystem/HyperThreadScheduleInfo.rst#available>`_ is set to false).


DisableHyperThreading():
   Don't treat hyperthreads as schedulable resources the next time the CPU scheduler starts. If successful, this operation will change the configured setting.


  Privilege:
               Host.Config.HyperThreading



  Args:


  Returns:
    None
         

  Raises:

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the hyperthreading optimization is not available on the host (the boolean `available <vim/host/CpuSchedulerSystem/HyperThreadScheduleInfo.rst#available>`_ is set to false).


