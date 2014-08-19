
vim.host.VirtualNic.Specification
=================================
  The `HostVirtualNicSpec <vim/host/VirtualNic/Specification.rst>`_ data object describes the `HostVirtualNic <vim/host/VirtualNic.rst>`_ configuration containing both the configured properties on a virtual NIC and identification information.
:extends: vmodl.DynamicData_

Attributes:
    ip (`vim.host.IpConfig <vim/host/IpConfig.rst>`_, optional):

       IP configuration on the virtual network adapter.
    mac (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Media access control (MAC) address of the virtual network adapter.
    distributedVirtualPort (`vim.dvs.PortConnection <vim/dvs/PortConnection.rst>`_, optional):

        `DistributedVirtualPort <vim/dvs/DistributedVirtualPort.rst>`_ or `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_ connection. To specify a port connection, set the `portKey <vim/dvs/PortConnection.rst#portKey>`_ property. To specify a portgroup connection, set the `portgroupKey <vim/dvs/PortConnection.rst#portgroupKey>`_ property.
    portgroup (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Portgroup ( `key <vim/dvs/DistributedVirtualPortgroup.rst#key>`_ ) to which the virtual NIC is connected.When reconfiguring a virtual NIC, this property indicates the new portgroup to which the virtual NIC should connect. You can specify this property only if you do not specify `distributedVirtualPort <vim/host/VirtualNic/Specification.rst#distributedVirtualPort>`_ .
    mtu (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Maximum transmission unit for packets size in bytes for the virtual NIC. This property is applicable to VMkernel virtual NICs and will be ignored if specified for service console virtual NICs. If not specified, the Server will use the system default value.
    tsoEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag enabling or disabling TCP segmentation offset for a virtual NIC. This property is applicable to VMkernel virtual NICs and will be ignored if specified for service console vitual nics. If not specified, a default value of true shall be used.
    netStackInstanceKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The NetStackInstance that the vNic uses, the value of this property is default to be `defaultTcpipStack <vim/host/NetStackInstance/SystemStackKey.rst#defaultTcpipStack>`_ 
