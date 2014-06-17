.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _PhysicalNicCdpDeviceCapability: ../../../vim/host/PhysicalNic/CdpDeviceCapability.rst

.. _vim.host.PhysicalNic.CdpDeviceCapability: ../../../vim/host/PhysicalNic/CdpDeviceCapability.rst


vim.host.PhysicalNic.CdpInfo
============================
  CDP (Cisco Discovery Protocol) is a link level protocol that allows for discovering the CDP-awared network hardware at either end of a DIRECT connection. It's only good for direct connection because CDP doesn't get forwarded through switches. It's a simple advertisement protocol which beacons information about the switch or host along with some port information. The CDP information allows ESX Server admins to know which Cisco switch port is connected to any given virtual switch uplink (PNIC).
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    cdpVersion (`int`_, optional):

       CDP version. The value is always 1.
    timeout (`int`_, optional):

       This is the periodicity of advertisement, the time between two successive CDP message transmissions
    ttl (`int`_, optional):

       Time-To-Live. the amount of time, in seconds, that a receiver should retain the information contained in the CDP packet.
    samples (`int`_, optional):

       The number of CDP messages we have received from the device.
    devId (`str`_, optional):

       Device ID which identifies the device. By default, the device ID is either the device's fully-qualified host name (including the domain name) or the device's hardware serial number in ASCII.
    address (`str`_, optional):

       The advertised IP address that is assigned to the interface of the device on which the CDP message is sent. The device can advertise all addresses for a given protocol suite and, optionally, can advertise one or more loopback IP addresses. But this property only show the first address.
    portId (`str`_, optional):

       Port ID. An ASCII character string that identifies the port on which the CDP message is sent, e.g. "FastEthernet0/8"
    deviceCapability (`vim.host.PhysicalNic.CdpDeviceCapability`_, optional):

       Device Capability `PhysicalNicCdpDeviceCapability`_ 
    softwareVersion (`str`_, optional):

       Software version on the device. A character string that provides information about the software release version that the device is running. e.g. "Cisco Internetwork Operating Syscisco WS-C2940-8TT-S"
    hardwarePlatform (`str`_, optional):

       Hardware platform. An ASCII character string that describes the hardware platform of the device , e.g. "cisco WS-C2940-8TT-S"
    ipPrefix (`str`_, optional):

       IP prefix. Each IP prefix represents one of the directly connected IP network segments of the local route.
    ipPrefixLen (`int`_, optional):

       ipPrefix length.
    vlan (`int`_, optional):

       The native VLAN of advertising port. The native VLAN is the VLAN to which a port returns when it is not trunking. Also, the native VLAN is the untagged VLAN on an 802.1Q trunk.
    fullDuplex (`bool`_, optional):

       Half/full duplex setting of the advertising port.
    mtu (`int`_, optional):

       MTU, the maximum transmission unit for the advertising port. Possible values are 1500 through 18190.
    systemName (`str`_, optional):

       The configured SNMP system name of the device.
    systemOID (`str`_, optional):

       The configured SNMP system OID of the device.
    mgmtAddr (`str`_, optional):

       The configured IP address of the SNMP management interface for the device.
    location (`str`_, optional):

       The configured location of the device.
