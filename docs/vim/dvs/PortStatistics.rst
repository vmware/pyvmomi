.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.dvs.PortStatistics
======================
  Statistic data of a DistributedVirtualPort.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    packetsInMulticast (`long`_):

       The number of multicast packets received.
    packetsOutMulticast (`long`_):

       The number of multicast packets forwarded.
    bytesInMulticast (`long`_):

       The number of bytes received from multicast packets.
    bytesOutMulticast (`long`_):

       The number of bytes forwarded from multicast packets.
    packetsInUnicast (`long`_):

       The number of unicast packets received.
    packetsOutUnicast (`long`_):

       The number of unicast packets forwarded.
    bytesInUnicast (`long`_):

       The number of bytes received from unicast packets.
    bytesOutUnicast (`long`_):

       The number of bytes forwarded from unicast packets.
    packetsInBroadcast (`long`_):

       The number of broadcast packets received.
    packetsOutBroadcast (`long`_):

       The number of broadcast packets forwarded.
    bytesInBroadcast (`long`_):

       The number of bytes received from broadcast packets.
    bytesOutBroadcast (`long`_):

       The number of bytes forwarded from broadcast packets.
    packetsInDropped (`long`_):

       The number of received packets dropped.
    packetsOutDropped (`long`_):

       The number of packets to be forwarded dropped.
    packetsInException (`long`_):

       The number of packets received that cause an exception.
    packetsOutException (`long`_):

       The number of packets to be forwarded that cause an exception.
