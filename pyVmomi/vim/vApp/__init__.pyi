# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.ext
import pyVmomi.vim.option



class CloneSpec(pyVmomi.vmodl.DynamicData):
   """
   Specification for a vApp cloning operation.
   
   Attributes:
       location: Location where the destination vApp must be stored
       host: The target host for the virtual machines.
           
           This is often not a required
           parameter. If not specified, the behavior is as follows:
           - If the target pool represents a stand-alone host, that host is used.
           - If the target pool represents a DRS-enabled cluster, a host selected
             by DRS is used.
           - If the target pool represents a cluster without DRS enabled or a
             DRS-enabled cluster in manual mode, an InvalidArgument exception is
             thrown.
       resourceSpec: The resource configuration for the vApp.
       vmFolder: The VM Folder to associate the vApp with
       networkMapping: Network mappings.
           
           See `pyVmomi.vim.vApp.CloneSpec.NetworkMappingPair`.
       property: A set of property values to override.
       resourceMapping: The resource configuration for the cloned vApp.
       provisioning: Specify how the VMs in the vApp should be provisioned.
   """
   class NetworkMappingPair(pyVmomi.vmodl.DynamicData):
      """
      Maps one network to another as part of the clone process.
      
      Instances of this class are used in the field `pyVmomi.vim.vApp.CloneSpec.networkMapping`
      
      Attributes:
          source: The source network
          destination: The destination network
      """
      source: pyVmomi.vim.Network
      destination: pyVmomi.vim.Network

   class ResourceMap(pyVmomi.vmodl.DynamicData):
      """
      Maps source child entities to destination resource pools
      and resource settings.
      
      If a mapping is not specified,
      a child is copied as a direct child of the parent.
      
      Attributes:
          source: Source entity
          parent: Resource pool to use for the cloned entity of source.
              
              This must specify a
              resource pool that is not part of the vApp. If this is specified, a linked
              child (as opposed to a direct child) is created for the vApp.
          resourceSpec: An optional resource configuration for the cloned entity of the source.
              
              If
              not specified, the same resource configuration as the source is used.
          location: A client can optionally specify a datastore in the resource map to
              override the default datastore location set in `pyVmomi.vim.vApp.CloneSpec.ResourceMap.location` field.
              
              This
              enables cloning to different compute resources that do not have shared
              datastores.
      """
      source: pyVmomi.vim.ManagedEntity
      parent: _typing.Optional[pyVmomi.vim.ResourcePool] = None
      resourceSpec: _typing.Optional[pyVmomi.vim.ResourceConfigSpec] = None
      location: _typing.Optional[pyVmomi.vim.Datastore] = None

   class ProvisioningType(pyVmomi.VmomiSupport.Enum):
      """
      The cloned VMs can either be provisioned the same way as the VMs
      they are a clone of, thin provisioned or thick provisioned, or
      linked clones (i.e., using delta disks).
      
      Attributes:
          sameAsSource: Each disk in the cloned virtual machines will have the same
              type of disk as the source vApp.
          thin: Each disk in the cloned virtual machines is allocated in full
              size now and committed on demand.
              
              This is only supported on
              VMFS-3 and newer datastores. Other types of datastores may
              create thick disks.
          thick: Each disk in the cloned virtual machines are allocated and
              committed in full size immediately.
      """
      sameAsSource: _typing.ClassVar['CloneSpec.ProvisioningType'] = 'sameAsSource'
      thin: _typing.ClassVar['CloneSpec.ProvisioningType'] = 'thin'
      thick: _typing.ClassVar['CloneSpec.ProvisioningType'] = 'thick'

   location: pyVmomi.vim.Datastore
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   resourceSpec: _typing.Optional[pyVmomi.vim.ResourceConfigSpec] = None
   vmFolder: _typing.Optional[pyVmomi.vim.Folder] = None
   networkMapping: list[CloneSpec.NetworkMappingPair] = []
   property: list[pyVmomi.vim.KeyValue] = []
   resourceMapping: list[CloneSpec.ResourceMap] = []
   provisioning: _typing.Optional[str] = None


class EntityConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   This object type describes the behavior of an entity (virtual machine or
   sub-vApp container) in a vApp container.
   
   The auto-start/auto-stop configurations control the behavior of the
   start/stop vApp operations.
   
   An virtual machine entity can be configured to wait for a period of time before
   starting or to wait to receive a successful heartbeat from a virtual machine
   before starting the next virtual machine in the sequence.
   - For a power-on operation, if waitForHeartbeat is true, then the power-on
     sequence continues after the the first heartbeat has been received. If
     waitingForGuest is false, the system waits for the specified delay and
     then continues the power-on sequence.
   - For a power-off operation, if delay is non-zero, the requested power-off
     action is invoked (powerOff, suspend, guestShutdown) on the virtual
     machine and the system waits until the number of seconds specified in the
     delay have passed.
     
   If startAction and stopAction for an entity are both set to none, that
   entity does not participate in the sequence.
   
   The start/stop delay and waitingForGuest is not used if the entity is a
   vApp container. For a vApp the only value values for startAction is none
   or powerOn, and the valid values for stopAction is none or powerOff.
   
   Attributes:
       key: Entity to power on or power off.
           
           This can be a virtual machine or a vApp.
       tag: Tag for entity.
           
           Reconfigure privilege: VApp.ApplicationConfig
       startOrder: Specifies the start order for this entity.
           
           Entities are started from lower
           numbers to higher-numbers and reverse on shutdown. Multiple entities with the
           same start-order can be started in parallel and the order is unspecified. This
           value must be 0 or higher.
           
           Reconfigure privilege: VApp.ApplicationConfig
       startDelay: Delay in seconds before continuing with the next entity in the order of entities
           to be started.
           
           Reconfigure privilege: VApp.ApplicationConfig
       waitingForGuest: Determines if the virtual machine should start after receiving a heartbeat,
           from the guest.
           
           When a virtual machine is next in the start
           order, the system either waits a specified period of time for a virtual
           machine to power on or it waits until it receives a successful heartbeat from a
           powered on virtual machine. By default, this is set to false.
           
           This property has no effect for vApps.
           
           Reconfigure privilege: VApp.ApplicationConfig
       startAction: How to start the entity.
           
           Valid settings are none or powerOn. If set to none, then
           the entity does not participate in auto-start.
           
           Reconfigure privilege: VApp.ApplicationConfig
       stopDelay: Delay in seconds before continuing with the next entity in the order
           sequence.
           
           This is only used if the stopAction is guestShutdown.
           
           Reconfigure privilege: VApp.ApplicationConfig
       stopAction: Defines the stop action for the entity.
           
           Can be set to none, powerOff,
           guestShutdown, or suspend. If set to none, then the entity does not participate in
           auto-stop.
           
           Reconfigure privilege: VApp.ApplicationConfig
       destroyWithParent: Whether the entity should be removed, when this vApp is removed.
           
           This is only set for linked children.
           
           Reconfigure privilege: VApp.ApplicationConfig
   """
   class Action(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          none: No action is taken for this virtual machine.
              
              This virtual machine is
              not a part of the auto-start sequence. This can be used for both auto-start
              and auto-start settings.
          powerOn: This virtual machine is powered on when it is next in the auto-start order.
          powerOff: This virtual machine is powered off when it is next in the auto-stop order.
              
              This is the default stopAction.
          guestShutdown: The guest operating system for a virtual machine is shut down when that
              virtual machine in next in the auto-stop order.
          suspend: This virtual machine is suspended when it is next in the auto-stop order.
      """
      none: _typing.ClassVar['EntityConfigInfo.Action'] = 'none'
      powerOn: _typing.ClassVar['EntityConfigInfo.Action'] = 'powerOn'
      powerOff: _typing.ClassVar['EntityConfigInfo.Action'] = 'powerOff'
      guestShutdown: _typing.ClassVar['EntityConfigInfo.Action'] = 'guestShutdown'
      suspend: _typing.ClassVar['EntityConfigInfo.Action'] = 'suspend'

   key: _typing.Optional[pyVmomi.vim.ManagedEntity] = None
   tag: _typing.Optional[str] = None
   startOrder: _typing.Optional[int] = None
   startDelay: _typing.Optional[int] = None
   waitingForGuest: _typing.Optional[bool] = None
   startAction: _typing.Optional[str] = None
   stopDelay: _typing.Optional[int] = None
   stopAction: _typing.Optional[str] = None
   destroyWithParent: _typing.Optional[bool] = None


