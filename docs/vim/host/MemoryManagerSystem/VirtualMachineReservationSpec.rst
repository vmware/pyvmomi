
vim.host.MemoryManagerSystem.VirtualMachineReservationSpec
==========================================================
  The VirtualMachineReservationSpec data object specifies configurable parameters for virtual machine memory reservation.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    virtualMachineReserved (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The amount of memory reserved for all running virtual machines, in bytes.
    allocationPolicy (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Policy for allocating additional memory for virtual machines.See VirtualMachineReservationInfo.AllocationPolicy
