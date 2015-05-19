.. _vim.host.MemoryManagerSystem.VirtualMachineReservationInfo: ../../../../vim/host/MemoryManagerSystem/VirtualMachineReservationInfo.rst

.. _vim.host.MemoryManagerSystem.VirtualMachineReservationInfo.AllocationPolicy: ../../../../vim/host/MemoryManagerSystem/VirtualMachineReservationInfo/AllocationPolicy.rst

vim.host.MemoryManagerSystem.VirtualMachineReservationInfo.AllocationPolicy
===========================================================================
  Means for allocating additional memory for virtual machines.
  :contained by: `vim.host.MemoryManagerSystem.VirtualMachineReservationInfo`_

  :type: `vim.host.MemoryManagerSystem.VirtualMachineReservationInfo.AllocationPolicy`_

  :name: swapMost

values:
--------

swapMost
   Allow most virtual machine memory to be swapped.

swapSome
   Allow some virtual machine memory to be swapped.

swapNone
   Fit all virtual machine memory into reserved host memory.