class IPAssignmentInfo(pyVmomi.vmodl.DynamicData):
   """
   The IPAssignmentInfo class specifies how the guest software gets
   configured with IP addresses, including protocol type (IPv4 or IPv6)
   and the life-time of those IP addresses.
   
   A vApp/virtual machine can either use DHCP to acquire an IP
   configuration, or it can acquire its IP configuration through the
   use of the vSphere platform using the OVF environment's properties.
   The latter is a known as OVF-environment-assigned IP configuration.
   
   Guest software can be constructed to support DHCP , OVF assigned
   IP configuration, or both. The supportedAssignmentScheme property
   lists the supported schemes. This is typically specified by the author
   of a vApp.
   
   The deployer / operator of a vApp, specifies what IP allocation
   policy should be used:
   - Using DHCP, if the vApp and deployed network supports it
   - Transient Assignment, if the vApp supports OVF-assigned IP
     configuration and the network has an IP range configured.
   - Fixed Assignment, if the vApp supports OVF-assigned IP
     configuration.
   - Fixed Allocated, if the vApp supports OVF-assigned IP
     configuration and the network has an IP range configured.
     
   Transient and fixed assignment differs in the life time of the IP
   allocation. For transient, IP addresses are automatically assigned on
   power-on and released on power-off. For fixed, the IP
   addresses are explicitly specified by the deployer and does not change
   between a power-on/power-off.
   Fixed allocated is a hybrid of transient and fixed assignment. IP
   addresses are allocated at first power-on and remain allocated on power-off.
   
   The IPAssignment settings are global to a deployment. Thus, if a vApp or
   virtual machine is part of another vApp, then the settings are ignored,
   and the ones for the top-most vApp container is used.
   
   Attributes:
       supportedAllocationScheme: Specifies the IP allocation schemes supported by the guest software.
           
           When updating this field, an empty array will be interpreted as no changes.
           An array of the form [\"\"] will clear all settings. Otherwise, the supplied
           value will overwrite the current setting.
           
           Reconfigure privilege: VApp.ApplicationConfig
       ipAllocationPolicy: Specifies how IP allocation should be managed by the VI platform.
           
           This is
           typically specified by the deployer. The set of valid options for the policy
           is based on the capabilities of the vApp software, as specified by the
           supportedAllocationSchemes property.
           
           Reconfigure privilege: VApp.InstanceConfig
       supportedIpProtocol: Specifies the IP protocols supported by the guest software.
           
           When updating this field, an empty array will be interpreted as no changes.
           An array of the form [\"\"] will clear all settings. Otherwise, the supplied
           value will overwrite the current setting.
           
           Reconfigure privilege: VApp.ApplicationConfig
       ipProtocol: Specifies the chosen IP protocol for this deployment.
           
           This must be one of the
           values in the supportedIpProtocol field.
           
           Reconfigure privilege: VApp.InstanceConfig
   """
   class IpAllocationPolicy(pyVmomi.VmomiSupport.Enum):
      """
      IP allocation policy for a deployment.
      
      Attributes:
          dhcpPolicy: Specifies that DHCP must be used to allocate IP addresses to the vApp
          transientPolicy: Specifies that IP allocation is done through the range managed by the
              vSphere platform.
              
              The IP addresses are allocated when needed, typically at
              power-on, and deallocated during power-off. There is no guarantee that a
              vApp will get the same IP address when restarted.
          fixedPolicy: Specifies that IP addresses are configured manually when the vApp is deployed
              and will be kept until reconfigured or the vApp destroyed.
              
              This will ensure
              that a vApp gets a consistent IP for its life-time.
          fixedAllocatedPolicy: Specifies that IP allocation is done through the range managed by the VI
              platform.
              
              The IP addresses are allocated at first power-on, and remain
              allocated at power-off. This will ensure that a vApp gets a consistent
              IP for its life-time.
      """
      dhcpPolicy: _typing.ClassVar['IPAssignmentInfo.IpAllocationPolicy'] = 'dhcpPolicy'
      transientPolicy: _typing.ClassVar['IPAssignmentInfo.IpAllocationPolicy'] = 'transientPolicy'
      fixedPolicy: _typing.ClassVar['IPAssignmentInfo.IpAllocationPolicy'] = 'fixedPolicy'
      fixedAllocatedPolicy: _typing.ClassVar['IPAssignmentInfo.IpAllocationPolicy'] = 'fixedAllocatedPolicy'

   class AllocationSchemes(pyVmomi.VmomiSupport.Enum):
      """
      IP allocation schemes supported by the guest.
      
      Attributes:
          dhcp: The vApp supports DHCP to acquire IP configuration.
          ovfenv: The vApp supports setting the IP configuration through the
              properties provided in the OVF environment.
      """
      dhcp: _typing.ClassVar['IPAssignmentInfo.AllocationSchemes'] = 'dhcp'
      ovfenv: _typing.ClassVar['IPAssignmentInfo.AllocationSchemes'] = 'ovfenv'

   class Protocols(pyVmomi.VmomiSupport.Enum):
      """
      IP protocols supported by the guest.
      
      Attributes:
          IPv4: The vApp supports IPv4 protocol.
          IPv6: The vApp supports IPv6 protocol.
      """
      IPv4: _typing.ClassVar['IPAssignmentInfo.Protocols'] = 'IPv4'
      IPv6: _typing.ClassVar['IPAssignmentInfo.Protocols'] = 'IPv6'

   supportedAllocationScheme: list[str] = []
   ipAllocationPolicy: _typing.Optional[str] = None
   supportedIpProtocol: list[str] = []
   ipProtocol: _typing.Optional[str] = None


