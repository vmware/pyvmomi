.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.MemoryManagerSystem.VirtualMachineReservationInfo
==========================================================
  The VirtualMachineReservationInfo data object type describes the amount of memory that is being reserved for virtual machines on the host, and how additional memory may be acquired.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    virtualMachineMin (`long`_):

       The minimum amount of memory reserved for all running virtual machines, in bytes.
    virtualMachineMax (`long`_):

       The maximum amount of memory reserved for all running virtual machines, in bytes.
    virtualMachineReserved (`long`_):

       The amount of memory reserved for all running virtual machines, in bytes.
    allocationPolicy (`str`_):

       Policy for allocating additional memory for virtual machines.See AllocationPolicy
