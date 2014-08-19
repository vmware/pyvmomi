
vim.host.MemoryManagerSystem.ServiceConsoleReservationInfo
==========================================================
  The ServiceConsoleReservationInfo data object type describes the amount of memory that is being reserved by the service console. Memory reserved for use by the service console is a hard reservation that cannot be changed except across hardware restarts.This memory that is reserved for the service console is used primarily to provide system management services. In addition, a small overhead is needed by each virtual machine on the service console.The only property of the data object that can be changed directly is the serviceConsoleReservedCfg property. This property indicates how much memory should be reserved for the service console on the next boot. In most cases, this amount is the same as the current reservation.
:extends: vmodl.DynamicData_

Attributes:
    serviceConsoleReservedCfg (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The amount of memory that should be reserved for the service console on the next boot.
    serviceConsoleReserved (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The amount of memory that is currently reserved for the service console.
    unreserved (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The amount of memory that is not reserved for use by the service console.