class IpPool(pyVmomi.vmodl.DynamicData):
   """
   Specifications of the network configuration to be used on a
   network.
   
   This is used to generate IP addresses and for self-customization
   of vApps.
   
   Attributes:
       id: Unique ID, generated by the server.
           
           This is used to identify the pool in
           subsequent lookups or updates. The generated value is also returned by the `pyVmomi.vim.IpPoolManager.createIpPool` method.
       name: Pool name.
           
           The pool name must be unique within the datacenter.
           
           Any / (slash), \\ (backslash), character used in this
           name element is escaped. Similarly, any % (percent) character used in
           this name element is escaped, unless it is used to start an escape
           sequence. A slash is escaped as %2F or %2f. A backslash is escaped as %5C or
           %5c, and a percent is escaped as %25.
       ipv4Config: IPv4 configuration.
           
           This configuration is always present on the pool. To disable allocation, set the
           ipPoolEnabled flag of the config to false.
       ipv6Config: IPv6 configuration.
           
           This configuration is always present on the pool. To disable allocation, set the
           ipPoolEnabled flag of the config to false.
       dnsDomain: DNS Domain.
           
           For example, vmware.com. This can be an empty string if no
           domain is configured.
       dnsSearchPath: DNS Search Path.
           
           For example, eng.vmware.com;vmware.com
       hostPrefix: Prefix for hostnames.
       httpProxy: The HTTP proxy to use on this network, e.g., <host>:<port>
       networkAssociation: The networks that are associated with this IP pool
       availableIpv4Addresses: The number of IPv4 addresses available for allocation.
       availableIpv6Addresses: The number of IPv6 addresses available for allocation.
       allocatedIpv4Addresses: The number of allocated IPv4 addresses.
       allocatedIpv6Addresses: The number of allocated IPv6 addresses.
   """
   class IpPoolConfigInfo(pyVmomi.vmodl.DynamicData):
      """
      Specifications of either IPv4 or IPv6 configuration to be used
      on this network.
      
      This is a part of network configuration.
      
      IPv4 addresses are in dot-decimal notation, e.g.: 192.0.2.235
      
      IPv6 addresses are in colon-hexadecimal notation,
      e.g.: 2001:0db8:85a3::0370:7334
      
      Attributes:
          subnetAddress: Address of the subnet.
              
              For example:
              - IPv4: 192.168.5.0
              - IPv6: 2001:0db8:85a3::
          netmask: Netmask
              
              For example:
              - IPv4: 255.255.255.0
              - IPv6: ffff:ffff:ffff::
          gateway: Gateway.
              
              This can be an empty string - if no gateway is configured.
              
              Examples:
              - IPv4: 192.168.5.1
              - IPv6: 2001:0db8:85a3::1
          range: IP range.
              
              This is specified as a set of ranges separated with commas.
              One range is given by a start address, a hash (#), and the length
              of the range.
              
              For example:
              - 192.0.2.235 # 20 is the IPv4 range from 192.0.2.235 to 192.0.2.254
              - 2001::7334 # 20 is the IPv6 range from 2001::7334 to 2001::7347
          dns: DNS servers
              
              For example:
              - IPv4: [\"10.20.0.1\", \"10.20.0.2\"]
              - IPv6: [\"2001:0db8:85a3::0370:7334\", \"2001:0db8:85a3::0370:7335\"]
                
              If an empty list is passed, the existing value remains unchanged. To clear this
              list, pass an array containing the empty string as it's only element.
          dhcpServerAvailable: Whether a DHCP server is available on this network.
          ipPoolEnabled: IP addresses can only be allocated from the range if the IP pool is
              enabled.
      """
      subnetAddress: _typing.Optional[str] = None
      netmask: _typing.Optional[str] = None
      gateway: _typing.Optional[str] = None
      range: _typing.Optional[str] = None
      dns: list[str] = []
      dhcpServerAvailable: _typing.Optional[bool] = None
      ipPoolEnabled: _typing.Optional[bool] = None

   class Association(pyVmomi.vmodl.DynamicData):
      """
      Information about a network or portgroup that is associated to an IP pool.
      
      Attributes:
          network: The network object
          networkName: The name of the network or portgroup
              
              This field is only used when querying existing IP pools. It is ignored when
              creating or updating pools.
      """
      network: _typing.Optional[pyVmomi.vim.Network] = None
      networkName: str

   id: _typing.Optional[int] = None
   name: _typing.Optional[str] = None
   ipv4Config: _typing.Optional[IpPool.IpPoolConfigInfo] = None
   ipv6Config: _typing.Optional[IpPool.IpPoolConfigInfo] = None
   dnsDomain: _typing.Optional[str] = None
   dnsSearchPath: _typing.Optional[str] = None
   hostPrefix: _typing.Optional[str] = None
   httpProxy: _typing.Optional[str] = None
   networkAssociation: list[IpPool.Association] = []
   availableIpv4Addresses: _typing.Optional[int] = None
   availableIpv6Addresses: _typing.Optional[int] = None
   allocatedIpv4Addresses: _typing.Optional[int] = None
   allocatedIpv6Addresses: _typing.Optional[int] = None


