.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.MemoryManagerSystem.VirtualMachineReservationSpec
==========================================================
  The VirtualMachineReservationSpec data object specifies configurable parameters for virtual machine memory reservation.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    virtualMachineReserved (`long`_, optional):

       The amount of memory reserved for all running virtual machines, in bytes.
    allocationPolicy (`str`_, optional):

       Policy for allocating additional memory for virtual machines.See VirtualMachineReservationInfo.AllocationPolicy
