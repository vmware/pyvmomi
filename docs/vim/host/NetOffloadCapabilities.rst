
vim.host.NetOffloadCapabilities
===============================
  Offload capabilities are used to optimize virtual machine network performance. When a virtual machine is transmitting on a network, some operations can be offloaded either to the host or to physical hardware. This data object type defines the set of offload capabilities that may be available on a host.This data object type is used both to publish the list of offload capabilities and to contain offload capability policy settings. The network policy logic is built on a two-level inheritance scheme which requires that all settings be optional. As a result, all properties on the NetOffloadCapabilities object must be optional.See `HostNetworkPolicy <vim/host/NetworkPolicy.rst>`_ 
:extends: vmodl.DynamicData_
**deprecated**


Attributes:
    csumOffload (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       (Optional) The flag to indicate whether or not checksum offloading is supported.
    tcpSegmentation (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       (Optional) The flag to indicate whether or not TCP segmentation offloading (TSO) is supported.
    zeroCopyXmit (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       (Optional) The flag to indicate whether or not zero copy transmits are supported.