class OvfSectionInfo(pyVmomi.vmodl.DynamicData):
   """
   The OvfSection encapsulates uninterpreted meta-data sections in
   an OVF descriptor.
   
   When an OVF package is imported, non-required /
   non-interpreted sections will be stored as OvfSection object. During
   the creation of an OVF package, these sections will be placed in the
   OVF descriptor.
   
   Attributes:
       key: A unique key to identify a section.
       namespace: The namespace for the value in xsi:type attribute.
       type: The value of the xsi:type attribute not including the namespace prefix.
       atEnvelopeLevel: Whether this is a global envelope section
       contents: The XML fragment including the top-level <Section...> element.
           
           The
           fragment is self-contained will all required namespace definitions.
   """
   key: _typing.Optional[int] = None
   namespace: _typing.Optional[str] = None
   type: _typing.Optional[str] = None
   atEnvelopeLevel: _typing.Optional[bool] = None
   contents: _typing.Optional[str] = None


class OvfSectionSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   """An incremental update to the OvfSection list."""
   info: _typing.Optional[OvfSectionInfo] = None


class ProductInfo(pyVmomi.vmodl.DynamicData):
   """
   Information that describes what product a vApp contains, for example,
   the software that is installed in the contained virtual machines.
   
   Attributes:
       key: A unique key for the product section
       classId: Class name for this attribute.
           
           Valid values for classId:
           Any string except any white-space characters.
       instanceId: Class name for this attribute.
           
           Valid values for instanceId:
           Any string except any white-space characters.
       name: Name of the product.
       vendor: Vendor of the product.
       version: Short version of the product, for example, 1.0.
       fullVersion: Full-version of the product, for example, 1.0-build 12323.
       vendorUrl: URL to vendor homepage.
       productUrl: URL to product homepage.
       appUrl: URL to entry-point for application.
           
           This is often specified using
           a macro, for example, http://${app.ip}/, where app.ip is a defined property
           on the virtual machine or vApp container.
   """
   key: int
   classId: _typing.Optional[str] = None
   instanceId: _typing.Optional[str] = None
   name: _typing.Optional[str] = None
   vendor: _typing.Optional[str] = None
   version: _typing.Optional[str] = None
   fullVersion: _typing.Optional[str] = None
   vendorUrl: _typing.Optional[str] = None
   productUrl: _typing.Optional[str] = None
   appUrl: _typing.Optional[str] = None


class ProductSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   """An incremental update to the Product information list."""
   info: _typing.Optional[ProductInfo] = None


