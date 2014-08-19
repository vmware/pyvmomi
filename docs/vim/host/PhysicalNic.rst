
vim.host.PhysicalNic
====================
  This data object type describes the physical network adapter as seen by the primary operating system.
:extends: vmodl.DynamicData_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The linkable identifier.
    device (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The device name of the physical network adapter.
    pci (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Device hash of the PCI device corresponding to this physical network adapter.
    driver (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The name of the driver.
    linkSpeed (`vim.host.PhysicalNic.LinkSpeedDuplex <vim/host/PhysicalNic/LinkSpeedDuplex.rst>`_, optional):

       The current link state of the physical network adapter. If this object is not set, then the link is down.
    validLinkSpecification ([`vim.host.PhysicalNic.LinkSpeedDuplex <vim/host/PhysicalNic/LinkSpeedDuplex.rst>`_], optional):

       The valid combinations of speed and duplexity for this physical network adapter. The speed and the duplex settings usually must be configured as a pair. This array lists all the valid combinations available for a physical network adapter.Autonegotiate is not listed as one of the combinations supported. If is implicitly supported by the physical network adapter unless `autoNegotiateSupported <vim/host/PhysicalNic.rst#autoNegotiateSupported>`_ is set to false.
    spec (`vim.host.PhysicalNic.Specification <vim/host/PhysicalNic/Specification.rst>`_):

       The specification of the physical network adapter.
    wakeOnLanSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether the NIC is wake-on-LAN capable
    mac (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The media access control (MAC) address of the physical network adapter.
    fcoeConfiguration (`vim.host.FcoeConfig <vim/host/FcoeConfig.rst>`_, optional):

       The FCoE configuration of the physical network adapter.
    vmDirectPathGen2Supported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag indicating whether the NIC supports VMDirectPath Gen 2. Note that this is only an indicator of the capabilities of this NIC, not of the whole host.If the host software is not capable of VMDirectPath Gen 2, this property will be unset, as the host cannot provide information on the NIC capability.See `vmDirectPathGen2Supported <vim/host/Capability.rst#vmDirectPathGen2Supported>`_ 
    vmDirectPathGen2SupportedMode (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If `vmDirectPathGen2Supported <vim/host/PhysicalNic.rst#vmDirectPathGen2Supported>`_ is true, this property advertises the VMDirectPath Gen 2 mode supported by this NIC (chosen from `PhysicalNicVmDirectPathGen2SupportedMode <vim/host/PhysicalNic/VmDirectPathGen2SupportedMode.rst>`_ ). A mode may require that the associated vSphere Distributed Switch have a particular ProductSpec in order for network passthrough to be possible.
    resourcePoolSchedulerAllowed (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag indicating whether the NIC allows resource pool based scheduling for network I/O control.
    resourcePoolSchedulerDisallowedReason ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       If `resourcePoolSchedulerAllowed <vim/host/PhysicalNic.rst#resourcePoolSchedulerAllowed>`_ is false, this property advertises the reason for disallowing resource scheduling on this NIC. The reasons may be one of `PhysicalNicResourcePoolSchedulerDisallowedReason <vim/host/PhysicalNic/ResourcePoolSchedulerDisallowedReason.rst>`_ 
    autoNegotiateSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If set the flag indicates if the physical network adapter supports autonegotiate.
