.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _VMwareVspanSession: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VspanSession.rst

.. _encapsulationVlanId: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VspanSession.rst#encapsulationVlanId

.. _wildcardPortConnecteeType: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VspanPorts.rst#wildcardPortConnecteeType

.. _VMwareDVSVspanSessionType: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VspanSessionType.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.VspanPorts: ../../../vim/dvs/VmwareDistributedVirtualSwitch/VspanPorts.rst


vim.dvs.VmwareDistributedVirtualSwitch.VspanSession
===================================================
  The `VMwareVspanSession`_ data object defines the configuration of a VLAN Services and Protocols for Advanced Networks (VSPAN) session. You use a VSPAN session for the following operations:
   * To mirror network traffic (inbound/outbound) from a set of source entities to a set of destination entities.
   * To assist in troubleshooting.
   * As input for security and other network analysis appliances.
   * 
   * The type of entities that you can specify as source or destination is determined by the session type. You can use uplink distributed virtual ports only for mixed destination mirror VSPAN sessions (mixedDestMirror). For all sessions except mixedDestMirror sessions, you cannot use uplink distributed virtual ports as destination ports. sessionType is required for vSphere Distributed Switch 5.1 and later, ignored for prior version if set.
   * 
   * 
   * 
   * Session Type
   * 
   * Source
   * 
   * Destination
   * 
   * 
   * 
   * mixedDestMirror
   * 
   * Distributed Ports
   * 
   * Distributed Ports + Uplink Ports Name
   * 
   * 
   * 
   * dvPortMirror
   * 
   * Distributed Ports
   * 
   * Distributed Ports
   * 
   * 
   * 
   * remoteMirrorSource
   * 
   * Distributed Ports
   * 
   * Uplink Ports Name
   * 
   * 
   * 
   * remoteMirrorDest
   * 
   * VLAN
   * 
   * Distributed Ports
   * 
   * 
   * 
   * encapRemoteMirrorSource
   * 
   * Distributed Ports
   * 
   * IP address
   * 
   * 
   * 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    key (`str`_, optional):

       The generated key as the identifier for the session.
    name (`str`_, optional):

       The display name.
    description (`str`_, optional):

       The description for the session.
    enabled (`bool`_):

       Whether the session is enabled.
    sourcePortTransmitted (`vim.dvs.VmwareDistributedVirtualSwitch.VspanPorts`_, optional):

       Source ports for which transmitted packets are mirrored.
    sourcePortReceived (`vim.dvs.VmwareDistributedVirtualSwitch.VspanPorts`_, optional):

       Source ports for which received packets are mirrored.
    destinationPort (`vim.dvs.VmwareDistributedVirtualSwitch.VspanPorts`_, optional):

       Destination ports that received the mirrored packets. You cannot use wild card ports as destination ports. If `wildcardPortConnecteeType`_ is set in the value, the reconfigure operation will raise a fault. Also any port designated in the value of this property can not match the wild card source port in any of the Distributed Port Mirroring session.
    encapsulationVlanId (`int`_, optional):

       VLAN ID used to encapsulate the mirrored traffic.
    stripOriginalVlan (`bool`_):

       Whether to strip the original VLAN tag. if false, the original VLAN tag will be preserved on the mirrored traffic. If `encapsulationVlanId`_ has been set and this property is false, the frames will be double tagged with the original VLAN ID as the inner tag.
    mirroredPacketLength (`int`_, optional):

       An integer that describes how much of each frame to mirror. If unset, all of the frame would be mirrored. Setting this property to a smaller value is useful when the consumer will look only at the headers. The value cannot be less than 60.
    normalTrafficAllowed (`bool`_):

       Whether or not destination ports can send and receive "normal" traffic. Setting this to false will make mirror ports be used solely for mirroring and not double as normal access ports.
    sessionType (`str`_, optional):

       Type of the session. See `VMwareDVSVspanSessionType`_ for valid values. Default value is mixedDestMirror if unspecified in a VSPAN create operation.
    samplingRate (`int`_, optional):

       Sampling rate of the session. If its value is n, one of every n packets is mirrored. Valid values are between 1 to 65535, and default value is 1.