class PropertyInfo(pyVmomi.vmodl.DynamicData):
   """
   A vApp Property description, including deployment values
   
   Attributes:
       key: A unique integer key for the property.
       classId: class name for this property
           
           Valid values for classId:
           Any string except any white-space characters
           
           Reconfigure privilege: VApp.ApplicationConfig
       instanceId: class name for this property
           
           Valid values for instanceId:
           Any string except any white-space characters
           
           Reconfigure privilege: VApp.ApplicationConfig
       id: Name of property.
           
           In the OVF environment, the property is listed as
           [classId.]id[.instanceId]. The [classId.]name[.instanceId] must be unique.
           
           This field cannot be empty for a property. Thus, it must be specified at creation
           and cannot be set to the empty string.
           
           Valid values for id:
           Any string except any white-space characters
           
           Reconfigure privilege: VApp.ApplicationConfig
       category: A user-visible description the category the property belongs to.
           
           Reconfigure privilege: VApp.ApplicationConfig
       label: The display name for the property.
           
           Reconfigure privilege: VApp.ApplicationConfig
       type: Describes the valid format of the property.
           
           A type must be one of:
           - string : A generic string. Max length 65535 (64k).
           - string(x..) : A string with minimum character length x.
           - string(..y) : A string with maximum character length y.
           - string(x..y) : A string with minimum character length x and maximum
             character length y.
           - string[\"choice1\", \"choice2\", \"choice3\"] : A set of choices. \" inside a choice
             must be either \\\" or ' e.g \"start\\\"middle\\\"end\" or \"start'middle'end\" and
             a \\ inside a string choice must be encoded as \\\\ e.g. \"start\\\\end\".
           - int : An integer value. Is semantically equivalent to
             int(-2147483648..2147483647) e.g. signed int32.
           - int(x..y): An integer value with a minimum size x and a maximum size y.
             For example int(0..255) is a number between 0 and 255 both incl. This is
             also a way to specify that the number must be a uint8. There is always a lower
             and lower bound. Max number of digits is 100 including any sign. If exported to OVF the
             value will be truncated to max of uint64 or int64.
           - real : IEEE 8-byte floating-point value.
           - real(x..y) : IEEE 8-byte floating-point value with a minimum size x and a
             maximum size y. For example real(-1.5..1.5) must be a number between -1.5 and 1.5.
             Because of the nature of float some conversions can truncate the value.
             Real must be encoded according to CIM:
             RealValue = [ \"+\" | \"-\" } *decimalDigit \".\" 1*decimalDigit
             [ (\"e\" | \"E\" ) [ \"+\" | \"-\" ] 1*decimalDigit ] ]
           - boolean : A boolean. The value can be True or False
           - password : A generic string. Max length 65535 (64k).
           - password(x..) : A string with minimum character length x.
           - password(..y) : A string with maximum character length y.
           - password(x..y) : A string with minimum character length x and maximum
             character length y.
           - ip : An IPv4 address in dot-decimal notation or an IPv6 address in
             colon-hexadecimal notation.
           - ip:network : An IP address in dot-notation (IPv4) and colon-hexadecimal (IPv6)
             on a particular network. The behavior of this type depends on the
             ipAllocationPolicy. See below.
           - expression: The default value specifies an expression that is calculated
             by the system.
             
           For properties of type 'password', the value field and default value field will
           always be returned as an empty string when queried. Thus, it is a write-only property.
           Typically, a client application will also render these as a text field with hidden
           text and double prompting.
             
           An expression follows the general patterns of either ${arg} or ${cmd:arg}. The
           list of supported expressions are listed below:
           - ${<name>} : This expression evaluates to the same value as the named
             property in the parent vApp. A parent vApp is the
             first vApp in the ancestry chain (resource pools are
             skipped). If no parent vApp exists or the property is
             not defined on the parent vApp, the expression
             evaluates to the empty value.
           - ${subnet:<network>} : The subnet value of the given network.
           - ${netmask:<network>} : The netmask value of the given network.
           - ${gateway:<network>} : The gateway value of the given network.
           - ${autoIp:<network>} : An auto-assigned network address on the given
             network
           - ${net:<network>} : The name of the network
           - ${domainName:<network>} : The DNS domain name, e.g., vmware.com, of
             the given network.
           - ${searchPath:<network>} : The DNS search path, e.g.,
             eng.vmware.com;vmware.com, of the given
             network.
           - ${hostPrefix:<network>}: The host prefix on a given network, e.g.,
             \"voe-\"
           - ${dns:network}: A comma-separated string of configured network addresses
           - ${httpProxy:network}: The hostname:port for a proxy on the network
           - ${vimIp:} : The IP address of the VIM API provider server. This would
             typical be an ESX Server or VirtualCenter Server.
             
           A vApp will fail to start if any of the properties cannot be computed. For
           example, if a property reference a gateway on a network, for which is has not
           been specified. The value of the computed computation is assigned to the 'value'
           field upon start of the vApp or virtual machine. The value is cleared once
           the vApp or virtual machine is not-running.
           
           The system provides three ways of specifying IP addresses:
           - ip,
           - ip:network type,
           - ${ip:network} expression.
             
           The ip types are typically used to specify an IP addressed to an
           external system. Thus, these are not used by a virtual ethernet adapter
           within the guest itself. Both the ip:network expression and the ${ip:network}
           expression are intended as a way to obtain an IP address for a virtual machine
           in a vApp.
           
           The behavior of ip:network type is controlled by the ipAssignPolicy, as
           described in the following table:
           
           Policy
            - ip:<network> type
           
           DHCP
            - The user is not prompted to enter a value. The variable is set to the
           empty string during power-on, and later updated with the IP value reported
           by the guest software.
           
           Transient
            - The user is not prompted to enter a value. An IP address is allocated by
           the platform and is assigned to the variable which is available to the
           guest. The IP address is released at power-off.
           
           Fixed
            - The user is prompted to enter a value. This value is available to the
           guest.
           
           Fixed Allocated
            - The user is not prompted to enter a value. An IP address is allocated by
           the platform and is assigned to the variable which is available to the
           guest. The IP address remains allocated at power-off, and are only
           released if the property is deleted or the vApp is destroyed.
           
           Reconfigure privilege: VApp.ApplicationConfig
       typeReference: Contains extra configuration data depending on the property type.
           
           For types that
           refer to network names the type reference is the managed object reference
           of the network.
       userConfigurable: Whether the property is user-configurable or a system property.
           
           This is not used
           if the type is expression.
           
           Reconfigure privilege: VApp.ApplicationConfig
       defaultValue: This either contains the default value of a field (used if value is empty
           string), or the expression if the type is \"expression\".
           
           See comment for the
       value: The value of the field at deployment time.
           
           For expressions, this will contain
           the value that has been computed.
           
           Reconfigure privilege: VApp.InstanceConfig
       description: A description of the field.
           
           Reconfigure privilege: VApp.ApplicationConfig
   """
   key: int
   classId: _typing.Optional[str] = None
   instanceId: _typing.Optional[str] = None
   id: _typing.Optional[str] = None
   category: _typing.Optional[str] = None
   label: _typing.Optional[str] = None
   type: _typing.Optional[str] = None
   typeReference: _typing.Optional[str] = None
   userConfigurable: _typing.Optional[bool] = None
   defaultValue: _typing.Optional[str] = None
   value: _typing.Optional[str] = None
   description: _typing.Optional[str] = None


