.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vim.host.HostBusAdapter: ../../vim/host/HostBusAdapter.rst

.. _vim.host.FibreChannelHba.PortType: ../../vim/host/FibreChannelHba/PortType.rst


vim.host.FibreChannelHba
========================
  This data object type describes the Fibre Channel host bus adapter.
:extends: vim.host.HostBusAdapter_

Attributes:
    portWorldWideName (`long`_):

       The world wide port name for the adapter.
    nodeWorldWideName (`long`_):

       The world wide node name for the adapter.
    portType (`vim.host.FibreChannelHba.PortType`_):

       The type of the fiber channel port.
    speed (`long`_):

       The current operating speed of the adapter in bits per second.
