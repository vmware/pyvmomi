.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _portKey: ../../../vim/dvs/PortConnection.rst#portKey

.. _portgroupKey: ../../../vim/dvs/PortConnection.rst#portgroupKey

.. _HostVirtualNic: ../../../vim/host/VirtualNic.rst

.. _vim.host.IpConfig: ../../../vim/host/IpConfig.rst

.. _defaultTcpipStack: ../../../vim/host/NetStackInstance/SystemStackKey.rst#defaultTcpipStack

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostVirtualNicSpec: ../../../vim/host/VirtualNic/Specification.rst

.. _distributedVirtualPort: ../../../vim/host/VirtualNic/Specification.rst#distributedVirtualPort

.. _DistributedVirtualPort: ../../../vim/dvs/DistributedVirtualPort.rst

.. _vim.dvs.PortConnection: ../../../vim/dvs/PortConnection.rst

.. _DistributedVirtualPortgroup: ../../../vim/dvs/DistributedVirtualPortgroup.rst


vim.host.VirtualNic.Specification
=================================
  The `HostVirtualNicSpec`_ data object describes the `HostVirtualNic`_ configuration containing both the configured properties on a virtual NIC and identification information.
:extends: vmodl.DynamicData_

Attributes:
    ip (`vim.host.IpConfig`_, optional):

       IP configuration on the virtual network adapter.
    mac (`str`_, optional):

       Media access control (MAC) address of the virtual network adapter.
    distributedVirtualPort (`vim.dvs.PortConnection`_, optional):

        `DistributedVirtualPort`_ or `DistributedVirtualPortgroup`_ connection. To specify a port connection, set the `portKey`_ property. To specify a portgroup connection, set the `portgroupKey`_ property.
    portgroup (`str`_, optional):

       Portgroup ( `key`_ ) to which the virtual NIC is connected.When reconfiguring a virtual NIC, this property indicates the new portgroup to which the virtual NIC should connect. You can specify this property only if you do not specify `distributedVirtualPort`_ .
    mtu (`int`_, optional):

       Maximum transmission unit for packets size in bytes for the virtual NIC. This property is applicable to VMkernel virtual NICs and will be ignored if specified for service console virtual NICs. If not specified, the Server will use the system default value.
    tsoEnabled (`bool`_, optional):

       Flag enabling or disabling TCP segmentation offset for a virtual NIC. This property is applicable to VMkernel virtual NICs and will be ignored if specified for service console vitual nics. If not specified, a default value of true shall be used.
    netStackInstanceKey (`str`_, optional):

       The NetStackInstance that the vNic uses, the value of this property is default to be `defaultTcpipStack`_ 