class PropertySpec(pyVmomi.vim.option.ArrayUpdateSpec):
   """An incremental update to the Property list."""
   info: _typing.Optional[PropertyInfo] = None


class VmConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   VM Configuration.
   
   Attributes:
       product: Information about the package content.
       property: List of properties
       ipAssignment: IP assignment policy and DHCP support configuration.
       eula: End User Licenses Agreements.
       ovfSection: List of uninterpreted OVF meta-data sections.
       ovfEnvironmentTransport: List the transports to use for properties.
           
           Supported values are: iso and
           com.vmware.guestInfo.
       installBootRequired: Specifies whether the VM needs an initial boot before the deployment is complete.
           
           Not relevant for vApps. This means that the value is always false when reading the
           configuration and is ignored when setting the configuration.
           
           If a vApp requires an install boot (because one of its VMs does), this is visible
           on the `pyVmomi.vim.VirtualApp.Summary.installBootRequired` field of the vApp.
       installBootStopDelay: Specifies the delay in seconds to wait for the VM to power off after the initial
           boot (used only if installBootRequired is true).
           
           A value of 0 means wait forever.
           
           Not relevant for vApps. This means that the value is always false when reading the
           configuration and is ignored when setting the configuration.
   """
   product: list[ProductInfo] = []
   property: list[PropertyInfo] = []
   ipAssignment: IPAssignmentInfo
   eula: list[str] = []
   ovfSection: list[OvfSectionInfo] = []
   ovfEnvironmentTransport: list[str] = []
   installBootRequired: bool
   installBootStopDelay: int


class VAppConfigInfo(VmConfigInfo):
   """
   Configuration of a vApp container.
   
   Attributes:
       entityConfig: Configuration of sub-entities (virtual machine or vApp).
       annotation: Description for the vApp.
       instanceUuid: vCenter-specific 128-bit UUID of a vApp, represented as a hexadecimal
           string.
           
           This identifier is used by vCenter to uniquely identify all
           vApp instances.
       managedBy: Specifies that this vApp is managed by a VC Extension.
           
           See the
           `pyVmomi.vim.vApp.VAppConfigSpec.managedBy` property in the
           VAppConfigSpec for more details.
   """
   entityConfig: list[EntityConfigInfo] = []
   annotation: str
   instanceUuid: _typing.Optional[str] = None
   managedBy: _typing.Optional[pyVmomi.vim.ext.ManagedByInfo] = None


class VmConfigSpec(pyVmomi.vmodl.DynamicData):
   """
   vApp related configuration of a VM.
   
   Attributes:
       product: Information about the product.
           
           Reconfigure privilege: VApp.ApplicationConfig
       property: List of properties.
           
           Adding and editing properties requires various privileges depending on which fields
           are affected. See `pyVmomi.vim.vApp.PropertyInfo` for details.
           
           Deleting properties requires the privilege VApp.ApplicationConfig.
       ipAssignment: IP assignment policy and DHCP support configuration.
           
           Reconfigure privilege: See `pyVmomi.vim.vApp.IPAssignmentInfo`
       eula: End User Licenses Agreements.
           
           If this list is set, it replaces all exiting licenses. An empty list will not
           make any changes to installed licenses. A list with a single element {\"\"} will
           remove all licenses and leave an empty list.
           
           Reconfigure privilege: VApp.ApplicationConfig
       ovfSection: List of uninterpreted OVF meta-data sections.
           
           Reconfigure privilege: VApp.ApplicationConfig
       ovfEnvironmentTransport: List the transports to use for properties.
           
           Supported values are: iso and
           com.vmware.guestInfo.
           
           If this list is set, it replaces all exiting entries. An empty list will not make
           any changes. A list with a single element {\"\"} will clear the list of transports.
           
           Reconfigure privilege: VApp.ApplicationConfig
       installBootRequired: If this is on a VirtualMachine object, it specifies whether the VM needs an
           initial boot before the deployment is complete.
           
           If this is on a vApp object,
           it indicates than one or more VMs needs an initial reboot. This flag is
           automatically reset once the reboot has happened.
           
           Reconfigure privilege: VApp.ApplicationConfig
       installBootStopDelay: Specifies the delay in seconds to wait for the VM to power off after the initial
           boot (used only if installBootRequired is true).
           
           A value of 0 means wait forever.
           
           Reconfigure privilege: VApp.ApplicationConfig
   """
   product: list[ProductSpec] = []
   property: list[PropertySpec] = []
   ipAssignment: _typing.Optional[IPAssignmentInfo] = None
   eula: list[str] = []
   ovfSection: list[OvfSectionSpec] = []
   ovfEnvironmentTransport: list[str] = []
   installBootRequired: _typing.Optional[bool] = None
   installBootStopDelay: _typing.Optional[int] = None


class VAppConfigSpec(VmConfigSpec):
   """
   Configuration of a vApp
   
   Attributes:
       entityConfig: Configuration of sub-entities (virtual machine or vApp container).
           
           Reconfigure privilege: See EntityConfigInfo
       annotation: Description for the vApp.
           
           Reconfigure privilege: VApp.Rename.
       instanceUuid: vCenter-specific 128-bit UUID of a vApp, represented as a hexadecimal
           string.
           
           This identifier is used by vCenter to uniquely identify all
           vApp instances in the Virtual Infrastructure environment.
           
           Normally, this property is not set by a client, allowing the
           Virtual Infrastructure environment to assign or change it when
           VirtualCenter detects an identifier conflict between vApps.
           
           Reconfigure privilege: VApp.ApplicationConfig
       managedBy: Specifies that this vApp is managed by a VC Extension.
           
           This information is primarily used in the Client to show a custom icon for
           managed vApps, and a description of the function of the vApp. If no extension
           can be found with the extension key in the `pyVmomi.vim.ext.ManagedByInfo`
           object, or the type is not found in the
           `pyVmomi.vim.Extension.managedEntityInfo` list of the
           extension, the default vApp icon is used, and no description is shown.
           
           Reconfigure privilege: VApp.ApplicationConfig
   """
   entityConfig: list[EntityConfigInfo] = []
   annotation: _typing.Optional[str] = None
   instanceUuid: _typing.Optional[str] = None
   managedBy: _typing.Optional[pyVmomi.vim.ext.ManagedByInfo] = None


class VAppImportSpec(pyVmomi.vim.ImportSpec):
   """
   A VAppImportSpec is used by `pyVmomi.vim.ResourcePool.importVApp` when importing vApps (single VM or multi-VM).
   
   It provides all information needed to import a `pyVmomi.vim.VirtualApp`.
   
   See also `pyVmomi.vim.ImportSpec`.
   
   Attributes:
       name: The name of the vApp
       vAppConfigSpec: vApp configuration
       resourcePoolSpec: Resource pool specification.
           
           If resourcePoolSpec.entity is specified, that resource pool is used as the parent
           resource pool and the vApp will be made a linked child to the parent vApp. This
           field is ignored for the root node in an ImportSpec tree.
           Use of resourcePoolSpec.entity for creating linked children is deprecated as of
           vSphere API 5.1.
       child: Contains a list of children (`pyVmomi.vim.VirtualMachine`s and
           `pyVmomi.vim.VirtualApp`s).
   """
   name: str
   vAppConfigSpec: VAppConfigSpec
   resourcePoolSpec: pyVmomi.vim.ResourceConfigSpec
   child: list[pyVmomi.vim.ImportSpec] = []
