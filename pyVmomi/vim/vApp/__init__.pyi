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
   class NetworkMappingPair(pyVmomi.vmodl.DynamicData):
      source: pyVmomi.vim.Network
      destination: pyVmomi.vim.Network

   class ResourceMap(pyVmomi.vmodl.DynamicData):
      source: pyVmomi.vim.ManagedEntity
      parent: _typing.Optional[pyVmomi.vim.ResourcePool] = None
      resourceSpec: _typing.Optional[pyVmomi.vim.ResourceConfigSpec] = None
      location: _typing.Optional[pyVmomi.vim.Datastore] = None

   class ProvisioningType(pyVmomi.VmomiSupport.Enum):
      sameAsSource: _typing.ClassVar['ProvisioningType'] = 'sameAsSource'
      thin: _typing.ClassVar['ProvisioningType'] = 'thin'
      thick: _typing.ClassVar['ProvisioningType'] = 'thick'

   location: pyVmomi.vim.Datastore
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   resourceSpec: _typing.Optional[pyVmomi.vim.ResourceConfigSpec] = None
   vmFolder: _typing.Optional[pyVmomi.vim.Folder] = None
   networkMapping: list[NetworkMappingPair] = []
   property: list[pyVmomi.vim.KeyValue] = []
   resourceMapping: list[ResourceMap] = []
   provisioning: _typing.Optional[str] = None


class EntityConfigInfo(pyVmomi.vmodl.DynamicData):
   class Action(pyVmomi.VmomiSupport.Enum):
      none: _typing.ClassVar['Action'] = 'none'
      powerOn: _typing.ClassVar['Action'] = 'powerOn'
      powerOff: _typing.ClassVar['Action'] = 'powerOff'
      guestShutdown: _typing.ClassVar['Action'] = 'guestShutdown'
      suspend: _typing.ClassVar['Action'] = 'suspend'

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
   class IpAllocationPolicy(pyVmomi.VmomiSupport.Enum):
      dhcpPolicy: _typing.ClassVar['IpAllocationPolicy'] = 'dhcpPolicy'
      transientPolicy: _typing.ClassVar['IpAllocationPolicy'] = 'transientPolicy'
      fixedPolicy: _typing.ClassVar['IpAllocationPolicy'] = 'fixedPolicy'
      fixedAllocatedPolicy: _typing.ClassVar['IpAllocationPolicy'] = 'fixedAllocatedPolicy'

   class AllocationSchemes(pyVmomi.VmomiSupport.Enum):
      dhcp: _typing.ClassVar['AllocationSchemes'] = 'dhcp'
      ovfenv: _typing.ClassVar['AllocationSchemes'] = 'ovfenv'

   class Protocols(pyVmomi.VmomiSupport.Enum):
      IPv4: _typing.ClassVar['Protocols'] = 'IPv4'
      IPv6: _typing.ClassVar['Protocols'] = 'IPv6'

   supportedAllocationScheme: list[str] = []
   ipAllocationPolicy: _typing.Optional[str] = None
   supportedIpProtocol: list[str] = []
   ipProtocol: _typing.Optional[str] = None


class IpPool(pyVmomi.vmodl.DynamicData):
   class IpPoolConfigInfo(pyVmomi.vmodl.DynamicData):
      subnetAddress: _typing.Optional[str] = None
      netmask: _typing.Optional[str] = None
      gateway: _typing.Optional[str] = None
      range: _typing.Optional[str] = None
      dns: list[str] = []
      dhcpServerAvailable: _typing.Optional[bool] = None
      ipPoolEnabled: _typing.Optional[bool] = None

   class Association(pyVmomi.vmodl.DynamicData):
      network: _typing.Optional[pyVmomi.vim.Network] = None
      networkName: str

   id: _typing.Optional[int] = None
   name: _typing.Optional[str] = None
   ipv4Config: _typing.Optional[IpPoolConfigInfo] = None
   ipv6Config: _typing.Optional[IpPoolConfigInfo] = None
   dnsDomain: _typing.Optional[str] = None
   dnsSearchPath: _typing.Optional[str] = None
   hostPrefix: _typing.Optional[str] = None
   httpProxy: _typing.Optional[str] = None
   networkAssociation: list[Association] = []
   availableIpv4Addresses: _typing.Optional[int] = None
   availableIpv6Addresses: _typing.Optional[int] = None
   allocatedIpv4Addresses: _typing.Optional[int] = None
   allocatedIpv6Addresses: _typing.Optional[int] = None


class OvfSectionInfo(pyVmomi.vmodl.DynamicData):
   key: _typing.Optional[int] = None
   namespace: _typing.Optional[str] = None
   type: _typing.Optional[str] = None
   atEnvelopeLevel: _typing.Optional[bool] = None
   contents: _typing.Optional[str] = None


class OvfSectionSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   info: _typing.Optional[OvfSectionInfo] = None


class ProductInfo(pyVmomi.vmodl.DynamicData):
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
   info: _typing.Optional[ProductInfo] = None


class PropertyInfo(pyVmomi.vmodl.DynamicData):
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
   info: _typing.Optional[PropertyInfo] = None


class VAppConfigInfo(VmConfigInfo):
   entityConfig: list[EntityConfigInfo] = []
   annotation: str
   instanceUuid: _typing.Optional[str] = None
   managedBy: _typing.Optional[pyVmomi.vim.ext.ManagedByInfo] = None


class VAppConfigSpec(VmConfigSpec):
   entityConfig: list[EntityConfigInfo] = []
   annotation: _typing.Optional[str] = None
   instanceUuid: _typing.Optional[str] = None
   managedBy: _typing.Optional[pyVmomi.vim.ext.ManagedByInfo] = None


class VAppImportSpec(pyVmomi.vim.ImportSpec):
   name: str
   vAppConfigSpec: VAppConfigSpec
   resourcePoolSpec: pyVmomi.vim.ResourceConfigSpec
   child: list[pyVmomi.vim.ImportSpec] = []


class VmConfigInfo(pyVmomi.vmodl.DynamicData):
   product: list[ProductInfo] = []
   property: list[PropertyInfo] = []
   ipAssignment: IPAssignmentInfo
   eula: list[str] = []
   ovfSection: list[OvfSectionInfo] = []
   ovfEnvironmentTransport: list[str] = []
   installBootRequired: bool
   installBootStopDelay: int


class VmConfigSpec(pyVmomi.vmodl.DynamicData):
   product: list[ProductSpec] = []
   property: list[PropertySpec] = []
   ipAssignment: _typing.Optional[IPAssignmentInfo] = None
   eula: list[str] = []
   ovfSection: list[OvfSectionSpec] = []
   ovfEnvironmentTransport: list[str] = []
   installBootRequired: _typing.Optional[bool] = None
   installBootStopDelay: _typing.Optional[int] = None
