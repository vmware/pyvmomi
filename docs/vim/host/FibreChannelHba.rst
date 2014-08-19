
vim.host.FibreChannelHba
========================
  This data object type describes the Fibre Channel host bus adapter.
:extends: vim.host.HostBusAdapter_

Attributes:
    portWorldWideName (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The world wide port name for the adapter.
    nodeWorldWideName (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The world wide node name for the adapter.
    portType (`vim.host.FibreChannelHba.PortType <vim/host/FibreChannelHba/PortType.rst>`_):

       The type of the fiber channel port.
    speed (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The current operating speed of the adapter in bits per second.
