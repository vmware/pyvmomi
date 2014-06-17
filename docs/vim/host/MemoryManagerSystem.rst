.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.fault.NotSupported: ../../vmodl/fault/NotSupported.rst

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vim.ExtensibleManagedObject: ../../vim/ExtensibleManagedObject.rst

.. _vim.host.MemoryManagerSystem.ServiceConsoleReservationInfo: ../../vim/host/MemoryManagerSystem/ServiceConsoleReservationInfo.rst

.. _vim.host.MemoryManagerSystem.VirtualMachineReservationSpec: ../../vim/host/MemoryManagerSystem/VirtualMachineReservationSpec.rst

.. _vim.host.MemoryManagerSystem.VirtualMachineReservationInfo: ../../vim/host/MemoryManagerSystem/VirtualMachineReservationInfo.rst


vim.host.MemoryManagerSystem
============================
  The MemoryManagerSystem managed object provides an interface through which the host memory management policies that affect the performance of running virtual machines can be gathered and configured.


:extends: vim.ExtensibleManagedObject_


Attributes
----------
    consoleReservationInfo (`vim.host.MemoryManagerSystem.ServiceConsoleReservationInfo`_):
       Service console reservation information for the memory manager. The existence of this data object indicates if the service console memory reservation must be configured for this host.
    virtualMachineReservationInfo (`vim.host.MemoryManagerSystem.VirtualMachineReservationInfo`_):
       Virtual machine reservation information for the memory manager. The existence of this data object indicates if the virtual machine memory reservation must be configured for this host.


Methods
-------


ReconfigureServiceConsoleReservation(cfgBytes):
   Sets the configured service console memory reservation. This change affects only the serviceConsoleReservedCfg property. The configuration change propagates to the other properties after the next boot.


  Privilege:
               Host.Config.Memory



  Args:
    cfgBytes (`long`_):




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       if cfgBytes is negative or is greater than the total memory available.

    `vmodl.fault.NotSupported`_: 
       if the service console memory reservation does not apply to this host. The existence of the consoleReservation property will indicate if this feature is applicable.


ReconfigureVirtualMachineReservation(spec):
   Updates the virtual machine reservation information.
  since: `VI API 2.5`_


  Privilege:
               Host.Config.Memory



  Args:
    spec (`vim.host.MemoryManagerSystem.VirtualMachineReservationSpec`_):




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       if virtualMachineReserved is negative or is greater than the maximum amount reservable.

    `vmodl.fault.NotSupported`_: 
       if the virtualMachine reservation does not apply to this host. The existence of the virtualMachineReservationInfo property will indicate if this feature is applicable.


