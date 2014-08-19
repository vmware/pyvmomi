
vim.vm.ConfigOption
===================
  This configuration data object type contains information about the execution environment for a virtual machine. This includes information about which features are supported, such as:
   * Which guest operating systems are supported.
   * How devices are emulated. For example, that a CD-ROM drive can be emulated with a file or that a serial port can be emulated with a pipe.
   * VirtualCenter can provide a broader environment than any single physical host. This is a departure from traditional virtualization approaches, which rely on the host system to define the environment for virtual machines. This data object describes environment capabilities and is used by VirtualCenter to choose hosts on which to run virtual machines.
:extends: vmodl.DynamicData_

Attributes:
    version (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The version corresponding to this configOption.
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       A description string for this configOption.
    guestOSDescriptor ([`vim.vm.GuestOsDescriptor <vim/vm/GuestOsDescriptor.rst>`_]):

       List of supported guest operating systems. The choice of guest operating system may limit the set of valid devices. For example, you cannot select Vmxnet with all guest operating systems.
    guestOSDefaultIndex (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Index into guestOsDescriptor array denoting the default guest operating system.
    hardwareOptions (`vim.vm.VirtualHardwareOption <vim/vm/VirtualHardwareOption.rst>`_):

       Processor, memory, and virtual device options for a virtual machine.
    capabilities (`vim.vm.Capability <vim/vm/Capability.rst>`_):

       Capabilities supported by a virtual machine.
    datastore (`vim.vm.DatastoreOption <vim/vm/DatastoreOption.rst>`_):

       The datastore options for this virtual machine.
    defaultDevice ([`vim.vm.device.VirtualDevice <vim/vm/device/VirtualDevice.rst>`_], optional):

       The list of virtual devices that are created on a virtual machine by default. Clients should not create these devices.
    supportedMonitorType ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       The monitor types supported by a host. The acceptable monitor types are enumerated by `VirtualMachineFlagInfoMonitorType <vim/vm/FlagInfo/MonitorType.rst>`_ .
    supportedOvfEnvironmentTransport ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Specifies the supported property transports that are available for the OVF environment
    supportedOvfInstallTransport ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Specifies the supported transports for the OVF installation phase.
