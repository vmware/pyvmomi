# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.fault
import pyVmomi.vim.host



class DistributedVirtualPort(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.dvs.DistributedVirtualPort` data object represents a port in a
   `pyVmomi.vim.DistributedVirtualSwitch`.
   
   Virtual ports are part of a distributed
   virtual portgroup. Servers create virtual ports according to the portgroup type
   (`pyVmomi.vim.dvs.DistributedVirtualPortgroup`.`pyVmomi.vim.dvs.DistributedVirtualPortgroup.config`.`pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo.type`).
   See `pyVmomi.vim.dvs.DistributedVirtualPortgroup.PortgroupType`.
   - To configure host network access by port, set the distributed virtual port
     in the host virtual NIC specification
     (`pyVmomi.vim.host.VirtualNic.Specification`.`pyVmomi.vim.host.VirtualNic.Specification.distributedVirtualPort`.`pyVmomi.vim.dvs.PortConnection.portKey`).
   - To configure virtual machine network access by port, set the port
     in the virtual Ethernet card backing
     (`pyVmomi.vim.vm.device.VirtualEthernetCard`.`pyVmomi.vim.vm.device.VirtualDevice.backing`.`pyVmomi.vim.vm.device.VirtualEthernetCard.DistributedVirtualPortBackingInfo.port`.`pyVmomi.vim.dvs.PortConnection.portKey`).
   
   Attributes:
       key: Port key.
       config: Port configuration, including identifying information, network
           settings, and the set of entities that can connect to the port.
       dvsUuid: UUID of the `pyVmomi.vim.DistributedVirtualSwitch` to which the port belongs.
       portgroupKey: Key of the portgroup `pyVmomi.vim.dvs.DistributedVirtualPortgroup` to which
           the port belongs, if any.
       proxyHost: `pyVmomi.vim.HostSystem` that services this port.
       connectee: Entity that connects to the port.
       conflict: Specifies whether the port is a conflict port.
           
           A port could be marked
           as conflict if an entity is discovered connecting to a port that is
           already occupied, or if the host creates a port without conferring
           with vCenter Server.
           
           The distributed virtual switch does not persist the runtime state
           of a conflict port. Also, the port cannot move away from the host.
           vCenter Server will not move a virtual machine (VMotion) that is
           using a conflict port.
       conflictPortKey: If the port is marked conflict in the case of two entities connecting to
           the same port (see
           `pyVmomi.vim.dvs.DistributedVirtualPort.conflict`), this is the
           key of the port which the connected entity is contending for.
       state: Runtime state of the port.
       connectionCookie: Cookie representing the current instance of association between a
           port and a virtual or physical NIC.
           
           See `pyVmomi.vim.dvs.PortConnection`.
           The same cookie is present in the physical or virtual NIC configuration
           (`pyVmomi.vim.dvs.PortConnection`.`pyVmomi.vim.dvs.PortConnection.connectionCookie`)
           so that the Server can verify that the entity is the rightful
           connectee of the port.
       lastStatusChange: The last time the
           `pyVmomi.vim.dvs.DistributedVirtualPort.state`.`pyVmomi.vim.dvs.DistributedVirtualPort.State.runtimeInfo`
           value was changed.
       hostLocalPort: Specifies whether the port is a host local port.
           
           A host local port is created
           to resurrect the management network connection on a VMkernel virtual NIC.
           You cannot use vCenter Server to reconfigure this port and you cannot
           reassign the port.
       externalId: Populate the Id assigned to vmknic or vnic by external management plane
           to port, if the port is connected to the nics.
       segmentPortId: Populate the segmentPortId assigned to LSP.
   """
   class ConfigSpec(pyVmomi.vmodl.DynamicData):
      """
      Specification to reconfigure a `pyVmomi.vim.dvs.DistributedVirtualPort`.
      
      Attributes:
          operation: The operation to remove or modify the existing ports.
              
              The valid values
              are:
              - `edit`
              - `remove`
          key: Key of the port to be reconfigured.
          name: The name of the port.
          scope: The eligible entities that can connect to the port, for detail see
              `pyVmomi.vim.dvs.DistributedVirtualPort.ConfigInfo.scope`.
          description: The description string of the port.
          setting: The network setting of the port.
          configVersion: The version string of the configuration.
      """
      operation: str
      key: _typing.Optional[str] = None
      name: _typing.Optional[str] = None
      scope: list[pyVmomi.vim.ManagedEntity] = []
      description: _typing.Optional[str] = None
      setting: _typing.Optional[DistributedVirtualPort.Setting] = None
      configVersion: _typing.Optional[str] = None

   class ConfigInfo(pyVmomi.vmodl.DynamicData):
      """
      Management related configuration of a DistributedVirtualPort.
      
      Attributes:
          name: The name of the port.
          scope: The eligible entities that can connect to the port.
              
              If unset, there
              is no restriction on which entity can connect to the port. If set,
              only the entities in the specified list or their child entities are
              allowed to connect to the port. If scopes are defined at both port
              and portgroup level, they are taken as an \"AND\" relationship. If such
              a relationship doesn't make sense, the reconfigure operation will
              raise an exception.
          description: A description string of the port.
          setting: The network configuration of the port.
          configVersion: The version string of the configuration.
      """
      name: _typing.Optional[str] = None
      scope: list[pyVmomi.vim.ManagedEntity] = []
      description: _typing.Optional[str] = None
      setting: _typing.Optional[DistributedVirtualPort.Setting] = None
      configVersion: str

   class TrafficShapingPolicy(pyVmomi.vim.InheritablePolicy):
      """
      This data object type describes traffic shaping policy.
      
      Attributes:
          enabled: The flag to indicate whether or not traffic shaper is enabled on
              the port.
          averageBandwidth: The average bandwidth in bits per second if shaping is enabled on
              the port.
          peakBandwidth: The peak bandwidth during bursts in bits per second if traffic
              shaping is enabled on the port.
          burstSize: The maximum burst size allowed in bytes if shaping is enabled on
              the port.
      """
      enabled: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      averageBandwidth: _typing.Optional[pyVmomi.vim.LongPolicy] = None
      peakBandwidth: _typing.Optional[pyVmomi.vim.LongPolicy] = None
      burstSize: _typing.Optional[pyVmomi.vim.LongPolicy] = None

   class HostLocalPortInfo(pyVmomi.vmodl.DynamicData):
      """
      This data object type describes the information about the host local port.
      
      A host local port is created to resurrect the management network connection
      on a VMkernel Virtual NIC.
      
      Attributes:
          switchUuid: UUID of the vSphere Distributed Switch that management interface is connected to.
          portKey: Portkey of the DVPort that management interface is now connected to.
          setting: The configuration of the new host local port.
          vnic: The Virtual NIC device connected to this port
      """
      switchUuid: str
      portKey: str
      setting: DistributedVirtualPort.Setting
      vnic: str

   class VendorSpecificConfig(pyVmomi.vim.InheritablePolicy):
      """
      This data object type describes vendor specific configuration.
      
      Attributes:
          keyValue: An opaque binary blob that stores vendor specific configuration.
      """
      keyValue: list[KeyedOpaqueBlob] = []

   class FilterParameter(pyVmomi.vmodl.DynamicData):
      """
      This class defines Network Filter parameter.
      
      Attributes:
          parameters: List of parameters for a Network Filter.
      """
      parameters: list[str] = []

   class FilterOnFailure(pyVmomi.VmomiSupport.Enum):
      """
      Network Filter on Failure Type.
      
      It specifies whether all the
      packets will be allowed or all the packets will be denied when
      Filter fails to configure.
      
      Attributes:
          failOpen: Allows all the packets when the Filter fails to configure.
          failClosed: Denies all the packets when the Filter fails to configure.
      """
      failOpen: _typing.ClassVar['DistributedVirtualPort.FilterOnFailure'] = 'failOpen'
      failClosed: _typing.ClassVar['DistributedVirtualPort.FilterOnFailure'] = 'failClosed'

   class FilterConfig(pyVmomi.vim.InheritablePolicy):
      """
      This class defines Network Filter configuration.
      
      Supported Qualifier and Actions 
      
      Network Filter Config
       - Supported classes
      
      Qualifiers supported
       - `pyVmomi.vim.SingleIp`, `pyVmomi.vim.IpRange`,
      `pyVmomi.vim.SingleMac`, `pyVmomi.vim.MacRange`,
      `pyVmomi.vim.dvs.TrafficRule.SingleIpPort`,
      `pyVmomi.vim.dvs.TrafficRule.SystemTrafficQualifier`
      
      Actions Supported
       - `pyVmomi.vim.dvs.TrafficRule.DropAction`,
      `pyVmomi.vim.dvs.TrafficRule.AcceptAction`,
      `pyVmomi.vim.dvs.TrafficRule.PuntAction`,
      `pyVmomi.vim.dvs.TrafficRule.CopyAction`,
      `pyVmomi.vim.dvs.TrafficRule.MacRewriteAction`,
      `pyVmomi.vim.dvs.TrafficRule.GreAction`,
      `pyVmomi.vim.dvs.TrafficRule.LogAction`,
      `pyVmomi.vim.dvs.TrafficRule.UpdateTagAction`,
      `pyVmomi.vim.dvs.TrafficRule.RateLimitAction`
      
      Attributes:
          key: The key of Network Filter Config.
          agentName: The name of the network traffic filter agent.
          slotNumber: The slot number of the network filter agent.
          parameters: Network Filter Parameter
          onFailure: This property specifies whether to allow all traffic or to deny all
              traffic when a Network Filter fails to configure.
              
              Please see `pyVmomi.vim.dvs.DistributedVirtualPort.FilterOnFailure`
              for more details.
      """
      key: _typing.Optional[str] = None
      agentName: _typing.Optional[str] = None
      slotNumber: _typing.Optional[str] = None
      parameters: _typing.Optional[DistributedVirtualPort.FilterParameter] = None
      onFailure: _typing.Optional[str] = None

   class TrafficFilterConfig(DistributedVirtualPort.FilterConfig):
      """
      This class defines Traffic Filter configuration.
      
      Supported Qualifier and Actions 
      
      Traffic Filter Config
       - Supported classes
      
      Qualifiers supported
       - `pyVmomi.vim.SingleIp`, `pyVmomi.vim.IpRange`,
      `pyVmomi.vim.SingleMac`, `pyVmomi.vim.MacRange`,
      `pyVmomi.vim.dvs.TrafficRule.SingleIpPort`,
      `pyVmomi.vim.dvs.TrafficRule.SystemTrafficQualifier`
      
      Actions Supported
       - `pyVmomi.vim.dvs.TrafficRule.DropAction`,
      `pyVmomi.vim.dvs.TrafficRule.AcceptAction`,
      `pyVmomi.vim.dvs.TrafficRule.PuntAction`,
      `pyVmomi.vim.dvs.TrafficRule.CopyAction`,
      `pyVmomi.vim.dvs.TrafficRule.MacRewriteAction`,
      `pyVmomi.vim.dvs.TrafficRule.GreAction`,
      `pyVmomi.vim.dvs.TrafficRule.LogAction`,
      `pyVmomi.vim.dvs.TrafficRule.UpdateTagAction`,
      `pyVmomi.vim.dvs.TrafficRule.RateLimitAction`
      
      Attributes:
          trafficRuleset: Network Traffic Ruleset
      """
      trafficRuleset: _typing.Optional[TrafficRuleset] = None

   class FilterConfigSpec(DistributedVirtualPort.FilterConfig):
      """
      The specification to reconfigure Network Filter.
      
      This specification allows the user to do fine-grained updates for the
      Filter in the port settings.
      If the operation is `remove`, only the
      `pyVmomi.vim.dvs.DistributedVirtualPort.key` needs to be specified.
      If other fields are specified, they will be ignored. We cannot remove
      an inherited element. Only when the inherited flag is set to false and
      parent does not have an element with same key this operation succeeds.
      If the operation is `add`, then
      `pyVmomi.vim.dvs.DistributedVirtualPort.key` should not be specified and
      other fields need to be specified. The inherited flag should be set to
      false.
      If the operation is `edit`, then
      `pyVmomi.vim.dvs.DistributedVirtualPort.key` needs be specified and
      specify the other properties that need modification. If the inherited
      flag is set to true, a `pyVmomi.vim.dvs.DistributedVirtualPort.FilterConfig` object of same
      key must exist at the parent's level. The property values in the spec
      object will be ignored and use the values from the parent's
      `pyVmomi.vim.dvs.DistributedVirtualPort.FilterConfig` object instead. If inherited
      flag is set to false, then the new modifications will be applied.
      
      Attributes:
          operation: Operation type.
              
              See `pyVmomi.vim.ConfigSpecOperation` for valid values.
      """
      operation: str

   class TrafficFilterConfigSpec(DistributedVirtualPort.TrafficFilterConfig):
      """
      The specification to reconfigure Traffic Filter.
      
      This specification allows the user to do fine-grained updates for the
      Traffic Filter in the port settings.
      If the operation is `remove`, only the
      `pyVmomi.vim.dvs.DistributedVirtualPort.key` needs to be specified.
      If other fields are specified, they will be ignored. We cannot remove
      an inherited element. Only when the inherited flag is set to false and
      parent does not have an element with same key this operation succeeds.
      If the operation is `add`, then
      `pyVmomi.vim.dvs.DistributedVirtualPort.key` should not be specified and
      other fields need to be specified. The inherited flag should be set to
      false.
      If the operation is `edit`, then
      `pyVmomi.vim.dvs.DistributedVirtualPort.key` needs be specified and
      specify the other properties that need modification. If the inherited
      flag is set to true, a `pyVmomi.vim.dvs.DistributedVirtualPort.TrafficFilterConfig` object of same
      key must exist at the parent's level. The property values in the spec
      object will be ignored and use the values from the parent's
      `pyVmomi.vim.dvs.DistributedVirtualPort.TrafficFilterConfig` object instead. If inherited
      flag is set to false, then the new modifications will be applied.
      
      Attributes:
          operation: Operation type.
              
              See `pyVmomi.vim.ConfigSpecOperation` for valid values.
      """
      operation: str

   class FilterPolicy(pyVmomi.vim.InheritablePolicy):
      """
      This class defines Network Filter Policy.
      
      Attributes:
          filterConfig: List of Network Filter Configurations.
              
              In an update operation, the array can contain all
              `pyVmomi.vim.dvs.DistributedVirtualPort.TrafficFilterConfigSpec` objects
              or all `pyVmomi.vim.dvs.DistributedVirtualPort.FilterConfig` and
              `pyVmomi.vim.dvs.DistributedVirtualPort.TrafficFilterConfig`
              object, but not mixed of Config and Spec objects. If array of
              `pyVmomi.vim.dvs.DistributedVirtualPort.FilterConfigSpec` and `pyVmomi.vim.dvs.DistributedVirtualPort.TrafficFilterConfigSpec` is used
              for updating Network Filter then only the Network Filters
              matching `pyVmomi.vim.dvs.DistributedVirtualPort.key` /
              `pyVmomi.vim.dvs.DistributedVirtualPort.key`
              is updated.
              If array of `pyVmomi.vim.dvs.DistributedVirtualPort.FilterConfig` and
              `pyVmomi.vim.dvs.DistributedVirtualPort.TrafficFilterConfig`
              is used for updating port settings, the Network Filter
              settings will be overridden with the new array specified. The
              specified array should only contain `pyVmomi.vim.dvs.DistributedVirtualPort.FilterConfig` and
              `pyVmomi.vim.dvs.DistributedVirtualPort.TrafficFilterConfig` objects with `pyVmomi.vim.InheritablePolicy.inherited` /
              `pyVmomi.vim.InheritablePolicy.inherited` set to false.
              `pyVmomi.vim.dvs.DistributedVirtualPort.FilterConfig`/`pyVmomi.vim.dvs.DistributedVirtualPort.TrafficFilterConfig` objects with
              `pyVmomi.vim.InheritablePolicy.inherited`/`pyVmomi.vim.InheritablePolicy.inherited` as
              true in the specified array will be ignored. The updated result will
              include `pyVmomi.vim.dvs.DistributedVirtualPort.FilterConfig`/`pyVmomi.vim.dvs.DistributedVirtualPort.TrafficFilterConfig` objects
              inherited from parent, if any.
      """
      filterConfig: list[DistributedVirtualPort.FilterConfig] = []

   class Setting(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.dvs.DistributedVirtualPort.Setting` data object
      describes the network configuration of a `pyVmomi.vim.dvs.DistributedVirtualPort`.
      
      Attributes:
          blocked: Indicates whether this port is blocked.
              
              If a port is blocked,
              packet forwarding is stopped.
          vmDirectPathGen2Allowed: Indicates whether this port is allowed to do VMDirectPath Gen2 network passthrough.
              
              Direct path capability is defined at host, switch, and device levels.
              See the `vmDirectPathGen2Supported` properties on the
              `pyVmomi.vim.DistributedVirtualSwitch.FeatureCapability`,
              `pyVmomi.vim.host.Capability`, `pyVmomi.vim.host.PhysicalNic`,
              and `pyVmomi.vim.vm.device.VirtualEthernetCardOption` objects.
          inShapingPolicy: Network shaping policy for controlling throughput of inbound traffic.
          outShapingPolicy: Network shaping policy for controlling throughput of outbound traffic.
          vendorSpecificConfig: Opaque binary blob that stores vendor specific configuration.
          networkResourcePoolKey: The key of user defined network resource pool to be associated with a port.
              
              The default value for this property is \"-1\", indicating that
              this port is not associated with any network resource pool.
          filterPolicy: Configuration for Network Filter Policy.
      """
      blocked: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      vmDirectPathGen2Allowed: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      inShapingPolicy: _typing.Optional[DistributedVirtualPort.TrafficShapingPolicy] = None
      outShapingPolicy: _typing.Optional[DistributedVirtualPort.TrafficShapingPolicy] = None
      vendorSpecificConfig: _typing.Optional[DistributedVirtualPort.VendorSpecificConfig] = None
      networkResourcePoolKey: _typing.Optional[pyVmomi.vim.StringPolicy] = None
      filterPolicy: _typing.Optional[DistributedVirtualPort.FilterPolicy] = None

   class RuntimeInfo(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo` data object
      contains runtime information about a `pyVmomi.vim.dvs.DistributedVirtualPort`.
      
      Attributes:
          linkUp: Indicates whether the port is in linkUp status.
          blocked: Indicates whether the port is blocked by switch implementation.
          vlanIds: VLAN ID of the port.
          trunkingMode: True if the port VLAN tagging/stripping is disabled.
          mtu: Maximum transmission unit (MTU) of the port.
              
              You can set the MTU only
              at the switch level
              (`pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.ConfigSpec`).
              If you attempt to change it at the portgroup or port level,
              the Server throws an exception.
          linkPeer: Name of the connected entity.
          macAddress: The MAC address that is used at this port.
          statusDetail: Additional information regarding the current status of the port.
          vmDirectPathGen2Active: Indicates whether VMDirectPath Gen 2 is active on this port.
              
              If false, the reason(s) for inactivity will be provided in one or
              more of `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo.vmDirectPathGen2InactiveReasonNetwork`,
              `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo.vmDirectPathGen2InactiveReasonOther`,
              and `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo.vmDirectPathGen2InactiveReasonExtended`.
              
              If the host software is not capable of VMDirectPath Gen 2,
              this property will be unset. See
              `pyVmomi.vim.host.Capability`.`pyVmomi.vim.host.Capability.vmDirectPathGen2Supported`.
          vmDirectPathGen2InactiveReasonNetwork: If `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo.vmDirectPathGen2Active` is false, this array will be
              populated with reasons for the inactivity that are related to network
              state or configuration.
              
              The reasons are chosen from the
              `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo.VmDirectPathGen2InactiveReasonNetwork`
              values.
              
              Other reasons for inactivity will be provided in
              `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo.vmDirectPathGen2InactiveReasonOther`. If there is a reason
              for inactivity that cannot be described by the available constants,
              `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo.vmDirectPathGen2InactiveReasonExtended` will be populated
              with an additional explanation provided by the platform.
              
              Note that this list of reasons is not guaranteed to be exhaustive.
          vmDirectPathGen2InactiveReasonOther: If `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo.vmDirectPathGen2Active` is false, this array will be
              populated with reasons for the inactivity that are not related to
              network state or configuration.
              
              The reasons are chosen from the
              `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo.VmDirectPathGen2InactiveReasonOther`
              values.
              
              Network-related reasons for inactivity will be provided in
              `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo.vmDirectPathGen2InactiveReasonNetwork`. If there is a reason
              for inactivity that cannot be described by the available constants,
              `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo.vmDirectPathGen2InactiveReasonExtended` will be populated
              with an additional explanation provided by the platform.
              
              Note that this list of reasons is not guaranteed to be exhaustive.
          vmDirectPathGen2InactiveReasonExtended: If `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo.vmDirectPathGen2Active` is false, this property may
              contain an explanation provided by the platform, beyond the reasons
              (if any) listed in `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo.vmDirectPathGen2InactiveReasonNetwork`
              and/or `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo.vmDirectPathGen2InactiveReasonOther`.
      """
      class VmDirectPathGen2InactiveReasonNetwork(pyVmomi.VmomiSupport.Enum):
         """
         Set of possible values for
         `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo`.`pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo.vmDirectPathGen2InactiveReasonNetwork`.
         
         Attributes:
             portNptIncompatibleDvs: The switch for which this port is defined does not support VMDirectPath Gen 2.
                 
                 See
                 `pyVmomi.vim.DistributedVirtualSwitch.FeatureCapability`.`pyVmomi.vim.DistributedVirtualSwitch.FeatureCapability.vmDirectPathGen2Supported`.
             portNptNoCompatibleNics: None of the physical NICs used as uplinks for this port support
                 VMDirectPath Gen 2.
             portNptNoVirtualFunctionsAvailable: At least some of the physical NICs used as uplinks for this port
                 support VMDirectPath Gen 2, but all available network-passthrough
                 resources are in use by other ports.
             portNptDisabledForPort: VMDirectPath Gen 2 has been explicitly disabled for this port.
         """
         portNptIncompatibleDvs: _typing.ClassVar['DistributedVirtualPort.RuntimeInfo.VmDirectPathGen2InactiveReasonNetwork'] = 'portNptIncompatibleDvs'
         portNptNoCompatibleNics: _typing.ClassVar['DistributedVirtualPort.RuntimeInfo.VmDirectPathGen2InactiveReasonNetwork'] = 'portNptNoCompatibleNics'
         portNptNoVirtualFunctionsAvailable: _typing.ClassVar['DistributedVirtualPort.RuntimeInfo.VmDirectPathGen2InactiveReasonNetwork'] = 'portNptNoVirtualFunctionsAvailable'
         portNptDisabledForPort: _typing.ClassVar['DistributedVirtualPort.RuntimeInfo.VmDirectPathGen2InactiveReasonNetwork'] = 'portNptDisabledForPort'

      class VmDirectPathGen2InactiveReasonOther(pyVmomi.VmomiSupport.Enum):
         """
         Set of possible values for
         `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo`.`pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo.vmDirectPathGen2InactiveReasonOther`.
         
         Attributes:
             portNptIncompatibleHost: The host for which this port is defined does not support VMDirectPath Gen 2.
                 
                 See `pyVmomi.vim.host.Capability`.`pyVmomi.vim.host.Capability.vmDirectPathGen2Supported`
             portNptIncompatibleConnectee: Configuration or state of the port's connectee prevents
                 VMDirectPath Gen 2.
                 
                 See
                 `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.vmDirectPathGen2InactiveReasonVm`
                 and/or
                 `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.vmDirectPathGen2InactiveReasonExtended`
                 in the appropriate element of the RuntimeInfo.device array of the
                 virtual machine connected to this port.
         """
         portNptIncompatibleHost: _typing.ClassVar['DistributedVirtualPort.RuntimeInfo.VmDirectPathGen2InactiveReasonOther'] = 'portNptIncompatibleHost'
         portNptIncompatibleConnectee: _typing.ClassVar['DistributedVirtualPort.RuntimeInfo.VmDirectPathGen2InactiveReasonOther'] = 'portNptIncompatibleConnectee'

      linkUp: bool
      blocked: bool
      vlanIds: list[pyVmomi.vim.NumericRange] = []
      trunkingMode: _typing.Optional[bool] = None
      mtu: _typing.Optional[int] = None
      linkPeer: _typing.Optional[str] = None
      macAddress: _typing.Optional[str] = None
      statusDetail: _typing.Optional[str] = None
      vmDirectPathGen2Active: _typing.Optional[bool] = None
      vmDirectPathGen2InactiveReasonNetwork: list[str] = []
      vmDirectPathGen2InactiveReasonOther: list[str] = []
      vmDirectPathGen2InactiveReasonExtended: _typing.Optional[str] = None

   class State(pyVmomi.vmodl.DynamicData):
      """
      The state of a DistributedVirtualPort.
      
      Attributes:
          runtimeInfo: Run time information of the port.
              
              This property is set only when the port is running.
          stats: Statistics of the port.
          vendorSpecificState: Opaque binary blob that stores vendor-specific runtime state data.
      """
      runtimeInfo: _typing.Optional[DistributedVirtualPort.RuntimeInfo] = None
      stats: PortStatistics
      vendorSpecificState: list[KeyedOpaqueBlob] = []

   key: str
   config: DistributedVirtualPort.ConfigInfo
   dvsUuid: str
   portgroupKey: _typing.Optional[str] = None
   proxyHost: _typing.Optional[pyVmomi.vim.HostSystem] = None
   connectee: _typing.Optional[PortConnectee] = None
   conflict: bool
   conflictPortKey: _typing.Optional[str] = None
   state: _typing.Optional[DistributedVirtualPort.State] = None
   connectionCookie: _typing.Optional[int] = None
   lastStatusChange: _datetime.datetime
   hostLocalPort: _typing.Optional[bool] = None
   externalId: _typing.Optional[str] = None
   segmentPortId: _typing.Optional[str] = None


class DistributedVirtualPortgroup(pyVmomi.vim.Network):
   """
   The `pyVmomi.vim.dvs.DistributedVirtualPortgroup` managed object
   defines how hosts and virtual machines connect to a network.
   
   A distributed virtual portgroup specifies `pyVmomi.vim.dvs.DistributedVirtualPort`
   configuration options for the ports on a `pyVmomi.vim.DistributedVirtualSwitch`.
   A portgroup also represents a `pyVmomi.vim.Network` entity in the datacenter.
   - To configure host access by portgroup, set the portgroup in the host virtual NIC specification
     (`pyVmomi.vim.host.VirtualNic.Specification`.`pyVmomi.vim.host.VirtualNic.Specification.portgroup`).
   - To configure virtual machine access by portgroup, set the portgroup
     in the virtual Ethernet card backing
     (`pyVmomi.vim.vm.device.VirtualEthernetCard`.`pyVmomi.vim.vm.device.VirtualDevice.backing`.`pyVmomi.vim.vm.device.VirtualEthernetCard.DistributedVirtualPortBackingInfo.port`.`pyVmomi.vim.dvs.PortConnection.portgroupKey`).
     
   When you use a portgroup for network access, the Server will create a port according
   to `pyVmomi.vim.dvs.DistributedVirtualPortgroup.config`.`pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo.type`.
   """
   class PortgroupType(pyVmomi.VmomiSupport.Enum):
      """
      The `pyVmomi.vim.dvs.DistributedVirtualPortgroup.PortgroupType` enum defines
      the distributed virtual portgroup types
      (`pyVmomi.vim.dvs.DistributedVirtualPortgroup`.`pyVmomi.vim.dvs.DistributedVirtualPortgroup.config`.`pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo.type`).
      
      Early binding specifies a static set of ports that are created
      when you create the distributed virtual portgroup. An ephemeral portgroup uses dynamic
      ports that are created when you power on a virtual machine.
      
      Attributes:
          earlyBinding: A free `pyVmomi.vim.dvs.DistributedVirtualPort` will be selected and assigned to
              a `pyVmomi.vim.VirtualMachine` when the virtual machine is reconfigured to
              connect to the portgroup.
          lateBinding: A free `pyVmomi.vim.dvs.DistributedVirtualPort` will be selected and
              assigned to a `pyVmomi.vim.VirtualMachine` when the virtual machine is
              powered on.
          ephemeral: A `pyVmomi.vim.dvs.DistributedVirtualPort` will be created and assigned to a
              `pyVmomi.vim.VirtualMachine` when the virtual machine is powered on, and will
              be deleted when the virtual machine is powered off.
              
              An ephemeral portgroup has
              no limit on the number of ports that can be a part of this portgroup.
              In cases where the vCenter Server is unavailable the host can
              create conflict ports in this portgroup to be used by a virtual machine
              at power on.
      """
      earlyBinding: _typing.ClassVar['DistributedVirtualPortgroup.PortgroupType'] = 'earlyBinding'
      lateBinding: _typing.ClassVar['DistributedVirtualPortgroup.PortgroupType'] = 'lateBinding'
      ephemeral: _typing.ClassVar['DistributedVirtualPortgroup.PortgroupType'] = 'ephemeral'

   class BackingType(pyVmomi.VmomiSupport.Enum):
      """
      The `pyVmomi.vim.dvs.DistributedVirtualPortgroup.BackingType` enum defines
      the distributed virtual portgroup backing type.
      
      Attributes:
          standard: The portgroup is created by vCenter.
          nsx: The portgroup is created by NSX manager.
              
              For NSX backing type, We only support ephemeral portgroup type.
              If `pyVmomi.vim.dvs.DistributedVirtualPortgroup.PortgroupType` is
              ephemeral, A `pyVmomi.vim.dvs.DistributedVirtualPort` will be
              dynamically created by NSX when the virtual machine is reconfigured
              to connect to the portgroup.
      """
      standard: _typing.ClassVar['DistributedVirtualPortgroup.BackingType'] = 'standard'
      nsx: _typing.ClassVar['DistributedVirtualPortgroup.BackingType'] = 'nsx'

   class PortgroupPolicy(pyVmomi.vmodl.DynamicData):
      """
      The DistributedVirtualPortgroup policies.
      
      This field is not applicable
      when queried directly against an ESX host.
      
      Attributes:
          blockOverrideAllowed: Allow the `pyVmomi.vim.dvs.DistributedVirtualPort.Setting.blocked` setting
              of an individual port to override the setting in
              `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo.defaultPortConfig` of
              a portgroup.
          shapingOverrideAllowed: Allow the `pyVmomi.vim.dvs.DistributedVirtualPort.Setting.inShapingPolicy` or
              `pyVmomi.vim.dvs.DistributedVirtualPort.Setting.outShapingPolicy` settings
              of an individual port to override the setting in
              `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo.defaultPortConfig` of
              a portgroup.
          vendorConfigOverrideAllowed: Allow the `pyVmomi.vim.dvs.DistributedVirtualPort.Setting.vendorSpecificConfig`
              setting of an individual port to override the setting in
              `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo.defaultPortConfig` of
              a portgroup.
          livePortMovingAllowed: Allow a live port to be moved in and out of the portgroup.
          portConfigResetAtDisconnect: If true, reset the port network setting back to the portgroup setting
              (thus removing the per-port setting) when the port is disconnected from
              the connectee.
          networkResourcePoolOverrideAllowed: Allow the setting of
              `pyVmomi.vim.dvs.DistributedVirtualPort.Setting.networkResourcePoolKey` of an
              individual port to override the setting in
              `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo.defaultPortConfig`
              of a portgroup.
          trafficFilterOverrideAllowed: Allow the setting of
              `pyVmomi.vim.dvs.DistributedVirtualPort.Setting.filterPolicy`,
              for an individual port to override the setting in
              `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo.defaultPortConfig` of
              a portgroup.
      """
      blockOverrideAllowed: bool
      shapingOverrideAllowed: bool
      vendorConfigOverrideAllowed: bool
      livePortMovingAllowed: bool
      portConfigResetAtDisconnect: bool
      networkResourcePoolOverrideAllowed: _typing.Optional[bool] = None
      trafficFilterOverrideAllowed: _typing.Optional[bool] = None

   class MetaTagName(pyVmomi.VmomiSupport.Enum):
      """
      The meta tag names recognizable in the
      `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo.portNameFormat` string.
      
      Attributes:
          dvsName: This tag will be expanded to the name of the switch.
          portgroupName: This tag will be expanded to the name of the portgroup.
          portIndex: This tag will be expanded to the current index of the port.
      """
      dvsName: _typing.ClassVar['DistributedVirtualPortgroup.MetaTagName'] = 'dvsName'
      portgroupName: _typing.ClassVar['DistributedVirtualPortgroup.MetaTagName'] = 'portgroupName'
      portIndex: _typing.ClassVar['DistributedVirtualPortgroup.MetaTagName'] = 'portIndex'

   class SubnetAddressInfo(pyVmomi.vmodl.DynamicData):
      """
      The subnet address(es) used for the port group.
      
      Attributes:
          cidr: A list of subnet addresses in CIDR format (IPv4 or IPv6).
              
              In ConfigSpec: unset indicates removing the current CIDR(s).
              In ConfigInfo: unset indicates no CIDR is assigned to the port group.
      
      Since: vSphere API Release 9.1.0.0
      """
      cidr: list[str] = []

   class NsxConfig(pyVmomi.vmodl.DynamicData):
      """
      The NSX-related configurations.
      
      Attributes:
          vlanIdExtended: The VLAN ID this NSX port group extends to.
              
              If unset, this NSX port group doesn't extend to any VLAN.
          subnetAddresses: The subnet address(es) assigned to this NSX port group.
              
              If unset, no subnet address is configured.
          spanIds: The span IDs of the subnet.
              
              It can only be set when the `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigSpec.subnetId` is set. If unset, all the hosts
              join the corresponding transport zone can access the subnet.
      
      Since: vSphere API Release 9.1.0.0
      """
      vlanIdExtended: _typing.Optional[int] = None
      subnetAddresses: _typing.Optional[DistributedVirtualPortgroup.SubnetAddressInfo] = None
      spanIds: list[str] = []

   class ConfigSpec(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigSpec`
      data object contains configuration data for a
      `pyVmomi.vim.dvs.DistributedVirtualPortgroup`.
      
      Use the
      `pyVmomi.vim.dvs.DistributedVirtualPortgroup.reconfigure`
      method to apply the configuration to the portgroup.
      
      Attributes:
          configVersion: Version string of the configuration that this spec is trying to
              change.
              
              This property is required in reconfiguring a portgroup and
              should be set to the same value as the
              `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo.configVersion`.
              This property is ignored in creating a portgroup if set.
          name: Name of the portgroup.
          numPorts: Number of ports in the portgroup.
              
              Setting this number larger than the
              number of existing ports in the portgroup causes new ports to
              be added to the portgroup to meet the number. Setting this property
              smaller than the number of existing ports deletes the free ports
              from the portgroup. If the number cannot be met by deleting free ports,
              a fault is raised. If new ports are added to the portgroup, they
              are also added to the switch. For portgroups of type ephemeral this
              property is ignored.
          portNameFormat: Format of the name of the ports when ports are created in the portgroup.
              
              For details see `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo.portNameFormat`.
          defaultPortConfig: Default network setting for all the ports in the portgroup.
          description: Description of the portgroup.
          type: Type of portgroup.
              
              See
              `pyVmomi.vim.dvs.DistributedVirtualPortgroup`.`pyVmomi.vim.dvs.DistributedVirtualPortgroup.PortgroupType`
              for possible values.
          backingType: Backing type of portgroup.
              
              See
              `pyVmomi.vim.dvs.DistributedVirtualPortgroup`.`pyVmomi.vim.dvs.DistributedVirtualPortgroup.BackingType`
              for possible values.
              The default value is \"standard\"
          scope: Eligible entities that can connect to the port.
              
              See
              `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo`.`pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo.scope`.
          policy: Portgroup policy.
          vendorSpecificConfig: Opaque binary blob that stores vendor specific configuration.
          autoExpand: If set to true, this property ignores the limit on the number of ports in the
              portgroup.
              
              When a Virtual Machine/Host tries to connect to the portgroup and there
              are no free ports available in the portgroup, new ports will be automatically
              added to the portgroup. The flag is currently supported only for static portgroups.
              
              Setting this property to true makes the portgroup a potential candidate for
              auto-shrink. Once the portgroup has auto-expanded then its disconnected ports are
              likely to be deleted automatically, as a part of auto-shrink step, if there are more
              than certain number of free ports. If the portgroup never auto-expanded, then it will
              never lose any free ports.
          vmVnicNetworkResourcePoolKey: The key of virtual NIC network resource pool to be associated with a portgroup.
              
              Setting this property to \"-1\", would mean that this portgroup
              is not associated with any virtual NIC network resource pool.
          transportZoneUuid: The UUID of transport zone to be associated with a NSX portgroup.
          transportZoneName: The name of transport zone to be associated with a NSX portgroup.
          logicalSwitchUuid: The logical switch UUID, which is used by NSX portgroup
          segmentId: The segment ID of logical switch
          subnetId: The subnet ID of logical switch
              
              Since: vSphere API Release 9.0.0.0
          nsxConfig: The NSX-related configurations.
              
              Update semantics: This structure uses an override model: the provided
              values replace existing ones, and omitted or unset properties are cleared.
              
              Since: vSphere API Release 9.1.0.0
      """
      configVersion: _typing.Optional[str] = None
      name: _typing.Optional[str] = None
      numPorts: _typing.Optional[int] = None
      portNameFormat: _typing.Optional[str] = None
      defaultPortConfig: _typing.Optional[DistributedVirtualPort.Setting] = None
      description: _typing.Optional[str] = None
      type: _typing.Optional[str] = None
      backingType: _typing.Optional[str] = None
      scope: list[pyVmomi.vim.ManagedEntity] = []
      policy: _typing.Optional[DistributedVirtualPortgroup.PortgroupPolicy] = None
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []
      autoExpand: _typing.Optional[bool] = None
      vmVnicNetworkResourcePoolKey: _typing.Optional[str] = None
      transportZoneUuid: _typing.Optional[str] = None
      transportZoneName: _typing.Optional[str] = None
      logicalSwitchUuid: _typing.Optional[str] = None
      segmentId: _typing.Optional[str] = None
      subnetId: _typing.Optional[str] = None
      nsxConfig: _typing.Optional[DistributedVirtualPortgroup.NsxConfig] = None

   class ConfigInfo(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo` data object defines
      the configuration of a `pyVmomi.vim.dvs.DistributedVirtualPortgroup`.
      
      Attributes:
          key: Key of the portgroup.
          name: Name of the portgroup.
          numPorts: Number of ports in the portgroup.
          distributedVirtualSwitch: Distributed virtual switch that the portgroup is defined on.
              
              This property should always be set unless the user's setting
              does not have System.Read privilege on the object referred to
              by this property.
          defaultPortConfig: Common network setting for all the ports in the portgroup.
          description: Description of the portgroup.
          type: Type of portgroup.
              
              See
              `pyVmomi.vim.dvs.DistributedVirtualPortgroup`.`pyVmomi.vim.dvs.DistributedVirtualPortgroup.PortgroupType`
              for possible values.
          backingType: Backing type of portgroup.
              
              See
              `pyVmomi.vim.dvs.DistributedVirtualPortgroup`.`pyVmomi.vim.dvs.DistributedVirtualPortgroup.BackingType`
              for possible values.
              The default value is \"standard\"
          policy: Portgroup policy.
          portNameFormat: If set, a name will be automatically generated based on this format
              string for a port when it is created in or moved into the portgroup.
              
              The format string can contain meta tags that will be resolved
              to the corresponding values in generating a name, if applicable for
              the port at the time of name generation.
              
              To insert a meta tag in the format string,
              enclose the names defined as meta tag names inside angle brackets.
              See `pyVmomi.vim.dvs.DistributedVirtualPortgroup.MetaTagName` for a list of
              currently available meta tags. For example,
              \"redNetwork-<portIndex>\" and \"<dvsName>-pnic<portIndex>\"
              result in generated port names like \"redNetwork-2\" and \"switch-pnic3\".
              
              If a meta tag is recognized, but there is no applicable value, the tag
              will be expanded to empty string. If an arbitrary name appears inside
              a \"<>\" pair and is not recognized as one of the defined meta tags,
              the substring is treated as-is and appear unchanged in the generated name.
              
              To prevent a meta tag from being expanded, prefix the meta tag with a
              '\\' (backslash). For example, the format string \"abc\\<portIndex>def\"
              results in the generated port name \"abc<portIndex>def\".
          scope: Eligible entities that can connect to the portgroup.
              
              If unset,
              there is no restriction on which entity can connect to the portgroup.
              If set, only the entities in the specified list or their child
              entities are allowed to connect to the portgroup. If scopes are
              defined at both port and portgroup level, they are taken as an \"AND\"
              relationship. If such a relationship doesn't make sense, the
              reconfigure operation will raise an exception.
          vendorSpecificConfig: Opaque binary blob that stores vendor specific configuration.
          configVersion: Configuration version number.
          autoExpand: If set to true, this property ignores the limit on the number of ports in the
              portgroup.
              
              When a Virtual Machine/Host tries to connect to the portgroup and there
              are no free ports available in the portgroup, new ports will be automatically
              added to the portgroup. The flag is currently supported only for static portgroups.
              
              When this property is set to true, the portgroup becomes a potential candidate for
              auto-shrink. Once the portgroup has auto-expanded then its disconnected ports are
              likely to be deleted automatically, as a part of auto-shrink step, if there are more
              than certain number of free ports. If the portgroup never auto-expanded, then it will
              never lose any free ports.
          vmVnicNetworkResourcePoolKey: The key of virtual NIC network resource pool to be associated with a portgroup.
              
              The default value for this property is unset, indicating that
              this portgroup is not associated with any virtual NIC network resource pool.
              To clear the value of this property and revert to unset, set the
              `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigSpec.vmVnicNetworkResourcePoolKey`
              to \"-1\" in an update operation.
          uplink: Indicates whether the portgroup is an uplink portroup.
          transportZoneUuid: The UUID of transport zone to be associated with a NSX portgroup.
          transportZoneName: The name of transport zone to be associated with a NSX portgroup.
          logicalSwitchUuid: The logical switch UUID, which is used by NSX portgroup
          segmentId: The segment ID of logical switch
          subnetId: ID of the VPC Subnet when the DVPG is backed by a VPC Subnet
              
              Since: vSphere API Release 9.0.0.0
          nsxConfig: The NSX-related configurations.
              
              Since: vSphere API Release 9.1.0.0
      """
      key: str
      name: str
      numPorts: int
      distributedVirtualSwitch: _typing.Optional[pyVmomi.vim.DistributedVirtualSwitch] = None
      defaultPortConfig: _typing.Optional[DistributedVirtualPort.Setting] = None
      description: _typing.Optional[str] = None
      type: str
      backingType: _typing.Optional[str] = None
      policy: DistributedVirtualPortgroup.PortgroupPolicy
      portNameFormat: _typing.Optional[str] = None
      scope: list[pyVmomi.vim.ManagedEntity] = []
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []
      configVersion: _typing.Optional[str] = None
      autoExpand: _typing.Optional[bool] = None
      vmVnicNetworkResourcePoolKey: _typing.Optional[str] = None
      uplink: _typing.Optional[bool] = None
      transportZoneUuid: _typing.Optional[str] = None
      transportZoneName: _typing.Optional[str] = None
      logicalSwitchUuid: _typing.Optional[str] = None
      segmentId: _typing.Optional[str] = None
      subnetId: _typing.Optional[str] = None
      nsxConfig: _typing.Optional[DistributedVirtualPortgroup.NsxConfig] = None

   class Problem(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.dvs.DistributedVirtualPortgroup.Problem`
      data object defines the error while executing NSX port group operations.
      
      Attributes:
          logicalSwitchUuid: The problematic logical switch UUID
          fault: The failure reason for each problematic logical switch UUID
      """
      logicalSwitchUuid: str
      fault: pyVmomi.vmodl.MethodFault

   class NsxPortgroupOperationResult(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.dvs.DistributedVirtualPortgroup.NsxPortgroupOperationResult`
      data object defines the result of NSX port group operations, including
      create, reconfigure and delete.
      
      Attributes:
          portgroups: The management object of NSX port group.
              
              For add operation, it indicates the port groups created successfully.
              For reconfigure operation, it indicates the port groups updated
              successfully.
              For delete operation, it indicates the port groups failed deleted.
          problems: The failed port group operation details.
      """
      portgroups: list[DistributedVirtualPortgroup] = []
      problems: list[DistributedVirtualPortgroup.Problem] = []

   @property
   def key(self) -> str:
      """Generated UUID of the portgroup."""
      ...
   @property
   def config(self) -> DistributedVirtualPortgroup.ConfigInfo:
      """Configuration of the portgroup."""
      ...
   @property
   def portKeys(self) -> list[str]:
      """Port keys for the set of ports in the portgroup."""
      ...

   def Reconfigure(self, spec: DistributedVirtualPortgroup.ConfigSpec) -> pyVmomi.vim.Task:
      """
      Reconfigures one or more distributed virtual portgroups.
      
      You can use this method to set portgroup properties or
      to reset the portgroup to a previous state.
      
      Reconfiguring a Standard Distributed Virtual Portgroup
      
      To reconfigure a `pyVmomi.vim.dvs.DistributedVirtualPortgroup`,
      use a `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigSpec`
      to set the portgroup properties.
      
      Reconfiguring a Portgroup Associated With a VMware Distributed Virtual Switch
      
      If you use a `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch`,
      you can perform the following portgroup reconfiguration:
      - Use a `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigSpec`
        to set the portgroup properties.
      - Use the `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigSpec`
        returned by `pyVmomi.vim.dvs.DistributedVirtualPortgroup.rollback`
        to reset the portgroup to a previous state.
        
      The following privileges are required to reconfigure a portgroup.
      - DVPortgroup.PolicyOp if you are changing the policy of the portgroup.
      - DVPortgroup.ScopeOp if you are changing the scope of the portgroup.
      - DVPortgroup.Modify for anything else.
      
      Args:
          spec: Configuration data for the portgroup.
      
      Raises:
          pyVmomi.vim.fault.DvsFault: if spec is not valid.
          pyVmomi.vim.fault.ConcurrentAccess: A ConcurrentAccess fault is thrown when an operation
              fails because another operation has modified the
              datastructure.
              
              For non-transactional operations, such as a recursive
              delete of a subtree of the inventory, the operation might
              fail with ConcurrentAccess if another thread has added
              a new entity to the hierarchy.
          pyVmomi.vim.fault.DuplicateName: A DuplicateName exception is thrown because a name already exists
              in the same name space.
          pyVmomi.vim.fault.InvalidName: A InvalidName fault is thrown when the name
              contains an invalid character or format.
      """
      ...
   def Rollback(self, entityBackup: _typing.Optional[EntityBackup.Config]) -> pyVmomi.vim.Task:
      """
      This method determines if the portgroup configuration has changed.
      
      If it has changed, the method returns a
      `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigSpec`.
      Use the `pyVmomi.vim.dvs.DistributedVirtualPortgroup.reconfigure` method
      to apply the rollback configuration to the portgroup. You can use the
      rollback method only on a portgroup that is associated with a
      `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch`.
      - If you specify the `entityBackup` parameter, the returned
        configuration specification represents the exported portgroup configuration.
        If the `entityBackup` matches the current portgroup
        configuration, the method does not return a configuration specification.
      - If `entityBackup` is not specified, the returned configuration
        specification represents a previous state of the portgroup, if available.
        When you use a VMware distributed virtual switch, each time you reconfigure
        the switch, the Server saves the switch configuration before applying the updates.
        If the vCenter Server is restarted, the saved configuration is not preserved
        and the method does not return a configuration specification.
        
      To use the rollback method, you must have the DVPortgroup.Read privilege.
      
      Args:
          entityBackup: The backup of Distributed Virtual PortGroup entity.
      
      Raises:
          pyVmomi.vim.fault.DvsFault: if operation fails.
          pyVmomi.vim.fault.RollbackFailure: if there is no configuration specified in entityBackup and
              the previous configuration does not exist either
      """
      ...


class DistributedVirtualPortgroupInfo(pyVmomi.vmodl.DynamicData):
   """
   This class describes a DistributedVirtualPortgroup that a device backing
   can be attached to.
   
   Attributes:
       switchName: The name of the switch.
       switchUuid: The UUID of the switch.
       portgroupName: The name of the portgroup.
       portgroupKey: The key of the portgroup.
       portgroupType: The type of portgroup.
           
           See `pyVmomi.vim.dvs.DistributedVirtualPortgroup.PortgroupType`
       uplinkPortgroup: Whether this portgroup is an uplink portgroup.
       portgroup: The portgroup.
       networkReservationSupported: Indicates whether network bandwidth reservation is supported on
           the portgroup
       backingType: Backing type of portgroup.
           
           See
           `pyVmomi.vim.dvs.DistributedVirtualPortgroup`.`pyVmomi.vim.dvs.DistributedVirtualPortgroup.BackingType`
           for possible values.
           The default value is \"standard\".
       logicalSwitchUuid: The logical switch UUID, which is used by NSX portgroup
       segmentId: The segment ID of logical switch, which is used by NSX portroup
       subnetId: The subnet ID of logical switch
           
           Since: vSphere API Release 9.0.0.0
   """
   switchName: str
   switchUuid: str
   portgroupName: str
   portgroupKey: str
   portgroupType: str
   uplinkPortgroup: bool
   portgroup: DistributedVirtualPortgroup
   networkReservationSupported: _typing.Optional[bool] = None
   backingType: _typing.Optional[str] = None
   logicalSwitchUuid: _typing.Optional[str] = None
   segmentId: _typing.Optional[str] = None
   subnetId: _typing.Optional[str] = None


class DistributedVirtualPortgroupSelection(pyVmomi.vim.SelectionSet):
   """
   Class to specify selection criteria of list of vNetwork Distributed Portgroups.
   
   Attributes:
       dvsUuid: vSphere Distributed Switch uuid
       portgroupKey: List of vNetwork Distributed Portgroup keys
   """
   dvsUuid: str
   portgroupKey: list[str] = []


class DistributedVirtualSwitchInfo(pyVmomi.vmodl.DynamicData):
   """
   This class describes a DistributedVirtualSwitch that a device backing
   can attached to its ports.
   
   Attributes:
       switchName: The name of the switch.
       switchUuid: The UUID of the switch.
       distributedVirtualSwitch: The switch.
       networkReservationSupported: Indicates whether network bandwidth reservation is supported on
           the switch
   """
   switchName: str
   switchUuid: str
   distributedVirtualSwitch: pyVmomi.vim.DistributedVirtualSwitch
   networkReservationSupported: _typing.Optional[bool] = None


class DistributedVirtualSwitchManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   The `pyVmomi.vim.dvs.DistributedVirtualSwitchManager` provides methods
   that support the following operations:
   - Backup and restore operations for `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch`
     and associated `pyVmomi.vim.dvs.DistributedVirtualPortgroup` managed objects.
   - Query operations for information about portgroups and distributed
     virtual switches.
   - Distributed virtual switch configuration update operations.
   """
   class PhysicalNicsList(pyVmomi.vmodl.DynamicData):
      """
      This class is used to store valid PhysicalNics for a specific host
      
      Since: vSphere API Release 8.0.0.1
      """
      host: pyVmomi.vim.HostSystem
      physicalNics: list[pyVmomi.vim.host.PhysicalNic] = []

   class DvsConfigTarget(pyVmomi.vmodl.DynamicData):
      """
      Configuration specification for a DistributedVirtualSwitch or
      DistributedVirtualPortgroup.
      
      Attributes:
          distributedVirtualPortgroup: List of any DistributedVirtualPortgroup available for host Virtual NIC connection.
          distributedVirtualSwitch: List of any DistributedVirtualSwitch available for host Virtual NIC connection.
      """
      distributedVirtualPortgroup: list[DistributedVirtualPortgroupInfo] = []
      distributedVirtualSwitch: list[DistributedVirtualSwitchInfo] = []

   class CompatibilityResult(pyVmomi.vmodl.DynamicData):
      """
      This is the return type for the checkCompatibility method.
      
      This object
      has a host property and optionally a fault which would
      be populated only if that host is not compatible with a given dvsProductSpec.
      If the host is compatible then the error property would be unset.
      
      Attributes:
          host: The host for which results are annotated.
              
              The whole object will be
              filtered out if the caller did not have view permissions on the
              host entity.
          error: This property contains the faults that makes the host not compatible
              with a given DvsProductSpec.
              
              For example, a host might not be compatible
              because it's an older version of ESX that doesn't support DVS.
      """
      host: pyVmomi.vim.HostSystem
      error: list[pyVmomi.vmodl.MethodFault] = []

   class HostContainer(pyVmomi.vmodl.DynamicData):
      """
      Check host compatibility for all hosts in the container.
      
      If the recursive
      flag is true, then check hosts at all levels within this container, otherwise
      check only at the container level. In case of container being a `pyVmomi.vim.Datacenter`,
      the recursive flag is applied to its HostFolder.
      
      Attributes:
          container: Check compatibility of hosts in this container.
              
              The supported container
              types are Datacenter, Folder, and ComputeResource.
          recursive: If true, include hosts of all levels in the hierarchy with
              container as root of the tree.
              
              In case of container being a `pyVmomi.vim.Datacenter`,
              the recursive flag is applied to its HostFolder.
      """
      container: pyVmomi.vim.ManagedEntity
      recursive: bool

   class HostDvsFilterSpec(pyVmomi.vmodl.DynamicData):
      """
      Base class for filters to check host compatibility.
      
      Attributes:
          inclusive: If this flag is true, then the filter returns the hosts in the
              `pyVmomi.vim.dvs.DistributedVirtualSwitchManager.HostContainer`
              that satisfy the criteria specified by this filter, otherwise
              it returns hosts that don't meet the criteria.
      """
      inclusive: bool

   class HostArrayFilter(DistributedVirtualSwitchManager.HostDvsFilterSpec):
      """
      Check host compatibility against all hosts specified in the array.
      
      Attributes:
          host: List of hosts to consider.
      """
      host: list[pyVmomi.vim.HostSystem] = []

   class HostContainerFilter(DistributedVirtualSwitchManager.HostDvsFilterSpec):
      """
      Check host compatibility against all hosts in this
      `pyVmomi.vim.dvs.DistributedVirtualSwitchManager.HostContainer`
      
      Attributes:
          hostContainer: Container of hosts that are part of the filter.
      """
      hostContainer: DistributedVirtualSwitchManager.HostContainer

   class HostDvsMembershipFilter(DistributedVirtualSwitchManager.HostDvsFilterSpec):
      """
      Check host compatibility against all hosts in the DVS (or not in the DVS if
      inclusive flag in base class is false)
      """
      distributedVirtualSwitch: pyVmomi.vim.DistributedVirtualSwitch

   class DvsProductSpec(pyVmomi.vmodl.DynamicData):
      """
      This class is used to specify ProductSpec for the DVS.
      
      The two properties are
      strictly mutually exclusive. If both properties are set, then
      an InvalidArgument fault would be thrown.
      
      Attributes:
          newSwitchProductSpec: The ProductSpec for new DVS
          distributedVirtualSwitch: Get ProductSpec from the existing DVS
      """
      newSwitchProductSpec: _typing.Optional[ProductSpec] = None
      distributedVirtualSwitch: _typing.Optional[pyVmomi.vim.DistributedVirtualSwitch] = None

   class ImportResult(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.dvs.DistributedVirtualSwitchManager.ImportResult`
      data object represents the results of a
      `pyVmomi.vim.dvs.DistributedVirtualSwitchManager.importEntity`
      operation.
      
      It contains lists of the switches and portgroups
      that were created. It also contains a list of faults
      that occurred during the operation.
      
      Attributes:
          distributedVirtualSwitch: List of distributed virtual switches.
          distributedVirtualPortgroup: List of distributed virtual portgroups.
          importFault: Faults that occurred on the entities during the import operation.
      """
      distributedVirtualSwitch: list[pyVmomi.vim.DistributedVirtualSwitch] = []
      distributedVirtualPortgroup: list[DistributedVirtualPortgroup] = []
      importFault: list[pyVmomi.vim.fault.ImportOperationBulkFault.FaultOnImport] = []

   class SpanInfo(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.dvs.DistributedVirtualSwitchManager.SpanInfo`
      data object defines the configuration of a span.
      
      A span is referenced by a `pyVmomi.vim.dvs.DistributedVirtualPortgroup`
      managed by NSX. Only the hosts in the cluster of the span can access the
      DVPG
      
      Attributes:
          ID: The policy path of the span in NSX
          clusters: The clusters in this span
              The array of clusters included in the span definition.
          exclusive: Whether the span is exclusive
              A boolean value indicating whether the span is in exclusive
              or non-exclusive mode.
      
      Since: vSphere API Release 9.1.0.0
      """
      ID: str
      clusters: list[pyVmomi.vim.ClusterComputeResource] = []
      exclusive: _typing.Optional[bool] = None

   def QuerySupportedSwitchSpec(self, recommended: _typing.Optional[bool]) -> list[ProductSpec]:
      """
      This operation returns a list of switch product specifications that
      are supported by the vCenter Server.
      
      Args:
          recommended: If set to true, return only the recommended versions.
              If set to false, return only the not recommended versions.
              If unset, return all supported versions.
      """
      ...
   def QuerySupportedNetworkOffloadSpec(self, switchProductSpec: ProductSpec) -> list[NetworkOffloadSpec]:
      """
      This operation returns a list of network offload specifications that are
      compatible with the given DistributedVirtualSwitch product specification.
      
      Args:
          switchProductSpec: The productSpec of a
              `pyVmomi.vim.DistributedVirtualSwitch`.
      
      Since: vSphere API Release 8.0.0.1
      """
      ...
   def QueryCompatibleVmnicsFromHosts(self, hosts: list[pyVmomi.vim.HostSystem], dvs: pyVmomi.vim.DistributedVirtualSwitch) -> list[DistributedVirtualSwitchManager.PhysicalNicsList]:
      """
      This operation returns a list of vmnics which are compatible
      with the given DistributedVirtualSwitch product specification.
      
      Args:
          hosts: The array of hosts on which the query is to be made to
              fetch valid PhysicalNics on each host.
          dvs: The distributed virtual switch on which the query is to be
              made.
      
      Since: vSphere API Release 8.0.0.1
      """
      ...
   def QueryCompatibleHostForNewDvs(self, container: pyVmomi.vim.ManagedEntity, recursive: bool, switchProductSpec: _typing.Optional[ProductSpec]) -> list[pyVmomi.vim.HostSystem]:
      """
      This operation returns a list of hosts that are compatible with
      the given DistributedVirtualSwitch product specification.
      
      Args:
          container: Where to look for hosts. Supported types of objects for
              this parameter are `pyVmomi.vim.Datacenter`,
              `pyVmomi.vim.ComputeResource` and `pyVmomi.vim.Folder`.
          recursive: Whether to search for hosts in the subfolders,
              if applicable. In the case when container is a `pyVmomi.vim.Datacenter`,
              the recursive flag is applied to its HostFolder.
          switchProductSpec: The productSpec of a `pyVmomi.vim.DistributedVirtualSwitch`.
              If not set, it is assumed to be the default one used for
              DistributedVirtualSwitch creation.
      """
      ...
   def QueryCompatibleHostForExistingDvs(self, container: pyVmomi.vim.ManagedEntity, recursive: bool, dvs: pyVmomi.vim.DistributedVirtualSwitch) -> list[pyVmomi.vim.HostSystem]:
      """
      This operation returns a list of hosts that are compatible with
      the given DistributedVirtualSwitch product specification.
      
      Args:
          container: Where to look for hosts. Supported types of objects for
              this parameter are `pyVmomi.vim.Datacenter`,
              `pyVmomi.vim.ComputeResource` and `pyVmomi.vim.Folder`.
          recursive: Whether to search for hosts in the subfolders,
              if applicable. In the case when container is a `pyVmomi.vim.Datacenter`,
              the recursive flag is applied to its HostFolder.
          dvs: Search the host based on the specification published in the
              `pyVmomi.vim.DistributedVirtualSwitch.Capability.compatibleHostComponentProductInfo`
              of a `pyVmomi.vim.DistributedVirtualSwitch`. If not
              set, it is assumed to be the specification that a
              DistributedVirtualSwitch would have if it is created
              with the default `pyVmomi.vim.dvs.ProductSpec`.
      """
      ...
   def QueryCompatibleHostSpec(self, switchProductSpec: _typing.Optional[ProductSpec]) -> list[HostProductSpec]:
      """
      This operation returns a list of host product specifications that
      are compatible with the given DistributedVirtualSwitch product
      specification.
      
      Args:
          switchProductSpec: The productSpec of a `pyVmomi.vim.DistributedVirtualSwitch`.
              If not set, it is assumed to be the default one used for
              DistributedVirtualSwitch creation.
      """
      ...
   def QueryFeatureCapability(self, switchProductSpec: _typing.Optional[ProductSpec]) -> _typing.Optional[pyVmomi.vim.DistributedVirtualSwitch.FeatureCapability]:
      """
      This operation indicates which version-specific DVS features are
      available for the given DistributedVirtualSwitch product specification.
      
      Args:
          switchProductSpec: The productSpec of a `pyVmomi.vim.DistributedVirtualSwitch`.
              If not set, it is assumed to be the default one used for
              DistributedVirtualSwitch creation.
      """
      ...
   def QuerySwitchByUuid(self, uuid: str) -> _typing.Optional[pyVmomi.vim.DistributedVirtualSwitch]:
      """
      This operation returns a DistributedVirtualSwitch given a UUID.
      
      Raises:
          pyVmomi.vim.fault.NotFound: If a switch with the UUID doesn't exist.
      """
      ...
   def QueryDvsConfigTarget(self, host: _typing.Optional[pyVmomi.vim.HostSystem], dvs: _typing.Optional[pyVmomi.vim.DistributedVirtualSwitch]) -> DistributedVirtualSwitchManager.DvsConfigTarget:
      """
      This operation returns the DistributedVirtualSwitch or
      DistributedVirtualPortgroup configuration target on a host.
      
      Args:
          host: The host on which the query is to be made. If called
              directly on the host this parameter need not be specified.
          dvs: The distributed virtual switch on which the query is to be
              made. If unspecified the config target will encompass all the
              distributed virtual switches available on the host.
      """
      ...
   def CheckCompatibility(self, hostContainer: DistributedVirtualSwitchManager.HostContainer, dvsProductSpec: _typing.Optional[DistributedVirtualSwitchManager.DvsProductSpec], hostFilterSpec: list[DistributedVirtualSwitchManager.HostDvsFilterSpec]) -> list[DistributedVirtualSwitchManager.CompatibilityResult]:
      """
      This operation returns a list of compatibility results.
      
      Each compatibility result
      is an object that has a host property and optionally a fault which would
      be populated only if that host is not compatible with a given dvsProductSpec.
      All filters in hostFilerSpecs are ANDed to derive the intersection of hosts against
      which compatibility is checked. If caller did not have view privileges on the
      host entity in an element of the CompatibilityResult array, then that entire
      element would be removed from the CompatibilityResult array.
      Typical uses:
      - For the createDVS situation, hostFilterSpec is of type HostDvsFilterSpec and DvsProductSpec
        will have newSwitchProductSpec set.
      - For the Add-Host-To-DVS situation, you can use either HostDvsFilterSpec or
        HostDvsMembershipFilter with inclusive being false, and pass the DVS in DvsProductSpec.
      - For the Upgrade-DVS situation, you can use either HostDvsFilterSpec or
        HostDvsMembershipFilter with inclusive being true, and pass the new desired ProductSpec
        for DVS in newSwitchProductSpec.
      
      Args:
          hostContainer: The container of hosts on which we check the compatibility.
              This container can be a datacenter, folder, or computeResource.
              We can also include all the hosts in the hierarchy with container
              as root of the tree.
          dvsProductSpec: The productSpec of a DistributedVirtualSwitch. If not
              set, it is assumed to be the default one used for
              DistributedVirtualSwitch creation for current version.
          hostFilterSpec: The hosts against which to check compatibility. This is a
              filterSpec and users can use this to specify all hosts in a
              container (datacenter, folder, or computeResource), an array
              of hosts, or hosts that might or might not be a DVS member.
      """
      ...
   def RectifyHost(self, hosts: list[pyVmomi.vim.HostSystem]) -> pyVmomi.vim.Task:
      """
      Update the Distributed Switch configuration on the hosts to bring them in sync with the
      current configuration in vCenter Server.
      
      Args:
          hosts: The hosts to be rectified.
      
      Raises:
          pyVmomi.vim.fault.DvsFault: if operation fails on any host or if there are other update failures.
      """
      ...
   def ExportEntity(self, selectionSet: list[pyVmomi.vim.SelectionSet]) -> pyVmomi.vim.Task:
      """
      Export the configuration for entities specified in the
      `selectionSet` parameter.
      
      You can use this method only
      for a `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch` and its
      associated `pyVmomi.vim.dvs.DistributedVirtualPortgroup` objects.
      
      Use the `pyVmomi.vim.dvs.DistributedVirtualSwitchManager.importEntity` method to restore the entity
      to the state represented by the exported configuration.
      You can also use the exported configuration to create
      a new switch or portgroup.
      
      Args:
          selectionSet: The selection criteria for a set of
              entities to export the configuration.
      
      Raises:
          pyVmomi.vim.fault.NotFound: If entity in selectionSet doesn't exist.
          pyVmomi.vim.fault.BackupBlobWriteFailure: if failed to create backup config blob.
      """
      ...
   def ImportEntity(self, entityBackup: list[EntityBackup.Config], importType: str) -> pyVmomi.vim.Task:
      """
      Import the configuration of entities specified in
      `pyVmomi.vim.dvs.EntityBackup.Config`.
      
      You can restore the
      existing configuration to the state represented by the
      backup configuration. You can also use the backup
      configuration to create a new switch or portgroup.
      See `pyVmomi.vim.dvs.EntityBackup.ImportType`.
      
      Args:
          entityBackup: Configuration of one or more entities to be imported.
              The entity backup configuration is returned
              by the `pyVmomi.vim.dvs.DistributedVirtualSwitchManager.exportEntity` method.
          importType: Specifies whether to create a new configuration
              or restore a previous configuration. See `pyVmomi.vim.dvs.EntityBackup.ImportType` for valid values.
      
      Raises:
          pyVmomi.vim.fault.DvsFault: if operation fails on any host.
          pyVmomi.vim.fault.NotFound: If entity in `pyVmomi.vim.dvs.EntityBackup.Config.key` doesn't exist.
      """
      ...
   def LookupPortgroup(self, switchUuid: str, portgroupKey: str) -> _typing.Optional[DistributedVirtualPortgroup]:
      """
      Returns the portgroup identified by the key within the specified VDS
      identified by its UUID.
      
      Args:
          switchUuid: The UUID of the `pyVmomi.vim.DistributedVirtualSwitch`.
          portgroupKey: The key that identifies a
              `pyVmomi.vim.dvs.DistributedVirtualPortgroup`.
      
      Raises:
          pyVmomi.vim.fault.NotFound: If the portgroup for the specified inputs was not found.
      """
      ...
   def GetVpcNetworkSpan(self, spanId: _typing.Optional[str]) -> list[DistributedVirtualSwitchManager.SpanInfo]:
      """
      Get all VPC network spans.
      
      Each span is represented by a
      `pyVmomi.vim.dvs.DistributedVirtualSwitchManager.SpanInfo`. If no spans exist,
      the function may return an empty list.
      
      Args:
          spanId: If spanId is specified, returns the span with the given ID.
              If spanId is not specified, returns all spans currently configured in the
              system.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the span does not exist.
      
      Since: vSphere API Release 9.1.0.0
      """
      ...


class DistributedVirtualSwitchSelection(pyVmomi.vim.SelectionSet):
   """
   Class to specify selection criteria of vSphere Distributed Switch.
   
   Attributes:
       dvsUuid: vSphere Distributed Switch uuid
   """
   dvsUuid: str


class EntityBackup(pyVmomi.vmodl.DynamicData):
   """
   `pyVmomi.vim.dvs.EntityBackup` is an abstract data object that contains
   the related entity backup and restore elements for virtual distributed
   switches and virtual distributed portgroups.
   
   See the following elements:
   - `pyVmomi.vim.dvs.EntityBackup.Config`
   - `pyVmomi.vim.dvs.EntityBackup.ImportType`
   - `pyVmomi.vim.dvs.EntityBackup.EntityType`
   """
   class Config(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.dvs.EntityBackup.Config` data object
      contains `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch`
      or `pyVmomi.vim.dvs.DistributedVirtualPortgroup` backup
      configuration data produced by the
      `pyVmomi.vim.dvs.DistributedVirtualSwitchManager.exportEntity`
      method.
      
      It also contains properties that support
      `pyVmomi.vim.dvs.DistributedVirtualSwitchManager.importEntity`
      operations.
      
      A `pyVmomi.vim.dvs.DistributedVirtualSwitchManager.exportEntity` operation
      sets properties that identify the entity instance
      (`pyVmomi.vim.dvs.EntityBackup.Config.entityType`,
      `pyVmomi.vim.dvs.EntityBackup.Config.key`, and
      `pyVmomi.vim.dvs.EntityBackup.Config.name`) and
      inventory location (`pyVmomi.vim.dvs.EntityBackup.Config.container`).
      When you import a backup configuration, you can set
      the `key`, `name`, and `container`
      properties in accordance with the `importType`
      specified in the call to
      `pyVmomi.vim.dvs.DistributedVirtualSwitchManager.importEntity`.
      See `pyVmomi.vim.dvs.EntityBackup.ImportType`.
      
      Attributes:
          entityType: Type of the exported entity
              (`pyVmomi.vim.dvs.DistributedVirtualSwitchManager.exportEntity`).
              
              See `pyVmomi.vim.dvs.EntityBackup.EntityType`
              for valid values.
          configBlob: Opaque blob that contains the configuration of the entity.
          key: Unique identifier of the exported entity or the entity to be restored
              through an import operation.
              - If you are importing a virtual distributed switch and the import type is
                `applyToEntitySpecified`,
                set the `key` to
                `pyVmomi.vim.DistributedVirtualSwitch`.`pyVmomi.vim.DistributedVirtualSwitch.uuid`.
              - If you are importing a virtual distributed portgroup and the import type is
                `applyToEntitySpecified`,
                set the `key` to
                `pyVmomi.vim.dvs.DistributedVirtualPortgroup`.`pyVmomi.vim.dvs.DistributedVirtualPortgroup.key`.
                
              The Server ignores the key value when the import operation creates a new entity.
          name: Name of the exported entity or the entity to be restored with the backup configuration.
              
              If you are importing an entity and the import type is
              `applyToEntitySpecified`,
              the Server will use this value to rename the existing entity.
          container: Container for this entity.
              
              If `pyVmomi.vim.dvs.EntityBackup.Config.entityType` is \"distributedVirtualSwitch\",
              the container type is `pyVmomi.vim.Folder`. If `pyVmomi.vim.dvs.EntityBackup.Config.entityType`
              is \"distributedVirtualPortgroup\", the container type is
              `pyVmomi.vim.DistributedVirtualSwitch`.
          configVersion: Configuration version.
      """
      entityType: str
      configBlob: pyVmomi.VmomiSupport.binary
      key: _typing.Optional[str] = None
      name: _typing.Optional[str] = None
      container: _typing.Optional[pyVmomi.vim.ManagedEntity] = None
      configVersion: _typing.Optional[str] = None

   class EntityType(pyVmomi.VmomiSupport.Enum):
      """
      The `pyVmomi.vim.dvs.EntityBackup.EntityType` enum identifies
      the type of entity that was exported
      (`pyVmomi.vim.dvs.DistributedVirtualSwitchManager.exportEntity`).
      
      Attributes:
          distributedVirtualSwitch: Indicates the exported entity is a `pyVmomi.vim.DistributedVirtualSwitch`.
          distributedVirtualPortgroup: Indicates the exported entity is a `pyVmomi.vim.dvs.DistributedVirtualPortgroup`.
      """
      distributedVirtualSwitch: _typing.ClassVar['EntityBackup.EntityType'] = 'distributedVirtualSwitch'
      distributedVirtualPortgroup: _typing.ClassVar['EntityBackup.EntityType'] = 'distributedVirtualPortgroup'

   class ImportType(pyVmomi.VmomiSupport.Enum):
      """
      The `pyVmomi.vim.dvs.EntityBackup.ImportType` enum defines the import type for a
      `pyVmomi.vim.dvs.DistributedVirtualSwitchManager`.`pyVmomi.vim.dvs.DistributedVirtualSwitchManager.importEntity`
      operation.
      
      Attributes:
          createEntityWithNewIdentifier: Create the entity with new identifiers.
              
              Specify the
              `pyVmomi.vim.dvs.EntityBackup.Config`.`pyVmomi.vim.dvs.EntityBackup.Config.name` and
              `pyVmomi.vim.dvs.EntityBackup.Config`.`pyVmomi.vim.dvs.EntityBackup.Config.container`
              properties.
              
              The Server ignores any value for the
              `pyVmomi.vim.dvs.EntityBackup.Config`.`pyVmomi.vim.dvs.EntityBackup.Config.key`
              property.
          createEntityWithOriginalIdentifier: Recreate the entities with the original identifiers of the entity from which backup was created.
              
              The Server throws an exception if an entity with the same identifier already exists.
              This option will also add the host members to the `pyVmomi.vim.DistributedVirtualSwitch` and will
              try to get the virtual machine networking back with the same `pyVmomi.vim.dvs.DistributedVirtualPortgroup`.
              Specify a `pyVmomi.vim.Folder` as the
              `pyVmomi.vim.dvs.EntityBackup.Config`.`pyVmomi.vim.dvs.EntityBackup.Config.container`
              for `pyVmomi.vim.dvs.EntityBackup.Config`.`pyVmomi.vim.dvs.EntityBackup.Config.entityType`
              \"distributedVirtualSwitch\".
              
              The Server ignores any values for the
              `pyVmomi.vim.dvs.EntityBackup.Config`.`pyVmomi.vim.dvs.EntityBackup.Config.key` and
              `pyVmomi.vim.dvs.EntityBackup.Config`.`pyVmomi.vim.dvs.EntityBackup.Config.name`
              properties.
          applyToEntitySpecified: Apply the configuration specified in the
              `pyVmomi.vim.dvs.EntityBackup.Config`.`pyVmomi.vim.dvs.EntityBackup.Config.configBlob`
              property to the entity specified in the
              `pyVmomi.vim.dvs.EntityBackup.Config`.`pyVmomi.vim.dvs.EntityBackup.Config.entityType` and
              `pyVmomi.vim.dvs.EntityBackup.Config`.`pyVmomi.vim.dvs.EntityBackup.Config.key`
              properties.
              
              If you specify
              `pyVmomi.vim.dvs.EntityBackup.Config`.`pyVmomi.vim.dvs.EntityBackup.Config.name`,
              the Server uses the specified name to rename the entity.
              
              The Server ignores any value for the
              `pyVmomi.vim.dvs.EntityBackup.Config`.`pyVmomi.vim.dvs.EntityBackup.Config.container`
              property.
      """
      createEntityWithNewIdentifier: _typing.ClassVar['EntityBackup.ImportType'] = 'createEntityWithNewIdentifier'
      createEntityWithOriginalIdentifier: _typing.ClassVar['EntityBackup.ImportType'] = 'createEntityWithOriginalIdentifier'
      applyToEntitySpecified: _typing.ClassVar['EntityBackup.ImportType'] = 'applyToEntitySpecified'


class HostMember(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.dvs.HostMember` data object represents an ESXi host that
   is a member of a distributed virtual switch.
   
   When you add a host to a switch
   (`pyVmomi.vim.dvs.HostMember.ConfigSpec`.`pyVmomi.vim.dvs.HostMember.ConfigSpec.host`),
   the Server creates a proxy switch (`pyVmomi.vim.host.HostProxySwitch`).
   The host member object contains information about the configuration
   and state of the proxy.
   
   Attributes:
       runtimeState: Host member runtime state.
       config: Host member configuration.
       productInfo: Vendor, product and version information for the proxy switch
           module.
       uplinkPortKey: Port keys of the uplink ports created for the host member.
           
           These ports
           will be deleted after the host leaves the switch.
       status: The host DistributedVirtualSwitch component status.
           
           See
           `pyVmomi.vim.dvs.HostMember.HostComponentState` for valid values.
       statusDetail: Additional information regarding the host's current status.
   """
   class HostComponentState(pyVmomi.VmomiSupport.Enum):
      """
      Describes the state of the host proxy switch.
      
      Attributes:
          up: The host proxy switch is up and running.
          pending: The host proxy switch is waiting to be initialized.
          outOfSync: The proxy switch configuration is not the same as the
              distributed virtual switch configuration in the vCenter Server.
          warning: The host requires attention.
          disconnected: The host is disconnected or it is not responding.
          down: The host proxy is down.
      """
      up: _typing.ClassVar['HostMember.HostComponentState'] = 'up'
      pending: _typing.ClassVar['HostMember.HostComponentState'] = 'pending'
      outOfSync: _typing.ClassVar['HostMember.HostComponentState'] = 'outOfSync'
      warning: _typing.ClassVar['HostMember.HostComponentState'] = 'warning'
      disconnected: _typing.ClassVar['HostMember.HostComponentState'] = 'disconnected'
      down: _typing.ClassVar['HostMember.HostComponentState'] = 'down'

   class ConfigSpec(pyVmomi.vmodl.DynamicData):
      """
      Specification to create or reconfigure ESXi host membership
      in a `pyVmomi.vim.DistributedVirtualSwitch`.
      
      Attributes:
          operation: Host member operation type.
              
              See
              `pyVmomi.vim.ConfigSpecOperation` for valid values.
          host: Identifies a host member of a `pyVmomi.vim.DistributedVirtualSwitch`
              for a `pyVmomi.vim.Folder.createDistributedVirtualSwitch` or
              `pyVmomi.vim.DistributedVirtualSwitch`.`pyVmomi.vim.DistributedVirtualSwitch.reconfigure` operation.
          backing: Specifies the physical NICs to use as backing for the proxy switch
              on the host.
          maxProxySwitchPorts: Maximum number of ports allowed in the `pyVmomi.vim.host.HostProxySwitch`.
              
              ESXi 5.0 and earlier hosts: If you are reconfiguring an existing
              host membership, that is, the proxy switch already exists, you must reboot
              the host for the new setting to take effect.
          vendorSpecificConfig: Opaque binary blob that stores vendor specific configuration.
      """
      operation: str
      host: pyVmomi.vim.HostSystem
      backing: _typing.Optional[HostMember.Backing] = None
      maxProxySwitchPorts: _typing.Optional[int] = None
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []

   class PnicSpec(pyVmomi.vmodl.DynamicData):
      """
      Specification for an individual physical NIC.
      
      Attributes:
          pnicDevice: Name of the physical NIC to be added to the proxy switch.
              
              See `pyVmomi.vim.host.PhysicalNic`.`pyVmomi.vim.host.PhysicalNic.device`.
          uplinkPortKey: Key of the port to be connected to the physical NIC.
          uplinkPortgroupKey: Key of the portgroup to be connected to the physical NIC.
          connectionCookie: Cookie that represents this `pyVmomi.vim.dvs.PortConnection`
              instance for the port.
              
              The cookie value is generated by the
              Server. The Server ignores any value set by an SDK client.
              
              The same cookie is present in the distributed virtual port configuration
              (`pyVmomi.vim.dvs.DistributedVirtualPort`.`pyVmomi.vim.dvs.DistributedVirtualPort.connectionCookie`)
              so that the Server can verify that the entity is the rightful
              connectee of the port.
      """
      pnicDevice: str
      uplinkPortKey: _typing.Optional[str] = None
      uplinkPortgroupKey: _typing.Optional[str] = None
      connectionCookie: _typing.Optional[int] = None

   class Backing(pyVmomi.vmodl.DynamicData):
      """Base class."""
      pass

   class PnicBacking(HostMember.Backing):
      """
      The `pyVmomi.vim.dvs.HostMember.PnicBacking` data object
      specifies a set of physical NICs to use for a proxy switch.
      
      When you add a host to a distributed virtual switch
      (`pyVmomi.vim.dvs.HostMember.ConfigSpec`.`pyVmomi.vim.dvs.HostMember.ConfigSpec.host`),
      the host creates a proxy switch that will use the pNICs as uplinks.
      
      Attributes:
          pnicSpec: List of physical NIC specifications.
              
              Each entry identifies
              a pNIC to the proxy switch and optionally specifies uplink
              portgroup and port connections for the pNIC.
      """
      pnicSpec: list[HostMember.PnicSpec] = []

   class RuntimeState(pyVmomi.vmodl.DynamicData):
      """
      Runtime state of a host member.
      
      Attributes:
          currentMaxProxySwitchPorts: Current maximum number of ports allowed to be created in the
              proxy switch.
      """
      currentMaxProxySwitchPorts: int

   class TransportZoneType(pyVmomi.VmomiSupport.Enum):
      """
      Transport zone type.
      
      Attributes:
          vlan: VLAN based networking
          overlay: VXLAN based networking
      """
      vlan: _typing.ClassVar['HostMember.TransportZoneType'] = 'vlan'
      overlay: _typing.ClassVar['HostMember.TransportZoneType'] = 'overlay'

   class TransportZoneInfo(pyVmomi.vmodl.DynamicData):
      """
      Transport zone information.
      
      Attributes:
          uuid: The UUID of transport zone.
          type: The type of transport zone.
              
              See `pyVmomi.vim.dvs.HostMember.TransportZoneType` for valid values.
      """
      uuid: str
      type: str

   class ConfigInfo(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.dvs.HostMember.ConfigInfo` data object
      contains membership configuration information for the ESXi host.
      
      Attributes:
          host: ESXi host.
              
              This property should always be set unless the user's setting
              does not have System.Read privilege on the object referred to
              by this property.
          maxProxySwitchPorts: Maximum number of ports than can be created in the proxy switch.
              
              ESXi 5.0 and earlier hosts:
              If you change the maximum number of ports, you must reboot
              the host for the new value to take effect.
          vendorSpecificConfig: Opaque binary blob that stores vendor specific configuration.
          backing: Host membership backing, specifying physical NIC, portgroup, and port
              bindings for the proxy switch.
          nsxSwitch: Indicate whether the proxy switch is used by NSX on this particular
              host member of the VDS.
          ensEnabled: Indicate if ENS is enabled for this particular host member of
              the VDS.
              
              It is read only.
          ensInterruptEnabled: Indicate if ENS interrupt mode is enabled for this particular host
              member of the VDS.
              
              It is read only.
          transportZones: Indicate which transport zones this host joins by this VDS.
          nsxtUsedUplinkNames: Indicate which uplink ports are used by NSX-T.
          networkOffloadingEnabled: Indicate if network offloading is enabled for this particular host
              member of the VDS.
              
              Unset implies that network offloading is disabled.
              
              Since: vSphere API Release 8.0.0.1
          teplessMode: Indicates whether this host member is configured to operate in NSX tepless mode.
              
              Tepless mode refers to a specific NSX overlay network configuration where the
              host does not have a Virtual Tunnel End Point (VTEP).
              This property is only effective when `pyVmomi.vim.dvs.HostMember.ConfigInfo.nsxSwitch` is true.
              If this property is unset, the host member is not in NSX tepless mode.
              
              Since: vSphere API Release 9.1.0.0
      """
      host: _typing.Optional[pyVmomi.vim.HostSystem] = None
      maxProxySwitchPorts: int
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []
      backing: HostMember.Backing
      nsxSwitch: _typing.Optional[bool] = None
      ensEnabled: _typing.Optional[bool] = None
      ensInterruptEnabled: _typing.Optional[bool] = None
      transportZones: list[HostMember.TransportZoneInfo] = []
      nsxtUsedUplinkNames: list[str] = []
      networkOffloadingEnabled: _typing.Optional[bool] = None
      teplessMode: _typing.Optional[bool] = None

   class HostUplinkState(pyVmomi.vmodl.DynamicData):
      """
      The runtime state of uplink on the host.
      
      Attributes:
          uplinkName: Name of the uplink.
          state: The runtime state of the uplink.
              
              See `pyVmomi.vim.dvs.HostMember.HostUplinkState.State` for supported values.
      
      Since: vSphere API Release 8.0.3.0
      """
      class State(pyVmomi.VmomiSupport.Enum):
         """Describe the runtime state of the uplink."""
         active: _typing.ClassVar['HostMember.HostUplinkState.State'] = 'active'
         standby: _typing.ClassVar['HostMember.HostUplinkState.State'] = 'standby'

      uplinkName: str
      state: str

   class HostPerfNicOffloadState(pyVmomi.vmodl.DynamicData):
      """
      Represents the runtime state of Performance NIC Offload on a host.
      
      Attributes:
          enabled: Indicates whether Performance NIC Offload is intended to be enabled on the host.
              
              This property reflects the user's configuration intent. The actual runtime
              status of the feature is provided by `pyVmomi.vim.dvs.HostMember.HostPerfNicOffloadState.runtimeStatus`.
          runtimeStatus: The runtime status of the Performance NIC Offload feature when `pyVmomi.vim.dvs.HostMember.HostPerfNicOffloadState.enabled` is true.
              
              This property reflects whether the enablement request has succeeded, is in progress,
              or has failed.
              See `pyVmomi.vim.dvs.HostMember.HostPerfNicOffloadState.Status` for supported values.
          statusDescription: A human-readable description providing additional details about the `pyVmomi.vim.dvs.HostMember.HostPerfNicOffloadState.runtimeStatus`.
              
              This property is set if and only if `pyVmomi.vim.dvs.HostMember.HostPerfNicOffloadState.runtimeStatus` is FAILED.
      
      Since: vSphere API Release 9.1.0.0
      """
      class Status(pyVmomi.VmomiSupport.Enum):
         """
         Enumerates the possible runtime statuses for enabling Performance NIC Offload.
         
         Attributes:
             SUCCEEDED: Performance NIC offload is successfully enabled.
             IN_PROGRESS: Performance NIC offload is in the process of being enabled.
             FAILED: The attempt to enable Performance NIC Offload has failed.
         
         Since: vSphere API Release 9.1.0.0
         """
         SUCCEEDED: _typing.ClassVar['HostMember.HostPerfNicOffloadState.Status'] = 'SUCCEEDED'
         IN_PROGRESS: _typing.ClassVar['HostMember.HostPerfNicOffloadState.Status'] = 'IN_PROGRESS'
         FAILED: _typing.ClassVar['HostMember.HostPerfNicOffloadState.Status'] = 'FAILED'

      enabled: bool
      runtimeStatus: _typing.Optional[str] = None
      statusDescription: _typing.Optional[str] = None

   class RuntimeInfo(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.dvs.HostMember.RuntimeInfo` data object
      contains healthcheck and status information about a host
      member of a distributed virtual switch.
      
      Attributes:
          host: The host.
          status: Host proxy switch status.
              
              See
              `pyVmomi.vim.dvs.HostMember.HostComponentState` for valid values.
              This property replaces the deprecated
              `pyVmomi.vim.dvs.HostMember`.`pyVmomi.vim.dvs.HostMember.status`.
          statusDetail: Additional information regarding the current membership status of the host.
              
              This property replaces the deprecated
              `pyVmomi.vim.dvs.HostMember`.`pyVmomi.vim.dvs.HostMember.statusDetail`.
          nsxtStatus: NSX-T component status.
          nsxtStatusDetail: Additional information regarding the NSX-T component status.
          healthCheckResult: Health check result for the host that joined the distributed virtual switch.
          hostUplinkState: Indicate the runtime state of uplink on the host.
              
              It is only applicable when `pyVmomi.vim.dvs.HostMember.ConfigInfo.networkOffloadingEnabled`
              is true.
              
              Since: vSphere API Release 8.0.3.0
          hostPerfNicOffloadState: Indicates the runtime state of the performance NIC offloading on the host.
              
              If unset, performance NIC offloading is considered disabled.
              
              Since: vSphere API Release 9.1.0.0
      """
      host: pyVmomi.vim.HostSystem
      status: _typing.Optional[str] = None
      statusDetail: _typing.Optional[str] = None
      nsxtStatus: _typing.Optional[str] = None
      nsxtStatusDetail: _typing.Optional[str] = None
      healthCheckResult: list[HostMember.HealthCheckResult] = []
      hostUplinkState: list[HostMember.HostUplinkState] = []
      hostPerfNicOffloadState: _typing.Optional[HostMember.HostPerfNicOffloadState] = None

   class HealthCheckResult(pyVmomi.vmodl.DynamicData):
      """
      This class defines healthcheck result of the vSphere Distributed Switch.
      
      Attributes:
          summary: The summary of health check result.
      """
      summary: _typing.Optional[str] = None

   class UplinkHealthCheckResult(HostMember.HealthCheckResult):
      """
      This class defines healthcheck result of a specified Uplink port
      in vSphere Distributed Switch.
      
      Attributes:
          uplinkPortKey: The uplink port key.
      """
      uplinkPortKey: str

   runtimeState: _typing.Optional[HostMember.RuntimeState] = None
   config: HostMember.ConfigInfo
   productInfo: _typing.Optional[ProductSpec] = None
   uplinkPortKey: list[str] = []
   status: str
   statusDetail: _typing.Optional[str] = None


class HostProductSpec(pyVmomi.vmodl.DynamicData):
   """
   This data object type is a subset of `pyVmomi.vim.AboutInfo`.
   
   An object of
   this type can be used to describe the specification for a host.
   
   Attributes:
       productLineId: The product-line name.
       version: Dot-separated version string.
           
           For example, \"1.2\".
   """
   productLineId: _typing.Optional[str] = None
   version: _typing.Optional[str] = None


class KeyedOpaqueBlob(pyVmomi.vmodl.DynamicData):
   """
   This class defines a data structure to hold opaque binary data
   identified by a key.
   
   Attributes:
       key: A key that identifies the opaque binary blob.
       opaqueData: The opaque data.
           
           It is recommended that base64 encoding be used for binary
           data.
   """
   key: str
   opaqueData: str


class NetworkOffloadSpec(pyVmomi.vmodl.DynamicData):
   """
   Describe the network offload specification of a
   `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch`.
   
   Attributes:
       id: Identifier of the specification.
       name: Name of the specification.
       types: DPU types supported in the specification.
       dpuCapability: The `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.DpuFeatureCapability`
           data object describes version-specific DPU capabilities.
           
           If unset, the DPU capability should be determined from
           `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.FeatureCapability.dpuCapability`.
           
           Since: vSphere API Release 9.1.0.0
   
   Since: vSphere API Release 8.0.0.1
   """
   id: str
   name: _typing.Optional[str] = None
   types: list[str] = []
   dpuCapability: _typing.Optional[VmwareDistributedVirtualSwitch.DpuFeatureCapability] = None


class NetworkResourcePool(pyVmomi.vmodl.DynamicData):
   """
   Deprecated: as of vSphere API 6.0
   Use `pyVmomi.vim.DistributedVirtualSwitch.HostInfrastructureTrafficResource`
   to manage resource allocation for host infrastructure traffic.
   Use `pyVmomi.vim.dvs.VmVnicNetworkResourcePool` to manage
   resource allocation for user defined pools.The `pyVmomi.vim.dvs.NetworkResourcePool` data object
   describes the resource configuration and management
   of network resource pools.
   
   Attributes:
       key: Key of the network resource pool.
       name: Name of the network resource pool.
       description: Description of the network resource pool.
       configVersion: Configuration version for the network resource pool.
       allocationInfo: Resource settings of the resource pool.
   """
   class AllocationInfo(pyVmomi.vmodl.DynamicData):
      """
      Resource allocation information for a network resource pool.
      
      Attributes:
          limit: Maximum allowed usage for network clients belonging to
              this resource pool per host.
              
              The utilization of network clients belonging to this resource pool
              will not exceed the specified limit even if there are available
              network resources. If set to -1, then there is no limit on the network
              resource usage for clients belonging to this resource pool. Units are
              in Mbits/sec. When setting the allocation of a particular resource
              pool, if the property is unset, it is treated as no change and the
              property is not updated. An unset limit value while reading back the
              allocation information of a network resource pool indicates that
              there is no limit on the network resource usage for the clients
              belonging to this resource group.
          shares: Share settings associated with the network resource pool to
              facilitate proportional sharing of the physical network resources.
              
              If the property is unset when setting the allocation of a particular
              resource pool, it is treated as unset and the property is not updated.
              The property is always set when reading back the allocation
              information of a network resource pool.
          priorityTag: 802.1p tag to be used for this resource pool.
              
              The tag is a priority value
              in the range 0..7 for Quality of Service operations on network traffic.
      """
      limit: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      shares: _typing.Optional[pyVmomi.vim.SharesInfo] = None
      priorityTag: _typing.Optional[int] = None

   class ConfigSpec(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.dvs.NetworkResourcePool.ConfigSpec` data object
      contains properties to create or update a network resource pool
      for a distributed virtual switch.
      
      Attributes:
          key: Key of the network resource pool.
              
              The property is ignored for
              `pyVmomi.vim.DistributedVirtualSwitch`.`pyVmomi.vim.DistributedVirtualSwitch.addNetworkResourcePool`
              operations.
          configVersion: Unique identifier for a given version
              of the configuration.
              
              Each change to the configuration will
              update this value. This is typically implemented as a
              non-decreasing count or a time-stamp. However, a client should
              always treat this as an opaque string.
              
              If you specify the configuration version when you update
              the resource configuration, the Server will apply the changes
              only if the specified identifier matches the current
              `pyVmomi.vim.dvs.NetworkResourcePool`.`pyVmomi.vim.dvs.NetworkResourcePool.configVersion`
              value. You can use this field to guard against updates
              that may have occurred between the time when the client
              reads `pyVmomi.vim.dvs.NetworkResourcePool.configVersion`
              and when the configuration is applied.
          allocationInfo: Network resource allocation for the network resource pool.
          name: User defined name for the resource pool.
              
              The property is required for
              `pyVmomi.vim.DistributedVirtualSwitch`.`pyVmomi.vim.DistributedVirtualSwitch.addNetworkResourcePool`
              operations.
          description: User-defined description for the resource pool.
      """
      key: str
      configVersion: _typing.Optional[str] = None
      allocationInfo: _typing.Optional[NetworkResourcePool.AllocationInfo] = None
      name: _typing.Optional[str] = None
      description: _typing.Optional[str] = None

   key: str
   name: _typing.Optional[str] = None
   description: _typing.Optional[str] = None
   configVersion: str
   allocationInfo: NetworkResourcePool.AllocationInfo


class PortConnectee(pyVmomi.vmodl.DynamicData):
   """
   Information about the entity that connects to a DistributedVirtualPort.
   
   Attributes:
       connectedEntity: The connected entity.
           
           This property should always be set unless the user's setting
           does not have System.Read privilege on the object referred to
           by this property.
       nicKey: The key of the virtual NIC that connects to this port.
       type: The type of the connectee.
           
           See `pyVmomi.vim.dvs.PortConnectee.ConnecteeType` for valid values.
       addressHint: A hint on address information of the NIC that connects to this port.
   """
   class ConnecteeType(pyVmomi.VmomiSupport.Enum):
      """
      The connectee types.
      
      Attributes:
          pnic: The port connects to a Physical NIC.
          vmVnic: The port connects to a Virtual NIC in a Virtual Machine.
          hostConsoleVnic: The port connects to a console Virtual NIC on a host.
          hostVmkVnic: The port connects to a VMkernel Virtual NIC on a host.
          systemCrxVnic: The port connects to a Virtual NIC in a System CRX VM.
              
              Since: vSphere API Release 8.0.1.0
      """
      pnic: _typing.ClassVar['PortConnectee.ConnecteeType'] = 'pnic'
      vmVnic: _typing.ClassVar['PortConnectee.ConnecteeType'] = 'vmVnic'
      hostConsoleVnic: _typing.ClassVar['PortConnectee.ConnecteeType'] = 'hostConsoleVnic'
      hostVmkVnic: _typing.ClassVar['PortConnectee.ConnecteeType'] = 'hostVmkVnic'
      systemCrxVnic: _typing.ClassVar['PortConnectee.ConnecteeType'] = 'systemCrxVnic'

   connectedEntity: _typing.Optional[pyVmomi.vim.ManagedEntity] = None
   nicKey: _typing.Optional[str] = None
   type: _typing.Optional[str] = None
   addressHint: _typing.Optional[str] = None


class PortConnection(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.dvs.PortConnection` data object represents a connection
   or association between a `pyVmomi.vim.dvs.DistributedVirtualPortgroup` or a
   `pyVmomi.vim.dvs.DistributedVirtualPort` and one of the following entities:
   - Virtual machine virtual NIC
     (`pyVmomi.vim.vm.device.VirtualEthernetCard.DistributedVirtualPortBackingInfo`)
   - Host virtual NIC (`pyVmomi.vim.host.VirtualNic`)
   - Physical NIC (`pyVmomi.vim.host.NetworkInfo`.`pyVmomi.vim.host.NetworkInfo.pnic`)
   
   Attributes:
       switchUuid: UUID of the switch (`pyVmomi.vim.DistributedVirtualSwitch`.`pyVmomi.vim.DistributedVirtualSwitch.uuid`).
       portgroupKey: Key of the portgroup.
           
           If specified, the connection object represents a connection
           or an association between a `pyVmomi.vim.dvs.DistributedVirtualPortgroup`
           and a Virtual NIC or physical NIC.
           In this case, setting the `pyVmomi.vim.dvs.PortConnection.portKey` is not necessary for a
           early-binding portgroup and is not allowed for a late-binding portgroup.
           The `pyVmomi.vim.dvs.PortConnection.portKey` property will be populated by the implementation
           at the time of port binding.
       portKey: Key of the port.
           
           If specified, this object represents a connection
           or an association between an individual `pyVmomi.vim.dvs.DistributedVirtualPort`
           and a Virtual NIC or physical NIC. See `pyVmomi.vim.dvs.PortConnection.portgroupKey` for more information on populating
           this property.
       connectionCookie: Cookie that represents this `pyVmomi.vim.dvs.PortConnection`
           instance for the port.
           
           The cookie value is generated by the
           Server. The Server ignores any value set by an SDK client.
           
           The same cookie is present in the distributed virtual port configuration
           (`pyVmomi.vim.dvs.DistributedVirtualPort`.`pyVmomi.vim.dvs.DistributedVirtualPort.connectionCookie`)
           so that the Server can verify that the entity is the rightful
           connectee of the port.
   """
   switchUuid: str
   portgroupKey: _typing.Optional[str] = None
   portKey: _typing.Optional[str] = None
   connectionCookie: _typing.Optional[int] = None


class PortCriteria(pyVmomi.vmodl.DynamicData):
   """
   The criteria specification for selecting ports.
   
   Attributes:
       connected: If set, only the connected ports are qualified.
       active: If set, only the active ports are qualified.
       uplinkPort: If set to true, only the uplink ports are qualified.
           
           If set to false, only
           non-uplink ports are qualified.
       nsxPort: If set to true, only the NSX ports are qualified.
           
           If set to false, only
           non-NSX ports are qualified.
           NSX ports are ports of NSX port group.
       scope: If set, only the ports of which the scope covers the entity are
           qualified.
       portgroupKey: The keys of the portgroup that is used for the scope of `pyVmomi.vim.dvs.PortCriteria.inside`.
           
           If this property is unset, it means any portgroup. If `pyVmomi.vim.dvs.PortCriteria.inside`
           is unset, this property is ignored.
       inside: If unset, all ports in the switch are qualified.
           
           If set to true, only ports inside `pyVmomi.vim.dvs.PortCriteria.portgroupKey` or any
           portgroup, if not set, are qualified.
           If set to false, only ports outside `pyVmomi.vim.dvs.PortCriteria.portgroupKey` or any
           portgroup, if not set, are qualified.
       portKey: If set, only the ports of which the key is in the array are
           qualified.
       host: If set, only the ports that are present in one of the host are qualified.
   """
   connected: _typing.Optional[bool] = None
   active: _typing.Optional[bool] = None
   uplinkPort: _typing.Optional[bool] = None
   nsxPort: _typing.Optional[bool] = None
   scope: _typing.Optional[pyVmomi.vim.ManagedEntity] = None
   portgroupKey: list[str] = []
   inside: _typing.Optional[bool] = None
   portKey: list[str] = []
   host: list[pyVmomi.vim.HostSystem] = []


class PortStatistics(pyVmomi.vmodl.DynamicData):
   """
   Statistic data of a DistributedVirtualPort.
   
   Attributes:
       packetsInMulticast: The number of multicast packets received.
       packetsOutMulticast: The number of multicast packets forwarded.
       bytesInMulticast: The number of bytes received from multicast packets.
       bytesOutMulticast: The number of bytes forwarded from multicast packets.
       packetsInUnicast: The number of unicast packets received.
       packetsOutUnicast: The number of unicast packets forwarded.
       bytesInUnicast: The number of bytes received from unicast packets.
       bytesOutUnicast: The number of bytes forwarded from unicast packets.
       packetsInBroadcast: The number of broadcast packets received.
       packetsOutBroadcast: The number of broadcast packets forwarded.
       bytesInBroadcast: The number of bytes received from broadcast packets.
       bytesOutBroadcast: The number of bytes forwarded from broadcast packets.
       packetsInDropped: The number of received packets dropped.
       packetsOutDropped: The number of packets to be forwarded dropped.
       packetsInException: The number of packets received that cause an exception.
       packetsOutException: The number of packets to be forwarded that cause an exception.
       bytesInFromPnic: The number of bytes received at a pnic on the behalf of a port's
           connectee (inter-host rx).
       bytesOutToPnic: The number of bytes transmitted at a pnic on the behalf of a port's
           connectee (inter-host tx).
   """
   packetsInMulticast: pyVmomi.VmomiSupport.long
   packetsOutMulticast: pyVmomi.VmomiSupport.long
   bytesInMulticast: pyVmomi.VmomiSupport.long
   bytesOutMulticast: pyVmomi.VmomiSupport.long
   packetsInUnicast: pyVmomi.VmomiSupport.long
   packetsOutUnicast: pyVmomi.VmomiSupport.long
   bytesInUnicast: pyVmomi.VmomiSupport.long
   bytesOutUnicast: pyVmomi.VmomiSupport.long
   packetsInBroadcast: pyVmomi.VmomiSupport.long
   packetsOutBroadcast: pyVmomi.VmomiSupport.long
   bytesInBroadcast: pyVmomi.VmomiSupport.long
   bytesOutBroadcast: pyVmomi.VmomiSupport.long
   packetsInDropped: pyVmomi.VmomiSupport.long
   packetsOutDropped: pyVmomi.VmomiSupport.long
   packetsInException: pyVmomi.VmomiSupport.long
   packetsOutException: pyVmomi.VmomiSupport.long
   bytesInFromPnic: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   bytesOutToPnic: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class ProductSpec(pyVmomi.vmodl.DynamicData):
   """
   This data object type is a subset of `pyVmomi.vim.AboutInfo`.
   
   An object of
   this type can be used to describe the specification for a proxy switch module
   of a `pyVmomi.vim.DistributedVirtualSwitch`.
   
   Attributes:
       name: Short form of the product name.
       vendor: Name of the vendor of this product.
       version: Dot-separated version string.
           
           For example, \"1.2\".
       build: Build string for the server on which this call is made.
           
           For example, x.y.z-num.
           This string does not apply to the API.
       forwardingClass: Forwarding class of the distributed virtual switch.
       bundleId: The ID of the bundle if a host component bundle needs to be installed on
           the host members to support the functionality of the switch.
       bundleUrl: The URL of the bundle that VMware Update Manager will use to install
           the bundle on the host members, if `pyVmomi.vim.dvs.ProductSpec.bundleId` is set.
   """
   name: _typing.Optional[str] = None
   vendor: _typing.Optional[str] = None
   version: _typing.Optional[str] = None
   build: _typing.Optional[str] = None
   forwardingClass: _typing.Optional[str] = None
   bundleId: _typing.Optional[str] = None
   bundleUrl: _typing.Optional[str] = None


class TrafficRule(pyVmomi.vmodl.DynamicData):
   """
   This class defines a single rule that will be applied to network traffic.
   
   Attributes:
       key: The key of the rule
       description: Description of the rule
       sequence: Sequence of this rule.
           
           i.e, the order in which this rule appears
           in the ruleset.
       qualifier: List of Network rule qualifiers.
           
           'AND' of this array of
           network rule qualifiers is applied as one network traffic rule.
           If the TrafficRule belongs to
           `pyVmomi.vim.dvs.DistributedVirtualPort.FilterPolicy` :
           There can be a maximum of 1 `pyVmomi.vim.dvs.TrafficRule.IpQualifier`,
           1 `pyVmomi.vim.dvs.TrafficRule.MacQualifier` and
           1 `pyVmomi.vim.dvs.TrafficRule.SystemTrafficQualifier` for a total of
           3 `pyVmomi.vim.dvs.TrafficRule.qualifier`
       action: Action to be applied for this rule.
       direction: Whether this rule needs to be applied to incoming packets,
           to outgoing packets or both.
           
           See `pyVmomi.vim.dvs.TrafficRule.RuleDirectionType` for valid values.
   """
   class Qualifier(pyVmomi.vmodl.DynamicData):
      """
      This class is the base class for identifying network traffic.
      
      Attributes:
          key: The key of the Qualifier
      """
      key: _typing.Optional[str] = None

   class Action(pyVmomi.vmodl.DynamicData):
      """This class is the base class for network rule action."""
      pass

   class RuleDirectionType(pyVmomi.VmomiSupport.Enum):
      """
      Network Traffic Rule direction types.
      
      It specifies whether rule
      needs to be applied for packets which are incoming/outgoing or both.
      
      Attributes:
          incomingPackets: This specifies that the network rule has to be applied only for
              incoming packets.
          outgoingPackets: This specifies that the network rule has to be applied only for
              outgoing packets.
          both: This specifies that the network rule has to be applied only for
              both incoming and outgoing packets.
      """
      incomingPackets: _typing.ClassVar['TrafficRule.RuleDirectionType'] = 'incomingPackets'
      outgoingPackets: _typing.ClassVar['TrafficRule.RuleDirectionType'] = 'outgoingPackets'
      both: _typing.ClassVar['TrafficRule.RuleDirectionType'] = 'both'

   class IpQualifier(TrafficRule.Qualifier):
      """
      This class defines the IP Rule Qualifier.
      
      Here IP addresses of source
      and destination will be used for classifying packets.
      
      Attributes:
          sourceAddress: IP qualifier for source.
              
              If this property is NULL, it will match \"any IPv4 or any IPv6 address\".
          destinationAddress: IP qualifier for destination.
              
              If this property is NULL, it will match \"any IPv4 or any IPv6 address\".
          protocol: Protocols like TCP, UDP, ICMP etc.
              
              The valid value for a protocol
              is got from IANA assigned value for the protocol. This can be got
              from RFC 5237 and IANA website section related to protocol numbers.
          sourceIpPort: Source IP Port.
          destinationIpPort: Destination IP Port.
          tcpFlags: TCP flags.
              
              The valid values can be found at RFC 3168.
              TCP flags are not supported by Traffic Filtering
      """
      sourceAddress: _typing.Optional[pyVmomi.vim.IpAddress] = None
      destinationAddress: _typing.Optional[pyVmomi.vim.IpAddress] = None
      protocol: _typing.Optional[pyVmomi.vim.IntExpression] = None
      sourceIpPort: _typing.Optional[TrafficRule.IpPort] = None
      destinationIpPort: _typing.Optional[TrafficRule.IpPort] = None
      tcpFlags: _typing.Optional[pyVmomi.vim.IntExpression] = None

   class IpPort(pyVmomi.vim.NegatableExpression):
      """
      Base class for specifying Ports.
      
      Objects of the base class represent any port (single/range/list).
      """
      pass

   class SingleIpPort(TrafficRule.IpPort):
      """
      This class defines a Single Port
      
      Attributes:
          portNumber: The IP port number.
      """
      portNumber: int

   class IpPortRange(TrafficRule.IpPort):
      """
      This class defines a range of Ports.
      
      Attributes:
          startPortNumber: Starting port number of the ports range.
          endPortNumber: Ending port number of the ports range.
      """
      startPortNumber: int
      endPortNumber: int

   class MacQualifier(TrafficRule.Qualifier):
      """
      This class defines the MAC Rule Qualifier.
      
      Here MAC addresses of source
      and destination will be used for classifying packets.
      
      Attributes:
          sourceAddress: MAC address for source.
              
              If this property is NULL, it will match \"any MAC address\".
          destinationAddress: MAC address for destination.
              
              If this property is NULL, it will match \"any MAC address\".
          protocol: Protocol used.
              
              This corresponds to the EtherType field in Ethernet
              frame. The valid values can be found from IEEE list at:
              http://standards.ieee.org/regauth/ as mentioned in RFC 5342.
          vlanId: vlan id.
      """
      sourceAddress: _typing.Optional[pyVmomi.vim.MacAddress] = None
      destinationAddress: _typing.Optional[pyVmomi.vim.MacAddress] = None
      protocol: _typing.Optional[pyVmomi.vim.IntExpression] = None
      vlanId: _typing.Optional[pyVmomi.vim.IntExpression] = None

   class SystemTrafficQualifier(TrafficRule.Qualifier):
      """
      This class defines the System Traffic Qualifier.
      
      Here the type of
      traffic will be used for classifying packets.
      
      Attributes:
          typeOfSystemTraffic: Type of system traffic.
              
              See `pyVmomi.vim.DistributedVirtualSwitch.HostInfrastructureTrafficClass`
              for valid values.
      """
      typeOfSystemTraffic: _typing.Optional[pyVmomi.vim.StringExpression] = None

   class DropAction(TrafficRule.Action):
      """This class defines network rule action to drop packets."""
      pass

   class AcceptAction(TrafficRule.Action):
      """This class defines network rule action to accept packets."""
      pass

   class UpdateTagAction(TrafficRule.Action):
      """
      This class defines network rule action to tag packets(qos,dscp) or
      clear tags(clear qos, dscp tags) on packets.
      
      One or both of qos and dscp may be specified.
      
      Attributes:
          qosTag: QOS tag.
              
              IEEE 802.1p supports 3 bit Priority Code Point (PCP).
              The valid values are between 0-7. Please refer the IEEE 802.1p
              documentation for more details about what each value represents.
              If qosTag is set to 0 then the tag on the packets will be cleared.
          dscpTag: DSCP tag.
              
              The valid values for DSCP tag can be found in
              'Differentiated Services Field Codepoints' section of IANA website.
              The information can also be got from reading all of the below RFC:
              RFC 2474, RFC 2597, RFC 3246, RFC 5865.
              If the dscpTag is set to 0 then the dscp tag on packets will be cleared.
      """
      qosTag: _typing.Optional[int] = None
      dscpTag: _typing.Optional[int] = None

   class RateLimitAction(TrafficRule.Action):
      """
      This class defines network rule action to ratelimit packets.
      
      Attributes:
          packetsPerSecond: Rate limit value specified in packets per second.
      """
      packetsPerSecond: int

   class LogAction(TrafficRule.Action):
      """This class defines network rule action to just log the rule."""
      pass

   class GreAction(TrafficRule.Action):
      """
      This class defines network rule action to GRE Encapsulate a packet.
      
      Attributes:
          encapsulationIp: Single IP address.
              
              Only IPv4 is supported for vSphere API 5.5.
      """
      encapsulationIp: pyVmomi.vim.SingleIp

   class MacRewriteAction(TrafficRule.Action):
      """
      This class defines network rule action to MAC Rewrite.
      
      Attributes:
          rewriteMac: Rewrite Destination MAC with this MAC address.
      """
      rewriteMac: str

   class PuntAction(TrafficRule.Action):
      """
      This class defines network rule action to punt.
      
      i.e, forward packets
      to an associated slow-path service Virtual Machine.
      """
      pass

   class CopyAction(TrafficRule.Action):
      """
      This class defines network rule action to copy the packet to an
      associated slow-path service Virtual Machine and let the original
      frame continue.
      """
      pass

   key: _typing.Optional[str] = None
   description: _typing.Optional[str] = None
   sequence: _typing.Optional[int] = None
   qualifier: list[TrafficRule.Qualifier] = []
   action: _typing.Optional[TrafficRule.Action] = None
   direction: _typing.Optional[str] = None


class TrafficRuleset(pyVmomi.vmodl.DynamicData):
   """
   This class defines a ruleset(set of rules) that will be
   applied to network traffic.
   
   Attributes:
       key: The key of the ruleset.
       enabled: Whether ruleset is enabled or not.
       precedence: Precedence of the ruleset.
           
           Rulesets for a port will be executed
           in the order of their precedence.
       rules: List of rules belonging to this ruleset.
   """
   key: _typing.Optional[str] = None
   enabled: _typing.Optional[bool] = None
   precedence: _typing.Optional[int] = None
   rules: list[TrafficRule] = []


class VmVnicNetworkResourcePool(pyVmomi.vmodl.DynamicData):
   """
   DataObject describing the resource configuration and management of
   virtual NIC network resource pools.
   
   Attributes:
       key: The key of the virtual NIC network resource pool.
       name: The name of the virtual NIC network resource pool.
       description: The description of the virtual NIC network resource pool.
       configVersion: The config version for the virtual NIC network resource pool.
       allocationInfo: The resource settings of the virtual NIC network resource pool.
   """
   class ResourceAllocation(pyVmomi.vmodl.DynamicData):
      """
      Resource allocation information for a virtual NIC network resource pool.
      
      Attributes:
          reservationQuota: Quota for the total amount of virtual machine nic reservation in this pool.
              
              Unit in Mbits/sec.
      """
      reservationQuota: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   class ConfigSpec(pyVmomi.vmodl.DynamicData):
      """
      The configuration specification data object to update the resource configuration
      for a virtual NIC network resource pool.
      
      Attributes:
          operation: The type of operation on the virtual NIC network resource pool
              Possible value can be of
              `pyVmomi.vim.ConfigSpecOperation`
          key: The key of the network resource pool.
              
              The property is ignored for add
              operations.
          configVersion: The configVersion is a unique identifier for a given version
              of the configuration.
              
              Each change to the configuration will
              update this value. This is typically implemented as a
              non-decreasing count or a time-stamp. However, a client should
              always treat this as an opaque string.
              
              If specified when updating the resource configuration, the
              changes will only be applied if the current configVersion matches the
              specified configVersion. This field can be used to guard against
              updates that that may have occurred between the time when configVersion
              was read and when it is applied.
          allocationInfo: The resource allocation for the virtual NIC network resource pool.
          name: The name for the virtual NIC network resource pool.
              
              The property is required for Add operations.
          description: The description for the virtual NIC network resource pool.
      """
      operation: str
      key: _typing.Optional[str] = None
      configVersion: _typing.Optional[str] = None
      allocationInfo: _typing.Optional[VmVnicNetworkResourcePool.ResourceAllocation] = None
      name: _typing.Optional[str] = None
      description: _typing.Optional[str] = None

   class VnicAllocatedResource(pyVmomi.vmodl.DynamicData):
      """
      This class defines the allocated resource information on a virtual NIC
      
      Attributes:
          vm: The virtual machine
          vnicKey: The virtual NIC key
          reservation: The reservation specification on the virtual NIC.
              
              Units in Mbits/s
      """
      vm: pyVmomi.vim.VirtualMachine
      vnicKey: str
      reservation: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   class RuntimeInfo(pyVmomi.vmodl.DynamicData):
      """
      This class defines the runtime information for the
      virtual NIC network resource pool
      
      Attributes:
          key: The key of the virtual NIC network resource pool
          name: The name of the virtual NIC network resource pool
          capacity: Capacity: Reservation allocated for this Network Resource Pool.
              
              Units in Mbits/s.
          usage: usage: Reservation taken by all `pyVmomi.vim.vm.device.VirtualEthernetCard` for which the
              backing is associated with this `pyVmomi.vim.dvs.VmVnicNetworkResourcePool`.
              
              Units in Mbits/s.
          available: Available: Current available resource for reservation (capacity - usage).
              
              Units in Mbits/s.
          status: The status of the virtual NIC network resource pool
              See `pyVmomi.vim.ManagedEntity.Status` for possible values
              
              `red` indicates that the
              reservations used by all the virtual network adapters belonging
              to this resource pool exceeds the total reservation quota allocated to the
              resource pool. This can happen due to failure of one or more uplink
              or if the user bypasses VirtualCenter and powers on VMs directly on host.
              The reservation of one or more virtual network adapters cannot be guaranteed
              and corrective action needs to be taken by the user.
              
              `green` indicates that the resource pool
              is in good state. The reservations for all virtual network adapters can
              be fulfilled.
          allocatedResource: The virtual network adapters that
              are currently associated with the resource pool
      """
      key: str
      name: _typing.Optional[str] = None
      capacity: _typing.Optional[int] = None
      usage: _typing.Optional[int] = None
      available: _typing.Optional[int] = None
      status: str
      allocatedResource: list[VmVnicNetworkResourcePool.VnicAllocatedResource] = []

   key: str
   name: _typing.Optional[str] = None
   description: _typing.Optional[str] = None
   configVersion: str
   allocationInfo: _typing.Optional[VmVnicNetworkResourcePool.ResourceAllocation] = None


class VmwareDistributedVirtualSwitch(pyVmomi.vim.DistributedVirtualSwitch):
   """
   The `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch` managed object
   is the VMware implementation of a distributed virtual switch.
   
   The functionality listed here is for a VMware distributed virtual switch only.
   
   When you use a VMware distributed virtual switch, you can perform
   backup and restore operations on the VMware switch. You can also
   perform rollback operations on the switch and on portgroups
   associated with the VMware switch. See the description for the
   following methods:
   - `pyVmomi.vim.dvs.DistributedVirtualSwitchManager.exportEntity`
   - `pyVmomi.vim.dvs.DistributedVirtualSwitchManager.importEntity`
   - `pyVmomi.vim.DistributedVirtualSwitch.rollback`
   - `pyVmomi.vim.dvs.DistributedVirtualPortgroup.rollback`
   """
   class FeatureCapability(pyVmomi.vim.DistributedVirtualSwitch.FeatureCapability):
      """
      Indicators of support for version-specific DVS features that are only
      available on a VMware-class switch.
      
      Attributes:
          vspanSupported: Flag to indicate whether vspan(DVMirror) is supported on the
              vSphere Distributed Switch.
              
              Distributed Port Mirroring is supported in vSphere Distributed Switch Version 5.0 or later.
          lldpSupported: Flag to indicate whether LLDP(Link Layer Discovery Protocol) is supported on the
              vSphere Distributed Switch.
              
              LLDP is supported in vSphere Distributed Switch Version 5.0 or later.
          ipfixSupported: Flag to indicate whether IPFIX(NetFlow) is supported on the
              vSphere Distributed Switch.
              
              IPFIX is supported in vSphere Distributed Switch Version 5.0 or later.
          ipfixCapability: The support for version-specific IPFIX(NetFlow).
          multicastSnoopingSupported: Flag to indicate whether multicast snooping(IGMP/MLD Snooping)
              is supported on the vSphere Distributed Switch.
              
              IGMP/MLD Snooping is supported in vSphere Distributed Switch Version 6.0 or later.
          vspanCapability: The support for version-specific Distributed Port Mirroring sessions.
          lacpCapability: The support for version-specific Link Aggregation Control Protocol.
          dpuCapability: The support for version-specific DPU(SmartNic).
              
              Since: vSphere API Release 8.0.0.1
          nsxSupported: Flag to indicate whether NSX is supported on the
              vSphere Distributed Switch.
              
              NSX is supported in vSphere Distributed Switch Version 7.0 or later.
          mtuCapability: The support for version-specific supported MTU.
              
              Since: vSphere API Release 7.0.2.0
          realTimeConfigSupported: Flag to indicate whether real-time configuration is supported on
              Distributed Switch.
              
              Real-time configuration is supported in vSphere Distributed Switch
              Version 9.0 or later.
              
              Since: vSphere API Release 8.0.3.1
          perfNicOffloadCapability: The support for version-specific performance NIC offloading.
              
              Since: vSphere API Release 9.1.0.0
          systemTrafficCapabilities: The support for version-specific system traffic qualifiers of Traffic Filtering and Marking.
              
              Since: vSphere API Release 9.1.0.0
      """
      vspanSupported: _typing.Optional[bool] = None
      lldpSupported: _typing.Optional[bool] = None
      ipfixSupported: _typing.Optional[bool] = None
      ipfixCapability: _typing.Optional[VmwareDistributedVirtualSwitch.IpfixFeatureCapability] = None
      multicastSnoopingSupported: _typing.Optional[bool] = None
      vspanCapability: _typing.Optional[VmwareDistributedVirtualSwitch.VspanFeatureCapability] = None
      lacpCapability: _typing.Optional[VmwareDistributedVirtualSwitch.LacpFeatureCapability] = None
      dpuCapability: _typing.Optional[VmwareDistributedVirtualSwitch.DpuFeatureCapability] = None
      nsxSupported: _typing.Optional[bool] = None
      mtuCapability: _typing.Optional[VmwareDistributedVirtualSwitch.MtuCapability] = None
      realTimeConfigSupported: _typing.Optional[bool] = None
      perfNicOffloadCapability: _typing.Optional[VmwareDistributedVirtualSwitch.PerfNicOffloadFeatureCapability] = None
      systemTrafficCapabilities: _typing.Optional[VmwareDistributedVirtualSwitch.SystemTrafficCapabilities] = None

   class IpfixFeatureCapability(pyVmomi.vmodl.DynamicData):
      """
      The feature capabilities of Ipfix supported by the vSphere Distributed Switch.
      
      Attributes:
          ipfixSupported: Flag to indicate whether IPFIX(NetFlow) is supported on the
              vSphere Distributed Switch.
              
              IPFIX is supported in vSphere Distributed Switch Version 5.0 or later.
          ipv6ForIpfixSupported: Flag to indicate whether IPv6 for IPFIX(NetFlow) is supported on the
              vSphere Distributed Switch.
              
              IPv6 for IPFIX is supported in vSphere Distributed Switch Version 6.0 or later.
          observationDomainIdSupported: Flag to indicate whether Observation Domain Id for IPFIX is supported
              on the vSphere Distributed Switch.
              
              Observation Domain Id is supported in vSphere Distributed Switch Version 6.0 or later.
      """
      ipfixSupported: _typing.Optional[bool] = None
      ipv6ForIpfixSupported: _typing.Optional[bool] = None
      observationDomainIdSupported: _typing.Optional[bool] = None

   class LacpFeatureCapability(pyVmomi.vmodl.DynamicData):
      """
      The feature capabilities of Link Aggregation Control Protocol supported by the
      vSphere Distributed Switch.
      
      Attributes:
          lacpSupported: Flag to indicate whether Link Aggregation Control Protocol is supported on the
              vSphere Distributed Switch.
          multiLacpGroupSupported: Flag to indicate whether the vSphere Distributed Switch supports more
              than one Link Aggregation Control Protocol group to be configured.
              
              It is supported in vSphere Distributed Switch Version 5.5 or later.
          lacpFastModeSupported: Flag to indicate whether LACP Fast Mode is supported on the
              vSphere Distributed Switch.
              
              LACP Fast Mode is supported in vSphere Distributed Switch Version 7.0 or later.
              
              Since: vSphere API Release 7.0.2.0
      """
      lacpSupported: _typing.Optional[bool] = None
      multiLacpGroupSupported: _typing.Optional[bool] = None
      lacpFastModeSupported: _typing.Optional[bool] = None

   class DpuFeatureCapability(pyVmomi.vmodl.DynamicData):
      """
      The feature capabilities of Dpu Features supported by the
      vSphere Distributed Switch.
      
      Attributes:
          networkOffloadSupported: Flag to indicate whether network offloading is supported on the
              vSphere Distributed Switch.
          activeStandbyModeSupported: Flag to indicate whether the vSphere Distributed Switch supports
              connecting two DPUs to an offloading VDS and operating in an
              active-standby mode.
              
              If not set, the feature is not supported.
              
              Since: vSphere API Release 8.0.3.0
      
      Since: vSphere API Release 8.0.0.1
      """
      networkOffloadSupported: _typing.Optional[bool] = None
      activeStandbyModeSupported: _typing.Optional[bool] = None

   class PerfNicOffloadFeatureCapability(pyVmomi.vmodl.DynamicData):
      """
      The feature capabilities of performance NIC offloading features
      supported by the vSphere Distributed Switch.
      
      Attributes:
          supported: Flag to indicate whether performance NIC offloading is supported
              on the vSphere Distributed Switch.
              
              If not set, the feature is not supported.
      
      Since: vSphere API Release 9.1.0.0
      """
      supported: _typing.Optional[bool] = None

   class SystemTrafficCapabilities(pyVmomi.vmodl.DynamicData):
      """
      The feature capabilities of system traffic qualifiers supported by the
      vSphere Distributed Switch for Traffic Filtering and Marking.
      
      Attributes:
          systemTrafficQualifiers: List of system traffic qualifiers supported by the vSphere Distributed Switch
              for Traffic Filtering and Marking.
              
              See `pyVmomi.vim.DistributedVirtualSwitch.HostInfrastructureTrafficClass` for supported values.
      
      Since: vSphere API Release 9.1.0.0
      """
      systemTrafficQualifiers: list[str] = []

   class VmwareHealthCheckFeatureCapability(pyVmomi.vim.DistributedVirtualSwitch.HealthCheckFeatureCapability):
      """
      The feature capabilities of health check supported by the
      vSphere Distributed Switch
      
      Attributes:
          vlanMtuSupported: Flag to indicate whether vlan/mtu health check is supported on the
              vSphere Distributed Switch.
          teamingSupported: Flag to indicate whether teaming health check is supported on the
              vSphere Distributed Switch.
      """
      vlanMtuSupported: bool
      teamingSupported: bool

   class VspanFeatureCapability(pyVmomi.vmodl.DynamicData):
      """
      Indicators of support for version-specific Distributed Port Mirroring sessions.
      
      Attributes:
          mixedDestSupported: Flag to indicate whether mixed dest mirror session is supported on the
              vSphere Distributed Switch.
          dvportSupported: Flag to indicate whether dvport mirror session is supported on the
              vSphere Distributed Switch.
          remoteSourceSupported: Flag to indicate whether remote mirror source session is supported on the
              vSphere Distributed Switch.
          remoteDestSupported: Flag to indicate whether remote mirror destination session is supported on the
              vSphere Distributed Switch.
          encapRemoteSourceSupported: Flag to indicate whether encapsulated remote mirror source session is supported on the
              vSphere Distributed Switch.
          erspanProtocolSupported: Flag to indicate whether ERSPAN protocol encapsulation is supported
              on the vSphere Distributed Switch.
          mirrorNetstackSupported: Flag to indicate whether dvport mirror can be configured to use a
              dedicated network stack instance.
      """
      mixedDestSupported: bool
      dvportSupported: bool
      remoteSourceSupported: bool
      remoteDestSupported: bool
      encapRemoteSourceSupported: bool
      erspanProtocolSupported: _typing.Optional[bool] = None
      mirrorNetstackSupported: _typing.Optional[bool] = None

   class MtuCapability(pyVmomi.vmodl.DynamicData):
      """
      Indicators of support for version-specific supported MTU.
      
      Attributes:
          minMtuSupported: Minimum supported MTU on VDS.
          maxMtuSupported: Maximum supported MTU on VDS.
      
      Since: vSphere API Release 7.0.2.0
      """
      minMtuSupported: int
      maxMtuSupported: int

   class VspanPorts(pyVmomi.vmodl.DynamicData):
      """
      This class defines the ports, uplink ports name, vlans and IP addresses participating in a
      Distributed Port Mirroring session.
      
      See `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VspanSession`.
      
      Attributes:
          portKey: Individual ports to participate in the Distributed Port Mirroring session.
          uplinkPortName: Uplink ports used as destination ports to participate in the Distributed Port Mirroring session.
              
              A fault will be raised if uplinkPortName is used as source ports
              in any Distributed Port Mirroring session.
          wildcardPortConnecteeType: Wild card specification for source ports participating in the Distributed Port Mirroring session.
              
              See `pyVmomi.vim.dvs.PortConnectee.ConnecteeType` for valid values.
              Any port that has a connectee of the specified type has its receive traffic
              mirrored. A fault will be raised if wildcards are specified as destination
              ports or source ports mirroring traffic on the transmit side.
              It is to be not used.
          vlans: Vlan Ids for ingress source of Remote Mirror destination
              session.
          ipAddress: IP address for the destination of encapsulated remote mirror source session,
              IPv4 address is specified using dotted decimal notation.
              
              For example, \"192.0.2.1\".
              IPv6 addresses are 128-bit addresses represented as eight fields
              of up to four hexadecimal digits.
              A colon separates each field (:). For example,
              2001:DB8:101::230:6eff:fe04:d9ff.
      """
      portKey: list[str] = []
      uplinkPortName: list[str] = []
      wildcardPortConnecteeType: list[str] = []
      vlans: list[int] = []
      ipAddress: list[str] = []

   class VspanSession(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VspanSession` data object
      defines the configuration of a VLAN Services and Protocols for Advanced Networks
      (VSPAN) session.
      
      You use a VSPAN session for the following operations:
      - To mirror network traffic (inbound/outbound) from a set of source
        entities to a set of destination entities.
      - To assist in troubleshooting.
      - As input for security and other network analysis appliances.
        
      The type of entities that you can specify as source or destination is determined
      by the session type. You can use uplink distributed virtual ports only for
      mixed destination mirror VSPAN sessions (mixedDestMirror).
      For all sessions except mixedDestMirror sessions, you cannot
      use uplink distributed virtual ports as destination ports.
      sessionType is required for vSphere Distributed Switch 5.1 and later,
      ignored for prior version if set.
      
      Session Type
       - Source
       - Destination 
      
      mixedDestMirror
       - Distributed Ports
       - Distributed Ports + Uplink Ports Name
      
      dvPortMirror
       - Distributed Ports
       - Distributed Ports
      
      remoteMirrorSource
       - Distributed Ports
       - Uplink Ports Name
      
      remoteMirrorDest
       - VLAN
       - Distributed Ports
      
      encapRemoteMirrorSource
       - Distributed Ports
       - IP address
      
      Attributes:
          key: The generated key as the identifier for the session.
          name: The display name.
          description: The description for the session.
          enabled: Whether the session is enabled.
          sourcePortTransmitted: Source ports for which transmitted packets are mirrored.
          sourcePortReceived: Source ports for which received packets are mirrored.
          destinationPort: Destination ports that received the mirrored packets.
              
              You cannot use wild card ports as destination ports. If `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VspanPorts.wildcardPortConnecteeType`
              is set in the value, the reconfigure
              operation will raise a fault. Also any port designated in the value of
              this property can not match the wild card source port in any of the
              Distributed Port Mirroring session.
          encapsulationVlanId: VLAN ID used to encapsulate the mirrored traffic.
          stripOriginalVlan: Whether to strip the original VLAN tag.
              
              if false, the original VLAN tag
              will be preserved on the mirrored traffic. If `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VspanSession.encapsulationVlanId`
              has been set and this property is false, the frames will be double tagged
              with the original VLAN ID as the inner tag.
          mirroredPacketLength: An integer that describes how much of each frame to mirror.
              
              If unset, all
              of the frame would be mirrored. Setting this property to a smaller value
              is useful when the consumer will look only at the headers.
              The value cannot be less than 60.
          normalTrafficAllowed: Whether or not destination ports can send and receive \"normal\" traffic.
              
              Setting this to false will make mirror ports be used solely for mirroring
              and not double as normal access ports.
          sessionType: Type of the session.
              
              See
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VspanSessionType`
              for valid values.
              Default value is mixedDestMirror if unspecified in a VSPAN create operation.
          samplingRate: Sampling rate of the session.
              
              If its value is n, one of every n
              packets is mirrored.
              Valid values are between 1 to 65535, and default value is 1.
          encapType: Encapsulation type of the session.
              
              See
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VspanSessionEncapType`
              for valid values.
              Default value is encapProtocolGRE if unspecified in a
              VSPAN create operation.
          erspanId: ERSPAN ID of the session.
              
              Valid values are between 0 to 0x3ff, and default value is 0.
              This value is applicable only if encaptType is
              `erspan2` or
              `erspan3`
          erspanCOS: Class of Service of the monitored frame.
              
              Valid values are between 0 to 7, and default value is 0.
              This value is applicable only if encaptType is
              `erspan2` or
              `erspan3`
          erspanGraNanosec: Timestamp Granularity.
              
              If the value is false, timestamp-granularity will be microsecond.
              Otherwise the timestamp-granularity will be nanosecond
              This value is applicable only if encaptType is
              `erspan3`
          netstack: Netstack instance of the session.
      """
      key: _typing.Optional[str] = None
      name: _typing.Optional[str] = None
      description: _typing.Optional[str] = None
      enabled: bool
      sourcePortTransmitted: _typing.Optional[VmwareDistributedVirtualSwitch.VspanPorts] = None
      sourcePortReceived: _typing.Optional[VmwareDistributedVirtualSwitch.VspanPorts] = None
      destinationPort: _typing.Optional[VmwareDistributedVirtualSwitch.VspanPorts] = None
      encapsulationVlanId: _typing.Optional[int] = None
      stripOriginalVlan: bool
      mirroredPacketLength: _typing.Optional[int] = None
      normalTrafficAllowed: bool
      sessionType: _typing.Optional[str] = None
      samplingRate: _typing.Optional[int] = None
      encapType: _typing.Optional[str] = None
      erspanId: _typing.Optional[int] = None
      erspanCOS: _typing.Optional[int] = None
      erspanGraNanosec: _typing.Optional[bool] = None
      netstack: _typing.Optional[str] = None

   class IpfixConfig(pyVmomi.vmodl.DynamicData):
      """
      Configuration for IPFIX monitoring of distributed virtual switch traffic.
      
      IPFIX monitoring must be enabled to use this capability. See
      `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VmwarePortConfigPolicy`.`pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VmwarePortConfigPolicy.ipfixEnabled`.
      
      Attributes:
          collectorIpAddress: IP address for the ipfix collector, using IPv4 or IPv6.
              
              IPv6 is supported in vSphere Distributed Switch Version 6.0 or later.
              This must be set before ipfix monitoring can be enabled for the
              switch, or for any portgroup or port of the switch.
          collectorPort: Port for the ipfix collector.
              
              This must be set before ipfix monitoring
              can be enabled for the switch, or for any portgroup or port of the
              switch. Legal value range is 0-65535.
          observationDomainId: Observation Domain Id for the ipfix collector.
              
              Observation Domain Id is supported
              in vSphere Distributed Switch Version 6.0 or later.
              Legal value range is 0-((2^32)-1)
          activeFlowTimeout: The number of seconds after which \"active\" flows are forced to be
              exported to the collector.
              
              Legal value range is 60-3600. Default: 60.
          idleFlowTimeout: The number of seconds after which \"idle\" flows are forced to be
              exported to the collector.
              
              Legal value range is 10-600. Default: 15.
          samplingRate: The ratio of total number of packets to the number of packets
              analyzed.
              
              Set to 0 to disable sampling. Legal value range is 0-16384.
              Default: 4096.
              Since the 9.1 release, the ipfix sampling rate is no longer supported
              if NSX is enabled on this DVS host switch on that ESXi host.
              Any specified value for the sampling rate during DVS creation or
              reconfiguration will be ignored on ESXi hosts.
          internalFlowsOnly: Whether to limit analysis to traffic that has both source and
              destination served by the same host.
              
              Default: false.
      """
      collectorIpAddress: _typing.Optional[str] = None
      collectorPort: _typing.Optional[int] = None
      observationDomainId: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      activeFlowTimeout: int
      idleFlowTimeout: _typing.Optional[int] = None
      samplingRate: int
      internalFlowsOnly: bool

   class DpuFailoverPolicy(pyVmomi.vmodl.DynamicData):
      """
      This data structure defines the failover policy for a distributed
      virtual switch when network offload is enabled, specifically
      related to the Data Processing Unit(DPU).
      
      The active and standby uplinks are expected to be backed by different
      DPUs to provide redundancy. If DPU backing active uplinks fails, then
      the standby DPU takes over to ensure uninterrupted network connectivity.
      
      Attributes:
          activeUplink: The name of the active uplink(s).
              
              These uplink(s) must be backed
              by vmnic(s) from a single DPU.
          standbyUplink: The name of the standby uplink(s).
              
              These uplink(s) must be backed
              by vmnic(s) from a different DPU than the active uplink(s).
              An empty standbyUplink indicates that no failover action will be
              taken after the active DPU fails.
      
      Since: vSphere API Release 8.0.3.0
      """
      activeUplink: list[str] = []
      standbyUplink: list[str] = []

   class NetworkOffloadConfig(pyVmomi.vmodl.DynamicData):
      """
      This data structure defines the network offoad specific configuration of
      a distributed virtual switch.
      
      Attributes:
          dpuFailoverPolicy: The DPU failover policy of the switch.
              
              If this property is not set, all uplink ports are active uplinks.
      
      Since: vSphere API Release 8.0.3.0
      """
      dpuFailoverPolicy: _typing.Optional[VmwareDistributedVirtualSwitch.DpuFailoverPolicy] = None

   class RealTimeLanAnnotation(pyVmomi.vmodl.DynamicData):
      """
      This data structure defines the real-time configuration for a distributed
      virtual switch when real-time flag is enabled.
      
      The uplink(s) are set in
      two different LANs (LAN A/LAN B).
      
      Attributes:
          lanAUplink: The name(s) of the LAN A uplink(s).
          lanBUplink: The name(s) of the LAN B uplink(s).
      
      Since: vSphere API Release 8.0.3.1
      """
      lanAUplink: list[str] = []
      lanBUplink: list[str] = []

   class RealTimeConfig(pyVmomi.vmodl.DynamicData):
      """
      This data structure defines the real-time specific configuration of
      a distributed virtual switch when real-time flag is enabled.
      
      Attributes:
          allowed: The flag to indicate whether real-time configuration is allowed on
              the switch.
          lanAnnotation: The real-time LANs (LAN A/LAN B) annotation, to mark the uplink(s)
              for each LAN.
      
      Since: vSphere API Release 8.0.3.1
      """
      allowed: _typing.Optional[bool] = None
      lanAnnotation: _typing.Optional[VmwareDistributedVirtualSwitch.RealTimeLanAnnotation] = None

   class ConfigInfo(pyVmomi.vim.DistributedVirtualSwitch.ConfigInfo):
      """
      This class defines the VMware specific configuration for
      DistributedVirtualSwitch.
      
      Attributes:
          vspanSession: The Distributed Port Mirroring sessions in the switch.
          pvlanConfig: The PVLAN configured in the switch.
          maxMtu: The maximum MTU in the switch.
          linkDiscoveryProtocolConfig: See `pyVmomi.vim.host.LinkDiscoveryProtocolConfig`.
          ipfixConfig: Configuration for ipfix monitoring of the switch traffic.
              
              This must be
              set before ipfix monitoring can be enabled for the switch, or for any
              portgroup or port of the switch.
          lacpGroupConfig: The Link Aggregation Control Protocol groups in the switch.
          lacpApiVersion: The Link Aggregation Control Protocol group version in the switch.
              
              See `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.LacpApiVersion` for valid values.
          multicastFilteringMode: The Multicast Filtering mode in the switch.
              
              See `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.MulticastFilteringMode` for valid values.
          networkOffloadSpecId: Indicate the ID of NetworkOffloadSpec used in the switch.
              
              ID \"None\" means that network offload is not allowed in the switch.
              
              Since: vSphere API Release 8.0.0.1
          networkOffloadConfig: The network offload specific configuration of the switch.
              
              It is only set when network offload is allowed
              (`pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.ConfigInfo.networkOffloadSpecId`
              is not \"None\").
              
              Since: vSphere API Release 8.0.3.0
          realTimeConfig: The real-time specific configuration of the switch.
              
              Since: vSphere API Release 8.0.3.1
      """
      vspanSession: list[VmwareDistributedVirtualSwitch.VspanSession] = []
      pvlanConfig: list[VmwareDistributedVirtualSwitch.PvlanMapEntry] = []
      maxMtu: int
      linkDiscoveryProtocolConfig: _typing.Optional[pyVmomi.vim.host.LinkDiscoveryProtocolConfig] = None
      ipfixConfig: _typing.Optional[VmwareDistributedVirtualSwitch.IpfixConfig] = None
      lacpGroupConfig: list[VmwareDistributedVirtualSwitch.LacpGroupConfig] = []
      lacpApiVersion: _typing.Optional[str] = None
      multicastFilteringMode: _typing.Optional[str] = None
      networkOffloadSpecId: _typing.Optional[str] = None
      networkOffloadConfig: _typing.Optional[VmwareDistributedVirtualSwitch.NetworkOffloadConfig] = None
      realTimeConfig: _typing.Optional[VmwareDistributedVirtualSwitch.RealTimeConfig] = None

   class ConfigSpec(pyVmomi.vim.DistributedVirtualSwitch.ConfigSpec):
      """
      This class defines the VMware specific configuration for
      DistributedVirtualSwitch.
      
      Attributes:
          pvlanConfigSpec: The PVLAN configuration specification.
              
              A `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry`
              that has the same value for
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry.primaryVlanId` and
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry.secondaryVlanId`
              is referred to as a primary PVLAN entry.
              Otherwise, the `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry`
              is referred to as a secondary PVLAN entry.
              
              The `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry.pvlanType`
              of a primary PVLAN entry must be
              `promiscuous`.
              A secondary PVLAN entry can have a
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry.pvlanType`
              of either
              `community` or
              `isolated`.
              
              Primary PVLAN entries must be explicitly added.
              If there is no primary PVLAN entry corresponding to the
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry.primaryVlanId`
              of a secondary PVLAN entry, a fault is thrown.
              
              While deleting a primary PVLAN entry, any associated secondary PVLAN
              entries must be explicitly deleted.
          vspanConfigSpec: The Distributed Port Mirroring configuration specification.
              
              The VSPAN
              sessions in the array cannot be of the same key.
          maxMtu: The maximum MTU in the switch.
          linkDiscoveryProtocolConfig: See `pyVmomi.vim.host.LinkDiscoveryProtocolConfig`.
          ipfixConfig: Configuration for ipfix monitoring of the switch traffic.
              
              This must be
              set before ipfix monitoring can be enabled for the switch, or for any
              portgroup or port of the switch.
          lacpApiVersion: The Link Aggregation Control Protocol group version in the switch.
              
              See `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.LacpApiVersion` for valid values.
          multicastFilteringMode: The Multicast Filtering mode in the switch.
              
              See `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.MulticastFilteringMode` for valid values.
          networkOffloadSpecId: Indicate the ID of NetworkOffloadSpec used in the switch.
              
              Unset it when network offload is not allowed when creating a switch.
              Use ID \"None\" to change network offload from allowed to not allowed.
              
              Since: vSphere API Release 8.0.0.1
          networkOffloadConfig: The network offload specific configuration of the switch.
              
              This can be set only when network offload is allowed
              (`pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.ConfigInfo.networkOffloadSpecId`
              is not \"None\").
              
              Since: vSphere API Release 8.0.3.0
          realTimeConfig: The real-time specific configuration of the switch.
              
              Since: vSphere API Release 8.0.3.1
      """
      pvlanConfigSpec: list[VmwareDistributedVirtualSwitch.PvlanConfigSpec] = []
      vspanConfigSpec: list[VmwareDistributedVirtualSwitch.VspanConfigSpec] = []
      maxMtu: _typing.Optional[int] = None
      linkDiscoveryProtocolConfig: _typing.Optional[pyVmomi.vim.host.LinkDiscoveryProtocolConfig] = None
      ipfixConfig: _typing.Optional[VmwareDistributedVirtualSwitch.IpfixConfig] = None
      lacpApiVersion: _typing.Optional[str] = None
      multicastFilteringMode: _typing.Optional[str] = None
      networkOffloadSpecId: _typing.Optional[str] = None
      networkOffloadConfig: _typing.Optional[VmwareDistributedVirtualSwitch.NetworkOffloadConfig] = None
      realTimeConfig: _typing.Optional[VmwareDistributedVirtualSwitch.RealTimeConfig] = None

   class UplinkPortOrderPolicy(pyVmomi.vim.InheritablePolicy):
      """
      This data object type describes uplink port ordering policy for a
      distributed virtual port.
      
      A uplink port can be in the active
      list, the standby list, or neither. It cannot be in both lists.
      
      Attributes:
          activeUplinkPort: List of active uplink ports used for load balancing.
          standbyUplinkPort: Standby uplink ports used for failover.
      """
      activeUplinkPort: list[str] = []
      standbyUplinkPort: list[str] = []

   class FailureCriteria(pyVmomi.vim.InheritablePolicy):
      """
      This data object type describes the network adapter failover
      detection algorithm for a network adapter team.
      
      Attributes:
          checkSpeed: To use link speed as the criteria, checkSpeed must be one of
              the following values:
              - exact: Use exact speed to detect link failure.
                speed is the configured exact speed in megabits per second.
              - minimum: Use minimum speed to detect failure.
                speed is the configured minimum speed in megabits per second.
              - empty string: Do not use link speed to detect failure.
                speed is unused in this case.
          checkDuplex: The flag to indicate whether or not to use the link duplex reported
              by the driver as link selection criteria.
              
              If checkDuplex is true, then fullDuplex is the configured
              duplex mode. The link is considered bad if the link duplex reported
              by driver is not the same as fullDuplex.
              
              If checkDuplex is false, then fullDuplex is unused, and
              link duplexity is not used as a detection method.
          checkErrorPercent: The flag to indicate whether or not to use link error percentage
              to detect failure.
              
              If checkErrorPercent is true, then percentage is the configured
              error percentage that is tolerated. The link is considered bad
              if error rate exceeds percentage.
              
              If checkErrorPercent is false, percentage is unused, and
              error percentage is not used as a detection method.
          checkBeacon: The flag to indicate whether or not to enable this property to
              enable beacon probing as a method to validate
              the link status of a physical network adapter.
              
              checkBeacon can be enabled only if the VirtualSwitch has been
              configured to use the beacon. Attempting to set checkBeacon
              on a PortGroup or VirtualSwitch that does not have beacon probing
              configured for the applicable VirtualSwitch results in an error.
      """
      checkSpeed: _typing.Optional[pyVmomi.vim.StringPolicy] = None
      speed: _typing.Optional[pyVmomi.vim.IntPolicy] = None
      checkDuplex: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      fullDuplex: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      checkErrorPercent: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      percentage: _typing.Optional[pyVmomi.vim.IntPolicy] = None
      checkBeacon: _typing.Optional[pyVmomi.vim.BoolPolicy] = None

   class UplinkPortTeamingPolicy(pyVmomi.vim.InheritablePolicy):
      """
      Policy for a uplink port team.
      
      Attributes:
          policy: Network adapter teaming policy.
              
              The policy defines the way traffic
              from the clients of the team is routed through the different uplinks
              in the team. The policies supported on the VDS platform is one of
              `pyVmomi.vim.DistributedVirtualSwitch.FeatureCapability.nicTeamingPolicy`.
          reversePolicy: The flag to indicate whether or not the teaming policy is applied
              to inbound frames as well.
              
              Also see `pyVmomi.vim.host.NetworkPolicy.NicTeamingPolicy.reversePolicy`
          notifySwitches: Flag to specify whether or not to notify the physical switch
              if a link fails.
              
              Also see `pyVmomi.vim.host.NetworkPolicy.NicTeamingPolicy.notifySwitches`
          rollingOrder: The flag to indicate whether or not to use a rolling policy when
              restoring links.
              
              Also see `pyVmomi.vim.host.NetworkPolicy.NicTeamingPolicy.rollingOrder`
          failureCriteria: Failover detection policy for the uplink port team.
          uplinkPortOrder: Failover order policy for uplink ports on the hosts.
      """
      policy: _typing.Optional[pyVmomi.vim.StringPolicy] = None
      reversePolicy: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      notifySwitches: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      rollingOrder: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      failureCriteria: _typing.Optional[VmwareDistributedVirtualSwitch.FailureCriteria] = None
      uplinkPortOrder: _typing.Optional[VmwareDistributedVirtualSwitch.UplinkPortOrderPolicy] = None

   class VlanSpec(pyVmomi.vim.InheritablePolicy):
      """Base class for Vlan Specification for ports."""
      pass

   class PvlanSpec(VmwareDistributedVirtualSwitch.VlanSpec):
      """
      This data type defines the configuration when PVLAN id is to be
      used for the ports.
      
      Attributes:
          pvlanId: The `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry.secondaryVlanId`.
      """
      pvlanId: int

   class VlanIdSpec(VmwareDistributedVirtualSwitch.VlanSpec):
      """
      This data type defines the configuration when single vlanId is used for
      the port.
      
      Attributes:
          vlanId: The VLAN ID for ports.
              
              Possible values:
              - A value of 0 specifies that you do not want the port associated
                with a VLAN.
              - A value from 1 to 4094 specifies a VLAN ID for the port.
      """
      vlanId: int

   class TrunkVlanSpec(VmwareDistributedVirtualSwitch.VlanSpec):
      """
      This data type specifies that the port uses trunk mode,
      which allows the guest operating system to manage its own VLAN tags.
      
      Attributes:
          vlanId: The VlanId range for the trunk port.
              
              The valid VlanId range is
              from 0 to 4094. Overlapping ranges are allowed.
      """
      vlanId: list[pyVmomi.vim.NumericRange] = []

   class SecurityPolicy(pyVmomi.vim.InheritablePolicy):
      """
      This data object type describes security policy governing ports.
      
      Attributes:
          allowPromiscuous: The flag to indicate whether or not all traffic is seen
              on the port.
          macChanges: The flag to indicate whether or not the Media Access
              Control (MAC) address can be changed.
          forgedTransmits: The flag to indicate whether or not the virtual network adapter
              should be allowed to send network traffic with a different MAC
              address than that of the virtual network adapter.
      """
      allowPromiscuous: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      macChanges: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      forgedTransmits: _typing.Optional[pyVmomi.vim.BoolPolicy] = None

   class MacLimitPolicyType(pyVmomi.VmomiSupport.Enum):
      allow: _typing.ClassVar['VmwareDistributedVirtualSwitch.MacLimitPolicyType'] = 'allow'
      drop: _typing.ClassVar['VmwareDistributedVirtualSwitch.MacLimitPolicyType'] = 'drop'

   class MacLearningPolicy(pyVmomi.vim.InheritablePolicy):
      """
      This data object type describes MAC learning policy of a port.
      
      Attributes:
          enabled: The flag to indicate if source MAC address learning is allowed.
          allowUnicastFlooding: The flag to allow flooding of unlearned MAC for ingress traffic.
          limit: The maximum number of MAC addresses that can be learned.
          limitPolicy: The default switching policy after MAC limit is exceeded.
              
              See `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.MacLimitPolicyType`
              for valid values.
      """
      enabled: bool
      allowUnicastFlooding: _typing.Optional[bool] = None
      limit: _typing.Optional[int] = None
      limitPolicy: _typing.Optional[str] = None

   class MacManagementPolicy(pyVmomi.vim.InheritablePolicy):
      """
      This data object type describes MAC management policy of a port.
      
      Attributes:
          allowPromiscuous: The flag to indicate whether or not all traffic is seen
              on the port.
          macChanges: The flag to indicate whether or not the Media Access
              Control (MAC) address can be changed.
          forgedTransmits: The flag to indicate whether or not the virtual network adapter
              should be allowed to send network traffic with a different MAC
              address than that of the virtual network adapter.
          macLearningPolicy: The MAC learning policy.
      """
      allowPromiscuous: _typing.Optional[bool] = None
      macChanges: _typing.Optional[bool] = None
      forgedTransmits: _typing.Optional[bool] = None
      macLearningPolicy: _typing.Optional[VmwareDistributedVirtualSwitch.MacLearningPolicy] = None

   class VmwarePortConfigPolicy(DistributedVirtualPort.Setting):
      """
      This class defines the VMware specific configuration for
      DistributedVirtualPort.
      
      Attributes:
          vlan: The VLAN Specification of the port.
          qosTag: The Quality Of Service tagging of the port.
          uplinkTeamingPolicy: The uplink teaming policy.
              
              This property is ignored for uplink
              ports.
          securityPolicy: The security policy.
          ipfixEnabled: True if ipfix monitoring is enabled.
              
              To successfully enable ipfix
              monitoring, the switch must have an assigned
              `pyVmomi.vim.DistributedVirtualSwitch.ConfigInfo.switchIpAddress`
              and an appropriately populated
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.ConfigInfo.ipfixConfig`
              that specifies a collector IP address and port.
              Since the 9.1 release, ipfix monitoring can not be enabled on uplink portgroups.
          txUplink: If true, a copy of packets sent to the switch will always be forwarded to
              an uplink in addition to the regular packet forwarded done by the switch.
          lacpPolicy: Link Aggregation Control Protocol policy.
              
              This policy is ignored on non-uplink portgroups.
              Setting this policy at port level is not supported.
          macManagementPolicy: The MAC learning policy.
          VNI: The VNI number of overlay logical switch, which is used by
              NSX portgroup.
      """
      vlan: _typing.Optional[VmwareDistributedVirtualSwitch.VlanSpec] = None
      qosTag: _typing.Optional[pyVmomi.vim.IntPolicy] = None
      uplinkTeamingPolicy: _typing.Optional[VmwareDistributedVirtualSwitch.UplinkPortTeamingPolicy] = None
      securityPolicy: _typing.Optional[VmwareDistributedVirtualSwitch.SecurityPolicy] = None
      ipfixEnabled: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      txUplink: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      lacpPolicy: _typing.Optional[VmwareDistributedVirtualSwitch.UplinkLacpPolicy] = None
      macManagementPolicy: _typing.Optional[VmwareDistributedVirtualSwitch.MacManagementPolicy] = None
      VNI: _typing.Optional[pyVmomi.vim.IntPolicy] = None

   class VMwarePortgroupPolicy(DistributedVirtualPortgroup.PortgroupPolicy):
      """
      This class defines the VMware specific configuration for
      DistributedVirtualPort.
      
      Attributes:
          vlanOverrideAllowed: Allow the setting of
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VlanIdSpec.vlanId`, trunk
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.TrunkVlanSpec.vlanId`, or
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.PvlanSpec.pvlanId`
              for an individual port to override the setting in
              `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo.defaultPortConfig` of
              a portgroup.
          uplinkTeamingOverrideAllowed: Allow the setting of
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VmwarePortConfigPolicy.uplinkTeamingPolicy`
              for an individual port to override the setting in
              `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo.defaultPortConfig` of
              a portgroup.
          securityPolicyOverrideAllowed: Allow the setting of
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VmwarePortConfigPolicy.securityPolicy`
              for an individual port to override the setting in
              `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo.defaultPortConfig` of
              a portgroup.
          ipfixOverrideAllowed: Allow the setting of
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VmwarePortConfigPolicy.ipfixEnabled`
              for an individual port to override the setting in
              `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo.defaultPortConfig` of
              a portgroup.
              
              Since the 9.1 release, it can not be set to True on uplink portgroups.
          macManagementOverrideAllowed: Allow the setting of
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VmwarePortConfigPolicy.macManagementPolicy`
              for an individual port to override the setting in
              `pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigInfo.defaultPortConfig` of
              a portgroup.
      """
      vlanOverrideAllowed: bool
      uplinkTeamingOverrideAllowed: bool
      securityPolicyOverrideAllowed: bool
      ipfixOverrideAllowed: _typing.Optional[bool] = None
      macManagementOverrideAllowed: _typing.Optional[bool] = None

   class PvlanPortType(pyVmomi.VmomiSupport.Enum):
      """
      The PVLAN port types.
      
      Attributes:
          promiscuous: The port can communicate with all other ports within the same PVLAN,
              including the isolated and community ports .
          isolated: The port can only communicate with the promiscuous ports within the
              same PVLAN, any other traffics are blocked.
          community: The ports communicates with other community ports and with
              promiscuous ports within the same PVLAN.
              
              any other traffics are
              blocked.
      """
      promiscuous: _typing.ClassVar['VmwareDistributedVirtualSwitch.PvlanPortType'] = 'promiscuous'
      isolated: _typing.ClassVar['VmwareDistributedVirtualSwitch.PvlanPortType'] = 'isolated'
      community: _typing.ClassVar['VmwareDistributedVirtualSwitch.PvlanPortType'] = 'community'

   class PvlanConfigSpec(pyVmomi.vmodl.DynamicData):
      """
      This class defines the configuration of a PVLAN map entry
      
      Attributes:
          pvlanEntry: The PVLAN entry to be added or removed.
          operation: Operation type.
              
              See
              `pyVmomi.vim.ConfigSpecOperation` for valid values,
              except for the \"edit\" value, which is not supported.
      """
      pvlanEntry: VmwareDistributedVirtualSwitch.PvlanMapEntry
      operation: str

   class PvlanMapEntry(pyVmomi.vmodl.DynamicData):
      """
      The class represents a PVLAN id.
      
      Attributes:
          primaryVlanId: The primary VLAN ID.
              
              The VLAN IDs of 0 and 4095 are reserved
              and cannot be used in this property.
          secondaryVlanId: The secondary VLAN ID.
              
              The VLAN IDs of 0 and 4095 are reserved
              and cannot be used in this property.
          pvlanType: The type of PVLAN.
              
              See `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.PvlanPortType`
              for valid values.
      """
      primaryVlanId: int
      secondaryVlanId: int
      pvlanType: str

   class VspanConfigSpec(pyVmomi.vmodl.DynamicData):
      """
      This class defines the configuration of a Distributed Port Mirroring session.
      
      A Distributed Port Mirroring session
      
      Attributes:
          vspanSession: The Distributed Port Mirroring session to be reconfigured.
          operation: Operation type, see
              `pyVmomi.vim.ConfigSpecOperation` for valid values.
      """
      vspanSession: VmwareDistributedVirtualSwitch.VspanSession
      operation: str

   class VspanSessionEncapType(pyVmomi.VmomiSupport.Enum):
      """
      Distributed Port Mirroring session Encapsulation types.
      
      Attributes:
          gre: Encapsulate original packets with GRE protocol
          erspan2: Encapsulate original packets with ERSPAN Type2 protocol
          erspan3: Encapsulate original packets with ERSPAN Type3 protocol
      """
      gre: _typing.ClassVar['VmwareDistributedVirtualSwitch.VspanSessionEncapType'] = 'gre'
      erspan2: _typing.ClassVar['VmwareDistributedVirtualSwitch.VspanSessionEncapType'] = 'erspan2'
      erspan3: _typing.ClassVar['VmwareDistributedVirtualSwitch.VspanSessionEncapType'] = 'erspan3'

   class VspanSessionType(pyVmomi.VmomiSupport.Enum):
      """
      Distributed Port Mirroring session types.
      
      Attributes:
          mixedDestMirror: In mixedDestMirror session, Distributed Ports can be used as source entities,
              and both Distributed Ports and Uplink Ports Name can be used as destination entities.
          dvPortMirror: In dvPortMirror session, Distributed Ports can be used as both source
              and destination entities.
          remoteMirrorSource: In remoteMirrorSource session, Distributed Ports can be used as source entities,
              and uplink ports name can be used as destination entities.
          remoteMirrorDest: In remoteMirrorDest session, vlan Ids can be used as source entities,
              and Distributed Ports can be used as destination entities.
          encapsulatedRemoteMirrorSource: In encapsulatedRemoteMirrorSource session, Distributed Ports can be used as source entities,
              and Ip address can be used as destination entities.
      """
      mixedDestMirror: _typing.ClassVar['VmwareDistributedVirtualSwitch.VspanSessionType'] = 'mixedDestMirror'
      dvPortMirror: _typing.ClassVar['VmwareDistributedVirtualSwitch.VspanSessionType'] = 'dvPortMirror'
      remoteMirrorSource: _typing.ClassVar['VmwareDistributedVirtualSwitch.VspanSessionType'] = 'remoteMirrorSource'
      remoteMirrorDest: _typing.ClassVar['VmwareDistributedVirtualSwitch.VspanSessionType'] = 'remoteMirrorDest'
      encapsulatedRemoteMirrorSource: _typing.ClassVar['VmwareDistributedVirtualSwitch.VspanSessionType'] = 'encapsulatedRemoteMirrorSource'

   class VmwareHealthCheckConfig(pyVmomi.vim.DistributedVirtualSwitch.HealthCheckConfig):
      """
      This class defines health check configuration for
      VMware vSphere Distributed Switch.
      """
      pass

   class VlanMtuHealthCheckConfig(VmwareDistributedVirtualSwitch.VmwareHealthCheckConfig):
      """
      This class defines the vlan and mtu health check configuration.
      
      Vlan health check is used to check whether vlans are trunked by the physical
      switch connected to the uplink ports.
      MTU health check is used to verify current MTU setting workable on all uplink ports of
      the vSphere Distributed Switch.
      """
      pass

   class TeamingHealthCheckConfig(VmwareDistributedVirtualSwitch.VmwareHealthCheckConfig):
      """
      This class defines the teaming health check configuration.
      
      Teaming health check is used to check whether the teaming policy configuration
      of the vSphere Distributed Switch matches the physical switch.
      """
      pass

   class VlanHealthCheckResult(HostMember.UplinkHealthCheckResult):
      """
      This class defines Vlan health check result of an uplink port
      in the VMware vSphered Distributed Switch.
      
      Attributes:
          trunkedVlan: The vlans which are trunked by the physical switch connected to the uplink port.
              
              If the vlan is not a range, but a single Id,
              both start and end have the same value with the single vlan Id.
          untrunkedVlan: The vlans which are not trunked by the physical switch connected to the uplink port.
              
              If the vlan is not a range, but a single Id,
              both start and end have the same value with the single vlan Id.
      """
      trunkedVlan: list[pyVmomi.vim.NumericRange] = []
      untrunkedVlan: list[pyVmomi.vim.NumericRange] = []

   class MtuHealthCheckResult(HostMember.UplinkHealthCheckResult):
      """
      This class defines MTU health check result of an uplink port
      in the VMware vSphered Distributed Switch.
      
      Attributes:
          mtuMismatch: True if the MTU configured in the vSphere Distributed Switch is different from
              the value configured in the Physical NIC, else false.
              
              If it is true,
              MTU health check is stopped. In this case, `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.MtuHealthCheckResult.vlanSupportSwitchMtu` and
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.MtuHealthCheckResult.vlanNotSupportSwitchMtu` will not have values.
          vlanSupportSwitchMtu: The vlan's MTU setting on physical switch allows vSphere Distributed Switch
              max MTU size packets passing.
              
              If the vlan is not a range, but a single Id,
              both start and end have the same value with the single vlan Id.
          vlanNotSupportSwitchMtu: The vlan's MTU setting on physical switch does not allow
              vSphere Distributed Switch max MTU size packets passing.
              
              If the vlan is not a range, but a single Id,
              both start and end have the same value with the single vlan Id.
      """
      mtuMismatch: bool
      vlanSupportSwitchMtu: list[pyVmomi.vim.NumericRange] = []
      vlanNotSupportSwitchMtu: list[pyVmomi.vim.NumericRange] = []

   class TeamingMatchStatus(pyVmomi.VmomiSupport.Enum):
      """
      The teaming health check match status.
      
      Attributes:
          iphashMatch: The value of 'loadbalance_ip' is used in a uplink teaming policy
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortTeamingPolicy.policy`
              in the vSphere Distributed Switch, and the external physical switch
              has the matching EtherChannel configuration.
          nonIphashMatch: The value of 'loadbalance_ip' is not used in a uplink teaming policy
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortTeamingPolicy.policy`
              in the vSphere Distributed Switch, and the external physical switch
              does not have EtherChannel configuration.
          iphashMismatch: The value of 'loadbalance_ip' is used in a uplink teaming policy
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortTeamingPolicy.policy`
              in the vSphere Distributed Switch, but the external physical switch
              does not have the matching EtherChannel configuration.
          nonIphashMismatch: The value of 'loadbalance_ip' is not used in a uplink teaming policy
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortTeamingPolicy.policy`
              in the vSphere Distributed Switch, but the external physical switch
              has EtherChannel configuration.
      """
      iphashMatch: _typing.ClassVar['VmwareDistributedVirtualSwitch.TeamingMatchStatus'] = 'iphashMatch'
      nonIphashMatch: _typing.ClassVar['VmwareDistributedVirtualSwitch.TeamingMatchStatus'] = 'nonIphashMatch'
      iphashMismatch: _typing.ClassVar['VmwareDistributedVirtualSwitch.TeamingMatchStatus'] = 'iphashMismatch'
      nonIphashMismatch: _typing.ClassVar['VmwareDistributedVirtualSwitch.TeamingMatchStatus'] = 'nonIphashMismatch'

   class TeamingHealthCheckResult(HostMember.HealthCheckResult):
      """
      This class defines teaming health check result of a host that
      joined the VMware vSphered Distributed Switch.
      
      Attributes:
          teamingStatus: Teaming check status.
              
              See `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.TeamingMatchStatus`
              for valid values.
      """
      teamingStatus: str

   class UplinkLacpPolicy(pyVmomi.vim.InheritablePolicy):
      """
      Deprecated: as of vSphere API 5.5.This class defines VMware specific Link Aggregation Control Protocol
      policy.
      
      Attributes:
          enable: The flag to indicate whether or not
              Link Aggregation Control Protocol is enabled.
              
              It can be set to true if the value of
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.ConfigInfo.lacpApiVersion`
              is `singleLag`,
              else an exception ConflictingConfiguration will be thrown.
          mode: The mode of Link Aggregation Control Protocol.
              
              See `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.UplinkLacpMode` for valid values.
      """
      enable: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      mode: _typing.Optional[pyVmomi.vim.StringPolicy] = None

   class LacpGroupConfig(pyVmomi.vmodl.DynamicData):
      """
      This class defines VMware specific multiple IEEE 802.3ad
      Dynamic Link Aggregation Control Protocol groups.
      
      Attributes:
          key: The generated key as the identifier for the Link Aggregation group.
          name: The display name.
          mode: The mode of Link Aggregation Control Protocol.
              
              See `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.UplinkLacpMode` for valid values.
          uplinkNum: The number of uplink ports.
          loadbalanceAlgorithm: Load balance policy.
              
              See `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm` for valid values.
          vlan: The VLAN Specification of the Uplink Ports in the Link Aggregation group.
          ipfix: Ipfix configuration of the Link Aggregation
              Control Protocol group.
              
              Since the 9.1 release, ipfix monitoring can not be enabled on
              Link Aggregation group anymore. Because
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VMwarePortgroupPolicy.ipfixOverrideAllowed`
              can not be set to True on uplink portgroups.
          uplinkName: Names for the Uplink Ports in the group.
              
              This property is ignored in an update operation.
          uplinkPortKey: Keys for the Uplink Ports in the group.
              
              This property is ignored in an update operation.
          timeoutMode: The timeout mode of LACP group.
              
              See `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.UplinkLacpTimeoutMode` for valid values.
              
              Since: vSphere API Release 7.0.2.0
      """
      key: _typing.Optional[str] = None
      name: _typing.Optional[str] = None
      mode: _typing.Optional[str] = None
      uplinkNum: _typing.Optional[int] = None
      loadbalanceAlgorithm: _typing.Optional[str] = None
      vlan: _typing.Optional[VmwareDistributedVirtualSwitch.LagVlanConfig] = None
      ipfix: _typing.Optional[VmwareDistributedVirtualSwitch.LagIpfixConfig] = None
      uplinkName: list[str] = []
      uplinkPortKey: list[str] = []
      timeoutMode: _typing.Optional[str] = None

   class LagVlanConfig(pyVmomi.vmodl.DynamicData):
      """
      This class defines the vlan configuration of the Link Aggregation
      Control Protocol group.
      
      Attributes:
          vlanId: The VlanId range for the Uplink Ports in the Link Aggregation
              Control Protocol group.
              
              The valid VlanId range is from 0 to 4094. Overlapping ranges are allowed.
              If set, this property will override the VLAN configuration of Uplink Ports
              in the Link Aggregation Control Protocol group.
              Thus they are no longer inheriting VLAN configuration from their Uplink Port Group.
              Setting this property would require
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VMwarePortgroupPolicy.vlanOverrideAllowed`
              of all the Uplink Port Groups to be true,
              otherwise ConflictingConfiguration fault will be raised.
      """
      vlanId: list[pyVmomi.vim.NumericRange] = []

   class LagIpfixConfig(pyVmomi.vmodl.DynamicData):
      """
      Deprecated: as of vSphere API 9.1.This class defines the ipfix configuration of the Link Aggregation
      Control Protocol group.
      
      Since the 9.1 release, ipfix monitoring can not be enabled on
      Link Aggregation group anymore. Because
      `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VMwarePortgroupPolicy.ipfixOverrideAllowed`
      can not be set to True on uplink portgroups.
      
      Attributes:
          ipfixEnabled: True if ipfix monitoring is enabled in the Link Aggregation Control Protocol group.
              
              If set, this property will override the ipfix configuration of Uplink Ports
              in the Link Aggregation Control Protocol group.
              Thus they are no longer inheriting ipfix configuration from their Uplink Port Group.
              Setting this property would require
              `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.VMwarePortgroupPolicy.ipfixOverrideAllowed`
              of all the Uplink Port Groups to be true,
              otherwise ConflictingConfiguration fault will be raised.
      """
      ipfixEnabled: _typing.Optional[bool] = None

   class UplinkLacpMode(pyVmomi.VmomiSupport.Enum):
      """
      Link Aggregation Control Protocol policy modes.
      
      Attributes:
          active: Link Aggregation Control Protocol always sends frames along the configured uplinks
          passive: Link Aggregation Control Protocol acts as \"speak when spoken to\".
      """
      active: _typing.ClassVar['VmwareDistributedVirtualSwitch.UplinkLacpMode'] = 'active'
      passive: _typing.ClassVar['VmwareDistributedVirtualSwitch.UplinkLacpMode'] = 'passive'

   class UplinkLacpTimeoutMode(pyVmomi.VmomiSupport.Enum):
      """
      Link Aggregation Control Protocol timeout policy modes.
      
      Attributes:
          fast: Set long timeout for vmnics in one LACP LAG.
              
              Device send fast LACPDUs
          slow: Set short timeout for vmnics in one LACP LAG.
              
              Device send slow LACPDUs
      
      Since: vSphere API Release 7.0.2.0
      """
      fast: _typing.ClassVar['VmwareDistributedVirtualSwitch.UplinkLacpTimeoutMode'] = 'fast'
      slow: _typing.ClassVar['VmwareDistributedVirtualSwitch.UplinkLacpTimeoutMode'] = 'slow'

   class LacpGroupSpec(pyVmomi.vmodl.DynamicData):
      """
      This class defines the configuration of a Link Aggregation
      Control Protocol group.
      
      Attributes:
          lacpGroupConfig: The Link Aggregation Control Protocol group to be configured.
          operation: Operation type, see
              `pyVmomi.vim.ConfigSpecOperation` for valid values.
      """
      lacpGroupConfig: VmwareDistributedVirtualSwitch.LacpGroupConfig
      operation: str

   class LacpLoadBalanceAlgorithm(pyVmomi.VmomiSupport.Enum):
      """
      Load balance algorithm in a Link Aggregation Control Protocol group.
      
      Attributes:
          srcMac: Source MAC address
          destMac: Destination MAC address
          srcDestMac: Source and destination MAC address
          destIpVlan: Destination IP and VLAN
          srcIpVlan: Source IP and VLAN
          srcDestIpVlan: Source and destination IP and VLAN
          destTcpUdpPort: Destination TCP/UDP port number
          srcTcpUdpPort: Source TCP/UDP port number
          srcDestTcpUdpPort: Source and destination TCP/UDP port number
          destIpTcpUdpPort: Destination IP and TCP/UDP port number
          srcIpTcpUdpPort: Source IP and TCP/UDP port number
          srcDestIpTcpUdpPort: Source and destination IP and TCP/UDP port number
          destIpTcpUdpPortVlan: Destination IP, TCP/UDP port number and VLAN
          srcIpTcpUdpPortVlan: Source IP, TCP/UDP port number and VLAN
          srcDestIpTcpUdpPortVlan: Source and destination IP,
              source and destination TCP/UDP port number and VLAN.
          destIp: Destination IP
          srcIp: Source IP
          srcDestIp: Source and Destination IP
          vlan: VLAN only
          srcPortId: Source Virtual Port Id
      """
      srcMac: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'srcMac'
      destMac: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'destMac'
      srcDestMac: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'srcDestMac'
      destIpVlan: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'destIpVlan'
      srcIpVlan: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'srcIpVlan'
      srcDestIpVlan: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'srcDestIpVlan'
      destTcpUdpPort: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'destTcpUdpPort'
      srcTcpUdpPort: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'srcTcpUdpPort'
      srcDestTcpUdpPort: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'srcDestTcpUdpPort'
      destIpTcpUdpPort: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'destIpTcpUdpPort'
      srcIpTcpUdpPort: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'srcIpTcpUdpPort'
      srcDestIpTcpUdpPort: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'srcDestIpTcpUdpPort'
      destIpTcpUdpPortVlan: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'destIpTcpUdpPortVlan'
      srcIpTcpUdpPortVlan: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'srcIpTcpUdpPortVlan'
      srcDestIpTcpUdpPortVlan: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'srcDestIpTcpUdpPortVlan'
      destIp: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'destIp'
      srcIp: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'srcIp'
      srcDestIp: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'srcDestIp'
      vlan: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'vlan'
      srcPortId: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm'] = 'srcPortId'

   class LacpApiVersion(pyVmomi.VmomiSupport.Enum):
      """
      Link Aggregation Control Protocol API versions.
      
      Attributes:
          singleLag: One Link Aggregation Control Protocol group in the switch
          multipleLag: Multiple Link Aggregation Control Protocol in the switch.
      """
      singleLag: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpApiVersion'] = 'singleLag'
      multipleLag: _typing.ClassVar['VmwareDistributedVirtualSwitch.LacpApiVersion'] = 'multipleLag'

   class MulticastFilteringMode(pyVmomi.VmomiSupport.Enum):
      """
      Multicast Filtering mode.
      
      Attributes:
          legacyFiltering: Legacy filtering mode
          snooping: IGMP/MLD snooping mode
      """
      legacyFiltering: _typing.ClassVar['VmwareDistributedVirtualSwitch.MulticastFilteringMode'] = 'legacyFiltering'
      snooping: _typing.ClassVar['VmwareDistributedVirtualSwitch.MulticastFilteringMode'] = 'snooping'

   def UpdateLacpGroupConfig(self, lacpGroupSpec: list[VmwareDistributedVirtualSwitch.LacpGroupSpec]) -> pyVmomi.vim.Task:
      """
      Update Link Aggregation Control Protocol groups.
      
      It can be called if the value of
      `pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch.ConfigInfo.lacpApiVersion` is
      `multipleLag`
      else an exception ConflictingConfiguration will be thrown.
      
      Args:
          lacpGroupSpec: The Link Aggregation Control Protocol groups to be configured.
      
      Raises:
          pyVmomi.vim.fault.DvsFault: if operation fails on any host or if there are other update failures.
      """
      ...
