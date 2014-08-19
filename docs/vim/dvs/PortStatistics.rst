
vim.dvs.PortStatistics
======================
  Statistic data of a DistributedVirtualPort.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    packetsInMulticast (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of multicast packets received.
    packetsOutMulticast (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of multicast packets forwarded.
    bytesInMulticast (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of bytes received from multicast packets.
    bytesOutMulticast (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of bytes forwarded from multicast packets.
    packetsInUnicast (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of unicast packets received.
    packetsOutUnicast (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of unicast packets forwarded.
    bytesInUnicast (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of bytes received from unicast packets.
    bytesOutUnicast (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of bytes forwarded from unicast packets.
    packetsInBroadcast (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of broadcast packets received.
    packetsOutBroadcast (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of broadcast packets forwarded.
    bytesInBroadcast (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of bytes received from broadcast packets.
    bytesOutBroadcast (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of bytes forwarded from broadcast packets.
    packetsInDropped (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of received packets dropped.
    packetsOutDropped (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of packets to be forwarded dropped.
    packetsInException (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of packets received that cause an exception.
    packetsOutException (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of packets to be forwarded that cause an exception.
