
vim.host.HostBusAdapter
=======================
  This data object type describes the bus adapter for the host. A host bus adapter (HBA) is a hardware or software adapter that connects the host to storage devices.
:extends: vmodl.DynamicData_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The linkable identifier.
    device (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The device name of host bus adapter.
    bus (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The host bus number.
    status (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The operational status of the adapter. Valid values include "online", "offline", "unbound", and "unknown".
    model (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The model name of the host bus adapter.
    driver (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The name of the driver.
    pci (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The Peripheral Connect Interface (PCI) ID of the device representing the host bus adapter.
