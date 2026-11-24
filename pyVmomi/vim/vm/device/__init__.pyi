# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.dvs
import pyVmomi.vim.encryption
import pyVmomi.vim.option
import pyVmomi.vim.vm
import pyVmomi.vim.vslm



class HostDiskMappingInfo(pyVmomi.vmodl.DynamicData):
   """
   The HostDiskMappingInfo data object type describes
   a virtual disk mapping to a host disk.
   
   Attributes:
       physicalPartition: The partition used on the host, if not mapping
           to a full disk device.
       name: Host resource name.
       exclusive: Flag to indicate whether or not the virtual machine has exclusive access
           to the host device.
   """
   class PartitionInfo(pyVmomi.vmodl.DynamicData):
      """
      The PhysicalPartitionInfo data class.
      
      Attributes:
          name: Partition name.
          fileSystem: Filesystem, if the partition is formatted.
          capacityInKb: Partition capacity, in KB.
      """
      name: str
      fileSystem: str
      capacityInKb: pyVmomi.VmomiSupport.long

   physicalPartition: _typing.Optional[HostDiskMappingInfo.PartitionInfo] = None
   name: str
   exclusive: _typing.Optional[bool] = None


class HostDiskMappingOption(pyVmomi.vmodl.DynamicData):
   """
   The HostDiskMappingOption data object type describes
   the options for a virtual disk mapping to a host disk.
   
   Attributes:
       physicalPartition: Array of valid partitions on this physical disk.
           
           There is no default for this array.
       name: Host resource name.
   """
   class PartitionOption(pyVmomi.vmodl.DynamicData):
      """
      The PhysicalPartitionOption data class contains the options
      for a partition on a physical disk.
      
      Attributes:
          name: Partition name.
          fileSystem: File system, if the partition is formatted.
          capacityInKb: Partition capacity, in KB.
      """
      name: str
      fileSystem: str
      capacityInKb: pyVmomi.VmomiSupport.long

   physicalPartition: list[HostDiskMappingOption.PartitionOption] = []
   name: str


class VirtualDevice(pyVmomi.vmodl.DynamicData):
   """
   VirtualDevice is the base data object type for devices in a virtual machine.
   
   This type contains enough information about a virtual device to allow clients
   to display devices they do not recognize. For example, a client with an
   older version than the server to which it connects may see a device
   without knowing what it is.
   
   Attributes:
       key: A unique key that distinguishes this device from other
           devices in the same virtual machine.
           
           Keys are immutable but may be
           recycled; that is, a key does not change as long as the device is
           associated with a particular virtual machine. However, once a device is
           removed, its key may be used when another device is added.
           
           This property is not read-only, but the client cannot control its value.
           Persistent device keys are always assigned and managed by the server, which
           guarantees that all devices will have non-negative key values.
           
           When adding new devices, it may be necessary for a client to assign keys
           temporarily in order to associate controllers with devices in
           configuring a virtual machine. However, the server does not allow a
           client to reassign a device key, and the server may assign a different
           value from the one passed during configuration. Clients should ensure
           that existing device keys are not reused as temporary key values for the
           new device to be added (for example, by using unique negative integers as
           temporary keys).
           
           When editing or deleting a device, clients must use the server-provided key
           to refer to an existing device.
       deviceInfo: Provides a label and summary information for the device.
       backing: Information about the backing of this virtual device presented
           in the context of the virtual machine's environment.
           
           Not all devices are required to have backing information.
       connectable: Provides information about restrictions on removing this device while
           a virtual machine is running.
           
           If the device is not removable, then
           this property is null.
       slotInfo: Information about the bus slot of a device in a virtual machine.
       controllerKey: Object key for the controller object for this device.
           
           This property contains the key property value of the controller device
           object.
       unitNumber: The unit number of this device on its controller.
           
           This property is null if
           the controller property is null (for example, when the device is not
           attached to a specific controller object).
           
           Normally, two devices on the same controller
           may not be assigned the same unit number. If
           multiple devices could exist on a controller,
           then unit number has to be specified to
           configure respective devices.
       numaNode: The virtual NUMA node.
           
           A negative number means there is no
           affinity for the device. A positive number is a vNUMA node.
           An unset value of numaNode is status-quo during Reconfigure time.
           If numaNode is unset during ConfigInfo, then it means there is no
           affinity for the device.
           
           Since: vSphere API Release 8.0.0.1
       deviceGroupInfo: Information about device group device is part of.
           
           Devices in the device group cannot be added/removed individually,
           whole group has to be added/removed at once. Value can be set
           during device add, it cannot be modified later.
           
           Since: vSphere API Release 8.0.0.1
   """
   class BackingInfo(pyVmomi.vmodl.DynamicData):
      """
      ``pyVmomi.vim.vm.device.VirtualDevice.BackingInfo`` is a base data object type
      for information about the backing of a device in a virtual machine.
      
      This base type does not define any properties. It is used as a namespace
      for general-purpose subtypes. Specific devices are represented by subtypes
      which define properties for device-specific backing information.
      """
      pass

   class FileBackingInfo(VirtualDevice.BackingInfo):
      """
      ``pyVmomi.vim.vm.device.VirtualDevice.FileBackingInfo`` is a data object type
      for information about file backing for a device in a virtual machine.
      
      Attributes:
          fileName: Filename for the host file used in this backing.
          datastore: Reference to the datastore managed object where this file is stored.
              
              If the file is not located on a datastore, then this reference is null.
              This is not used for configuration.
          backingObjectId: Backing object's durable and unmutable identifier.
              
              Each backing object has a unique identifier which is not settable.
      """
      fileName: str
      datastore: _typing.Optional[pyVmomi.vim.Datastore] = None
      backingObjectId: _typing.Optional[str] = None

   class DeviceBackingInfo(VirtualDevice.BackingInfo):
      """
      The ``pyVmomi.vim.vm.device.VirtualDevice.DeviceBackingInfo`` data object type
      defines information about a host device or resource that backs a device
      in a virtual machine.
      
      Attributes:
          deviceName: The name of the device on the host system.
          useAutoDetect: Indicates whether the device should be auto detected
              instead of directly specified.
              
              If this value is set to TRUE,
              deviceName is ignored.
      """
      deviceName: str
      useAutoDetect: _typing.Optional[bool] = None

   class RemoteDeviceBackingInfo(VirtualDevice.BackingInfo):
      """
      ``pyVmomi.vim.vm.device.VirtualDevice.RemoteDeviceBackingInfo`` is a data object type
      for information
      about a remote device backing used by a device in a virtual machine.
      
      The primary difference between a remote device backing and a
      local device backing is that the VirtualCenter server cannot provide a list
      of remote host devices available for this virtual device backing.
      
      Attributes:
          deviceName: The name of the device on the remote system.
          useAutoDetect: Indicates whether the device should be auto detected
              instead of directly specified.
              
              If this value is set to TRUE,
              `deviceName` is ignored.
      """
      deviceName: str
      useAutoDetect: _typing.Optional[bool] = None

   class PipeBackingInfo(VirtualDevice.BackingInfo):
      """
      The ``pyVmomi.vim.vm.device.VirtualDevice.PipeBackingInfo`` data object type
      defines information for using a named pipe as backing for a device
      in a virtual machine.
      
      Attributes:
          pipeName: Pipe name for the host pipe associated with this backing.
      """
      pipeName: str

   class URIBackingInfo(VirtualDevice.BackingInfo):
      """
      The ``pyVmomi.vim.vm.device.VirtualDevice.URIBackingInfo`` data object type
      defines information for using a network socket as backing for a virtual device.
      
      Attributes:
          serviceURI: Identifies the local host or a system on the network,
              depending on the value of ``pyVmomi.vim.vm.device.VirtualDevice.URIBackingInfo.direction``.
              - If you use the virtual machine as a server, the URI identifies
                the host on which the virtual machine runs. In this case,
                the host name part of the URI should be empty, or it should
                specify the address of the local host.
              - If you use the virtual machine as a client, the URI identifies
                the remote system on the network.
          direction: The direction of the connection.
              
              For possible values see
              `pyVmomi.vim.vm.device.VirtualDeviceOption.URIBackingOption.Direction`
          proxyURI: Identifies a proxy service that provides network access to the
              ``pyVmomi.vim.vm.device.VirtualDevice.URIBackingInfo.serviceURI``.
              
              If you specify a proxy URI, the virtual machine initiates
              a connection with the proxy service and forwards the
              `pyVmomi.vim.vm.device.VirtualDevice.URIBackingInfo.serviceURI` and `pyVmomi.vim.vm.device.VirtualDevice.URIBackingInfo.direction` to the proxy.
      """
      serviceURI: str
      direction: str
      proxyURI: _typing.Optional[str] = None

   class ConnectInfo(pyVmomi.vmodl.DynamicData):
      """
      The ``pyVmomi.vim.vm.device.VirtualDevice.ConnectInfo`` data object type
      contains information about connectable virtual devices.
      
      Attributes:
          migrateConnect: Specifies whether the virtual machine should override the
              virtual device connection state upon the completion of a
              migration.
              
              At this time, this property is only applicable to instant
              clone operations, and will be ignored for other migration
              types. The property is also only valid with
              VirtualEthernetCards, and any attempt to set this property
              on an unsupported device will result in an error.
              This property will persist only until the virtual machine
              undergoes a supported migration, at which point it will be
              consumed and unset on the destination virtual machine,
              preventing the property from affecting future migrations.
              The migration's success is not dependent on whether the device
              reaches the desired connection state.
              The set of possible values are described in
              `pyVmomi.vim.vm.device.VirtualDevice.ConnectInfo.MigrateConnectOp`.
          startConnected: Specifies whether or not to connect the device
              when the virtual machine starts.
          allowGuestControl: Enables guest control over whether the connectable device is
              connected.
          connected: Indicates whether the device is currently connected.
              
              Valid only while the virtual machine is running.
          status: Indicates the current status of the connectable device.
              
              Valid only while the
              virtual machine is running. The set of possible values is described in
              `pyVmomi.vim.vm.device.VirtualDevice.ConnectInfo.Status`
      """
      class Status(pyVmomi.VmomiSupport.Enum):
         """
         Specifies the connectable virtual device status.
         
         Attributes:
             ok: The device is working correctly.
             recoverableError: The device has reported a recoverable error.
                 
                 For example,
                 attempting to connect to floppy device that is being used by
                 another virtual machine or some other program would result in
                 this status.
             unrecoverableError: The device cannot be used.
                 
                 For example, attempting to connect to
                 a floppy device that does not exist would result in this status.
             untried: The device status is unknown, or it has not been requested to
                 connect when the VM is powered on.
         """
         ok: _typing.ClassVar['VirtualDevice.ConnectInfo.Status'] = 'ok'
         recoverableError: _typing.ClassVar['VirtualDevice.ConnectInfo.Status'] = 'recoverableError'
         unrecoverableError: _typing.ClassVar['VirtualDevice.ConnectInfo.Status'] = 'unrecoverableError'
         untried: _typing.ClassVar['VirtualDevice.ConnectInfo.Status'] = 'untried'

      class MigrateConnectOp(pyVmomi.VmomiSupport.Enum):
         """
         Contains information about connectable virtual devices when
         the virtual machine restores from a migration.
         
         Attributes:
             connect: Attempt to connect the virtual device when the virtual machine
                 restores from a migration.
                 
                 This property has no effect if it
                 is set on a device that is already connected.
             disconnect: Attempt to disconnect the virtual device when the virtual machine
                 restores from a migration.
                 
                 This property has no effect if it
                 is set on a device that is already disconnected.
             unset: Unset the property, which resets the device to its default state.
                 
                 Under most circumstances, a device will return to the same
                 connection state before the migration was initiated.
         """
         connect: _typing.ClassVar['VirtualDevice.ConnectInfo.MigrateConnectOp'] = 'connect'
         disconnect: _typing.ClassVar['VirtualDevice.ConnectInfo.MigrateConnectOp'] = 'disconnect'
         unset: _typing.ClassVar['VirtualDevice.ConnectInfo.MigrateConnectOp'] = 'unset'

      migrateConnect: _typing.Optional[str] = None
      startConnected: bool
      allowGuestControl: bool
      connected: bool
      status: _typing.Optional[str] = None

   class BusSlotInfo(pyVmomi.vmodl.DynamicData):
      """
      ``pyVmomi.vim.vm.device.VirtualDevice.BusSlotInfo`` is a base data object type
      for information about device connection to its bus.
      
      This base type does not
      define any properties. It is used as a namespace for general-purpose subtypes.
      Specific devices types are represented by subtypes which define properties for
      device-specific backing information.
      """
      pass

   class PciBusSlotInfo(VirtualDevice.BusSlotInfo):
      """
      The ``pyVmomi.vim.vm.device.VirtualDevice.PciBusSlotInfo`` data object type
      defines information about a pci bus slot of pci device in a virtual machine.
      
      Attributes:
          pciSlotNumber: The pci slot number of the virtual device.
              
              The pci slot number assignment should generally be left to the system.
              If assigned a value, and the value is invalid or duplicated, it will
              automatically be reassigned. This will not cause an error.
              
              Generally, the PCI slot numbers should never be specified in an
              Reconfigure operation, and only in a CreateVM operation if i) they
              are specified for all devices, and ii) the numbers have been
              determined by looking at an existing VM configuration of similar
              hardware version. In other words, when the virtual hardware configuration
              is duplicated.
      """
      pciSlotNumber: int

   class DeviceGroupInfo(pyVmomi.vmodl.DynamicData):
      """
      ``pyVmomi.vim.vm.device.VirtualDevice.DeviceGroupInfo`` contains information
      about the device group device is assigned to.
      
      Attributes:
          groupInstanceKey: Device group instance key from
              ``pyVmomi.vim.vm.VirtualDeviceGroups.DeviceGroup``.
          sequenceId: Device sequence in the group.
              
              Small unique positive integer obtained
              from ``pyVmomi.vim.vm.VendorDeviceGroupInfo.ComponentDeviceInfo.device``
              template.
      
      Since: vSphere API Release 8.0.0.1
      """
      groupInstanceKey: int
      sequenceId: int

   key: int
   deviceInfo: _typing.Optional[pyVmomi.vim.Description] = None
   backing: _typing.Optional[VirtualDevice.BackingInfo] = None
   connectable: _typing.Optional[VirtualDevice.ConnectInfo] = None
   slotInfo: _typing.Optional[VirtualDevice.BusSlotInfo] = None
   controllerKey: _typing.Optional[int] = None
   unitNumber: _typing.Optional[int] = None
   numaNode: _typing.Optional[int] = None
   deviceGroupInfo: _typing.Optional[VirtualDevice.DeviceGroupInfo] = None


class VirtualController(VirtualDevice):
   """
   VirtualController is the base data object type for a device controller in
   a virtual machine.
   
   VirtualController extends
   `pyVmomi.vim.vm.device.VirtualDevice` to inherit
   general information about a controller (such as name and description), and to allow
   controllers to appear in a generic list of virtual devices.
   
   Attributes:
       busNumber: Bus number associated with this controller.
       device: List of devices currently controlled by this controller.
           
           Each entry contains the `pyVmomi.vim.vm.device.VirtualDevice.key` property of the
           corresponding device object.
   """
   busNumber: int
   device: list[int] = []


class VirtualSCSIController(VirtualController):
   """
   The VirtualSCSIController data object type represents
   a SCSI controller in a virtual machine.
   
   Attributes:
       hotAddRemove: All SCSI controllers support hot adding and removing of devices.
           
           This
           support can't be toggled in the current implementation. Therefore, this
           option is ignored when reconfiguring a SCSI controller and is always set
           to \"true\" when reading an existing configuration.
       sharedBus: Mode for sharing the SCSI bus.
           
           The modes are physicalSharing,
           virtualSharing, and noSharing. See the
           `pyVmomi.vim.vm.device.VirtualSCSIController.Sharing`
           data object type for an explanation of these modes.
       scsiCtlrUnitNumber: The unit number of the SCSI controller.
           
           The SCSI controller sits on its
           own bus, so this field defines which slot the controller is using.
   """
   class Sharing(pyVmomi.VmomiSupport.Enum):
      """
      Sharing describes three possible ways of sharing the SCSI bus:
      One of these values is assigned to the sharedBus object to determine
      if or how the SCSI bus is shared.
      
      Attributes:
          noSharing: The virtual SCSI bus is not shared.
          virtualSharing: The virtual SCSI bus is shared between two or more virtual machines.
              
              In this case, no physical machine is involved.
          physicalSharing: The virtual SCSI bus is shared between two or more virtual machines
              residing on different physical hosts.
      """
      noSharing: _typing.ClassVar['VirtualSCSIController.Sharing'] = 'noSharing'
      virtualSharing: _typing.ClassVar['VirtualSCSIController.Sharing'] = 'virtualSharing'
      physicalSharing: _typing.ClassVar['VirtualSCSIController.Sharing'] = 'physicalSharing'

   hotAddRemove: _typing.Optional[bool] = None
   sharedBus: VirtualSCSIController.Sharing
   scsiCtlrUnitNumber: _typing.Optional[int] = None

class ParaVirtualSCSIController(VirtualSCSIController):
   """
   ParaVirtualSCSIController is the data object that represents
   a paravirtualized SCSI controller.
   """
   pass


class VirtualDeviceOption(pyVmomi.vmodl.DynamicData):
   """
   The VirtualDeviceOption data object type contains information about
   a virtual device type, the options for configuring the virtual device,
   and the relationship between this virtual device and other devices.
   
   The vSphere API groups device configurations that are mutually exclusive
   into different configuration objects; each of these configuration objects
   may define subtypes for virtual device backing options
   that are independent of the virtual device.
   Backing-dependent options should appear in a subtype of
   `pyVmomi.vim.vm.device.VirtualDeviceOption.BackingOption`.
   
   Attributes:
       type: The name of the run-time class the client should instantiate
           to create a run-time instance of this device.
       connectOption: If the device is connectable, then the connectOption
           describes the connect options and defaults.
       busSlotOption: If the device can use a bus slot configuration, then the busSlotOption
           describes the bus slot options.
       controllerType: Data object type that denotes the controller option object that is
           valid for controlling this device.
       autoAssignController: Flag to indicate whether or not this device will be auto-assigned a controller
           if one is required.
           
           If this is true, then a client need not explicitly create
           the controller that this device will plug into.
       backingOption: A list of backing options that can be used to map the virtual
           device to the host.
           
           The list is optional, since some devices exist only within
           the virtual machine; for example, a VirtualController.
       defaultBackingOptionIndex: Index into the backingOption list, indicating the default backing.
       licensingLimit: List of property names enforced by a licensing restriction
           of the underlying product.
           
           For example, a limit that is not
           derived based on the product or hardware features; the
           property name \"numCPU\".
       deprecated: Indicates whether this device is deprecated.
           
           Hence, if set the device
           cannot be used when creating a new virtual machine or be added to an existing
           virtual machine. However, the device is still supported by the platform.
       plugAndPlay: Indicates if this type of device can be hot-added to the virtual machine
           via a reconfigure operation when the virtual machine is powered on.
       hotRemoveSupported: Indicates if this type of device can be hot-removed from the virtual machine
           via a reconfigure operation when the virtual machine is powered on.
       numaSupported: Since: vSphere API Release 8.0.0.1
   """
   class BackingOption(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.vm.device.VirtualDeviceOption.BackingOption` data class
      defines options for device-specific virtual backing objects.
      
      Attributes:
          type: The name of the class the client should use to instantiate backing
              for the virtual device.
      """
      type: type

   class FileBackingOption(VirtualDeviceOption.BackingOption):
      """
      The FileBackingOption data class contains file-specific backing options.
      
      Attributes:
          fileNameExtensions: Valid filename extension for the filename.
              
              If no extensions are present, any file extension is acceptable.
      """
      class FileExtension(pyVmomi.VmomiSupport.Enum):
         """
         All known file extensions.
         
         Valid ones are:
         
         Attributes:
             iso: CD ISO Image backings
             flp: Floppy File Backings
             vmdk: virtual disks
             dsk: legacy virtual disks
             rdm: pre 3.0 virtual disks using Raw Disk Maps
         """
         iso: _typing.ClassVar['VirtualDeviceOption.FileBackingOption.FileExtension'] = 'iso'
         flp: _typing.ClassVar['VirtualDeviceOption.FileBackingOption.FileExtension'] = 'flp'
         vmdk: _typing.ClassVar['VirtualDeviceOption.FileBackingOption.FileExtension'] = 'vmdk'
         dsk: _typing.ClassVar['VirtualDeviceOption.FileBackingOption.FileExtension'] = 'dsk'
         rdm: _typing.ClassVar['VirtualDeviceOption.FileBackingOption.FileExtension'] = 'rdm'

      fileNameExtensions: _typing.Optional[pyVmomi.vim.option.ChoiceOption] = None

   class DeviceBackingOption(VirtualDeviceOption.BackingOption):
      """
      The DeviceBackingOption data class contains device-specific backing options.
      
      Attributes:
          autoDetectAvailable: Flag to indicate whether the specific instance of this device can
              be auto-detected on the host instead of having to specify a
              particular physical device.
      """
      autoDetectAvailable: pyVmomi.vim.option.BoolOption

   class RemoteDeviceBackingOption(VirtualDeviceOption.BackingOption):
      """
      VirtualDeviceOption.RemoteDeviceBackingOption describes the options
      for a remote device backing.
      
      The primary difference
      between a remote device backing and a local device backing is that
      the VirtualCenter server cannot provide a list of remote host devices
      available for this virtual device backing.
      
      Attributes:
          autoDetectAvailable: Flag to indicate whether the specific instance of this device can
              be auto-detected on the host instead of having to specify a
              particular physical device.
      """
      autoDetectAvailable: pyVmomi.vim.option.BoolOption

   class PipeBackingOption(VirtualDeviceOption.BackingOption):
      """
      The ``pyVmomi.vim.vm.device.VirtualDeviceOption.PipeBackingOption`` data object type contains options
      specific to pipe backings.
      """
      pass

   class URIBackingOption(VirtualDeviceOption.BackingOption):
      """
      The `pyVmomi.vim.vm.device.VirtualDeviceOption.URIBackingOption` data object type describes network communication
      options for virtual devices.
      
      When establishing a connection with a remote system on the network,
      the virtual machine can act as a server or a client.
      When the virtual machine acts as a server, it accepts a connection.
      When the virtual machine acts as a client, it initiates the connection.
      
      Attributes:
          directions: List of possible directions.
              
              Valid directions are:
              - `server`
              - `client`
      """
      class Direction(pyVmomi.VmomiSupport.Enum):
         """
         The `VirtualDeviceURIBackingOptionDirection` enum type
         provides values for the direction of a network connection.
         
         Attributes:
             server: Indicates that the virtual machine can listen for a connection
                 on the specified `pyVmomi.vim.vm.device.VirtualDevice.URIBackingInfo.serviceURI`.
             client: Indicates that the virtual machine can initiate a connection
                 with a system on the network using the specified
                 `pyVmomi.vim.vm.device.VirtualDevice.URIBackingInfo.serviceURI`.
         """
         server: _typing.ClassVar['VirtualDeviceOption.URIBackingOption.Direction'] = 'server'
         client: _typing.ClassVar['VirtualDeviceOption.URIBackingOption.Direction'] = 'client'

      directions: pyVmomi.vim.option.ChoiceOption

   class ConnectOption(pyVmomi.vmodl.DynamicData):
      """
      The ConnectOption data object type contains information about options for
      connectable virtual devices.
      
      Attributes:
          startConnected: Flag to indicate whether or not the device supports
              the startConnected feature.
          allowGuestControl: Flag to indicate whether or not the device can be
              connected and disconnected from within the guest operating system.
      """
      startConnected: pyVmomi.vim.option.BoolOption
      allowGuestControl: pyVmomi.vim.option.BoolOption

   class BusSlotOption(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.vm.device.VirtualDeviceOption.BusSlotOption` data class
      defines options for device-specific bus slot objects.
      
      Attributes:
          type: The name of the class the client should use to instantiate bus slot
              object for the virtual device.
      """
      type: type

   type: type
   connectOption: _typing.Optional[VirtualDeviceOption.ConnectOption] = None
   busSlotOption: _typing.Optional[VirtualDeviceOption.BusSlotOption] = None
   controllerType: _typing.Optional[type] = None
   autoAssignController: _typing.Optional[pyVmomi.vim.option.BoolOption] = None
   backingOption: list[VirtualDeviceOption.BackingOption] = []
   defaultBackingOptionIndex: _typing.Optional[int] = None
   licensingLimit: list[pyVmomi.VmomiSupport.PropertyPath] = []
   deprecated: bool
   plugAndPlay: bool
   hotRemoveSupported: bool
   numaSupported: _typing.Optional[bool] = None


class VirtualControllerOption(VirtualDeviceOption):
   """
   The VirtualControllerOption data object type contains information about
   a virtual controller type.
   
   Attributes:
       devices: The minimum and maximum number of devices this controller can control
           at run time.
       supportedDevice: Array of supported device options for this controller.
   """
   devices: pyVmomi.vim.option.IntOption
   supportedDevice: list[type] = []


class VirtualSCSIControllerOption(VirtualControllerOption):
   """
   The VirtualSCSIControllerOption data object type contains the options
   for a virtual SCSI controller defined by the
   `pyVmomi.vim.vm.device.VirtualSCSIController`
   data object type.
   
   Attributes:
       numSCSIDisks: Three properties (numSCSIDisks.min, numSCSIDisks.max, and
           numSCSIDisks.defaultValue) define the minimum, maximum, and default
           number of SCSI VirtualDisk instances available at any given time in the
           SCSI controller.
           
           The number of SCSI VirtualDisk instances is
           also limited by the number of available slots in the SCSI controller.
       numSCSICdroms: Three properties (numSCSICdroms.min, numSCSICdroms.max, and
           numSCSICdroms.defaultValue) define the minimum, maximum, and default
           number of SCSI VirtualCdrom instances available
           in the SCSI controller.
           
           The number of SCSI VirtualCdrom instances is
           also limited by the number of available slots in the SCSI controller.
       numSCSIPassthrough: Three properties (numSCSIPassthrough.min, numSCSIPassthrough.max, and
           numSCSIPassthrough.defaultValue) define the minimum, maximum, and
           default number of VirtualSCSIPassthrough instances available
           have at any given time in the SCSI controller.
           
           The number of
           VirtualSCSIPassthrough instances is also limited by the number of
           available slots in the SCSI controller.
       sharing: Supported shared bus modes.
       defaultSharedIndex: Index into sharing array specifying the default value.
       hotAddRemove: All SCSI controllers support hot adding and removing of devices.
           
           This
           support can't be toggled in the current implementation. Therefore, this
           option is ignored when reconfiguring a SCSI controller and is always set
           to \"true\" when reading an existing configuration.
       scsiCtlrUnitNumber: The unit number of the SCSI controller.
           
           The SCSI controller sits on its
           own bus, so that this field defines which slot the controller will use.
   """
   numSCSIDisks: pyVmomi.vim.option.IntOption
   numSCSICdroms: pyVmomi.vim.option.IntOption
   numSCSIPassthrough: pyVmomi.vim.option.IntOption
   sharing: list[VirtualSCSIController.Sharing] = []
   defaultSharedIndex: int
   hotAddRemove: pyVmomi.vim.option.BoolOption
   scsiCtlrUnitNumber: int

class ParaVirtualSCSIControllerOption(VirtualSCSIControllerOption):
   """
   ParaVirtualSCSIControllerOption is the data object that contains
   the options for a a paravirtualized SCSI controller.
   """
   pass

class VirtualSATAController(VirtualController):
   """
   The VirtualSATAController data object type represents
   a SATA controller in a virtual machine.
   """
   pass

class VirtualAHCIController(VirtualSATAController):
   """
   The VirtualAHCIController data object type represents
   an AHCI SATA controller in a virtual machine.
   """
   pass


class VirtualSATAControllerOption(VirtualControllerOption):
   """
   The VirtualSATAControllerOption data object type contains the options
   for a virtual SATA controller defined by the
   `pyVmomi.vim.vm.device.VirtualSATAController`
   data object type.
   
   Attributes:
       numSATADisks: Three properties (numSATADisks.min, numSATADisks.max, and
           numSATADisks.defaultValue) define the minimum, maximum, and default
           number of SATA VirtualDisk instances available at any given time in the
           SATA controller.
           
           The number of SATA VirtualDisk instances is
           also limited by the number of available slots in the SATA controller.
       numSATACdroms: Three properties (numSATACdroms.min, numSATACdroms.max, and
           numSATACdroms.defaultValue) define the minimum, maximum, and default
           number of SATA VirtualCdrom instances available
           in the SATA controller.
           
           The number of SATA VirtualCdrom instances is
           also limited by the number of available slots in the SATA controller.
   """
   numSATADisks: pyVmomi.vim.option.IntOption
   numSATACdroms: pyVmomi.vim.option.IntOption

class VirtualAHCIControllerOption(VirtualSATAControllerOption):
   """
   VirtualAHCIControllerOption is the data object that contains
   the options for an AHCI SATA controller.
   """
   pass

class VirtualBusLogicController(VirtualSCSIController):
   """
   VirtualBusLogicController is the data object that represents
   a BusLogic SCSI controller.
   """
   pass

class VirtualBusLogicControllerOption(VirtualSCSIControllerOption):
   """
   This data object contains
   the options for a BusLogic SCSI controller.
   """
   pass

class VirtualCdrom(VirtualDevice):
   """
   The VirtualCdrom data object type describes the configuration of a CD-ROM device
   in a virtual machine.
   """
   class IsoBackingInfo(VirtualDevice.FileBackingInfo):
      """
      The VirtualCdrom.IsoBackingInfo data class represents
      an ISO backing for a virtual CD-ROM.
      """
      pass

   class PassthroughBackingInfo(VirtualDevice.DeviceBackingInfo):
      """
      The VirtualCdrom.PassthroughBackingInfo data class
      represents a device pass-through backing for a
      virtual CD-ROM.
      
      Attributes:
          exclusive: Flag to indicate whether or not the virtual machine has
              exclusive CD-ROM device access.
      """
      exclusive: bool

   class RemotePassthroughBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
      """
      The VirtualCdrom.RemotePassthroughBackingInfo data object type
      contains the information to specify a remote pass-through device
      backing of a virtual CD-ROM.
      
      Attributes:
          exclusive: Flag to indicate whether or not the virtual machine
              has exclusive access to the CD-ROM device.
      """
      exclusive: bool

   class AtapiBackingInfo(VirtualDevice.DeviceBackingInfo):
      """
      The VirtualCdrom.AtapiBackingInfo data object type
      represents an ATAPI device backing for a virtual CD-ROM.
      """
      pass

   class RemoteAtapiBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
      """
      The VirtualCdrom.RemoteAtapiBackingInfo data class
      represents a remote ATAPI device backing for a virtual CD-ROM.
      """
      pass


class VirtualCdromOption(VirtualDeviceOption):
   """
   The VirtualCdromOption data object type contains the options for the
   virtual CD-ROM class.
   """
   class IsoBackingOption(VirtualDeviceOption.FileBackingOption):
      """
      The VirtualCdromOption.IsoBackingOption data object type contains
      the options for an ISO image backing.
      """
      pass

   class PassthroughBackingOption(VirtualDeviceOption.DeviceBackingOption):
      """
      The VirtualCdromOption.PassthroughBackingOption data object type
      contains the options for a pass-through CD-ROM device backing.
      
      Attributes:
          exclusive: Flag to indicate whether or not exclusive CD-ROM device access is supported.
      """
      exclusive: pyVmomi.vim.option.BoolOption

   class RemotePassthroughBackingOption(VirtualDeviceOption.RemoteDeviceBackingOption):
      """
      The VirtualCdromOption.RemotePassthroughBackingOption data object type
      contains the options for a remote pass-through CD-ROM device backing.
      
      Note that the server cannot present a list of valid remote backing devices
      because it is unable to scan remote hosts.
      
      Attributes:
          exclusive: Flag to indicate whether or not exclusive CD-ROM device access is supported.
      """
      exclusive: pyVmomi.vim.option.BoolOption

   class AtapiBackingOption(VirtualDeviceOption.DeviceBackingOption):
      """
      The VirtualCdromOption.AtapiBackingOption data object type
      contains the options for the ATAPI CD-ROM device backing.
      """
      pass

   class RemoteAtapiBackingOption(VirtualDeviceOption.DeviceBackingOption):
      """
      The VirtualCdromOption.RemoteAtapiBackingOption data object type
      contains the options for the remote ATAPI CD-ROM device backing.
      
      Note that the server cannot present a list of valid remote backing devices
      because it is unable to scan remote hosts.
      """
      pass


class VirtualDeviceSpec(pyVmomi.vmodl.DynamicData):
   """
   The VirtualDeviceSpec data object type encapsulates change
   specifications for an individual virtual device.
   
   The virtual
   device being added or modified must be fully specified.
   
   Attributes:
       operation: Type of operation being performed on the specified virtual device.
           
           If no operation is specified, the spec. is ignored.
       fileOperation: Type of operation being performed on the backing
           of the specified virtual device.
           
           If no file operation is specified in the VirtualDeviceSpec,
           then any backing filenames in the
           `pyVmomi.vim.vm.device.VirtualDevice`
           must refer to files that already exist.
           The \"replace\" and \"delete\" values for this property are only
           applicable to virtual disk backing files.
       device: Device specification, with all necessary properties set.
       profile: Virtual Device Profile requirement.
           
           Profiles are solution specifics.
           Storage Profile Based Management(SPBM) is a vSphere server extension.
           The API users who want to provision VMs using Storage Profiles, need to
           interact with SPBM service.
           This is an optional parameter and if user doesn't specify profile,
           the default behavior will apply.
       backing: BackingInfo configuration options.
           
           Each BackingSpec corresponds to a BackingInfo object. The member
           `pyVmomi.vim.vm.device.VirtualDeviceSpec.backing` refers to the
           `pyVmomi.vim.vm.device.VirtualDeviceSpec.device`.`pyVmomi.vim.vm.device.VirtualDevice.backing`.
       filterSpec: List of independent filters `pyVmomi.vim.vm.IndependentFilterSpec`
           to configure on the virtual device.
           
           Since: vSphere API Release 7.0.2.1
       changeMode: The change mode of the device.
           
           The values of the mode will be one of `pyVmomi.vim.vm.device.VirtualDeviceSpec.ChangeMode` enumerations.
           On unset, default to 'fail'.
           
           Since: vSphere API Release 8.0.0.1
   """
   class Operation(pyVmomi.VmomiSupport.Enum):
      """
      The type of operation being performed on the specified virtual device.
      
      Valid values are:
      
      Attributes:
          add: Specifies the addition of a virtual device to the configuration.
          remove: Specifies the removal of a virtual device.
          edit: Specifies changes to the virtual device specification.
      """
      add: _typing.ClassVar['VirtualDeviceSpec.Operation'] = 'add'
      remove: _typing.ClassVar['VirtualDeviceSpec.Operation'] = 'remove'
      edit: _typing.ClassVar['VirtualDeviceSpec.Operation'] = 'edit'

   class FileOperation(pyVmomi.VmomiSupport.Enum):
      """
      The type of operation being performed on the backing of a virtual device.
      
      Valid values are:
      
      Attributes:
          create: Specifies the creation of the device backing; for example,
              the creation of a virtual disk or floppy image file.
          destroy: Specifies the destruction of a device backing.
          replace: Specifies the deletion of the existing backing for a virtual device
              and the creation of a new backing.
      """
      create: _typing.ClassVar['VirtualDeviceSpec.FileOperation'] = 'create'
      destroy: _typing.ClassVar['VirtualDeviceSpec.FileOperation'] = 'destroy'
      replace: _typing.ClassVar['VirtualDeviceSpec.FileOperation'] = 'replace'

   class BackingSpec(pyVmomi.vmodl.DynamicData):
      """
      ``pyVmomi.vim.vm.device.VirtualDeviceSpec.BackingSpec`` is a data object
      type for information about configuration of the backing of a device
      in a virtual machine.
      
      The member `pyVmomi.vim.vm.device.VirtualDeviceSpec.BackingSpec.parent` refers the parent in the chain of
      `pyVmomi.vim.vm.device.VirtualDevice.BackingInfo` objects.
      """
      parent: _typing.Optional[VirtualDeviceSpec.BackingSpec] = None
      crypto: _typing.Optional[pyVmomi.vim.encryption.CryptoSpec] = None

   class ChangeMode(pyVmomi.VmomiSupport.Enum):
      """
      Describes the change mode of the device.
      
      Applies only to virtual disks during VirtualDeviceSpec.Operation \"add\"
      that have no VirtualDeviceSpec.FileOperation set.
      
      Since: vSphere API Release 8.0.0.1
      """
      fail: _typing.ClassVar['VirtualDeviceSpec.ChangeMode'] = 'fail'
      skip: _typing.ClassVar['VirtualDeviceSpec.ChangeMode'] = 'skip'

   operation: _typing.Optional[VirtualDeviceSpec.Operation] = None
   fileOperation: _typing.Optional[VirtualDeviceSpec.FileOperation] = None
   device: VirtualDevice
   profile: list[pyVmomi.vim.vm.ProfileSpec] = []
   backing: _typing.Optional[VirtualDeviceSpec.BackingSpec] = None
   filterSpec: list[pyVmomi.vim.vm.BaseIndependentFilterSpec] = []
   changeMode: _typing.Optional[str] = None


class VirtualDisk(VirtualDevice):
   """
   This data object type contains information about a disk in a virtual machine.
   
   The virtual disk backing object types describe the different virtual disk backings
   available.
   The disk format version in each case describes
   the version of the format that is used.
   
   Supported virtual disk backings:
   
   Sparse disk format, version 1 and 2: 
   The virtual disk backing grows when needed.
   Supported only for VMware Server.
   
   Flat disk format, version 1 and 2: 
   The virtual disk backing is preallocated.
   Version 1 is supported only for VMware Server.
   
   Space efficient sparse disk format: 
   The virtual disk backing grows on demand and
   incorporates additional space optimizations.
   
   Raw disk format, version 2: 
   The virtual disk backing uses a full physical disk drive
   to back the virtual disk. Supported only for VMware Server.
   
   Partitioned raw disk format, version 2: 
   The virtual disk backing uses one or more partitions on a
   physical disk drive to back a virtual disk. Supported only for VMware Server.
   
   Raw disk mapping, version 1: 
   The virtual disk backing uses a raw device mapping to back the virtual disk.
   Supported for ESX Server 2.5 and 3.x.
   
   Attributes:
       capacityInKB: Capacity of this virtual disk in kilobytes.
           
           Information might be lost when actual disk size is rounded off to kilobytes.
           If the disk is on a Virtual Volume datastore the disk size must be a multiple
           of a megabyte.
       capacityInBytes: Capacity of this virtual disk in bytes.
           
           Server will always populate this property. Clients must initialize it when
           creating a new non -RDM disk or in case they want to change the current
           capacity of an existing virtual disk, but can omit it otherwise.
           If the disk is on a Virtual Volume datastore the disk size must be a multiple
           of a megabyte.
       shares: Disk shares, used for resource scheduling.
       storageIOAllocation: Resource allocation for storage I/O.
       diskObjectId: Virtual disk durable and unmutable identifier.
           
           Virtual disk has a UUID field but that can be set through
           VirtualDiskManager APIs.
           This identifier is a universally unique identifier which is not settable.
           VirtualDisk can remain in existence even if it is not associated with VM.
       vFlashCacheConfigInfo: vFlash cache configuration supported on this virtual disk.
       iofilter: IDs of the IO Filters associated with the virtual disk.
           
           See `pyVmomi.vim.IoFilterManager.IoFilterInfo.id`. This information
           is provided when retrieving configuration information for
           an existing virtual machine. The client cannot modify this information
           on a virtual machine.
       vDiskId: ID of the virtual disk object as the first class entity.
           
           See `pyVmomi.vim.vslm.ID`
           The ID is a universally unique identifier for the disk lifecycle,
           even if the virtual disk is not associated with VM.
       vDiskVersion: Disk descriptor version of the virtual disk.
           
           Since: vSphere API Release 8.0.1.0
       virtualDiskFormat: Indicates the disk format of the virtual disk.
           
           The supported values are `native_4k`
           and `native_512`.
           If unset during virtual machine creation `pyVmomi.vim.Folder.createVm`,
           the default value will be based on `pyVmomi.vim.Datastore.Info.supportedVDiskFormats`.
           If `pyVmomi.vim.Datastore.Info.supportedVDiskFormats` has only one value
           then the default value will be the same.
           If `pyVmomi.vim.Datastore.Info.supportedVDiskFormats` has both the values
           `native_512` and `native_4k`
           then default value will be `native_512`.
           If unset when returned as part of a `pyVmomi.vim.vm.ConfigInfo` then the
           default value is `native_512`.
           
           Since: vSphere API Release 9.0.0.0
       nativeUnmanagedLinkedClone: Indicates whether a disk with
           `pyVmomi.vim.vm.device.VirtualDisk.FlatVer2BackingInfo` backing is a linked
           clone from an unmanaged delta disk and hence the
           `pyVmomi.vim.vm.device.VirtualDisk.FlatVer2BackingInfo.parent` chain to
           this delta disk will not be available.
       independentFilters: The IDs of the independent filters associated with the virtual disk.
           
           This information is provided when retrieving configuration information for
           an existing virtual machine. The client cannot modify this information on
           a virtual machine.
           
           Since: vSphere API Release 7.0.2.1
       guestReadOnly: Flag to indicate whether a disk should be presented to the guest
           in read-only mode (limited by choice of adapter).
           
           Since: vSphere API Release 8.0.2.0
       diskChainBrokenIssue: Broken issue for a disk chain.
           
           See `pyVmomi.vim.vm.device.VirtualDisk.DiskChainBrokenIssue` for the list
           of supported values. If not specified, the default value used is
           `noIssue`.
           
           Since: vSphere API Release 9.1.0.0
   """
   class DeltaDiskFormat(pyVmomi.VmomiSupport.Enum):
      """
      The delta disk format constants
      
      Attributes:
          redoLogFormat: redo-log based format
          nativeFormat: native snapshot format
          seSparseFormat: Flex-SE redo-log based format
      """
      redoLogFormat: _typing.ClassVar['VirtualDisk.DeltaDiskFormat'] = 'redoLogFormat'
      nativeFormat: _typing.ClassVar['VirtualDisk.DeltaDiskFormat'] = 'nativeFormat'
      seSparseFormat: _typing.ClassVar['VirtualDisk.DeltaDiskFormat'] = 'seSparseFormat'

   class DeltaDiskFormatVariant(pyVmomi.VmomiSupport.Enum):
      """
      The delta disk format variant constants
      
      Attributes:
          vmfsSparseVariant: vmfsSparse based redo-log format
          vsanSparseVariant: vsanSparse based redo-log format
      """
      vmfsSparseVariant: _typing.ClassVar['VirtualDisk.DeltaDiskFormatVariant'] = 'vmfsSparseVariant'
      vsanSparseVariant: _typing.ClassVar['VirtualDisk.DeltaDiskFormatVariant'] = 'vsanSparseVariant'

   class DiskChainBrokenIssue(pyVmomi.VmomiSupport.Enum):
      """
      The disk chain broken issue constants.
      
      Attributes:
          noIssue: Indicates the disk chain has no issue
          cidMismatch: Indicates the disk chain is broken due to cid mismatch
      
      Since: vSphere API Release 9.1.0.0
      """
      noIssue: _typing.ClassVar['VirtualDisk.DiskChainBrokenIssue'] = 'noIssue'
      cidMismatch: _typing.ClassVar['VirtualDisk.DiskChainBrokenIssue'] = 'cidMismatch'

   class Sharing(pyVmomi.VmomiSupport.Enum):
      """
      The sharing mode of the virtual disk.
      
      Setting the value to sharingMultiWriter means that multiple virtual
      machines can write to the virtual disk. This sharing mode is allowed
      only for eagerly zeroed thick virtual disks.
      
      Attributes:
          sharingNone: The virtual disk is not shared.
          sharingMultiWriter: The virtual disk is shared between multiple virtual machines.
      """
      sharingNone: _typing.ClassVar['VirtualDisk.Sharing'] = 'sharingNone'
      sharingMultiWriter: _typing.ClassVar['VirtualDisk.Sharing'] = 'sharingMultiWriter'

   class SparseVer1BackingInfo(VirtualDevice.FileBackingInfo):
      """
      This data object type contains information about backing a virtual disk by
      using a virtual disk file on the host, in the sparse disk format used by
      GSX Server 2.x.
      
      Attributes:
          diskMode: The disk persistence mode.
              
              Valid values are:
              - `persistent`
              - `nonpersistent`
              - `undoable`
              - `independent_persistent`
              - `independent_nonpersistent`
              - `append`
          split: Flag to indicate the type of virtual disk file: split or monolithic.
              
              If true, the virtual disk is stored in multiple files, each 2GB.
          writeThrough: Flag to indicate whether writes should go directly to the file system
              or should be buffered.
          spaceUsedInKB: The space in use for this sparse disk.
              
              This information is provided
              when retrieving configuration information for an existing virtual
              machine. The client cannot modify this information using reconfigure
              on a virtual machine.
          contentId: Content ID of the virtual disk file, if available.
              
              A content ID indicates the logical contents of the disk backing and its parents.
              
              This property is only guaranteed to be up to date if this disk backing is not
              currently being written to by any virtual machine.
              
              The only supported operation is comparing if two content IDs are equal or not.
              The guarantee provided by the content ID is that if two disk backings have the
              same content ID and are not currently being written to, then reads issued from
              the guest operating system to those disk backings will return the same data.
          parent: The parent of this virtual disk file, if this is a delta disk backing.
              
              This will be unset if this is not a delta disk backing.
              
              A delta disk backing is a way to preserve a virtual disk backing
              at some point in time. A delta disk backing is a file backing which in
              turn points to the original virtual disk backing (the parent). After a delta
              disk backing is added, all writes go to the delta disk backing. All reads
              first try the delta disk backing and then try the parent backing if needed.
              
              A delta disk backing can be added to a disk either implicitly during
              snapshot operations, or explicitly during create or reconfigure of the virtual
              machine.
              
              Note that the type of the backing is consistent throughout the chain; any new
              delta disk backing which is added is of the same type as the original disk .
              Also note that since the parent backing is not being written to,
              it is possible that the parent backing may be shared among multiple
              disks belonging to multiple virtual machines.
              
              During virtual machine `pyVmomi.vim.Folder.createVm` and
              `pyVmomi.vim.VirtualMachine.reconfigure` this property is
              only checked if the `pyVmomi.vim.vm.device.VirtualDeviceSpec` specifies
              an `add` with a
              `create`.
              In this case, a new delta disk backing is created which points to the parent
              disk backing. Only the `pyVmomi.vim.vm.device.VirtualDevice.FileBackingInfo.fileName`
              property is important; all other properties will be ignored. The parent backing
              is assumed to exist and will not be recursively created.
              
              This property may only be set if
              `pyVmomi.vim.host.Capability.deltaDiskBackingsSupported`
              is true.
      """
      diskMode: str
      split: _typing.Optional[bool] = None
      writeThrough: _typing.Optional[bool] = None
      spaceUsedInKB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      contentId: _typing.Optional[str] = None
      parent: _typing.Optional[VirtualDisk.SparseVer1BackingInfo] = None

   class SparseVer2BackingInfo(VirtualDevice.FileBackingInfo):
      """
      This data object type contains information about backing a virtual disk by
      using a virtual disk file on the host, in the sparse disk format used by
      VMware Server.
      
      Attributes:
          diskMode: The disk persistence mode.
              
              Valid modes are:
              - `persistent`
              - `independent_persistent`
              - `independent_nonpersistent`
          split: Flag to indicate the type of virtual disk file: split or monolithic.
              
              If true, the virtual disk is stored in multiple files, each 2GB.
          writeThrough: Flag to indicate whether writes should go directly to the file system
              or should be buffered.
          spaceUsedInKB: The space in use for this sparse disk.
              
              This information is provided
              when retrieving configuration information for an existing virtual
              machine. The client cannot modify this information using reconfigure
              on a virtual machine.
          uuid: Disk UUID for the virtual disk, if available.
          contentId: Content ID of the virtual disk file, if available.
              
              A content ID indicates the logical contents of the disk backing and its parents.
              
              This property is only guaranteed to be up to date if this disk backing is not
              currently being written to by any virtual machine.
              
              The only supported operation is comparing if two content IDs are equal or not.
              The guarantee provided by the content ID is that if two disk backings have the
              same content ID and are not currently being written to, then reads issued from
              the guest operating system to those disk backings will return the same data.
          changeId: The change ID of the virtual disk for the corresponding
              snapshot or virtual machine.
              
              This can be used to track
              incremental changes to a virtual disk. See
              `pyVmomi.vim.VirtualMachine.queryChangedDiskAreas`.
          parent: The parent of this virtual disk file, if this is a delta disk backing.
              
              This will be unset if this is not a delta disk backing.
              
              A delta disk backing is a way to preserve a virtual disk backing
              at some point in time. A delta disk backing is a file backing which in
              turn points to the original virtual disk backing (the parent). After a delta
              disk backing is added, all writes go to the delta disk backing. All reads
              first try the delta disk backing and then try the parent backing if needed.
              
              A delta disk backing can be added to a disk either implicitly during
              snapshot operations, or explicitly during create or reconfigure of the virtual
              machine.
              
              Note that the type of the backing is consistent throughout the chain; any new
              delta disk backing which is added is of the same type as the original disk .
              Also note that since the parent backing is not being written to,
              it is possible that the parent backing may be shared among multiple
              disks belonging to multiple virtual machines.
              
              During virtual machine `pyVmomi.vim.Folder.createVm` and
              `pyVmomi.vim.VirtualMachine.reconfigure` this property is
              only checked if the `pyVmomi.vim.vm.device.VirtualDeviceSpec` specifies
              an `add` with a
              `create`.
              In this case, a new delta disk backing is created which points to the parent
              disk backing. Only the `pyVmomi.vim.vm.device.VirtualDevice.FileBackingInfo.fileName`
              property is important; all other properties will be ignored. The parent backing
              is assumed to exist and will not be recursively created.
              
              This property may only be set if
              `pyVmomi.vim.host.Capability.deltaDiskBackingsSupported`
              is true.
          keyId: Virtual Disk Backing encryption options.
              
              On modification operations the value is ignored, use the specification
              `pyVmomi.vim.vm.device.VirtualDeviceSpec.BackingSpec.crypto` in
              `pyVmomi.vim.vm.device.VirtualDeviceSpec.backing`.
      """
      diskMode: str
      split: _typing.Optional[bool] = None
      writeThrough: _typing.Optional[bool] = None
      spaceUsedInKB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      uuid: _typing.Optional[str] = None
      contentId: _typing.Optional[str] = None
      changeId: _typing.Optional[str] = None
      parent: _typing.Optional[VirtualDisk.SparseVer2BackingInfo] = None
      keyId: _typing.Optional[pyVmomi.vim.encryption.CryptoKeyId] = None

   class FlatVer1BackingInfo(VirtualDevice.FileBackingInfo):
      """
      This data object type contains information about backing a virtual disk by
      using a virtual disk file on the host, in the flat file format used by
      GSX Server 2.x.
      
      Flat disks are allocated when created, unlike sparse disks, which
      grow as needed.
      
      Attributes:
          diskMode: The disk persistence mode.
              
              Valid modes are:
              - `persistent`
              - `nonpersistent`
              - `undoable`
          split: Flag to indicate the type of virtual disk file: split or monolithic.
              
              If true, the virtual disk is stored in multiple files, each 2GB.
          writeThrough: Flag to indicate whether writes should go directly to the file system
              or should be buffered.
          contentId: Content ID of the virtual disk file, if available.
              
              A content ID indicates the logical contents of the disk backing and its parents.
              
              This property is only guaranteed to be up to date if this disk backing is not
              currently being written to by any virtual machine.
              
              The only supported operation is comparing if two content IDs are equal or not.
              The guarantee provided by the content ID is that if two disk backings have the
              same content ID and are not currently being written to, then reads issued from
              the guest operating system to those disk backings will return the same data.
          parent: The parent of this virtual disk file, if this is a delta disk backing.
              
              This will be unset if this is not a delta disk backing.
              
              A delta disk backing is a way to preserve a virtual disk backing
              at some point in time. A delta disk backing is a file backing which in
              turn points to the original virtual disk backing (the parent). After a delta
              disk backing is added, all writes go to the delta disk backing. All reads
              first try the delta disk backing and then try the parent backing if needed.
              
              A delta disk backing can be added to a disk either implicitly during
              snapshot operations, or explicitly during create or reconfigure of the virtual
              machine.
              
              Note that the type of the backing is consistent throughout the chain; any new
              delta disk backing which is added is of the same type as the original disk .
              Also note that since the parent backing is not being written to,
              it is possible that the parent backing may be shared among multiple
              disks belonging to multiple virtual machines.
              
              During virtual machine `pyVmomi.vim.Folder.createVm` and
              `pyVmomi.vim.VirtualMachine.reconfigure` this property is
              only checked if the `pyVmomi.vim.vm.device.VirtualDeviceSpec` specifies
              an `add` with a
              `create`.
              In this case, a new delta disk backing is created which points to the parent
              disk backing. Only the `pyVmomi.vim.vm.device.VirtualDevice.FileBackingInfo.fileName`
              property is important; all other properties will be ignored. The parent backing
              is assumed to exist and will not be recursively created.
              
              This property may only be set if
              `pyVmomi.vim.host.Capability.deltaDiskBackingsSupported`
              is true.
      """
      diskMode: str
      split: _typing.Optional[bool] = None
      writeThrough: _typing.Optional[bool] = None
      contentId: _typing.Optional[str] = None
      parent: _typing.Optional[VirtualDisk.FlatVer1BackingInfo] = None

   class FlatVer2BackingInfo(VirtualDevice.FileBackingInfo):
      """
      This data object type contains information about backing a virtual disk using a
      virtual disk file on the host, in the flat file format used by VMware Server,
      ESX Server 2.x, and ESX Server 3.x.
      
      Flat disks are allocated when created, unlike sparse disks, which
      grow as needed.
      
      Attributes:
          diskMode: The disk persistence mode.
              
              Valid modes are:
              - `persistent`
              - `independent_persistent`
              - `independent_nonpersistent`
              - `nonpersistent`
              - `undoable`
              - `append`
          split: Flag to indicate the type of virtual disk file: split or monolithic.
              
              If true, the virtual disk is stored in multiple files, each 2GB.
              On ESX this property is ignored when creating new disks or
              editing existing disks. This property is always false for disks
              created on ESX.
              When an existing split disk such as those created by VMware
              Server is added to a virtual machine on ESX, the property will
              be set to true when retrieved from `pyVmomi.vim.vm.ConfigInfo`.
          writeThrough: Flag to indicate whether writes should go directly to the file system
              or should be buffered.
          thinProvisioned: Flag to indicate to the underlying filesystem, whether the
              virtual disk backing file should be allocated lazily (using
              thin provisioning).
              
              This flag is only used for file systems
              that support configuring the provisioning policy on a per file
              basis, such as VMFS3.
              
              When specified as part of a `pyVmomi.vim.vm.ConfigSpec`, this
              property applies only when creating a new virtual disk; it is
              ignored when editing an existing virtual disk.
              
              see `pyVmomi.vim.Datastore.Capability.perFileThinProvisioningSupported`
          eagerlyScrub: Flag to indicate to the underlying filesystem whether the
              virtual disk backing file should be scrubbed completely at
              this time.
              
              Virtual disks on some filesystems like VMFS3 are zeroed-out
              lazily so that disk creation time doesn't take too long.
              However, clustering applications and features like
              Fault Tolerance require that the virtual disk be
              completely scrubbed. This setting allows controlling the
              scrubbing policy on a per-disk basis.
              
              If this flag is unset or set to false when creating a new disk,
              the disk scrubbing policy will be decided by the filesystem. If
              this flag is unset or set to false when editing an existing disk,
              it is ignored.
              When returned as part of a `pyVmomi.vim.vm.ConfigInfo`, this
              property may be unset if its value is unknown.
          uuid: Disk UUID for the virtual disk, if available.
          contentId: Content ID of the virtual disk file, if available.
              
              A content ID indicates the logical contents of the disk backing and its parents.
              
              This property is only guaranteed to be up to date if this disk backing is not
              currently being written to by any virtual machine.
              
              The only supported operation is comparing if two content IDs are equal or not.
              The guarantee provided by the content ID is that if two disk backings have the
              same content ID and are not currently being written to, then reads issued from
              the guest operating system to those disk backings will return the same data.
          changeId: The change ID of the virtual disk for the corresponding
              snapshot or virtual machine.
              
              This can be used to track
              incremental changes to a virtual disk. See
              `pyVmomi.vim.VirtualMachine.queryChangedDiskAreas`.
          parent: The parent of this virtual disk file, if this is a delta disk backing.
              
              This will be unset if this is not a delta disk backing.
              
              A delta disk backing is a way to preserve a virtual disk backing
              at some point in time. A delta disk backing is a file backing which in
              turn points to the original virtual disk backing (the parent). After a delta
              disk backing is added, all writes go to the delta disk backing. All reads
              first try the delta disk backing and then try the parent backing if needed.
              
              A delta disk backing can be added to a disk either implicitly during
              snapshot operations, or explicitly during create or reconfigure of the virtual
              machine.
              
              Note that the type of the backing is consistent throughout the chain; any new
              delta disk backing which is added is of the same type as the original disk .
              Also note that since the parent backing is not being written to,
              it is possible that the parent backing may be shared among multiple
              disks belonging to multiple virtual machines.
              
              During virtual machine `pyVmomi.vim.Folder.createVm` and
              `pyVmomi.vim.VirtualMachine.reconfigure` this property is
              only checked if the `pyVmomi.vim.vm.device.VirtualDeviceSpec` specifies
              an `add` with a
              `create`.
              In this case, a new delta disk backing is created which points to the parent
              disk backing. Only the `pyVmomi.vim.vm.device.VirtualDevice.FileBackingInfo.fileName`
              property is important; all other properties will be ignored. The parent backing
              is assumed to exist and will not be recursively created.
              
              This property may only be set if
              `pyVmomi.vim.host.Capability.deltaDiskBackingsSupported`
              is true.
          deltaDiskFormat: The format of the delta disk.
              
              This field is valid only for a delta disk.
              
              See `pyVmomi.vim.vm.device.VirtualDisk.DeltaDiskFormat` for the
              supported formats. If not specified, the default value used is
              `redoLogFormat`.
              
              If `nativeFormat`
              is specified and the datastore does not support this format or the parent is
              on a different datastore,
              `pyVmomi.vim.fault.DeltaDiskFormatNotSupported` is
              thrown.
              
              vSphere server does not support relocation of virtual machines with
              `nativeFormat`.
              An exception is thrown for such requests.
          digestEnabled: Indicates whether the disk backing has digest file enabled.
          deltaGrainSize: Grain size in kB for a delta disk of format type seSparseFormat.
              
              The default
              size is 4 kB.
              This setting is used to specify the grain size of
              `pyVmomi.vim.vm.device.VirtualDisk.SeSparseBackingInfo` delta disks
              when the base disk is of type FlatVer2BackingInfo.
              The `pyVmomi.vim.vm.device.VirtualDisk.DeltaDiskFormat` must also
              be set to seSparseFormat.
          deltaDiskFormatVariant: The delta disk format variant, if applicable.
              
              This field is valid only for a delta disk and may specify more detailed
              information for the delta disk format specified in
              `pyVmomi.vim.vm.device.VirtualDisk.FlatVer2BackingInfo.deltaDiskFormat`.
              
              If `redoLogFormat` is
              specified for the
              `pyVmomi.vim.vm.device.VirtualDisk.FlatVer2BackingInfo.deltaDiskFormat`,
              see `pyVmomi.vim.vm.device.VirtualDisk.DeltaDiskFormatVariant` for the
              supported formats. If this is not specified for
              `redoLogFormat`,
              the default value used is
              `vmfsSparseVariant`.
              
              For other delta disk formats, this currently remains unspecified.
          sharing: The sharing mode of the virtual disk.
              
              See `pyVmomi.vim.vm.device.VirtualDisk.Sharing`. The default value is
              no sharing.
          keyId: Virtual Disk Backing encryption options.
              
              On modification operations the value is ignored, use the specification
              `pyVmomi.vim.vm.device.VirtualDeviceSpec.BackingSpec.crypto` in
              `pyVmomi.vim.vm.device.VirtualDeviceSpec.backing`.
      """
      diskMode: str
      split: _typing.Optional[bool] = None
      writeThrough: _typing.Optional[bool] = None
      thinProvisioned: _typing.Optional[bool] = None
      eagerlyScrub: _typing.Optional[bool] = None
      uuid: _typing.Optional[str] = None
      contentId: _typing.Optional[str] = None
      changeId: _typing.Optional[str] = None
      parent: _typing.Optional[VirtualDisk.FlatVer2BackingInfo] = None
      deltaDiskFormat: _typing.Optional[str] = None
      digestEnabled: _typing.Optional[bool] = None
      deltaGrainSize: _typing.Optional[int] = None
      deltaDiskFormatVariant: _typing.Optional[str] = None
      sharing: _typing.Optional[str] = None
      keyId: _typing.Optional[pyVmomi.vim.encryption.CryptoKeyId] = None

   class SeSparseBackingInfo(VirtualDevice.FileBackingInfo):
      """
      Deprecated: As of vSphere API 9.0, space efficient sparse format only
      applies to delta disks, see
      `pyVmomi.vim.vm.device.VirtualDisk.DeltaDiskFormat`.
      SE sparse base disk is no longer supported, instead set
      `pyVmomi.vim.vm.device.VirtualDisk.FlatVer2BackingInfo.thinProvisioned`
      to true for potential space saving.
      
      Space for space efficient sparse disks is allocated on
      demand and optimizations are applied to achieve additional
      space savings. The effective space usage of such a disk can
      be obtained from `pyVmomi.vim.vm.FileLayoutEx`.Backing type for virtual disks that use the space efficient
      sparse format.
      
      Attributes:
          diskMode: The disk persistence mode.
              
              Valid modes are:
              - `persistent`
              - `independent_persistent`
              - `independent_nonpersistent`
              - `nonpersistent`
              - `undoable`
              - `append`
          writeThrough: Flag to indicate whether writes should go directly to the file system
              or should be buffered.
          uuid: Disk UUID for the virtual disk, if available.
          contentId: Content ID of the virtual disk file, if available.
              
              A content ID indicates the logical contents of the disk backing and its parents.
              
              This property is only guaranteed to be up to date if this disk backing is not
              currently being written to by any virtual machine.
              
              The only supported operation is comparing if two content IDs are equal or not.
              The guarantee provided by the content ID is that if two disk backings have the
              same content ID and are not currently being written to, then reads issued from
              the guest operating system to those disk backings will return the same data.
          changeId: The change ID of the virtual disk for the corresponding
              snapshot or virtual machine.
              
              This can be used to track
              incremental changes to a virtual disk. See `pyVmomi.vim.VirtualMachine.queryChangedDiskAreas`.
          parent: The parent of this virtual disk file, if this is a delta disk backing.
              
              This will be unset if this is not a delta disk backing.
              
              A delta disk backing is a way to preserve a virtual disk backing
              at some point in time. A delta disk backing is a file backing which in
              turn points to the original virtual disk backing (the parent). After a delta
              disk backing is added, all writes go to the delta disk backing. All reads
              first try the delta disk backing and then try the parent backing if needed.
              
              A delta disk backing can be added to a disk either implicitly during
              snapshot operations, or explicitly during create or reconfigure of the virtual
              machine.
              
              Note that the type of the backing is consistent throughout the chain; any new
              delta disk backing which is added is of the same type as the original disk .
              Also note that since the parent backing is not being written to,
              it is possible that the parent backing may be shared among multiple
              disks belonging to multiple virtual machines.
              
              During virtual machine `pyVmomi.vim.Folder.createVm` and
              `pyVmomi.vim.VirtualMachine.reconfigure` this property is
              only checked if the `pyVmomi.vim.vm.device.VirtualDeviceSpec` specifies
              an `add` with a
              `create`.
              In this case, a new delta disk backing is created which points to the parent
              disk backing. Only the `pyVmomi.vim.vm.device.VirtualDevice.FileBackingInfo.fileName`
              property is important; all other properties will be ignored. The parent backing
              is assumed to exist and will not be recursively created.
              
              This property may only be set if
              `pyVmomi.vim.host.Capability.deltaDiskBackingsSupported`
              is true.
          deltaDiskFormat: The format of the delta disk.
              
              This field is valid only for a delta disk.
              
              See `pyVmomi.vim.vm.device.VirtualDisk.DeltaDiskFormat` for the
              supported formats. If not specified, the default value used is
              `redoLogFormat`.
          digestEnabled: Indicates whether the disk backing has digest file enabled.
          grainSize: Specify the grain size in kB.
              
              The default size is 4 kB.
          keyId: Virtual Disk Backing encryption options.
              
              On modification operations the value is ignored, use the specification
              `pyVmomi.vim.vm.device.VirtualDeviceSpec.BackingSpec.crypto` in
              `pyVmomi.vim.vm.device.VirtualDeviceSpec.backing`.
      """
      diskMode: str
      writeThrough: _typing.Optional[bool] = None
      uuid: _typing.Optional[str] = None
      contentId: _typing.Optional[str] = None
      changeId: _typing.Optional[str] = None
      parent: _typing.Optional[VirtualDisk.SeSparseBackingInfo] = None
      deltaDiskFormat: _typing.Optional[str] = None
      digestEnabled: _typing.Optional[bool] = None
      grainSize: _typing.Optional[int] = None
      keyId: _typing.Optional[pyVmomi.vim.encryption.CryptoKeyId] = None

   class RawDiskVer2BackingInfo(VirtualDevice.DeviceBackingInfo):
      """
      This data object type contains information about backing a virtual disk by
      using a host device, as used by VMware Server.
      
      Attributes:
          descriptorFileName: The name of the raw disk descriptor file.
          uuid: Disk UUID for the virtual disk, if available.
          changeId: The change ID of the virtual disk for the corresponding
              snapshot or virtual machine.
              
              This can be used to track
              incremental changes to a virtual disk. See
              `pyVmomi.vim.VirtualMachine.queryChangedDiskAreas`.
          sharing: The sharing mode of the virtual disk.
              
              See `pyVmomi.vim.vm.device.VirtualDisk.Sharing`. The default value is
              no sharing.
      """
      descriptorFileName: str
      uuid: _typing.Optional[str] = None
      changeId: _typing.Optional[str] = None
      sharing: _typing.Optional[str] = None

   class PartitionedRawDiskVer2BackingInfo(VirtualDisk.RawDiskVer2BackingInfo):
      """
      This data object type contains information about backing a virtual disk
      using one or more partitions on a physical disk device.
      
      This type of
      backing is supported for VMware Server.
      
      Attributes:
          partition: Array of partition indexes.
              
              This array identifies the
              partitions that are used on the physical disk drive.
      """
      partition: list[int] = []

   class RawDiskMappingVer1BackingInfo(VirtualDevice.FileBackingInfo):
      """
      This data object type contains information about backing a virtual disk using a
      raw device mapping.
      
      Supported for ESX Server 2.5 and 3.x.
      
      Attributes:
          lunUuid: Unique identifier of the LUN accessed by the raw disk mapping.
          deviceName: The host-specific device the LUN is being accessed through.
              
              If the
              target LUN is not available on the host then it is empty. For example, this
              could happen if it has accidentally been masked out.
          compatibilityMode: The compatibility mode of the raw disk mapping (RDM).
              
              This must be specified
              when a new virtual disk with an RDM backing is created. On subsequent virtual
              machine reconfigurations, this property should be handled as follows,
              depending on the version of the host:
              
              On ESX Server 2.5, the compatibility mode of an RDM backing is a
              characteristic of the virtual machine's configuration. When reconfiguring
              a virtual machine that currently uses a virtual disk backed by an RDM,
              the compatibility mode of that backing may be modified. When reconfiguring a
              virtual machine to add an existing virtual disk backed by an RDM, the
              compatibility mode of that backing may be specified. If left unspecified it
              defaults to \"physicalMode\".
              
              On ESX Server 3.x, the compatibility mode of an RDM backing is a
              characteristic of the RDM itself. Once the RDM is created, its compatibility
              mode cannot be changed by reconfiguring the virtual machine. When
              reconfiguring a virtual machine to add an existing virtual disk backed by an
              RDM, the compatibility mode of that backing must be left unspecified.
          diskMode: The disk mode.
              
              Valid values are:
              - `persistent`
              - `independent_persistent`
              - `independent_nonpersistent`
              - `nonpersistent`
              - `undoable`
              - `append`
                
              Disk modes are only supported when the raw disk mapping is using virtual
              compatibility mode.
          uuid: Disk UUID for the virtual disk, if available.
              
              Disk UUID is not available if
              the raw disk mapping is in physical compatibility mode.
          contentId: Content ID of the virtual disk file, if available.
              
              A content ID indicates the logical contents of the disk backing and its parents.
              
              This property is only guaranteed to be up to date if this disk backing is not
              currently being written to by any virtual machine.
              
              The only supported operation is comparing if two content IDs are equal or not.
              The guarantee provided by the content ID is that if two disk backings have the
              same content ID and are not currently being written to, then reads issued from
              the guest operating system to those disk backings will return the same data.
          changeId: The change ID of the virtual disk for the corresponding
              snapshot or virtual machine.
              
              This can be used to track
              incremental changes to a virtual disk. See
              `pyVmomi.vim.VirtualMachine.queryChangedDiskAreas`.
          parent: The parent of this virtual disk file, if this is a delta disk backing.
              
              This will be unset if this is not a delta disk backing.
              
              A delta disk backing is a way to preserve a virtual disk backing
              at some point in time. A delta disk backing is a file backing which in
              turn points to the original virtual disk backing (the parent). After a delta
              disk backing is added, all writes go to the delta disk backing. All reads
              first try the delta disk backing and then try the parent backing if needed.
              
              A delta disk backing can be added to a disk either implicitly during
              snapshot operations, or explicitly during create or reconfigure of the virtual
              machine.
              
              Note that the type of the backing is consistent throughout the chain; any new
              delta disk backing which is added is of the same type as the original disk .
              Also note that since the parent backing is not being written to,
              it is possible that the parent backing may be shared among multiple
              disks belonging to multiple virtual machines.
              
              During virtual machine `pyVmomi.vim.Folder.createVm` and
              `pyVmomi.vim.VirtualMachine.reconfigure` this property is
              only checked if the `pyVmomi.vim.vm.device.VirtualDeviceSpec` specifies
              an `add` with a
              `create`.
              In this case, a new delta disk backing is created which points to the parent
              disk backing. Only the `pyVmomi.vim.vm.device.VirtualDevice.FileBackingInfo.fileName`
              property is important; all other properties will be ignored. The parent backing
              is assumed to exist and will not be recursively created.
              
              Only raw disk mappings in `virtualMode` can have parents.
              
              This property may only be set if
              `pyVmomi.vim.host.Capability.deltaDiskBackingsSupported`
              is true.
          deltaDiskFormat: The format of the delta disk.
              
              This field is valid only for a delta disk.
              
              See `pyVmomi.vim.vm.device.VirtualDisk.DeltaDiskFormat` for the
              supported formats. The default value used for VM with hardware
              version 8 and lower is
              `redoLogFormat`.
              The default value used for VM with hardware
              version 9 and higher is
              `seSparseFormat`.
              
              `nativeFormat` is not
              supported for bask disk of type RawDiskMappingVer1BackingInfo.
          deltaGrainSize: Grain size in kB for a delta disk of format type seSparseFormat.
              
              The default
              size is 4 kB.
              The grain size of
              `pyVmomi.vim.vm.device.VirtualDisk.SeSparseBackingInfo` delta disks
              when the base disk is of type RawDiskMappingVer1BackingInfo.
              The `pyVmomi.vim.vm.device.VirtualDisk.DeltaDiskFormat` must also
              be set to seSparseFormat.
          sharing: The sharing mode of the virtual disk.
              
              See `pyVmomi.vim.vm.device.VirtualDisk.Sharing`. The default value is
              no sharing.
      """
      lunUuid: _typing.Optional[str] = None
      deviceName: _typing.Optional[str] = None
      compatibilityMode: _typing.Optional[str] = None
      diskMode: _typing.Optional[str] = None
      uuid: _typing.Optional[str] = None
      contentId: _typing.Optional[str] = None
      changeId: _typing.Optional[str] = None
      parent: _typing.Optional[VirtualDisk.RawDiskMappingVer1BackingInfo] = None
      deltaDiskFormat: _typing.Optional[str] = None
      deltaGrainSize: _typing.Optional[int] = None
      sharing: _typing.Optional[str] = None

   class LocalPMemBackingInfo(VirtualDevice.FileBackingInfo):
      """
      Deprecated: as of vSphere 9.0 APIs with no replacement.This data object type contains information about backing a virtual disk
      using non-volatile memory technologies (persistent memory).
      
      Supported for ESX Server 6.5 and later.
      
      Attributes:
          diskMode: The disk persistence mode.
          uuid: Disk UUID for the virtual disk, if available.
          volumeUUID: Persistent memory volume UUID - UUID which associates this
              virtual disk with a specific host.
              
              This is read only property.
          contentId: Content ID of the virtual disk file, if available.
              
              A content ID indicates the logical contents of the disk backing and
              its parents.
              
              This property is only guaranteed to be up to date if this disk backing
              is not currently being written to by any virtual machine.
              
              The only supported operation is comparing if two content IDs are equal
              or not. The guarantee provided by the content ID is that if two disk
              backings have the same content ID and are not currently being written
              to, then reads issued from the guest operating system to those disk
              backings will return the same data.
      """
      diskMode: str
      uuid: _typing.Optional[str] = None
      volumeUUID: _typing.Optional[str] = None
      contentId: _typing.Optional[str] = None

   class VFlashCacheConfigInfo(pyVmomi.vmodl.DynamicData):
      """
      Data object describes the vFlash cache configuration on this virtual disk.
      
      Attributes:
          vFlashModule: Name of vFlash module which manages the cache.
              
              If not specified, default setting
              `pyVmomi.vim.host.VFlashManager.VFlashCacheConfigSpec.defaultVFlashModule`
              will be used.
          reservationInMB: Amount of vFlash resource that is guaranteed available to the cache.
              
              If not specified,
              default reservation will be used.
          cacheConsistencyType: Cache data consistency types after a crash.
              
              See `pyVmomi.vim.vm.device.VirtualDisk.VFlashCacheConfigInfo.CacheConsistencyType`
              for supported types. If not specified, the default value used is
              `strong`
          cacheMode: Cache modes.
              
              See `pyVmomi.vim.vm.device.VirtualDisk.VFlashCacheConfigInfo.CacheMode`
              for supported modes. If not specified, the default value used is
              `write_thru`.
          blockSizeInKB: Cache block size.
              
              This parameter allows the user to control how much
              data gets cached on a single access to the VMDK. Max block size is 1MB.
              Default is 4KB.
      """
      class CacheConsistencyType(pyVmomi.VmomiSupport.Enum):
         """
         Pre-defined constants for cache consistency types
         
         Attributes:
             strong: With strong consistency, it ensures that
                 a crash will leave the cache data consistent.
             weak: Cache data consistency is not guaranteed after a crash.
         """
         strong: _typing.ClassVar['VirtualDisk.VFlashCacheConfigInfo.CacheConsistencyType'] = 'strong'
         weak: _typing.ClassVar['VirtualDisk.VFlashCacheConfigInfo.CacheConsistencyType'] = 'weak'

      class CacheMode(pyVmomi.VmomiSupport.Enum):
         """
         Pre-defined constants for cache modes.
         
         Attributes:
             write_thru: In write-through cache mode, writes to the cache cause writes
                 to the underlying storage.
                 
                 The cache acts as a facade to the underlying
                 storage.
             write_back: In write-back mode, writes to the cache do not go to the underlying storage
                 right away.
                 
                 Cache holds data temporarily till it can be permanently saved or
                 otherwise modified.
         """
         write_thru: _typing.ClassVar['VirtualDisk.VFlashCacheConfigInfo.CacheMode'] = 'write_thru'
         write_back: _typing.ClassVar['VirtualDisk.VFlashCacheConfigInfo.CacheMode'] = 'write_back'

      vFlashModule: _typing.Optional[str] = None
      reservationInMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      cacheConsistencyType: _typing.Optional[str] = None
      cacheMode: _typing.Optional[str] = None
      blockSizeInKB: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   capacityInKB: pyVmomi.VmomiSupport.long
   capacityInBytes: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   shares: _typing.Optional[pyVmomi.vim.SharesInfo] = None
   storageIOAllocation: _typing.Optional[pyVmomi.vim.StorageResourceManager.IOAllocationInfo] = None
   diskObjectId: _typing.Optional[str] = None
   vFlashCacheConfigInfo: _typing.Optional[VirtualDisk.VFlashCacheConfigInfo] = None
   iofilter: list[str] = []
   vDiskId: _typing.Optional[pyVmomi.vim.vslm.ID] = None
   vDiskVersion: _typing.Optional[int] = None
   virtualDiskFormat: _typing.Optional[str] = None
   nativeUnmanagedLinkedClone: _typing.Optional[bool] = None
   independentFilters: list[pyVmomi.vim.vm.BaseIndependentFilterSpec] = []
   guestReadOnly: _typing.Optional[bool] = None
   diskChainBrokenIssue: _typing.Optional[str] = None


class VirtualDiskId(pyVmomi.vmodl.DynamicData):
   """
   Identifier for a virtual disk.
   
   Attributes:
       vm: Virtual machine reference.
       diskId: Device ID `pyVmomi.vim.vm.device.VirtualDevice.key` of the virtual disk.
   """
   vm: pyVmomi.vim.VirtualMachine
   diskId: int


class VirtualDiskOption(VirtualDeviceOption):
   """
   The VirtualDiskOption data class contains the options for the
   virtual disk data object type.
   
   Attributes:
       capacityInKB: Minimum, maximum, and default capacity of the disk.
       ioAllocationOption: Minimum, maximum, and default values for Storage I/O allocation.
       vFlashCacheConfigOption: vFlash cache configuration on the disk.
   """
   class DiskMode(pyVmomi.VmomiSupport.Enum):
      """
      The list of known disk modes.
      
      The list of supported disk modes varies by the backing type. The \"persistent\"
      mode is supported by every backing type.
      
      Attributes:
          persistent: Changes are immediately and permanently written to the virtual disk.
          nonpersistent: Changes to virtual disk are made to a redo log and discarded at power off.
          undoable: Changes are made to a redo log, but you are given the option to commit or undo.
          independent_persistent: Same as persistent, but not affected by snapshots.
          independent_nonpersistent: Same as nonpersistent, but not affected by snapshots.
          append: Changes are appended to the redo log; you revoke changes by removing the undo log.
      """
      persistent: _typing.ClassVar['VirtualDiskOption.DiskMode'] = 'persistent'
      nonpersistent: _typing.ClassVar['VirtualDiskOption.DiskMode'] = 'nonpersistent'
      undoable: _typing.ClassVar['VirtualDiskOption.DiskMode'] = 'undoable'
      independent_persistent: _typing.ClassVar['VirtualDiskOption.DiskMode'] = 'independent_persistent'
      independent_nonpersistent: _typing.ClassVar['VirtualDiskOption.DiskMode'] = 'independent_nonpersistent'
      append: _typing.ClassVar['VirtualDiskOption.DiskMode'] = 'append'

   class CompatibilityMode(pyVmomi.VmomiSupport.Enum):
      """
      All known compatibility modes for raw disk mappings.
      
      Valid compatibility
      modes are:
      - virtualMode
      - physicalMode
      
      Attributes:
          virtualMode: A disk device backed by a virtual compatibility mode raw disk mapping can
              use disk modes.
          physicalMode: A disk device backed by a physical compatibility mode raw disk mapping cannot
              use disk modes, and commands are passed straight through to the LUN
              indicated by the raw disk mapping.
      """
      virtualMode: _typing.ClassVar['VirtualDiskOption.CompatibilityMode'] = 'virtualMode'
      physicalMode: _typing.ClassVar['VirtualDiskOption.CompatibilityMode'] = 'physicalMode'

   class SparseVer1BackingOption(VirtualDeviceOption.FileBackingOption):
      """
      This data object type contains the available options when backing a virtual
      disk using a host file with the sparse file format from GSX Server 2.x.
      
      Attributes:
          diskModes: The disk mode.
              
              Valid disk modes are:
              - `persistent`
              - `nonpersistent`
              - `undoable`
              - `independent_persistent`
              - `independent_nonpersistent`
              - `append`
          split: Flag to indicate whether or not the host supports
              allowing the client to select whether or not a sparse disk
              should be split.
          writeThrough: Flag to indicate whether or not the host supports
              allowing the client to select \"writethrough\" as a mode for
              virtual disks.
              
              Typically, this is available only for VMware Server Linux hosts.
          growable: Flag to indicate whether this backing can have its size changed.
      """
      diskModes: pyVmomi.vim.option.ChoiceOption
      split: pyVmomi.vim.option.BoolOption
      writeThrough: pyVmomi.vim.option.BoolOption
      growable: bool

   class SparseVer2BackingOption(VirtualDeviceOption.FileBackingOption):
      """
      This data object type contains the options available when backing a virtual
      disk using a host file with the sparse file format from VMware Server.
      
      Attributes:
          diskMode: The disk mode.
              
              Valid disk modes are:
              - `persistent`
              - `nonpersistent`
              - `undoable`
              - `independent_persistent`
              - `independent_nonpersistent`
              - `append`
          split: Flag to indicate whether or not the host supports
              allowing the client to select whether or not a sparse disk
              should be split.
          writeThrough: Flag to indicate whether or not the host supports
              allowing the client to select \"writethrough\" as a mode for
              virtual disks.
              
              Typically, this is available only for VMware Server Linux hosts.
          growable: Indicates whether or not this disk backing can be
              extended to larger sizes through a reconfigure operation.
              
              If set to true, reconfiguring this virtual disk
              with a `pyVmomi.vim.vm.device.VirtualDisk.capacityInKB` value greater
              than its current value will grow the disk to the newly specified size.
          hotGrowable: Indicates whether or not this disk backing can be
              extended to larger sizes through a reconfigure operation while
              the virtual machine is powered on.
              
              If set to true, reconfiguring this virtual disk
              with a `pyVmomi.vim.vm.device.VirtualDisk.capacityInKB` value greater
              than its current value will grow the disk to the newly specified size
              while the virtual machine is powered on.
          uuid: Flag to indicate whether this backing supports disk UUID property.
          virtualDiskFormat: Virtual disk format.
              
              See `pyVmomi.vim.Datastore.SectorFormat` for the list of supported types.
              
              Since: vSphere API Release 9.0.0.0
      """
      diskMode: pyVmomi.vim.option.ChoiceOption
      split: pyVmomi.vim.option.BoolOption
      writeThrough: pyVmomi.vim.option.BoolOption
      growable: bool
      hotGrowable: bool
      uuid: bool
      virtualDiskFormat: _typing.Optional[pyVmomi.vim.option.ChoiceOption] = None

   class FlatVer1BackingOption(VirtualDeviceOption.FileBackingOption):
      """
      This data object type contains the available options when backing a virtual disk
      using a host file with the flat file format from GSX Server 2.x.
      
      Flat disks are pre-allocated, whereas sparse disks are grown as needed.
      
      Attributes:
          diskMode: The disk mode.
              
              Valid disk modes are:
              - `persistent`
              - `nonpersistent`
              - `undoable`
              - `independent_persistent`
              - `independent_nonpersistent`
              - `append`
          split: Flag to indicate whether or not the host supports
              allowing the client to select whether or not a disk
              should be split.
          writeThrough: Flag to indicate whether or not the host supports
              allowing the client to select \"writethrough\" as a mode for
              virtual disks.
              
              Typically, this is available only for GSX Server Linux hosts.
          growable: Flag to indicate whether this backing can have its size changed.
      """
      diskMode: pyVmomi.vim.option.ChoiceOption
      split: pyVmomi.vim.option.BoolOption
      writeThrough: pyVmomi.vim.option.BoolOption
      growable: bool

   class DeltaDiskFormatsSupported(pyVmomi.vmodl.DynamicData):
      """
      Delta disk format supported for each datastore type.
      
      Attributes:
          datastoreType: Datastore type name
          deltaDiskFormat: Delta disk formats supported.
              
              Valid values are:
              - `redoLogFormat`
              - `nativeFormat`
      """
      datastoreType: type
      deltaDiskFormat: pyVmomi.vim.option.ChoiceOption

   class FlatVer2BackingOption(VirtualDeviceOption.FileBackingOption):
      """
      This data object type contains the available options when backing a virtual
      disk using a host file with the flat file format used in VMware Server and
      in ESX Server 2.x and greater.
      
      Flat disks are pre-allocated, whereas sparse disks are grown as needed.
      
      Attributes:
          diskMode: The disk mode.
              
              Valid disk modes are:
              - `persistent`
              - `independent_persistent`
              - `independent_nonpersistent`
          split: Flag to indicate whether or not the host supports
              allowing the client to select whether or not a disk
              should be split.
          writeThrough: Flag to indicate whether or not the host supports
              allowing the client to select \"writethrough\" as a mode for
              virtual disks.
              
              Typically, this is available only for VMware Server Linux hosts.
          growable: Indicates whether or not this disk backing can be
              extended to larger sizes through a reconfigure operation.
              
              If set to true, reconfiguring this virtual disk
              with a `pyVmomi.vim.vm.device.VirtualDisk.capacityInKB` value greater
              than its current value will grow the disk to the newly specified size.
          hotGrowable: Indicates whether or not this disk backing can be
              extended to larger sizes through a reconfigure operation while
              the virtual machine is powered on.
              
              If set to true, reconfiguring this virtual disk
              with a `pyVmomi.vim.vm.device.VirtualDisk.capacityInKB` value greater
              than its current value will grow the disk to the newly specified size
              while the virtual machine is powered on.
          uuid: Flag to indicate whether this backing supports disk UUID property.
          thinProvisioned: Flag to indicate if this backing supports thin-provisioned disks.
              
              When creating a thin-provisioned disk (or converting an existing disk to
              to a thin-provisioned one), both the target datastore and the
              host accessing it must support thin-provisioning. This flag indicates only
              the host capability. See `pyVmomi.vim.Datastore.Capability.perFileThinProvisioningSupported`
              for datastore capability.
          eagerlyScrub: Flag to indicate if this backing supports eager scrubbing.
          deltaDiskFormat: Delta disk formats supported.
              
              Valid values are:
              - `redoLogFormat`
              - `nativeFormat`
          deltaDiskFormatsSupported: Delta disk formats supported for each datastore type.
          virtualDiskFormat: Virtual disk format.
              
              See `pyVmomi.vim.Datastore.SectorFormat` for the list of supported types.
              
              Since: vSphere API Release 9.0.0.0
      """
      diskMode: pyVmomi.vim.option.ChoiceOption
      split: pyVmomi.vim.option.BoolOption
      writeThrough: pyVmomi.vim.option.BoolOption
      growable: bool
      hotGrowable: bool
      uuid: bool
      thinProvisioned: pyVmomi.vim.option.BoolOption
      eagerlyScrub: pyVmomi.vim.option.BoolOption
      deltaDiskFormat: pyVmomi.vim.option.ChoiceOption
      deltaDiskFormatsSupported: list[VirtualDiskOption.DeltaDiskFormatsSupported] = []
      virtualDiskFormat: _typing.Optional[pyVmomi.vim.option.ChoiceOption] = None

   class SeSparseBackingOption(VirtualDeviceOption.FileBackingOption):
      """
      Backing options for virtual disks that use the space
      efficient sparse format.
      
      Space for Flex-SE disks is allocated on demand and
      optimizations are applied to achieve additional
      space savings.
      
      Attributes:
          diskMode: The disk mode.
              
              Valid disk modes are:
              - `persistent`
              - `independent_persistent`
              - `independent_nonpersistent`
          writeThrough: Flag to indicate whether or not the host supports
              allowing the client to select \"writethrough\" as a mode for
              virtual disks.
              
              Typically, this is available only for VMware Server Linux hosts.
          growable: Indicates whether or not this disk backing can be
              extended to larger sizes through a reconfigure operation.
              
              If set to true, reconfiguring this virtual disk
              with a `pyVmomi.vim.vm.device.VirtualDisk.capacityInKB` value greater
              than its current value will grow the disk to the newly specified size.
          hotGrowable: Indicates whether or not this disk backing can be
              extended to larger sizes through a reconfigure operation while
              the virtual machine is powered on.
              
              If set to true, reconfiguring this virtual disk
              with a `pyVmomi.vim.vm.device.VirtualDisk.capacityInKB` value greater
              than its current value will grow the disk to the newly specified size
              while the virtual machine is powered on.
          uuid: Flag to indicate whether this backing supports disk UUID property.
          deltaDiskFormatsSupported: Delta disk formats supported for each datastore type.
          virtualDiskFormat: Virtual disk format.
              
              See `pyVmomi.vim.Datastore.SectorFormat` for the list of supported types.
              
              Since: vSphere API Release 9.0.0.0
      """
      diskMode: pyVmomi.vim.option.ChoiceOption
      writeThrough: pyVmomi.vim.option.BoolOption
      growable: bool
      hotGrowable: bool
      uuid: bool
      deltaDiskFormatsSupported: list[VirtualDiskOption.DeltaDiskFormatsSupported] = []
      virtualDiskFormat: _typing.Optional[pyVmomi.vim.option.ChoiceOption] = None

   class RawDiskVer2BackingOption(VirtualDeviceOption.DeviceBackingOption):
      """
      The VirtualDiskOption.RawDiskVer2BackingOption object type
      contains the available options when backing a virtual disk
      using a host device on VMware Server.
      
      Attributes:
          descriptorFileNameExtensions: Valid extensions for the filename of the raw disk descriptor
              file.
          uuid: Flag to indicate whether this backing supports disk UUID property.
      """
      descriptorFileNameExtensions: pyVmomi.vim.option.ChoiceOption
      uuid: bool

   class PartitionedRawDiskVer2BackingOption(VirtualDiskOption.RawDiskVer2BackingOption):
      """
      The VirtualDiskOption.PartitionedRawDiskVer2BackingOption object
      type contains the available options when backing a virtual disk
      using one or more partitions on a physical disk device.
      
      This
      backing is supported in VMware Server.
      """
      pass

   class RawDiskMappingVer1BackingOption(VirtualDeviceOption.DeviceBackingOption):
      """
      The VirtualDiskOption.RawDiskMappingVer1BackingOption object type
      contains the available options when backing a virtual disk using
      a raw device mapping on ESX Server 2.5 or 3.x.
      
      Attributes:
          descriptorFileNameExtensions: Valid extensions for the filename of the optional
              raw disk mapping descriptor file.
              
              This is present only for ESX Server 3.x and greater hosts.
          compatibilityMode: The supported raw disk mapping compatibility modes.
          diskMode: The disk mode.
              
              Valid values are:
              - `persistent`
              - `independent_persistent`
              - `independent_nonpersistent`
          uuid: Flag to indicate whether this backing supports disk UUID property.
          virtualDiskFormat: Virtual disk format.
              
              See `pyVmomi.vim.Datastore.SectorFormat` for the list of supported types.
              
              Since: vSphere API Release 9.0.0.0
      """
      descriptorFileNameExtensions: _typing.Optional[pyVmomi.vim.option.ChoiceOption] = None
      compatibilityMode: pyVmomi.vim.option.ChoiceOption
      diskMode: pyVmomi.vim.option.ChoiceOption
      uuid: bool
      virtualDiskFormat: _typing.Optional[pyVmomi.vim.option.ChoiceOption] = None

   class LocalPMemBackingOption(VirtualDeviceOption.FileBackingOption):
      """
      Deprecated: as of vSphere 9.0 APIs with no replacement.This data object type contains the available options when backing
      a virtualdisk using persistent memory.
      
      Attributes:
          diskMode: The disk mode.
          growable: Indicates whether or not this disk backing can be
              extended to larger sizes through a reconfigure operation.
              
              If set to true, reconfiguring this virtual disk
              with a `pyVmomi.vim.vm.device.VirtualDisk.capacityInKB` value greater
              than its current value will grow the disk to the newly specified size.
          hotGrowable: Indicates whether or not this disk backing can be
              extended to larger sizes through a reconfigure operation while
              the virtual machine is powered on.
              
              If set to true, reconfiguring this virtual disk
              with a `pyVmomi.vim.vm.device.VirtualDisk.capacityInKB` value greater
              than its current value will grow the disk to the newly specified size
              while the virtual machine is powered on.
          uuid: Flag to indicate whether this backing supports disk UUID property.
      """
      diskMode: pyVmomi.vim.option.ChoiceOption
      growable: bool
      hotGrowable: bool
      uuid: bool

   class VFlashCacheConfigOption(pyVmomi.vmodl.DynamicData):
      """
      Deprecated: since vSphere 7.0 because vFlash Read Cache
      end of availability.Options for vFlash cache configuration.
      
      Attributes:
          cacheConsistencyType: Cache data consistency type.
              
              See `pyVmomi.vim.vm.device.VirtualDisk.VFlashCacheConfigInfo.CacheConsistencyType`
          cacheMode: Cache mode
              See `pyVmomi.vim.vm.device.VirtualDisk.VFlashCacheConfigInfo.CacheMode`
          reservationInMB: Cache reservation
          blockSizeInKB: Cache block size
      """
      cacheConsistencyType: pyVmomi.vim.option.ChoiceOption
      cacheMode: pyVmomi.vim.option.ChoiceOption
      reservationInMB: pyVmomi.vim.option.LongOption
      blockSizeInKB: pyVmomi.vim.option.LongOption

   capacityInKB: pyVmomi.vim.option.LongOption
   ioAllocationOption: pyVmomi.vim.StorageResourceManager.IOAllocationOption
   vFlashCacheConfigOption: _typing.Optional[VirtualDiskOption.VFlashCacheConfigOption] = None


class VirtualDiskSpec(VirtualDeviceSpec):
   """
   The VirtualDiskSpec data object type encapsulates change
   specifications for an individual virtual disk device.
   
   The virtual
   disk being added or modified must be fully specified.
   
   Attributes:
       diskMoveType: Manner in which to move the virtual disk to the target datastore.
           
           The set of possible values is described in
           `pyVmomi.vim.vm.RelocateSpec.DiskMoveOptions`.
           
           This property can only be set if `pyVmomi.vim.host.Capability.deltaDiskBackingsSupported` is true.
           
           If left unset then `moveAllDiskBackingsAndDisallowSharing`
           is assumed.
       migrateCache: Manner in which to transfer the cache associated with the virtual disk to the
           target host.
           
           If left unset then migrate is used when virtual flash resource on the source host
           is accessible and when the backing vFlash module version is compatible with the
           specific vFlash module on the target host; otherwise flush is used for write back
           cache, or a no-op for write through cache. This setting can avoid VM migration failure
           due to incompatibility.
           If true then migrate is always used. VM migration may fail if the backing vFlash module
           version is incompatible with the module on the target host.
           If false then flush is used for write back cache. It is a no-op for write through
           cache. This setting can avoid VM migration failure due to incompatibility, but cache
           files have to be rebuilt on the target host.
           Default is unset.
   """
   diskMoveType: _typing.Optional[str] = None
   migrateCache: _typing.Optional[bool] = None


class VirtualEthernetCard(VirtualDevice):
   """
   The `pyVmomi.vim.vm.device.VirtualEthernetCard` data object contains the properties
   of an Ethernet adapter attached to a virtual machine.
   
   Attributes:
       addressType: MAC address type.
           
           Valid values for address type are:
           
           Manual: 
           Statically assigned MAC address.
           
           Generated: 
           Automatically generated MAC address.
           
           Assigned: 
           MAC address assigned by VirtualCenter.
       macAddress: MAC address assigned to the virtual network adapter.
           
           Clients can
           set this property to any of the allowed address types. The server might
           override the specified value for \"Generated\" or \"Assigned\" if it does not
           fall in the right ranges or is determined to be a duplicate.
       wakeOnLanEnabled: Indicates whether wake-on-LAN is enabled on this virtual network adapter.
           
           Clients
           can set this property to selectively enable or disable wake-on-LAN.
       resourceAllocation: Resource requirements of the virtual network adapter
       externalId: An ID assigned to the virtual network adapter by external management plane or
           controller.
           
           The value and format of this property is determined by external
           management plane or controller, and vSphere doesn't do any validation. It's
           also up to external management plane or controller to set, unset or maintain
           this property. Setting this property with an empty string value will unset the
           property.
       uptCompatibilityEnabled: Indicates whether UPT(Universal Pass-through) compatibility is enabled
           on this network adapter.
           
           UPT is only compatible for Vmxnet3 adapter.
           Clients can set this property enabled or disabled if ethernet
           virtual device is Vmxnet3.
       subnetId: The ID of the subnet the virtual network adapter connects to.
           
           It
           is only set when the virtual network adapter is connected
           to a subnet.
           
           Since: vSphere API Release 9.0.0.0
   """
   class NetworkBackingInfo(VirtualDevice.DeviceBackingInfo):
      """
      The `pyVmomi.vim.vm.device.VirtualEthernetCard.NetworkBackingInfo` data object
      defines network backing for a virtual Ethernet card.
      
      Attributes:
          network: Reference to the network managed object to which this backing applies.
              
              This is not used during configuration.
      """
      network: _typing.Optional[pyVmomi.vim.Network] = None
      inPassthroughMode: _typing.Optional[bool] = None

   class LegacyNetworkBackingInfo(VirtualDevice.DeviceBackingInfo):
      """
      The `pyVmomi.vim.vm.device.VirtualEthernetCard.LegacyNetworkBackingInfo` data object
      provides legacy backing for a virtual Ethernet card.
      """
      pass

   class DistributedVirtualPortBackingInfo(VirtualDevice.BackingInfo):
      """
      The `pyVmomi.vim.vm.device.VirtualEthernetCard.DistributedVirtualPortBackingInfo`
      data object defines backing for a virtual Ethernet card that connects
      to a distributed virtual switch port or portgroup.
      
      Attributes:
          port: `pyVmomi.vim.dvs.DistributedVirtualPort` or `pyVmomi.vim.dvs.DistributedVirtualPortgroup`
              connection.
              
              To specify a port connection, set the
              `pyVmomi.vim.dvs.PortConnection.portKey` property.
              To specify a portgroup connection, set the
              `pyVmomi.vim.dvs.PortConnection.portgroupKey` property.
              
              This property will be unset during Virtual Machine or template cloning
              operation unless it's set to a `pyVmomi.vim.dvs.PortConnection`
              object and the portgroup is a late binding portgroup.
      """
      port: pyVmomi.vim.dvs.PortConnection

   class OpaqueNetworkBackingInfo(VirtualDevice.BackingInfo):
      """
      This class defines backing for a virtual Ethernet card that connects
      to an opaque network.
      
      Attributes:
          opaqueNetworkId: The opaque network ID
          opaqueNetworkType: The opaque network type
      """
      opaqueNetworkId: str
      opaqueNetworkType: str

   class ResourceAllocation(pyVmomi.vmodl.DynamicData):
      """
      This class specifies the network resource requirement.
      
      Attributes:
          reservation: Amount of network bandwidth that is guaranteed to the
              virtual network adapter.
              
              If utilization is less than reservation, the resource can be used by
              other virtual network adapters. Reservation is not allowed to exceed the
              value of `pyVmomi.vim.vm.device.VirtualEthernetCard.ResourceAllocation.limit` if
              `pyVmomi.vim.vm.device.VirtualEthernetCard.ResourceAllocation.limit` is set.
              Units in Mbits/sec.
          share: Network share.
              
              The value is used as a relative weight in
              competing for shared bandwidth, in case of resource contention.
          limit: The bandwidth limit for the virtual network adapter.
              
              The utilization of the virtual network adapter will not
              exceed this limit, even if there are available resources.
              To clear the value of this property and revert it to unset,
              set the value to \"-1\" in an update operation.
              Units in Mbits/sec.
      """
      reservation: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      share: pyVmomi.vim.SharesInfo
      limit: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   addressType: _typing.Optional[str] = None
   macAddress: _typing.Optional[str] = None
   wakeOnLanEnabled: _typing.Optional[bool] = None
   resourceAllocation: _typing.Optional[VirtualEthernetCard.ResourceAllocation] = None
   externalId: _typing.Optional[str] = None
   uptCompatibilityEnabled: _typing.Optional[bool] = None
   subnetId: _typing.Optional[str] = None

class VirtualE1000(VirtualEthernetCard):
   """
   The VirtualE1000 data object type represents an instance
   of the E1000 virtual Ethernet adapter attached to a virtual machine.
   """
   pass


class VirtualEthernetCardOption(VirtualDeviceOption):
   """
   This data object type contains the options for the
   virtual ethernet card data object type.
   
   Attributes:
       supportedOUI: The valid Organizational Unique Identifiers (OUIs)
           supported by this virtual Ethernet card.
           
           Supported OUIs for statically assigned MAC addresses:: 
           \"00:50:56\"
       macType: The supported MAC address types.
       wakeOnLanEnabled: Flag to indicate whether or not wake-on-LAN is settable on this device.
       vmDirectPathGen2Supported: Flag to indicate whether VMDirectPath Gen 2 is available on this device.
       uptCompatibilityEnabled: Flag to indicate whether Universal Pass-through(UPT) is settable on this device.
   """
   class NetworkBackingOption(VirtualDeviceOption.DeviceBackingOption):
      """
      This data object type contains the options for
      the virtual network card backing data object type.
      """
      pass

   class OpaqueNetworkBackingOption(VirtualDeviceOption.BackingOption):
      """
      This data object type contains the options for
      the virtual network card backing data object type.
      """
      pass

   class LegacyNetworkBackingOption(VirtualDeviceOption.DeviceBackingOption):
      """
      This data object type contains the options
      for using a legacy virtual network card backing data object type.
      """
      class LegacyNetworkDeviceName(pyVmomi.VmomiSupport.Enum):
         """
         Possible device names for legacy network backing option are listed below.
         
         Note: This is not an exhaustive list. It is possible to specify
         a specific device as well.
         For example, on ESX hosts, the device name could be specified as \"vmnic[0-9]\"
         or vmnet_[0-9].
         For VMware Server Windows hosts, the device name could be specified as \"vmnet[0-9]\"
         and for VMware Server Linux hosts, the device name could be specified as \"/dev/vmnet[0-9]\"
         depending on what devices are available on that particular host.
         """
         bridged: _typing.ClassVar['VirtualEthernetCardOption.LegacyNetworkBackingOption.LegacyNetworkDeviceName'] = 'bridged'
         nat: _typing.ClassVar['VirtualEthernetCardOption.LegacyNetworkBackingOption.LegacyNetworkDeviceName'] = 'nat'
         hostonly: _typing.ClassVar['VirtualEthernetCardOption.LegacyNetworkBackingOption.LegacyNetworkDeviceName'] = 'hostonly'

   class DistributedVirtualPortBackingOption(VirtualDeviceOption.BackingOption):
      """
      This data object type contains the options for using a distributed
      virtual port virtual network card backing data object type.
      """
      pass

   class MacTypes(pyVmomi.VmomiSupport.Enum):
      """
      The enumeration of all known valid MAC address types.
      
      Attributes:
          manual: A statistically assigned MAC address.
          generated: An automatically generated MAC address.
          assigned: A MAC address assigned by VirtualCenter.
      """
      manual: _typing.ClassVar['VirtualEthernetCardOption.MacTypes'] = 'manual'
      generated: _typing.ClassVar['VirtualEthernetCardOption.MacTypes'] = 'generated'
      assigned: _typing.ClassVar['VirtualEthernetCardOption.MacTypes'] = 'assigned'

   supportedOUI: pyVmomi.vim.option.ChoiceOption
   macType: pyVmomi.vim.option.ChoiceOption
   wakeOnLanEnabled: pyVmomi.vim.option.BoolOption
   vmDirectPathGen2Supported: _typing.Optional[bool] = None
   uptCompatibilityEnabled: _typing.Optional[pyVmomi.vim.option.BoolOption] = None

class VirtualE1000Option(VirtualEthernetCardOption):
   """
   The VirtualE1000 option data object type contains the options for the
   `pyVmomi.vim.vm.device.VirtualE1000` data object type.
   """
   pass

class VirtualE1000e(VirtualEthernetCard):
   """
   The VirtualE1000e data object type represents an instance
   of the E1000e virtual Ethernet adapter attached to a virtual machine.
   """
   pass

class VirtualE1000eOption(VirtualEthernetCardOption):
   """
   The VirtualE1000e option data object type contains the options for the
   `pyVmomi.vim.vm.device.VirtualE1000e` data object type.
   """
   pass

class VirtualSoundCard(VirtualDevice):
   """
   This data object type represents a sound card in
   a virtual machine.
   """
   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      """The sound card device backing data class."""
      pass

class VirtualEnsoniq1371(VirtualSoundCard):
   """
   The VirtualEnsoniq1371 data object type represents an Ensoniq 1371
   sound card in a virtual machine.
   """
   pass

class VirtualSoundCardOption(VirtualDeviceOption):
   """
   The VirtualSoundCardOption data class contains the options for the
   virtual sound card class.
   """
   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      """
      The VirtualSoundCardBackingOption class contains the options
      for the virtual sound card backing class.
      """
      pass

class VirtualEnsoniq1371Option(VirtualSoundCardOption):
   """
   The VirtualEnsoniq1371Option data object type contains the options for the
   virtual Ensoniq 1371 sound card.
   """
   pass

class VirtualFloppy(VirtualDevice):
   """
   The VirtualFloppy data object type contains information about a floppy drive
   in a virtual machine.
   """
   class ImageBackingInfo(VirtualDevice.FileBackingInfo):
      """The data object type for file image backing of a virtual floppy drive."""
      pass

   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      """The data object type for device backing of a virtual floppy drive."""
      pass

   class RemoteDeviceBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
      """The data object type for remote device backing of a virtual floppy drive."""
      pass

class VirtualFloppyOption(VirtualDeviceOption):
   """
   The VirtualFloppyOption data class contains the options for the
   virtual floppy data object type.
   """
   class ImageBackingOption(VirtualDeviceOption.FileBackingOption):
      """
      The ImageBackingOption data object type contains the options
      for the floppy image backing type.
      """
      pass

   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      """
      The DeviceBackingOption data object type contains the options
      for the floppy device backing type.
      """
      pass

   class RemoteDeviceBackingOption(VirtualDeviceOption.RemoteDeviceBackingOption):
      """
      The RemoteDeviceBackingOption data object type contains the options
      for the floppy remote device backing type.
      """
      pass

class VirtualHdAudioCard(VirtualSoundCard):
   """
   The VirtualHdAudioCard data object type represents a HD Audio
   sound card in a virtual machine.
   """
   pass

class VirtualHdAudioCardOption(VirtualSoundCardOption):
   """
   The VirtualHdAudioCardOption data object type contains the options for a
   virtual HD Audio sound card.
   """
   pass

class VirtualIDEController(VirtualController):
   """The VirtualIDEController data object type specifies a virtual IDE controller."""
   pass


class VirtualIDEControllerOption(VirtualControllerOption):
   """
   The VirtualIDEControllerOption data object type contains the options
   for a virtual IDE controller.
   
   Attributes:
       numIDEDisks: The minimum, maximum, and default number of IDE VirtualDisk instances you can
           have, at any given time, in the IDE controller.
           
           The number is further constrained
           by the number of available slots in the virtual IDE controller.
       numIDECdroms: The minimum, maximum, and default number of IDE VirtualCdrom instances you can
           have, at any given time, in the IDE controller.
           
           The number is further constrained
           by the number of available slots in the virtual IDE controller.
   """
   numIDEDisks: pyVmomi.vim.option.IntOption
   numIDECdroms: pyVmomi.vim.option.IntOption

class VirtualKeyboard(VirtualDevice):
   """
   This data object type contains information about
   the keyboard on a virtual machine.
   """
   pass

class VirtualKeyboardOption(VirtualDeviceOption):
   """
   The VirtualKeyboardOption data object type contains the options for the
   virtual keyboard class.
   """
   pass

class VirtualLsiLogicController(VirtualSCSIController):
   """
   VirtualLsiLogicController is the data object that represents
   a LSI Logic SCSI controller.
   """
   pass

class VirtualLsiLogicControllerOption(VirtualSCSIControllerOption):
   """
   VirtualLsiLogicControllerOption is the data object that contains
   the options for a LSI Logic SCSI controller.
   """
   pass

class VirtualLsiLogicSASController(VirtualSCSIController):
   """
   VirtualLsiLogicSASController is the data object that represents
   a LSI Logic SAS SCSI controller.
   """
   pass

class VirtualLsiLogicSASControllerOption(VirtualSCSIControllerOption):
   """
   VirtualLsiLogicSASControllerOption is the data object that contains
   the options for a LSI Logic SAS SCSI controller.
   """
   pass


class VirtualNVDIMM(VirtualDevice):
   """
   Deprecated: as of vSphere 9.0 APIs with no replacement.The Virtual NVDIMM device.
   
   Attributes:
       capacityInMB: NVDIMM backing size in MiB.
           
           If backing is inaccessible, then
           capacity is reported as 0.
       configuredCapacityInMB: NVDIMM device's configured size in MiB.
           
           Since: vSphere API Release 7.0.2.0
   """
   class BackingInfo(VirtualDevice.FileBackingInfo):
      """
      The ``pyVmomi.vim.vm.device.VirtualNVDIMM.BackingInfo`` data object type
      defines information about a resource that backs a device
      in a virtual machine.
      
      Attributes:
          parent: Parent object in snapshot chain.
          changeId: The change ID of the virtual NVDIMM for the corresponding
              snapshot of virtual machine.
              
              This can be used to track
              incremental changes.
              See `pyVmomi.vim.VirtualMachine.queryChangedDiskAreas`.
      """
      parent: _typing.Optional[VirtualNVDIMM.BackingInfo] = None
      changeId: _typing.Optional[str] = None

   capacityInMB: pyVmomi.VmomiSupport.long
   configuredCapacityInMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None

class VirtualNVDIMMController(VirtualController):
   """Deprecated: as of vSphere 9.0 APIs with no replacement.The Virtual NVDIMM controller."""
   pass


class VirtualNVDIMMControllerOption(VirtualControllerOption):
   """
   Deprecated: as of vSphere 9.0 APIs with no replacement.VirtualNVDIMMControllerOption is the data object that contains
   the options for a virtual NVDIMM controller.
   
   Attributes:
       numNVDIMMControllers: Minimum, maximum and default number of virtual NVDIMM controllers.
   """
   numNVDIMMControllers: pyVmomi.vim.option.IntOption


class VirtualNVDIMMOption(VirtualDeviceOption):
   """
   Deprecated: as of vSphere 9.0 APIs with no replacement.The VirtualNVDIMMOption contains information about
   a virtual NVDIMM capacity limits and rules for
   capacity growth operations.
   
   Attributes:
       capacityInMB: Minimum and maximum capacity in MB.
       growable: Option to show if device capacity growth is supported for
           powered off VMs.
       hotGrowable: Option to show if device capacity growth is supported for
           powered on VMs.
       granularityInMB: Option to show capacity growth granularity if growth operation
           is supported in MB.
   """
   capacityInMB: pyVmomi.vim.option.LongOption
   growable: bool
   hotGrowable: bool
   granularityInMB: pyVmomi.VmomiSupport.long


class VirtualNVMEController(VirtualController):
   """
   The Virtual NVME controller.
   
   Attributes:
       sharedBus: Mode for sharing the SCSI bus.
           
           The modes are physicalSharing,
           and noSharing. See the
           `pyVmomi.vim.vm.device.VirtualNVMEController.Sharing`
           data object type for an explanation of these modes.
           
           Since: vSphere API Release 8.0.2.0
   """
   class Sharing(pyVmomi.VmomiSupport.Enum):
      """Since: vSphere API Release 8.0.2.0"""
      noSharing: _typing.ClassVar['VirtualNVMEController.Sharing'] = 'noSharing'
      physicalSharing: _typing.ClassVar['VirtualNVMEController.Sharing'] = 'physicalSharing'

   sharedBus: _typing.Optional[str] = None


class VirtualNVMEControllerOption(VirtualControllerOption):
   """
   VirtualNVMEControllerOption is the data object that contains
   the options for a virtual NVME controller.
   
   Attributes:
       numNVMEDisks: Three properties (numNVMEDisks.min, numNVMEDisks.max, and
           numNVMEDisks.defaultValue) define the minimum, maximum, and default
           number of NVME VirtualDisk instances available at any given time in the
           NVME controller.
           
           The number of NVME VirtualDisk instances is
           also limited by the number of available namespaces in the NVME controller.
       sharing: Supported shared bus modes.
           
           See `pyVmomi.vim.vm.device.VirtualNVMEController.Sharing` for the list of available modes.
           
           Since: vSphere API Release 8.0.2.0
   """
   numNVMEDisks: pyVmomi.vim.option.IntOption
   sharing: list[str] = []

class VirtualPCIController(VirtualController):
   """
   The VirtualPCIController data object type defines a virtual PCI
   controller.
   """
   pass


class VirtualPCIControllerOption(VirtualControllerOption):
   """
   This data object type contains the options
   for a virtual PCI Controller.
   
   Attributes:
       numSCSIControllers: Defines the minimum, maximum, and
           default number of VirtualSCSIController instances available
           at any given time in the PCI controller.
           
           The number of
           VirtualSCSIController instances is also limited by the number of
           available slots in the PCI controller.
       numEthernetCards: Defines the minimum, maximum, and
           default number of VirtualEthernetCard instances available,
           at any given time, in the PCI controller.
           
           The number of
           VirtualEthernetCard instances is also limited by the number of
           available slots in the PCI controller.
       numVideoCards: Defines the minimum, maximum, and default
           number of VirtualVideoCard instances available,
           at any given time, in the PCI controller.
           
           The number of
           VirtualVideoCard instances is also limited by the number of
           available slots in the PCI controller.
       numSoundCards: Defines the minimum, maximum, and default
           number of VirtualSoundCard instances available,
           at any given time, in the PCI controller.
           
           The number of
           VirtualSoundCard instances is also limited by the number of
           available slots in the PCI controller.
       numVmiRoms: Defines the minimum, maximum, and default
           number of VirtualVMIROM instances available,
           at any given time, in the PCI controller.
           
           This is also limited
           by the number of available slots in the PCI controller.
       numVmciDevices: Defines the minimum, maximum, and default
           number of VirtualVMCIDevice instances available,
           at any given time, in the PCI controller.
           
           This is also limited
           by the number of available slots in the PCI controller.
       numPCIPassthroughDevices: Defines the minimum, maximum, and default
           number of VirtualPCIPassthrough instances available,
           at any given time, in the PCI controller.
           
           This is also limited
           by the number of available PCI Express slots in the PCI controller.
       numSasSCSIControllers: Defines the minimum, maximum, and default
           number of VirtualLsiLogicSASController instances available,
           at any given time, in the PCI controller.
           
           This is also limited
           by the number of available PCI Express slots in the PCI controller
           as well as the total number of supported SCSI controllers.
       numVmxnet3EthernetCards: Defines the minimum, maximum, and default
           number of VirtualVmxnet3 ethernet card instances available,
           at any given time, in the PCI controller.
           
           This is also limited
           by the number of available PCI Express slots in the PCI controller
           as well as the total number of supported ethernet cards.
       numParaVirtualSCSIControllers: Defines the minimum, maximum, and default
           number of ParaVirtualScsiController instances available,
           at any given time, in the PCI controller.
           
           This is also limited
           by the number of available PCI Express slots in the PCI controller
           as well as the total number of supported SCSI controllers.
       numSATAControllers: Defines the minimum, maximum, and default
           number of VirtualSATAController instances available,
           at any given time, in the PCI controller.
           
           This is also limited
           by the number of available PCI Express slots in the PCI controller
           as well as the total number of supported SATA controllers.
       numNVMEControllers: Defines the minimum, maximum, and default
           number of VirtualNVMEController instances available,
           at any given time, in the PCI controller.
           
           This is also limited
           by the number of available PCI Express slots in the PCI controller
           as well as the total number of supported NVME controllers.
       numVmxnet3VrdmaEthernetCards: Defines the minimum, maximum, and default
           number of VirtualVmxnet3Vrdma ethernet card instances available,
           at any given time, in the PCI controller.
           
           This is also limited
           by the number of available PCI Express slots in the PCI controller
           as well as the total number of supported ethernet cards.
   """
   numSCSIControllers: pyVmomi.vim.option.IntOption
   numEthernetCards: pyVmomi.vim.option.IntOption
   numVideoCards: pyVmomi.vim.option.IntOption
   numSoundCards: pyVmomi.vim.option.IntOption
   numVmiRoms: pyVmomi.vim.option.IntOption
   numVmciDevices: pyVmomi.vim.option.IntOption
   numPCIPassthroughDevices: pyVmomi.vim.option.IntOption
   numSasSCSIControllers: pyVmomi.vim.option.IntOption
   numVmxnet3EthernetCards: pyVmomi.vim.option.IntOption
   numParaVirtualSCSIControllers: pyVmomi.vim.option.IntOption
   numSATAControllers: pyVmomi.vim.option.IntOption
   numNVMEControllers: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   numVmxnet3VrdmaEthernetCards: _typing.Optional[pyVmomi.vim.option.IntOption] = None


class VirtualPCIPassthrough(VirtualDevice):
   """
   The VirtualPCIPassthrough data object type contains information about a
   PCI device on the virtual machine that is being backed by
   a generic PCI device on the host via passthrough.
   """
   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      """
      The VirtualPCIPassthrough.DeviceBackingInfo data object type
      contains information about the backing that maps the
      virtual device onto a physical device.
      
      Attributes:
          id: The name ID of this PCI, composed of \"bus:slot.function\".
          deviceId: The device ID of this PCI.
              
              You must use the device ID retrieved
              from the vSphere host (`pyVmomi.vim.host.PciDevice`.deviceId), converted
              as is to a string.
          systemId: The ID of the system the PCI device is attached to.
          vendorId: The vendor ID for this PCI device.
              
              You must use the vendor ID retrieved
              from the vSphere host (`pyVmomi.vim.host.PciDevice`.vendorId).
      """
      id: str
      deviceId: str
      systemId: str
      vendorId: pyVmomi.VmomiSupport.short

   class AllowedDevice(pyVmomi.vmodl.DynamicData):
      """
      A tuple of vendorId and deviceId indicating an allowed device
      for a Dynamic DirectPath device.
      
      Attributes:
          vendorId: The vendor ID for this PCI device.
              
              You must use the vendor ID
              retrieved from the vSphere host or cluster.
          deviceId: The device ID of this PCI device.
              
              You must use the device ID
              retrieved from the vSphere host or cluster.
          subVendorId: The subVendor ID for this PCI device.
              
              If specified, you must use
              the subVendor ID retrieved from the vSphere host or cluster.
              Range of legal values is 0x0 to 0xFFFF.
          subDeviceId: The subDevice ID of this PCI device.
              
              If specified, you must use
              the subDevice ID retrieved from the vSphere host or cluster.
              Range of legal values is 0x0 to 0xFFFF.
          revisionId: The revision ID of this PCI device.
              
              If specified, you must use
              the revision ID retrieved from the vSphere host or cluster.
              Range of legal values is 0x0 to 0xFF.
      """
      vendorId: int
      deviceId: int
      subVendorId: _typing.Optional[int] = None
      subDeviceId: _typing.Optional[int] = None
      revisionId: _typing.Optional[pyVmomi.VmomiSupport.short] = None

   class DynamicBackingInfo(VirtualDevice.DeviceBackingInfo):
      """
      The VirtualPCIPassthrough.DynamicBackingInfo data object type
      contains information about the backing that maps the
      virtual device onto a physical device for a Dynamic DirectPath
      device.
      
      Attributes:
          allowedDevice: The list of allowed devices for use with a Dynamic DirectPath
              device.
          customLabel: An optional label.
              
              If set, the device must also have the same
              customLabel attribute set.
          assignedId: The id of the device assigned when the VM is powered on.
              
              This value
              is unset when the VM is powered off.
      """
      allowedDevice: list[VirtualPCIPassthrough.AllowedDevice] = []
      customLabel: _typing.Optional[str] = None
      assignedId: _typing.Optional[str] = None

   class PluginBackingInfo(VirtualDevice.BackingInfo):
      """
      The VirtualPCIPassthrough.PluginBackingInfo is a base data object type
      for encoding plugin-specific information.
      
      This base type does not define
      any properties. Specific plugin types are represented by subtypes which
      define properties for subtype-specific backing information.
      """
      pass

   class VmiopBackingInfo(VirtualPCIPassthrough.PluginBackingInfo):
      """
      The VirtualPCIPassthrough.VmiopBackingInfo data object type
      contains information about the plugin that emulates the
      virtual device via the VMIOP plugin interface.
      
      At present, this interface is only used to implement vGPU.
      
      Attributes:
          vgpu: The vGPU configuration type exposed by a VMIOP plugin.
          vgpuMigrateDataSizeMB: The expected size of the vGPU device state during migration.
              
              Since: vSphere API Release 8.0.0.1
          migrateSupported: Indicates whether the vGPU device is migration capable or not.
              
              Since: vSphere API Release 7.0.2.0
          enhancedMigrateCapability: Indicates whether the vGPU has enhanced migration features for
              sub-second downtime.
              
              Since: vSphere API Release 8.0.0.1
      """
      vgpu: _typing.Optional[str] = None
      vgpuMigrateDataSizeMB: _typing.Optional[int] = None
      migrateSupported: _typing.Optional[bool] = None
      enhancedMigrateCapability: _typing.Optional[bool] = None

   class DvxBackingInfo(VirtualDevice.BackingInfo):
      """
      DVX Device specific information.
      
      Attributes:
          deviceClass: The device class that backs this DVX device.
              
              During add operations, this value must be a non-empty string.
              During edit operations, if this value is not set or is an empty
              string, the current device class remains unchanged.
          configParams: The configuration parameters for this device class.
              
              All required configuration parameters must be provided for both add
              and edit operations. The provided configuration parameters replace
              the previous ones. In particular, passing an empty array will unset
              all existing configuration parameters.
      
      Since: vSphere API Release 8.0.0.1
      """
      deviceClass: _typing.Optional[str] = None
      configParams: list[pyVmomi.vim.option.OptionValue] = []


class VirtualPCIPassthroughOption(VirtualDeviceOption):
   """
   The VirtualPCIPassthroughOption data object type describes the options
   for the
   `pyVmomi.vim.vm.device.VirtualPCIPassthrough`
   data object type.
   """
   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      """
      This data object type describes the options for the
      `pyVmomi.vim.vm.device.VirtualPCIPassthrough.DeviceBackingInfo` data object type.
      """
      pass

   class PluginBackingOption(VirtualDeviceOption.BackingOption):
      """
      This data object type describes the options for the
      `pyVmomi.vim.vm.device.VirtualPCIPassthrough.PluginBackingInfo` data object type.
      """
      pass

   class VmiopBackingOption(VirtualPCIPassthroughOption.PluginBackingOption):
      """
      This data object type describes the options for the
      `pyVmomi.vim.vm.device.VirtualPCIPassthrough.VmiopBackingInfo` data object type.
      
      Attributes:
          vgpu: Parameter indicating which GPU profile the plugin should emulate.
          maxInstances: Maximum number of instances of this backing type allowed
              per virtual machine.
              
              This is a parameter of the plugin
              itself, which may support only a limited number of
              instances per virtual machine.
      """
      vgpu: pyVmomi.vim.option.StringOption
      maxInstances: int

   class DynamicBackingOption(VirtualDeviceOption.DeviceBackingOption):
      """
      This data object type describes the options for the
      `pyVmomi.vim.vm.device.VirtualPCIPassthrough.DynamicBackingInfo` data object type.
      """
      pass

   class DvxBackingOption(VirtualDeviceOption.BackingOption):
      """
      Describes the options for
      `pyVmomi.vim.vm.device.VirtualPCIPassthrough.DvxBackingInfo`.
      
      Since: vSphere API Release 8.0.0.1
      """
      pass

class VirtualPCNet32(VirtualEthernetCard):
   """
   This data object type defines the properties
   of an AMD Lance PCNet32 Ethernet card attached to a virtual machine.
   """
   pass

class VirtualPCNet32Option(VirtualEthernetCardOption):
   """
   The VirtualPCNet32Option data object type defines the options for the
   VirtualPCNet32 data object type.
   
   Except for the boolean
   supportsMorphing option, the options are inherited from the
   `pyVmomi.vim.vm.device.VirtualEthernetCardOption` data
   object type.
   
   Attributes:
       supportsMorphing: Indicates that this Ethernet card supports morphing into vmxnet when
           appropriate.
           
           This means that, if supportsMorphing=\"true\", the virtual
           AMD Lance PCNet32 Ethernet card becomes a vmxnet Ethernet card
           with its added performance capabilities when appropriate.
   """
   supportsMorphing: bool

class VirtualPS2Controller(VirtualController):
   """
   The VirtualPS2Controller data object type represents a controller
   for keyboards and mice.
   """
   pass


class VirtualPS2ControllerOption(VirtualControllerOption):
   """
   The VirtualPS2ControllerOption data object type contains the options
   for a virtual PS/2 controller for keyboards and mice.
   
   In addition to
   the options defined in the `pyVmomi.vim.vm.device.VirtualControllerOption` data object type, these options include the
   number of keyboards and mice.
   
   Attributes:
       numKeyboards: The minimum, maximum, and default number of keyboards you can
           have at any given time.
           
           This is further constrained by the number
           of available slots in the PS/2 controller. The minimum, maximum,
           and default are integers defined by three properties:
           - numKeyBoards.min: the minimum.
           - numKeyBoards.max: the maximum.
           - numKeyBoards.defaultValue: the default number.
       numPointingDevices: The minimum, maximum, and default number of mice you can
           have at any given time.
           
           The number of mice is also limited by the number
           of available slots in the PS/2 controller. The minimum, maximum, and
           default are integers defined by three properties:
           - numPointingDevices.min: the minimum.
           - numPointingDevices.max: the maximum.
           - numPointingDevices.defaultValue: the default number.
   """
   numKeyboards: pyVmomi.vim.option.IntOption
   numPointingDevices: pyVmomi.vim.option.IntOption

class VirtualParallelPort(VirtualDevice):
   """
   This data object type represents a parallel port
   in a virtual machine.
   """
   class FileBackingInfo(VirtualDevice.FileBackingInfo):
      """The data object type for a file backing of a virtual parallel port."""
      pass

   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      """The data object type for a device backing of a virtual parallel port."""
      pass

class VirtualParallelPortOption(VirtualDeviceOption):
   """
   This data object type contains the options for the
   virtual parallel port class.
   """
   class FileBackingOption(VirtualDeviceOption.FileBackingOption):
      """
      Data object type that represents the options for a file backing
      of a virtual parallel port.
      """
      pass

   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      """
      Data object type that represents the options for a device backing
      of a virtual parallel port.
      """
      pass

class VirtualPointingDevice(VirtualDevice):
   """
   The VirtualPointingDevice data object type contains information about
   the mouse type on a virtual machine.
   """
   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      """
      The VirtualPointingDevice.DeviceBackingInfo provides information about
      the physical mouse backing the VirtualPointingDevice data object
      type.
      
      Attributes:
          hostPointingDevice: This optional property defines the mouse type (two-button,
              three-button, and so on).
              
              The mouse type
              determines how the user interacts with the host mouse.
              The valid values are specified in the
              `pyVmomi.vim.vm.device.VirtualPointingDeviceOption.DeviceBackingOption.HostPointingDeviceChoice` list.
              
              Note: The value specified by this property must be
              one of the supported types listed in the hostPointingDevices.value
              array in the `pyVmomi.vim.vm.device.VirtualPointingDeviceOption` data object type. If this property is
              not set, then the property defaults to the
              hostPointingDevices.defaultIndex property in the same data
              object type.
      """
      hostPointingDevice: str


class VirtualPointingDeviceOption(VirtualDeviceOption):
   """
   The VirtualPointingDeviceOption data object type contains the options
   for the host mouse type defined in the
   `pyVmomi.vim.vm.device.VirtualPointingDevice` data object type.
   
   These options include the valid selections for the mouse type, the supported
   mouse types, and the default mouse type.
   """
   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      """
      The DeviceBackingOption data object type represents
      the options for a pointing device backing a
      VirtualPointingDevice data object type.
      
      Attributes:
          hostPointingDevice: This object defines the supported mouse types, including the default
              supported mouse type, with the following properties:
              - hostPointingDevices.value: This array defines the
                supported mouse types.
              - hostPointingDevices.choiceDescription: This array
                provides the descriptions for the supported mouse types defined by
                hostPointingDevices.value.
              - hostPointingDevices.defaultIndex: This integer points
                to an index in the hostPointingDevices.value array. This is the
                mouse type supported by default.
      """
      class HostPointingDeviceChoice(pyVmomi.VmomiSupport.Enum):
         """
         The valid choices for host pointing devices are:
         
         Attributes:
             autodetect: Automatically detects the host mouse type.
             intellimouseExplorer: The Microsoft IntelliMouse Explorer.
             intellimousePs2: The Microsoft Intellimouse with a PS2 connection.
             logitechMouseman: The Logitech MouseMan.
             microsoft_serial: The Microsoft Serial Mouse.
             mouseSystems: The Mouse Systems Mouse.
             mousemanSerial: The Logitech MouseMan Serial Bus Mouse.
             ps2: A generic mouse with a PS2 connection.
         """
         autodetect: _typing.ClassVar['VirtualPointingDeviceOption.DeviceBackingOption.HostPointingDeviceChoice'] = 'autodetect'
         intellimouseExplorer: _typing.ClassVar['VirtualPointingDeviceOption.DeviceBackingOption.HostPointingDeviceChoice'] = 'intellimouseExplorer'
         intellimousePs2: _typing.ClassVar['VirtualPointingDeviceOption.DeviceBackingOption.HostPointingDeviceChoice'] = 'intellimousePs2'
         logitechMouseman: _typing.ClassVar['VirtualPointingDeviceOption.DeviceBackingOption.HostPointingDeviceChoice'] = 'logitechMouseman'
         microsoft_serial: _typing.ClassVar['VirtualPointingDeviceOption.DeviceBackingOption.HostPointingDeviceChoice'] = 'microsoft_serial'
         mouseSystems: _typing.ClassVar['VirtualPointingDeviceOption.DeviceBackingOption.HostPointingDeviceChoice'] = 'mouseSystems'
         mousemanSerial: _typing.ClassVar['VirtualPointingDeviceOption.DeviceBackingOption.HostPointingDeviceChoice'] = 'mousemanSerial'
         ps2: _typing.ClassVar['VirtualPointingDeviceOption.DeviceBackingOption.HostPointingDeviceChoice'] = 'ps2'

      hostPointingDevice: pyVmomi.vim.option.ChoiceOption


class VirtualPrecisionClock(VirtualDevice):
   """
   This data object type represents a virtual clock device providing
   precision time in a virtual machine.
   """
   class SystemClockBackingInfo(VirtualDevice.BackingInfo):
      """
      The `pyVmomi.vim.vm.device.VirtualPrecisionClock.SystemClockBackingInfo`
      data object contains information about using host system clock as the
      backing reference clock for this virtual device.
      
      Attributes:
          protocol: The time synchronization protocol used to discipline system clock.
              
              See `pyVmomi.vim.host.DateTimeInfo.Protocol` for valid values.
      """
      protocol: _typing.Optional[str] = None


class VirtualPrecisionClockOption(VirtualDeviceOption):
   """
   The VirtualPrecisionClockOption data object type describes the
   options for the `pyVmomi.vim.vm.device.VirtualPrecisionClock` data
   object type.
   """
   class SystemClockBackingOption(VirtualDeviceOption.BackingOption):
      """
      This data object type describes the options for the
      `pyVmomi.vim.vm.device.VirtualPrecisionClock.SystemClockBackingInfo`
      VirtualPrecisionClockSystemClockBackingInfo} data object type.
      
      Attributes:
          protocol: Parameter indicating the protocol used to discipline the
              host system clock.
      """
      protocol: pyVmomi.vim.option.ChoiceOption

class VirtualSCSIPassthrough(VirtualDevice):
   """
   The VirtualSCSIPassthrough data object type contains information about a
   SCSI device on the virtual machine that is being backed by
   a generic SCSI device on the host via passthrough.
   """
   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      """
      The VirtualSCSIPassthrough.DeviceBackingInfo data object type
      contains information about the backing that maps the
      virtual device onto a physical device.
      """
      pass

class VirtualSCSIPassthroughOption(VirtualDeviceOption):
   """
   The VirtualSCSIPassthroughOption data object type describes the options
   for the
   `pyVmomi.vim.vm.device.VirtualSCSIPassthrough`
   data object type.
   """
   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      """
      This data object type describes
      the options for the
      `pyVmomi.vim.vm.device.VirtualSCSIPassthrough.DeviceBackingInfo` data object type.
      """
      pass

class VirtualSIOController(VirtualController):
   """
   This data object type defines a
   Super IO Controller for floppy drives, parallel ports,
   and serial ports.
   """
   pass


class VirtualSIOControllerOption(VirtualControllerOption):
   """
   The VirtualSIOControllerOption data object type contains the options
   for a virtual Super IO Controller.
   
   Attributes:
       numFloppyDrives: Three properties (numFloppyDrives.min, numFloppyDrives.max, and
           numFloppyDrives.defaultValue) define the minimum, maximum, and default
           number of floppy drives you can have at any given time in the Super IO
           Controller.
           
           This is further constrained by the number of available
           slots in the Super IO Controller.
       numSerialPorts: Three properties (numSerialPorts.min, numSerialPorts.max, and
           numSerialPorts.defaultValue) define the minimum, maximum, and default
           number of serial ports you can
           have at any given time in the Super IO Controller.
           
           This is further
           constrained by the number of available slots in the Super IO
           Controller.
       numParallelPorts: Three properties (numParallelPorts.min, numParallelPorts.max, and
           numParallelPorts.defaultValue) define the minimum, maximum, and default
           number of parallel ports you can
           have at any given time in the Super IO controller.
           
           This is further
           constrained by the number of available slots in the Super IO
           Controller.
   """
   numFloppyDrives: pyVmomi.vim.option.IntOption
   numSerialPorts: pyVmomi.vim.option.IntOption
   numParallelPorts: pyVmomi.vim.option.IntOption


class VirtualSerialPort(VirtualDevice):
   """
   The ``pyVmomi.vim.vm.device.VirtualSerialPort`` data object represents a serial port
   on a virtual machine.
   
   A virtual serial port uses one of the following backing types to specify
   how the virtual machine performs serial port operations.
   - Network backing (``pyVmomi.vim.vm.device.VirtualSerialPort.URIBackingInfo``)
     supports a connection between the virtual machine and a resource
     on the network. The virtual machine can initiate a connection with
     the network resource, or it can listen for connections originating
     from the network.
   - Pipe backing (``pyVmomi.vim.vm.device.VirtualSerialPort.PipeBackingInfo``)
     supports I/O through a named pipe. The pipe connects the virtual machine
     to a host application or a virtual machine on the same host.
   - File backing (``pyVmomi.vim.vm.device.VirtualSerialPort.FileBackingInfo``)
     supports output through the virtual serial port to a file on the same host.
   - Physical serial port backing
     (``pyVmomi.vim.vm.device.VirtualSerialPort.DeviceBackingInfo``)
     supports a connection between the virtual machine and a
     device that is connected to a physical serial port on the host.
   - ThinPrint backing (``pyVmomi.vim.vm.device.VirtualSerialPort.ThinPrintBackingInfo``)
     provides driver-free printing.
     
   When you use network backing, you can also configure a virtual serial port
   to use a virtual serial port concentrator. The virtual machine initiates
   a telnet connection with the concentrator, and the concentrator acts
   as a proxy between the virtual machine and a system on the network.
   By using a virtual serial port concentrator, you can maintain the connection
   between the virtual machine and the network resource
   when a vMotion event moves the virtual machine from one host to another.
   Without a virtual serial port concentrator, the connection would be lost.
   For information about using a serial port concentrator,
   see Using a Proxy with vSphere Virtual Serial Ports.
   
   You can configure a virtual serial port when you create or reconfigure
   a virtual machine. For example, to create a virtual serial port
   with network backing, use the following sequence of operations.
   In this procedure, the virtual serial port uses a proxy and will accept
   a network connection.
   1. Use the ``pyVmomi.vim.EnvironmentBrowser.queryConfigOption`` method
      to determine the backing options that are available on a host.
      The method returns a ``pyVmomi.vim.vm.ConfigOption`` data object.
      The virtual machine configuration data includes a list of backing options
      (``pyVmomi.vim.vm.device.VirtualDeviceOption.backingOption``).
      The following pseudocode shows the path to the backing options.
      
      
          ``pyVmomi.vim.vm.ConfigOption`.hardwareOptions.VirtualDeviceOption[].backingOption[]`
      
      
      The array of virtual device options can include a virtual serial port
      (``pyVmomi.vim.vm.device.VirtualSerialPortOption``). The array of serial port
      backing options can include URI, file, pipe, or device backing options.
   2. Use the ``pyVmomi.vim.Folder.createVm`` method
      (or the ``pyVmomi.vim.ResourcePool.createVm`` method)
      to create the virtual machine and configure the virtual serial port backing.
      Create a ``pyVmomi.vim.vm.ConfigSpec`` data object and nested
      data objects for the method's `config` parameter.
      The following pseudocode shows the resulting path to the backing
      information.
      
      
          ``pyVmomi.vim.vm.ConfigSpec`.deviceChange[].device.backing`
      
      
      Set the direction property to \"server\" to direct the virtual machine to accept
      a connection. Set the serviceURI property to the URI for the host on which
      the virtual machine runs.
      
   If you use physical device backing
   (``pyVmomi.vim.vm.device.VirtualSerialPortOption.DeviceBackingOption``),
   you should also use the ``pyVmomi.vim.EnvironmentBrowser.queryConfigTarget``
   method to determine if a serial device is available before configuring device backing.
   
   Attributes:
       yieldOnPoll: Enables CPU yield behavior.
           
           If you set `yieldOnPoll` to `true`,
           the virtual machine will periodically relinquish the processor if its sole task
           is polling the virtual serial port. The amount of time it takes to regain
           the processor will depend on the degree of other virtual machine activity on the host.
           
           To use this property, the CPU yield option must be supported. (See the
           ``pyVmomi.vim.vm.device.VirtualSerialPortOption.yieldOnPoll`` property for
           the virtual serial port option object.)
   """
   class FileBackingInfo(VirtualDevice.FileBackingInfo):
      """
      The ``pyVmomi.vim.vm.device.VirtualSerialPort.FileBackingInfo`` data object provides
      information for backing a virtual serial port with a host file.
      """
      pass

   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      """
      The ``pyVmomi.vim.vm.device.VirtualSerialPort.DeviceBackingInfo`` data object
      defines information for using a host serial port device as backing for a
      ``pyVmomi.vim.vm.device.VirtualSerialPort``.
      
      On a host, the first virtual machine
      to configure physical device backing for a virtual serial port will obtain
      the mapping. As long as that machine maintains the backing, any additional attempts
      to configure backing using that device will fail (a recoverable error, see
      the connection info ``pyVmomi.vim.vm.device.VirtualDevice.ConnectInfo.status``).
      """
      pass

   class PipeBackingInfo(VirtualDevice.PipeBackingInfo):
      """
      The ``pyVmomi.vim.vm.device.VirtualSerialPort.PipeBackingInfo`` data object defines information
      for backing a ``pyVmomi.vim.vm.device.VirtualSerialPort`` with a named pipe.
      
      You can use a pipe to connect a virtual serial port to a host
      application or to another virtual machine on the host computer.
      This is useful for capturing debugging information sent through
      the virtual serial port.
      
      Attributes:
          endpoint: Indicates the role the virtual machine assumes as an endpoint
              for the pipe.
              
              The valid values are \"client\" or \"server\".
          noRxLoss: Enables optimized data transfer over the pipe.
              
              When you use this feature,
              the ESX server buffers data to prevent data overrun.
              This allows the virtual machine to read
              all of the data transferred over the pipe with no data loss.
              To use optimized data transfer, set `noRxLoss` to `true`.
              To disable this feature, set the property to `false.
              
              This property is optional. If this property is not set, the ESX server
              uses the default value specified in the pipe backing options
              (noRxLoss.defaultValue - see
              ``pyVmomi.vim.vm.device.VirtualSerialPortOption.PipeBackingOption.noRxLoss``
              in the pipe backing option object).
              
              To use this property, optimized data transfer must be supported on the host.
              (See ``pyVmomi.vim.vm.device.VirtualSerialPortOption.PipeBackingOption.noRxLoss``
              in the pipe backing option object.)
              If the ESX server does not support the option, it ignores the
              `noRxLoss` setting in the pipe backing information object.
              
              Note: You can use this feature even if the other end of the pipe
              is not an application, but this is more likely to fail.
      """
      endpoint: str
      noRxLoss: _typing.Optional[bool] = None

   class URIBackingInfo(VirtualDevice.URIBackingInfo):
      """
      The ``pyVmomi.vim.vm.device.VirtualSerialPort.URIBackingInfo`` data object
      specifies network backing for a ``pyVmomi.vim.vm.device.VirtualSerialPort``.
      
      You can use URI backing to create a network serial port on the virtual machine,
      supporting connections between the virtual machine and remote systems.
      
      When a virtual machine establishes a connection with a remote system on the network,
      the virtual machine can act as a server or a client. When the virtual machine
      acts as a server, it accepts a connection. When the virtual machine acts as a client,
      it initiates the connection.
      
      You can configure the virtual serial port for communication through a
      virtual serial port concentrator that acts as a proxy between the virtual
      machine and the network. When you specify a
      ``pyVmomi.vim.vm.device.VirtualDevice.URIBackingInfo.proxyURI``,
      the virtual machine initiates the connection with the concentrator
      and forwards the ``pyVmomi.vim.vm.device.VirtualDevice.URIBackingInfo.direction``
      and ``pyVmomi.vim.vm.device.VirtualDevice.URIBackingInfo.serviceURI``
      to the concentrator.
      For information about using a virtual serial port concentrator,
      see Using a Proxy with vSphere Virtual Serial Ports.
      
      ESX hosts support different protocols depending on your virtual serial port configuration.
      - If the virtual machine is handling the network connection
        directly (no ``pyVmomi.vim.vm.device.VirtualDevice.URIBackingInfo.proxyURI`` specified),
        you can use telnet, TCP, and SSL protocols.
        The ``pyVmomi.vim.vm.device.VirtualDevice.URIBackingInfo.serviceURI``
        must use one of the following URI schemes:
        - `<host>:<port>` - this is the equivalent of
          `tcp://<host>:<port>`.
        - `tcp://<host>:<port>` - unencrypted TCP connection
          (IPv4 or IPv6).
        - `tcp4://<host>:<port>` - unencrypted TCP connection
          (IPv4 only).
        - `tcp6://<host>:<port>` - unencrypted TCP connection
          (IPv6 only).
        - `ssl://<host>:<port>` - this is the equivalent of
          `tcp+ssl://<host>:<port>`.
        - `tcp+ssl://<host>:<port>` - encrypted SSL over TCP.
        - `tcp4+ssl://<host>:<port>` - SSL over TCP over IPv4.
        - `tcp6+ssl://<host>:<port>` - SSL over TCP over IPv6.
        - `telnet://<host>:<port>` - telnet over TCP.
          The virtual machine and remote system can negotiate and use SSL if the remote
          system supports the telnet authentication option; if not, the connection
          uses unencrypted text (plaintext).
        - `telnets://<host>:<port>` - telnet over SSL over TCP.
          In this case, SSL negotiation begins immediately and you cannot use
          the telnet authentication option.
          
        As of vSphere 5.1 you can specify authentication parameters to support an encrypted
        connection with a remote system using SSL over telnet or telnets.
        The connection will fail if the peer does not support the protocols.
        You cannot use certificate verification when you specify
        `tcp`, `tcp4`, or `tcp6` schemas. For information
        about parameter specification, see Authentication Parameters
        below.
      - If you are using a ``pyVmomi.vim.vm.device.VirtualDevice.URIBackingInfo.proxyURI``
        to connect to a virtual serial port concentrator, the URI scheme for
        the communication between the remote system on the network and the concentrator
        depends on the concentrator implementation. The connection between
        the concentrator and the virtual serial port must use telnet or secure telnet
        (telnets). The proxy URI must use one of the following URI schemes. You cannot
        specify a username and password in the proxy URI.
        - `telnet://<host>:<port>`- telnet over TCP.
          The virtual machine and remote system can negotiate and use SSL if the remote
          system supports the telnet authentication option; if not, the connection
          uses unencrypted text (plaintext).
        - `telnets://<host>:<port>` - telnet over SSL over TCP.
          In this case, SSL negotiation starts immediately and you cannot use
          the telnet authentication option.
          
        As of vSphere 5.1 you can specify authentication parameters to support an encrypted
        connection with a concentrator using SSL over telnet or telnets.
        The connection will fail if the concentrator does not support the protocols.
        For information about parameter specification,
        see Authentication Parameters below.
        
      Authentication Parameters  
        
      For an encrypted connection, the URI includes a set of authentication
      parameters. The parameters are specified as key words or key/value pairs.
      The following syntax description uses `telnet`; you can also
      specify authentication parameters for secure telnet (`telnets`).
      
      `telnet://<host>:<port>#key[=value][&key[=value] ...]`
      
      The first parameter must have a number sign (#) prefix. Additional parameters
      must have an ampersand (&) prefix. The following list shows the valid parameters.
      - `certificate=value` - Specifies a certificate in PEM format
        against which the peer certificate is compared.
        When you specify a certificate, certificate verification is automatically enabled.
        See the description of the `verify` parameter below.
      - `thumbprint=value` - Specifies a certificate thumbprint against
        which the peer certificate thumbprint is compared. When you specify a thumbprint,
        certificate verification is automatically enabled. See the description of the
        `verify` parameter below.
      - `peerName=value` - Specifies the peer name that will be used
        to validate the peer certificate. When you specify a peer name,
        certificate verification is automatically enabled. See the description of the
        `verify` parameter below.
      - `verify` - Forces certificate verification. The virtual machine
        will verify that the peer certificate subject matches the specified
        `peerName` and that it was signed by a certificate authority
        known to the ESXi host. Verification is automatically enabled if you specify a
        `certificate`, `thumbprint`, or `peerName`.
      - `cipherList=value` - Specifies a list of SSL ciphers.
        See OpenSSL ciphers.
        The ciphers are specified as a list separated by colons, spaces, or commas.
        
      For information about URI format, see
      RFC 2396.
      """
      pass

   class ThinPrintBackingInfo(VirtualDevice.BackingInfo):
      """
      The ``pyVmomi.vim.vm.device.VirtualSerialPort.ThinPrintBackingInfo`` data object defines
      information required for backing a ``pyVmomi.vim.vm.device.VirtualSerialPort`` with a
      ThinPrint device.
      """
      pass

   yieldOnPoll: bool


class VirtualSerialPortOption(VirtualDeviceOption):
   """
   The ``pyVmomi.vim.vm.device.VirtualSerialPortOption`` data object contains the options
   for configuring the virtual serial port device defined by the
   ``pyVmomi.vim.vm.device.VirtualSerialPort`` data object.
   
   These options include information about how the device is backed
   physically on the host: by a network socket, a host file, a host serial port device,
   or a pipe to another process.
   
   Attributes:
       yieldOnPoll: Indicates whether the virtual machine supports the CPU yield option during
           virtual serial port polling.
           
           When this feature is supported and enabled,
           the virtual machine will periodically relinquish the processor if its
           sole task is polling the virtual serial port.
           
           If `yieldOnPoll.supported` is `false`, the virtual
           machine ignores the virtual serial port object setting for
           ``pyVmomi.vim.vm.device.VirtualSerialPort.yieldOnPoll``.
   """
   class EndPoint(pyVmomi.VmomiSupport.Enum):
      """
      The ``pyVmomi.vim.vm.device.VirtualSerialPortOption.EndPoint` enum defines
      endpoint values for virtual serial port pipe backing.
      
      When you use serial port pipe backing to connect a virtual machine
      to another process, you must define the endpoints.
      See the ``pyVmomi.vim.vm.device.VirtualSerialPort.PipeBackingInfo.endpoint``
      property for the virtual serial port pipe backing information data object.
      
      The possible endpoint values are:
      - client
      - server
        
      For the supported choices, see the
      ``pyVmomi.vim.vm.device.VirtualSerialPortOption.PipeBackingOption.endpoint``
      property for the virtual serial port pipe backing option data object.
      """
      client: _typing.ClassVar['VirtualSerialPortOption.EndPoint'] = 'client'
      server: _typing.ClassVar['VirtualSerialPortOption.EndPoint'] = 'server'

   class FileBackingOption(VirtualDeviceOption.FileBackingOption):
      """
      The ``pyVmomi.vim.vm.device.VirtualSerialPortOption.FileBackingOption`` data object type
      contains the options for backing a serial port with a host file.
      """
      pass

   class DeviceBackingOption(VirtualDeviceOption.DeviceBackingOption):
      """
      The ``pyVmomi.vim.vm.device.VirtualSerialPortOption.DeviceBackingOption`` data object type
      contains the options for backing a serial port with a host serial port device.
      """
      pass

   class PipeBackingOption(VirtualDeviceOption.PipeBackingOption):
      """
      The ``pyVmomi.vim.vm.device.VirtualSerialPortOption.PipeBackingOption`` data object contains
      the options for backing a serial port device with a pipe to another process.
      
      Attributes:
          endpoint: Indicates the choices available and the default setting
              for the pipe endpoint.
              
              As an endpoint, the virtual machine can act
              as a client or a server.
          noRxLoss: Indicates whether the server supports optimized data transfer
              over the pipe and also specifies default behavior.
              
              When this feature is supported and enabled, the server buffers data
              to prevent data overrun. This allows the virtual machine to read all
              of the data transferred over the pipe with no data loss.
              
              If optimized data transfer is supported (`noRxLoss.supported`
              is `true`):
              - You can enable (or disable) the feature explicitly by setting the
                ``pyVmomi.vim.vm.device.VirtualSerialPort.PipeBackingInfo.noRxLoss``
                property on the pipe backing information object.
              - If you do not set the
                ``pyVmomi.vim.vm.device.VirtualSerialPort.PipeBackingInfo.noRxLoss``
                property on the
                the pipe backing information object, the server enables
                optimized data transfer if the `noRxLoss.defaultValue`
                property on the pipe backing options object is `true`.
                
              If `noRxLoss.supported` is `false`, the server
              ignores the optimization settings.
              
              Note: You can use this feature even if the other end of the pipe
              is not an application, but it is more likely to fail.
      """
      endpoint: pyVmomi.vim.option.ChoiceOption
      noRxLoss: pyVmomi.vim.option.BoolOption

   class URIBackingOption(VirtualDeviceOption.URIBackingOption):
      """
      The ``pyVmomi.vim.vm.device.VirtualSerialPortOption.URIBackingOption`` data object type
      contains the options for using a network socket as backing for a virtual serial port.
      """
      pass

   class ThinPrintBackingOption(VirtualDeviceOption.BackingOption):
      """
      The ``pyVmomi.vim.vm.device.VirtualSerialPortOption.ThinPrintBackingOption`` data
      object type contains the options for backing a serial port with a ThinPrint device.
      """
      pass

   yieldOnPoll: pyVmomi.vim.option.BoolOption

class VirtualSoundBlaster16(VirtualSoundCard):
   """
   The VirtualSoundBlaster16 data object type represents a Sound
   Blaster 16 sound card in a virtual machine.
   """
   pass

class VirtualSoundBlaster16Option(VirtualSoundCardOption):
   """
   The VirtualSoundBlaster16Option data object type contains the options for a
   virtual SoundBlaster 16 sound card.
   """
   pass


class VirtualSriovEthernetCard(VirtualEthernetCard):
   """
   The `pyVmomi.vim.vm.device.VirtualSriovEthernetCard` data object defines the properties
   of a SR-IOV enabled Ethernet card attached to a virtual machine.
   
   Attributes:
       allowGuestOSMtuChange: Indicates whether MTU can be changed from guest OS.
       sriovBacking: Information about SR-IOV passthrough backing of this VirtualSriovEthernetCard.
           
           During an edit operation, if this value is unset, no changes to the
           SR-IOV backing will be made. During an add operation, if this is unset,
           an automatic physical function assignment scheme as described above will be used.
           This field is ignored and must be unset if this VirtualSriovEthernetCard
           is a DVX device, in which case the dvxBackingInfo field is set. In other
           words, sriovBacking and dvxBackingInfo cannot both be set at any time.
       dvxBackingInfo: Information about DVX backing of this VirtualSriovEthernetCard.
           
           This field is set if and only if this VirtualSriovEthernetCard is a DVX
           device.
           
           Since: vSphere API Release 8.0.0.1
   """
   class SriovBackingInfo(VirtualDevice.BackingInfo):
      """
      The `pyVmomi.vim.vm.device.VirtualSriovEthernetCard.SriovBackingInfo`
      data object contains information about the SR-IOV physical function and
      virtual function backing for a passthrough NIC.
      
      Attributes:
          physicalFunctionBacking: Physical function backing for this device.
              
              A specific physical function can be assigned to the device by specifying
              its id but the VirtualSriovNetworkCard can also be configured for automatic physical
              function assignment by providing a special value \"Automatic-0000:00:00.0\"
              as `pyVmomi.vim.vm.device.VirtualPCIPassthrough.DeviceBackingInfo.id`. This is supported if there is
              an associated SR-IOV network device pool for the network specified in
              `pyVmomi.vim.vm.device.VirtualDevice.backing` - in that case a physical function from
              the pool, if available, will be assigned to this device during power on.
              During reconfigure, if an SR-IOV backing is provided, the physical function backing
              may not be left unset.
              A value of \"Automatic-\" followed by a valid physical function id
              in `pyVmomi.vim.vm.device.VirtualPCIPassthrough.DeviceBackingInfo.id` indicates that assignment
              is automatic and the physical function in question is the one that has currently
              been assigned.
          virtualFunctionBacking: Virtual function backing for this device.
              
              During reconfigure, if this is unset, any currently assigned virtual function
              will be overwritten and a new one will be selected. If
              `pyVmomi.vim.vm.device.VirtualPCIPassthrough.DeviceBackingInfo.id` contains a valid id for
              a virtual function of the currently assigned physical function, this acts as
              a hint and, if possible, the specified virtual function will be the one
              allocated for the device.
              When a virtual function is yet to be assigned to the device (e.g. if the VM
              has not been powered on yet), the virtual function backing will be unset.
      """
      physicalFunctionBacking: _typing.Optional[VirtualPCIPassthrough.DeviceBackingInfo] = None
      virtualFunctionBacking: _typing.Optional[VirtualPCIPassthrough.DeviceBackingInfo] = None
      virtualFunctionIndex: _typing.Optional[int] = None

   allowGuestOSMtuChange: _typing.Optional[bool] = None
   sriovBacking: _typing.Optional[VirtualSriovEthernetCard.SriovBackingInfo] = None
   dvxBackingInfo: _typing.Optional[VirtualPCIPassthrough.DvxBackingInfo] = None

class VirtualSriovEthernetCardOption(VirtualEthernetCardOption):
   """
   The VirtualSriovEthernetCardOption data object contains the options for the
   VirtualSriovEthernetCard data object type.
   """
   class SriovBackingOption(VirtualDeviceOption.BackingOption):
      """
      This data object contains the option for SriovBackingInfo data
      of the virtual network SR-IOV card object type.
      """
      pass


class VirtualTPM(VirtualDevice):
   """
   This data object type represents a TPM 2.0 module
   in a virtual machine.
   
   Attributes:
       endorsementKeyCertificateSigningRequest: Endorsement Key Certificate Signing Request in DER format.
           
           There may be more than one - one for RSA 2048, one for ECC NIST P256,
           and any number of other signing requests for other algorithms.
       endorsementKeyCertificate: Endorsement Key Certificate in DER format.
           
           There may be more than one. Indices in this array do not match
           indices in `pyVmomi.vim.vm.device.VirtualTPM.endorsementKeyCertificateSigningRequest` array,
           entries must be matched by comparing fields in DER data between
           certificate signing requests and certificates.
   """
   endorsementKeyCertificateSigningRequest: list[pyVmomi.VmomiSupport.binary] = []
   endorsementKeyCertificate: list[pyVmomi.VmomiSupport.binary] = []


class VirtualTPMOption(VirtualDeviceOption):
   """
   This data object type contains the options for the
   virtual TPM class.
   
   Attributes:
       supportedFirmware: List of supported firmware selections, using
           `pyVmomi.vim.vm.GuestOsDescriptor.FirmwareType` enumeration.
           
           There is at least one value in this array.
   """
   supportedFirmware: list[str] = []


class VirtualUSB(VirtualDevice):
   """
   The `pyVmomi.vim.vm.device.VirtualUSB` data object describes the USB device configuration
   for a virtual machine.
   
   You can attach a USB device to an ESX host.
   The device is available to only one virtual machine at a time. When you remove
   the device from the virtual machine, it becomes available to other virtual machines
   located on the host. You can add up to 20 USB devices to a virtual machine.
   Virtual USB support requires virtual machine hardware version 7 or later.
   
   The `pyVmomi.vim.vm.device.VirtualUSB` object represents either a configuration to be applied to
   the virtual machine or the current device configuration on the virtual machine.
   - To configure a USB connection for the virtual machine, add a `pyVmomi.vim.vm.device.VirtualUSB`
     object to the `pyVmomi.vim.vm.device.VirtualDeviceSpec`.
     Use USB backing (`pyVmomi.vim.vm.device.VirtualUSB.USBBackingInfo`) to establish
     a connection with a virtual machine that will remain on the host to which
     the USB device is attached.
     The vSphere Server does not support vMotion for standard USB backing.
     To configure vMotion support for a virtual machine with a USB connection,
     use remote host backing for the USB connection
     (`pyVmomi.vim.vm.device.VirtualUSB.RemoteHostBackingInfo`).
     
     To configure a USB device for a virtual machine, the virtual machine
     must have a USB controller. To add a controller, include a
     `pyVmomi.vim.vm.device.VirtualUSBController` object in the virtual device
     specification for your virtual machine configuration. You can add only one
     USB controller to a virtual machine.
   - To determine USB device configuration status for the virtual machine,
     check the virtual hardware device list
     (`pyVmomi.vim.vm.VirtualHardware`.`pyVmomi.vim.vm.VirtualHardware.device`).
     The presence of the `pyVmomi.vim.vm.device.VirtualUSB` object in the hardware device list
     indicates that the virtual machine is configured to use a USB device.
     The `pyVmomi.vim.vm.device.VirtualUSB.connected` property indicates
     whether the virtual machine is connected to the device.
     
   To determine the USB options available on the host, use the
   `pyVmomi.vim.EnvironmentBrowser.queryConfigOption` method to retrieve the virtual
   machine configuration. The presence of the `pyVmomi.vim.vm.device.VirtualUSBOption`
   object in the retrieved configuration
   (`pyVmomi.vim.vm.ConfigOption`.`pyVmomi.vim.vm.ConfigOption.hardwareOptions`.`pyVmomi.vim.vm.VirtualHardwareOption.virtualDeviceOption`)
   indicates that the host supports USB connections.
   
   The following operations will disconnect a USB device, losing data if data transfer
   is in progress over the USB connection.
   - Hot add of memory, CPU, or PCI devices. A hot add operation disconnects only
     USB devices for virtual machines that use a local connection to the device
     (`pyVmomi.vim.vm.device.VirtualUSB.USBBackingInfo`).
   - Suspend and resume on a virtual machine.
   - vMotion of a virtual machine with a USB connection,
     if you are not using remote host USB backing.
     
   The following services do not support USB connections.
   - Fault Tolerance virtual machines cannot use USB devices.
   - DPM (Distributed Power Management) will put a host into standby,
     regardless of any connections to USB devices on the host.
   - DRS (Distributed Resource Scheduling) may power-off hosts that have
     USB connections to virtual machines.
   
   Attributes:
       connected: Flag indicating whether the device is currently connected.
           
           The virtual machine is not connected to the device if the autoconnect pattern
           specified in the USB device backing
           (`pyVmomi.vim.vm.device.VirtualDevice.DeviceBackingInfo`.`pyVmomi.vim.vm.device.VirtualDevice.DeviceBackingInfo.deviceName`)
           can not be satisfied, either
           because there is no such device, or the matching device is not
           available. Valid only while the virtual machine is running.
       vendor: Vendor ID of the USB device.
       product: Product ID of the USB device.
       family: Device class families.
           
           For possible values see
           `pyVmomi.vim.vm.UsbInfo.Family`.
       speed: Device speeds detected by server.
           
           For possible values see
           `pyVmomi.vim.vm.UsbInfo.Speed`.
   """
   class USBBackingInfo(VirtualDevice.DeviceBackingInfo):
      """
      The `pyVmomi.vim.vm.device.VirtualUSB.USBBackingInfo` data object
      identifies a USB device on the host where the virtual machine
      is located.
      
      This type of backing supports only a local connection
      where the virtual machine will remain on the host to which the
      USB device is attached.
      
      To identify the USB device, you specify an autoconnect pattern
      for the `pyVmomi.vim.vm.device.VirtualDevice.DeviceBackingInfo.deviceName`.
      The virtual machine can connect to the USB device if the ESX server
      can find a USB device described by the autoconnect pattern.
      The autoconnect pattern consists of name:value pairs. You can
      use any combination of the following fields.
      - path - USB connection path on the host
      - pid - idProduct field in the USB device descriptor
      - vid - idVendor field in the USB device descriptor
      - hostId - unique ID for the host
      - speed - device speed (low, full, or high)
        
      For example, the following pattern identifies a USB device:
      
          `\"path:1/3/0 hostId:44\\ 45\\ 4c\\ 43\\ 00\\ 10\\ 54-80\\ 35\\ ca\\ c0\\ 4f\\ 4d\\ 37\\ 31\"`
      
      This pattern identifies the USB device connected to port 1/3/0 on the
      host with the unique id `0x44454c4c430010548035cac04f4d3731`.
      
      Special characters for autoconnect pattern values:
      - The name and value are separated by a colon (:).
      - Name:value pairs are separated by spaces.
      - The escape character is a backslash (\\). Use a single backslash to embed
        a space in a value. Use a double backslash to embed a single backslash
        in the value.
      """
      pass

   class RemoteHostBackingInfo(VirtualDevice.DeviceBackingInfo):
      """
      The `pyVmomi.vim.vm.device.VirtualUSB.RemoteHostBackingInfo` data object
      identifies a host and a USB device that is attached to the host.
      
      Use this object to configure support for persistent access to the USB device
      when vMotion operations migrate a virtual machine to a different host.
      The vCenter Server will not migrate the virtual machine to a host
      that does not support the USB remote host backing capability.
      
      Specify remote host backing as part of the USB device configuration
      when you create or reconfigure a virtual machine
      (`pyVmomi.vim.vm.ConfigSpec`.`pyVmomi.vim.vm.ConfigSpec.deviceChange`.`pyVmomi.vim.vm.device.VirtualDeviceSpec.device`.`pyVmomi.vim.vm.device.VirtualDevice.backing`).
      
      To identify the USB device, you specify an autoconnect pattern
      for the `pyVmomi.vim.vm.device.VirtualDevice.DeviceBackingInfo.deviceName`.
      The virtual machine can connect to the USB device if the ESX server
      can find a USB device described by the autoconnect pattern.
      The autoconnect pattern consists of name:value pairs. You can
      use any combination of the following fields.
      - path - USB connection path on the host
      - pid - idProduct field in the USB device descriptor
      - vid - idVendor field in the USB device descriptor
      - hostId - unique ID for the host
      - speed - device speed (low, full, or high)
        
      For example, the following pattern identifies a USB device:
      
          `\"path:1/3/0 hostId:44\\ 45\\ 4c\\ 43\\ 00\\ 10\\ 54-80\\ 35\\ ca\\ c0\\ 4f\\ 4d\\ 37\\ 31\"`
      
      This pattern identifies the USB device connected to port 1/3/0 on the
      host with the unique id `0x44454c4c430010548035cac04f4d3731`.
      
      Special characters for autoconnect pattern values:
      - The name and value are separated by a colon (:).
      - Name:value pairs are separated by spaces.
      - The escape character is a backslash (\\). Use a single backslash to embed
        a space in a value. Use a double backslash to embed a single backslash
        in the value.
      
      Attributes:
          hostname: Name of the ESX host to which the physical USB device is attached
              (`pyVmomi.vim.HostSystem`.`pyVmomi.vim.ManagedEntity.name`).
              
              When you configure remote host backing, hostname must identify
              the local host on which the virtual machine is running.
      """
      hostname: str

   class RemoteClientBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
      """
      The virtual remote client USB device backing class.
      
      Attributes:
          hostname: Hostname of the remote client where the physical USB device resides.
      """
      hostname: str

   connected: bool
   vendor: _typing.Optional[int] = None
   product: _typing.Optional[int] = None
   family: list[str] = []
   speed: list[str] = []


class VirtualUSBController(VirtualController):
   """
   The `pyVmomi.vim.vm.device.VirtualUSBController` data object describes a virtual USB controller
   and contains a list of the devices connected to the controller.
   
   A virtual machine must have a virtual USB controller before you can add
   a USB device to the virtual machine configuration. To add a controller,
   include a `pyVmomi.vim.vm.device.VirtualUSBController` object in the
   `pyVmomi.vim.vm.device.VirtualDeviceSpec` for your virtual machine configuration.
   You can add only one controller to a virtual machine.
   A virtual USB controller supports up to 20 USB device connections on the
   virtual machine.
   
   The ESX Server host must have the USB controller hardware and modules
   that support USB 2.0 and USB1.1.
   You can use a maximum of 15 USB controllers on a host. If your system
   includes an additional number of controllers with connected devices,
   the additional devices will not be available to virtual machines on the host.
   
   You must remove all USB devices from a virtual machine before you can
   remove the USB controller.
   
   Attributes:
       autoConnectDevices: Flag to indicate whether or not the ability to hot plug devices
           is enabled on this controller.
       ehciEnabled: Flag to indicate whether or not enhanced host controller
           interface (USB 2.0) is enabled on this controller.
   """
   class PciBusSlotInfo(VirtualDevice.PciBusSlotInfo):
      """
      The ``pyVmomi.vim.vm.device.VirtualUSBController.PciBusSlotInfo`` data object type
      defines information about the pci bus slots of usb controller device
      in a virtual machine.
      
      Attributes:
          ehciPciSlotNumber: The pci slot number of eHCI controller.
              
              This property should be used only when the ehciEnabled property
              is set to true.
      """
      ehciPciSlotNumber: _typing.Optional[int] = None

   autoConnectDevices: _typing.Optional[bool] = None
   ehciEnabled: _typing.Optional[bool] = None


class VirtualUSBControllerOption(VirtualControllerOption):
   """
   The VirtualUSBControllerOption data object type contains the options
   for a virtual USB Host Controller Interface.
   
   Attributes:
       autoConnectDevices: Flag to indicate whether or not the ability to autoconnect devices
           is enabled for this virtual USB controller.
       ehciSupported: Flag to indicate whether or not enhanced host controller
           interface (USB 2.0) is available on this virtual USB controller.
       supportedSpeeds: Range of USB device speeds supported by this USB controller type.
           
           Acceptable values are specified at `pyVmomi.vim.vm.UsbInfo.Speed`.
   """
   autoConnectDevices: pyVmomi.vim.option.BoolOption
   ehciSupported: pyVmomi.vim.option.BoolOption
   supportedSpeeds: list[str] = []

class VirtualUSBOption(VirtualDeviceOption):
   """
   The `pyVmomi.vim.vm.device.VirtualUSBOption` data object type contains options for
   USB device configuration on a virtual machine.
   
   The vSphere API supports
   the following options:
   - Local host USB connection
     (`pyVmomi.vim.vm.device.VirtualUSBOption.USBBackingOption`)
   - Remote host USB connection
     (`pyVmomi.vim.vm.device.VirtualUSBOption.RemoteHostBackingOption`)
     
   For information about USB device configuration, see `pyVmomi.vim.vm.device.VirtualUSB`.
   """
   class USBBackingOption(VirtualDeviceOption.DeviceBackingOption):
      """
      The `pyVmomi.vim.vm.device.VirtualUSBOption.USBBackingOption` data object
      contains the options for virtual backing for a USB device.
      
      This backing option indicates support for a local connection where
      the virtual machine will remain on the host to which the USB device
      is attached.
      """
      pass

   class RemoteHostBackingOption(VirtualDeviceOption.DeviceBackingOption):
      """
      The `pyVmomi.vim.vm.device.VirtualUSBOption.RemoteHostBackingOption` data object
      contains options for remote host USB configuration.
      
      This backing option
      indicates support for persistent USB connections when vMotion operations
      migrate virtual machines to different hosts.
      """
      pass

   class RemoteClientBackingOption(VirtualDeviceOption.RemoteDeviceBackingOption):
      """
      This data object type contains the options for
      the virtual remote USB client backing data object type.
      """
      pass


class VirtualUSBXHCIController(VirtualController):
   """
   The `pyVmomi.vim.vm.device.VirtualUSBXHCIController` data object describes a virtual
   USB Extensible Host Controller Interface (USB 3.0).
   
   For more information see `pyVmomi.vim.vm.device.VirtualUSBController`.
   
   Attributes:
       autoConnectDevices: Flag to indicate whether or not the ability to hot plug devices
           is enabled on this controller.
   """
   autoConnectDevices: _typing.Optional[bool] = None


class VirtualUSBXHCIControllerOption(VirtualControllerOption):
   """
   The VirtualUSBXHCIControllerOption data object type contains the options
   for a virtual USB Extensible Host Controller Interface (USB 3.0).
   
   Attributes:
       autoConnectDevices: Flag to indicate whether or not the ability to autoconnect devices
           is enabled for this virtual USB controller.
       supportedSpeeds: Range of USB device speeds supported by this USB controller type.
           
           Acceptable values are specified at `pyVmomi.vim.vm.UsbInfo.Speed`.
   """
   autoConnectDevices: pyVmomi.vim.option.BoolOption
   supportedSpeeds: list[str] = []


class VirtualVMCIDevice(VirtualDevice):
   """
   The `pyVmomi.vim.vm.device.VirtualVMCIDevice` data object represents
   a virtual communication device that supports the VMCI
   (Virtual Machine Communication Interface).
   
   Each virtual machine has a VMCI device that handles
   interprocess socket-based communication.
   VMCI device information is available in the virtual machine
   hardware device list
   (`pyVmomi.vim.VirtualMachine`.`pyVmomi.vim.VirtualMachine.config`.`pyVmomi.vim.vm.ConfigInfo.hardware`.`pyVmomi.vim.vm.VirtualHardware.device`[]).
   
   An application running on a virtual machine uses the VMCI Sockets API
   for communication with other virtual machines on the same host
   (communication between virtual machines is not supported on vSphere
   5.1 and later platforms as described for
   VirtualVMCIDevice.`pyVmomi.vim.vm.device.VirtualVMCIDevice.allowUnrestrictedCommunication`),
   or for communication with the host.
   For information about using the vSphere VMCI Sockets API,
   see the VMCI Sockets Programming Guide.
   
   Attributes:
       id: Unique identifier for VMCI socket access to this virtual machine.
           
           Use this value to identify this virtual machine in calls to the
           VMCI Sockets API. Applications running on other virtual machines on this
           host will use this value to connect to this virtual machine.
           You can cast this value to a 32-bit unsigned integer.
           
           The vSphere Server sets this value when a virtual machine
           powers on. The Server may change this value after power
           operations such as vMotion or restoring a virtual machine
           from a snapshot. If you have saved a VMCI device identifier,
           check to see if the value is still valid after power
           operations.
       allowUnrestrictedCommunication: Determines the extent of VMCI communication with this virtual
           machine.
           
           Set this property to true to allow VMCI communication
           with all virtual machines on the host and with trusted services.
           Set this property to false to allow VMCI communication only
           with trusted services such as the hypervisor on the host.
           
           If unset, communication is restricted to trusted services only.
       filterEnable: Determines if filtering of VMCI communication is enabled for this virtual
           machine.
           
           Set this property to enable or disable filter rules as specified
           in `pyVmomi.vim.vm.device.VirtualVMCIDevice.filterInfo`.
       filterInfo: Specify a `pyVmomi.vim.vm.device.VirtualVMCIDevice.FilterInfo` data object that controls the extent of
           VMCI communication with this virtual machine.
   """
   class Action(pyVmomi.VmomiSupport.Enum):
      """
      Set of possible values for action field in FilterSpec.
      
      Determines whether traffic is allowed or denied.
      
      Attributes:
          allow: Allow communication.
          deny: Deny communication.
      """
      allow: _typing.ClassVar['VirtualVMCIDevice.Action'] = 'allow'
      deny: _typing.ClassVar['VirtualVMCIDevice.Action'] = 'deny'

   class Protocol(pyVmomi.VmomiSupport.Enum):
      """
      Set of possible values for protocol field in FilterSpec.
      
      Attributes:
          hypervisor: VMCI hypervisor datagram send op.
              
              Direction code is not applicable to this one.
          doorbell: VMCI doorbell notification
          queuepair: VMCI queue pair alloc operation.
              
              Direction code not applicable to this one.
          datagram: VMCI and VMCI Socket datagram send op.
              
              Since VMCI Socket datagrams map ports directly to resources,
              there is no need to distinguish between the two.
          stream: VMCI Stream Socket connect op.
          anyProtocol: All of the above.
      """
      hypervisor: _typing.ClassVar['VirtualVMCIDevice.Protocol'] = 'hypervisor'
      doorbell: _typing.ClassVar['VirtualVMCIDevice.Protocol'] = 'doorbell'
      queuepair: _typing.ClassVar['VirtualVMCIDevice.Protocol'] = 'queuepair'
      datagram: _typing.ClassVar['VirtualVMCIDevice.Protocol'] = 'datagram'
      stream: _typing.ClassVar['VirtualVMCIDevice.Protocol'] = 'stream'
      anyProtocol: _typing.ClassVar['VirtualVMCIDevice.Protocol'] = 'anyProtocol'

   class Direction(pyVmomi.VmomiSupport.Enum):
      """
      Set of possible values for direction field in FilterSpec.
      
      Attributes:
          guest: from host to guest
          host: from guest to host
          anyDirection: all of the above
      """
      guest: _typing.ClassVar['VirtualVMCIDevice.Direction'] = 'guest'
      host: _typing.ClassVar['VirtualVMCIDevice.Direction'] = 'host'
      anyDirection: _typing.ClassVar['VirtualVMCIDevice.Direction'] = 'anyDirection'

   class FilterSpec(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.vm.device.VirtualVMCIDevice.FilterSpec` data object describes a filter based on protocol,
      direction and port or port-range.
      
      Attributes:
          rank: Long value representing filter rank.
              
              This is the rank of this filter. Filters are guaranteed to be
              processed in ascending rank order, that is, if rank1 < rank2, then
              rank1 is processed before rank2. The ranks within an array of
              filters should be unique.
          action: String value from `pyVmomi.vim.vm.device.VirtualVMCIDevice.Action` enum object.
          protocol: String value from `pyVmomi.vim.vm.device.VirtualVMCIDevice.Protocol` enum object
          direction: String value from `pyVmomi.vim.vm.device.VirtualVMCIDevice.Direction` enum object.
          lowerDstPortBoundary: Long value representing the lower destination port boundary.
              
              If unset, the lower destination port boundary is default to the
              lowest port number supported by the given protocol.
              
              To specify a single port, both lowerDstPortBoundary and
              upperDstPortBoundary shall be set to the same value.
          upperDstPortBoundary: Long value representing the upper destination port range.
              
              If unset, the upper destination port boundary is default to the
              highest port number supported by the given protocol.
              
              To specify a single port, both lowerDstPortBoundary and
              upperDstPortBoundary shall be set to the same value.
      """
      rank: pyVmomi.VmomiSupport.long
      action: str
      protocol: str
      direction: str
      lowerDstPortBoundary: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      upperDstPortBoundary: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   class FilterInfo(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.vm.device.VirtualVMCIDevice.FilterInfo` data object contains an array of filters.
      
      To
      clear all existing filters, leave filters unset or specify an empty
      array.
      """
      filters: list[VirtualVMCIDevice.FilterSpec] = []

   id: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   allowUnrestrictedCommunication: _typing.Optional[bool] = None
   filterEnable: _typing.Optional[bool] = None
   filterInfo: _typing.Optional[VirtualVMCIDevice.FilterInfo] = None


class VirtualVMCIDeviceOption(VirtualDeviceOption):
   """
   The `pyVmomi.vim.vm.device.VirtualVMCIDeviceOption` data object contains the options
   for the virtual VMCI device (`pyVmomi.vim.vm.device.VirtualVMCIDevice`).
   
   Attributes:
       allowUnrestrictedCommunication: Indicates support for VMCI communication and specifies the default
           operation.
           
           If `pyVmomi.vim.option.BoolOption.defaultValue` is set to true,
           the virtual machine can participate in VMCI communication with all other
           virtual machines on the host. Otherwise, VMCI communication will be
           restricted to trusted services such as the hypervisor on the host.
           On vSphere 5.1 and later platforms, the VMCI device does not support
           communication with other virtual machines. Therefore, this property has
           no effect on these platforms.
       filterSpecOption: Filter specification options.
       filterSupported: Indicates support for VMCI firewall filters and specifies the default
           operation.
           
           If `pyVmomi.vim.option.BoolOption.supported` is set to true,
           then firewall filtering can be used for this virtual machine to allow
           or deny traffic over VMCI.
   """
   class FilterSpecOption(pyVmomi.vmodl.DynamicData):
      """
      Filter specification options.
      
      Indicates options for each filter
      specification, as defined by
      `pyVmomi.vim.vm.device.VirtualVMCIDevice.FilterSpec`.
      
      Attributes:
          action: Available actions.
          protocol: Available protocols.
          direction: Available directions.
          lowerDstPortBoundary: Minimum, maximum and default values for lower destination port
              boundary.
          upperDstPortBoundary: Minimum, maximum and default values for upper destination port
              boundary.
      """
      action: pyVmomi.vim.option.ChoiceOption
      protocol: pyVmomi.vim.option.ChoiceOption
      direction: pyVmomi.vim.option.ChoiceOption
      lowerDstPortBoundary: pyVmomi.vim.option.LongOption
      upperDstPortBoundary: pyVmomi.vim.option.LongOption

   allowUnrestrictedCommunication: pyVmomi.vim.option.BoolOption
   filterSpecOption: _typing.Optional[VirtualVMCIDeviceOption.FilterSpecOption] = None
   filterSupported: _typing.Optional[pyVmomi.vim.option.BoolOption] = None

class VirtualVMIROM(VirtualDevice):
   """
   Deprecated: As of vSphere API 6.0. On vSphere 6.0 and later
   platforms, the VMIROM device does not provide any functionality.The VirtualVMIROM data object type represents the ROM on the
   virtual machine's PCI bus that provides support for VMI.
   """
   pass

class VirtualVMIROMOption(VirtualDeviceOption):
   """
   This data object type contains the options for the
   `pyVmomi.vim.vm.device.VirtualVMIROM` data object type.
   """
   pass


class VirtualVideoCard(VirtualDevice):
   """
   The VirtualVideoCard data object type represents a video card in
   a virtual machine.
   
   Attributes:
       videoRamSizeInKB: The size of the framebuffer for a virtual machine.
       numDisplays: Indicates the number of supported monitors.
           
           The number of displays X the maximum resolution of each display is
           bounded by the video RAM size of the virtual video card.
           This property can only be updated when the virtual machine is
           powered off.
       useAutoDetect: Flag to indicate whether the display settings of the host on which the
           virtual machine is running should be used to automatically determine
           the display settings of the virtual machine's video card.
           
           This setting takes effect at virtual machine power-on time. If this
           value is set to TRUE, numDisplays will be ignored.
       enable3DSupport: Flag to indicate whether the virtual video card supports 3D functions.
           
           This property can only be updated when the virtual machine is powered
           off.
       use3dRenderer: Indicate how the virtual video device renders 3D graphics.
           
           The virtual video device can use hardware acceleration and software
           rendering. By default, VMware products determine whether or not to
           use hardware acceleration based on the availability of physical graphics
           devices. Certain workloads can benefit from explicitly specifying if
           hardware acceleration is required. For example, 3D intensive workloads
           may indicate to run on systems with graphics hardware.
           
           There are three settings.
           
           (automatic) - The virtual device chooses how to render 3D graphics (default).
           (software) - The virtual device will use software rendering and
           will not attempt to use hardware acceleration.
           (hardware) - The virtual device will use hardware acceleration and
           will not activate without it.
       graphicsMemorySizeInKB: The size of graphics memory.
           
           If 3d support is enabled this setting gives the amount of guest memory
           used for graphics resources.
           This property can only be updated when the virtual machine is
           powered off.
   """
   class Use3dRenderer(pyVmomi.VmomiSupport.Enum):
      """
      Set of possible values for `pyVmomi.vim.vm.device.VirtualVideoCard.use3dRenderer`.
      
      Attributes:
          automatic: Determine automatically whether to render 3D with software or hardware.
          software: Render 3D with software.
          hardware: Render 3D with graphics hardware.
      """
      automatic: _typing.ClassVar['VirtualVideoCard.Use3dRenderer'] = 'automatic'
      software: _typing.ClassVar['VirtualVideoCard.Use3dRenderer'] = 'software'
      hardware: _typing.ClassVar['VirtualVideoCard.Use3dRenderer'] = 'hardware'

   videoRamSizeInKB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   numDisplays: _typing.Optional[int] = None
   useAutoDetect: _typing.Optional[bool] = None
   enable3DSupport: _typing.Optional[bool] = None
   use3dRenderer: _typing.Optional[str] = None
   graphicsMemorySizeInKB: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VirtualVideoCardOption(VirtualDeviceOption):
   """
   This data object type contains the options for the
   `pyVmomi.vim.vm.device.VirtualVideoCard` data object type.
   
   Attributes:
       videoRamSizeInKB: Minimum, maximum and default size of the video frame buffer.
       numDisplays: Minimum, maximum and default value for the number of displays.
       useAutoDetect: Flag to indicate whether the display settings of the host should
           be used to automatically determine the display settings of the
           virtual machine's video card.
       support3D: Flag to indicate whether the virtual video card supports 3D functions.
       use3dRendererSupported: Flag to indicate whether the virtual video card can specify how to render 3D graphics.
       graphicsMemorySizeInKB: The minimum, maximum, and default values for graphics memory size.
       graphicsMemorySizeSupported: Flag to indicate whether the virtual video card can specify the size
           of graphics memory.
   """
   videoRamSizeInKB: _typing.Optional[pyVmomi.vim.option.LongOption] = None
   numDisplays: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   useAutoDetect: _typing.Optional[pyVmomi.vim.option.BoolOption] = None
   support3D: _typing.Optional[pyVmomi.vim.option.BoolOption] = None
   use3dRendererSupported: _typing.Optional[pyVmomi.vim.option.BoolOption] = None
   graphicsMemorySizeInKB: _typing.Optional[pyVmomi.vim.option.LongOption] = None
   graphicsMemorySizeSupported: _typing.Optional[pyVmomi.vim.option.BoolOption] = None

class VirtualVmxnet(VirtualEthernetCard):
   """
   The VirtualVmxnet data object type represents an instance
   of the Vmxnet virtual Ethernet adapter attached to a virtual machine.
   """
   pass

class VirtualVmxnet2(VirtualVmxnet):
   """
   The VirtualVmxnet2 data object type represents an instance
   of the Vmxnet2 virtual Ethernet adapter attached to a virtual machine.
   """
   pass

class VirtualVmxnetOption(VirtualEthernetCardOption):
   """
   The VirtualVmxnetOption data object type contains the options for the
   `pyVmomi.vim.vm.device.VirtualVmxnet` data object type.
   """
   pass

class VirtualVmxnet2Option(VirtualVmxnetOption):
   """
   The VirtualVmxnet2Option data object type contains the options for the
   `pyVmomi.vim.vm.device.VirtualVmxnet2` data object type.
   """
   pass


class VirtualVmxnet3(VirtualVmxnet):
   """
   The VirtualVmxnet3 data object type represents an instance
   of the Vmxnet3 virtual Ethernet adapter attached to a virtual machine.
   
   Attributes:
       uptv2Enabled: Indicates whether UPTv2(Uniform Pass-through version 2) compatibility is
           enabled on this network adapter.
           
           UPTv2 is only available on Vmxnet3
           adapter. Clients can set this property enabled or disabled if ethernet
           virtual device is Vmxnet3. It requires the VM hardware version is
           compatible with ESXi version which has enabled smartnic feature.
           
           Since: vSphere API Release 8.0.0.1
       strictLatencyConfig: Indicates whether strict latency parameters are configured on this
           network adapter.
           
           Clients can set these parameters to control behaviors
           on this network adapter, e.g., set the TX/RX ring size, etc. Requires
           VM hardware version compatible with ESXi release supporting the
           \"real-time switch\" feature.
           
           Since: vSphere API Release 8.0.3.1
   """
   class StrictLatencyConfig(pyVmomi.vmodl.DynamicData):
      """
      The structure below defines the strict latency configuration of a
      network adapter.
      
      The configuration parameters are only supported when
      the strict latency capability is enabled on the adapter. When adding
      a new adapter, unset config parameters are interpreted as \"use the
      default value\". When altering the configuration of an existing adapter,
      unset parameters mean \"do not change the current config\"
      
      Attributes:
          allowed: Indicates whether strict latency configuration is allowed on this
              network adapter.
              
              Requires VM hardware version compatible with ESXi
              release supporting the \"real-time switch\" feature.
          measureLatency: Indicates whether the latency measurement is enabled.
              
              The default
              value is \"enabled\".
          maxTxQueues: The number of transmit queues.
              
              The default value is 1. The allowed
              range is 1 to 32, including.
          maxRxQueues: The number of receive queues.
              
              The default value is 1. The allowed
              range is 1 to 32, including.
          txDataRingDescSize: The transmit data ring size.
              
              The default value is 256. The allowed
              range is 128 to 2048, including, must be multiple of 64.
          rxDataRingDescSize: The receive data ring size.
              
              The default value is 256. The allowed
              range is 128 to 2048, including, must be multiple of 64.
          disableOffload: Type of disable offload being performed on the specified network
              adapter.
              
              If not specified, TSO_LRO will be used as the default during
              adding new network adapter. The supported values are listed in
              `pyVmomi.vim.vm.device.VirtualVmxnet3.StrictLatencyConfig.DisableOffload`.
      
      Since: vSphere API Release 8.0.3.1
      """
      class DisableOffload(pyVmomi.VmomiSupport.Enum):
         """
         TSO (TCP Segmentation Offload) and LRO (Large Receive Offload)
         are both offloading techniques that improve network performance
         by reducing CPU overhead associated with packet segmentation
         and aggregation, respectively.
         
         They are commonly used in modern
         networking environments to optimize data transmission and
         reception processes. This is the type of disable offload on a
         network adapter.
         
         Attributes:
             NONE: Do not disable.
             TSO: Disable TCP Segmentation Offload (TSO).
             LRO: Disable Large Receive Offload (LRO).
             TSO_LRO: Disable both TSO and LRO.
         """
         NONE: _typing.ClassVar['VirtualVmxnet3.StrictLatencyConfig.DisableOffload'] = 'NONE'
         TSO: _typing.ClassVar['VirtualVmxnet3.StrictLatencyConfig.DisableOffload'] = 'TSO'
         LRO: _typing.ClassVar['VirtualVmxnet3.StrictLatencyConfig.DisableOffload'] = 'LRO'
         TSO_LRO: _typing.ClassVar['VirtualVmxnet3.StrictLatencyConfig.DisableOffload'] = 'TSO_LRO'

      allowed: _typing.Optional[bool] = None
      measureLatency: _typing.Optional[bool] = None
      maxTxQueues: _typing.Optional[int] = None
      maxRxQueues: _typing.Optional[int] = None
      txDataRingDescSize: _typing.Optional[int] = None
      rxDataRingDescSize: _typing.Optional[int] = None
      disableOffload: _typing.Optional[str] = None

   uptv2Enabled: _typing.Optional[bool] = None
   strictLatencyConfig: _typing.Optional[VirtualVmxnet3.StrictLatencyConfig] = None


class VirtualVmxnet3Option(VirtualVmxnetOption):
   """
   The VirtualVmxnet3Option data object type contains the options for the
   `pyVmomi.vim.vm.device.VirtualVmxnet3` data object type.
   
   Attributes:
       uptv2Enabled: Flag to indicate whether UPTv2(Uniform Pass-through version 2) is
           settable on this device.
           
           Since: vSphere API Release 8.0.0.1
       strictLatencyConfigOption: Strict latency configure options.
           
           Since: vSphere API Release 8.0.3.1
   """
   class StrictLatencyConfigOption(pyVmomi.vmodl.DynamicData):
      """
      Strict latency configure options.
      
      Indicates options for each strict
      latency configure specification, as defined by
      `pyVmomi.vim.vm.device.VirtualVmxnet3.StrictLatencyConfig`.
      
      Attributes:
          allowed: Indicates whether strict latency configuration is allowed on this
              network adapter.
          measureLatency: Indicates whether latency measurement is enabled on this network
              adapter.
          maxTxQueues: Three properties (maxTxQueues.min, maxTxQueues.max, and
              maxTxQueues.defaultValue) define the minimum, maximum, and default
              number of transmit queues on this network adapter.
          maxRxQueues: Three properties (maxRxQueues.min, maxRxQueues.max, and
              maxRxQueues.defaultValue) define the minimum, maximum, and default
              number of receive queues on this network adapter.
          txDataRingDescSize: Three properties (txDataRingDescSize.min, txDataRingDescSize.max, and
              txDataRingDescSize.defaultValue) define the minimum, maximum, and
              default transmit data ring size on this network adapter.
          rxDataRingDescSize: Three properties (rxDataRingDescSize.min, rxDataRingDescSize.max, and
              rxDataRingDescSize.defaultValue) define the minimum, maximum, and
              default receive data ring size on this network adapter.
          disableOffload: Type of disable offload being performed on the specified network
              adapter.
      
      Since: vSphere API Release 8.0.3.1
      """
      allowed: pyVmomi.vim.option.BoolOption
      measureLatency: pyVmomi.vim.option.BoolOption
      maxTxQueues: pyVmomi.vim.option.IntOption
      maxRxQueues: pyVmomi.vim.option.IntOption
      txDataRingDescSize: pyVmomi.vim.option.IntOption
      rxDataRingDescSize: pyVmomi.vim.option.IntOption
      disableOffload: pyVmomi.vim.option.ChoiceOption

   uptv2Enabled: _typing.Optional[pyVmomi.vim.option.BoolOption] = None
   strictLatencyConfigOption: _typing.Optional[VirtualVmxnet3Option.StrictLatencyConfigOption] = None


class VirtualVmxnet3Vrdma(VirtualVmxnet3):
   """
   The VirtualVmxnet3Vrdma data object type represents an instance of the
   VRDMA virtual Remote Direct Memory Access adapter attached to a virtual
   machine.
   
   Attributes:
       deviceProtocol: VRDMA Device protocol.
           
           See
           `pyVmomi.vim.vm.device.VirtualVmxnet3VrdmaOption.DeviceProtocols` for more information.
   """
   deviceProtocol: _typing.Optional[str] = None


class VirtualVmxnet3VrdmaOption(VirtualVmxnet3Option):
   """
   The VirtualVmxnet3VrdmaOption data object type contains the options for the
   `pyVmomi.vim.vm.device.VirtualVmxnet3Vrdma` data object type.
   
   Attributes:
       deviceProtocol: The supported device protocols.
   """
   class DeviceProtocols(pyVmomi.VmomiSupport.Enum):
      """
      The enumeration of all known valid VRDMA device protocols.
      
      Attributes:
          rocev1: A RoCEv1 device.
          rocev2: A RoCEv2 device.
      """
      rocev1: _typing.ClassVar['VirtualVmxnet3VrdmaOption.DeviceProtocols'] = 'rocev1'
      rocev2: _typing.ClassVar['VirtualVmxnet3VrdmaOption.DeviceProtocols'] = 'rocev2'

   deviceProtocol: _typing.Optional[pyVmomi.vim.option.ChoiceOption] = None

class VirtualWDT(VirtualDevice):
   """
   This data object type represents a watchdog timer in a virtual machine.
   
   Attributes:
       runOnBoot: Flag to indicate if the virtual watchdog timer device should be
           initialized as the Enabled/Stopped or Enabled/Running sub-state.
           
           If not set, the device will default to being initialized as the
           Enabled/Stopped sub-state.
       running: Flag to indicate if the virtual watchdog timer device is currently
           in the Enabled/Running state.
           
           The guest can cause state changes,
           which will result in this flag being either set or cleared.
   """
   runOnBoot: bool
   running: bool


class VirtualWDTOption(VirtualDeviceOption):
   """
   This data object type contains the options for the
   virtual watchdog timer class.
   
   Attributes:
       runOnBoot: Flag to indicate whether or not the \"run on boot\" option
           is settable on this device.
   """
   runOnBoot: pyVmomi.vim.option.BoolOption
