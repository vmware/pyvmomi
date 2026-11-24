# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl



class DhcpConfigInfo(pyVmomi.vmodl.DynamicData):
   class DhcpOptions(pyVmomi.vmodl.DynamicData):
      enable: bool
      config: list[pyVmomi.vim.KeyValue] = []

   ipv6: _typing.Optional[DhcpOptions] = None
   ipv4: _typing.Optional[DhcpOptions] = None


class DhcpConfigSpec(pyVmomi.vmodl.DynamicData):
   class DhcpOptionsSpec(pyVmomi.vmodl.DynamicData):
      enable: _typing.Optional[bool] = None
      config: list[pyVmomi.vim.KeyValue] = []
      operation: str

   ipv6: _typing.Optional[DhcpOptionsSpec] = None
   ipv4: _typing.Optional[DhcpOptionsSpec] = None


class DnsConfigInfo(pyVmomi.vmodl.DynamicData):
   dhcp: bool
   hostName: str
   domainName: str
   ipAddress: list[str] = []
   searchDomain: list[str] = []


class DnsConfigSpec(pyVmomi.vmodl.DynamicData):
   dhcp: _typing.Optional[bool] = None
   hostName: _typing.Optional[str] = None
   domainName: _typing.Optional[str] = None
   ipAddress: list[str] = []
   searchDomain: list[str] = []


class IpConfigInfo(pyVmomi.vmodl.DynamicData):
   class IpAddressOrigin(pyVmomi.VmomiSupport.Enum):
      other: _typing.ClassVar['IpAddressOrigin'] = 'other'
      manual: _typing.ClassVar['IpAddressOrigin'] = 'manual'
      dhcp: _typing.ClassVar['IpAddressOrigin'] = 'dhcp'
      linklayer: _typing.ClassVar['IpAddressOrigin'] = 'linklayer'
      random: _typing.ClassVar['IpAddressOrigin'] = 'random'

   class IpAddressStatus(pyVmomi.VmomiSupport.Enum):
      preferred: _typing.ClassVar['IpAddressStatus'] = 'preferred'
      deprecated: _typing.ClassVar['IpAddressStatus'] = 'deprecated'
      invalid: _typing.ClassVar['IpAddressStatus'] = 'invalid'
      inaccessible: _typing.ClassVar['IpAddressStatus'] = 'inaccessible'
      unknown: _typing.ClassVar['IpAddressStatus'] = 'unknown'
      tentative: _typing.ClassVar['IpAddressStatus'] = 'tentative'
      duplicate: _typing.ClassVar['IpAddressStatus'] = 'duplicate'

   class IpAddress(pyVmomi.vmodl.DynamicData):
      ipAddress: str
      prefixLength: int
      origin: _typing.Optional[str] = None
      state: _typing.Optional[str] = None
      lifetime: _typing.Optional[_datetime.datetime] = None

   ipAddress: list[IpAddress] = []
   dhcp: _typing.Optional[DhcpConfigInfo] = None
   autoConfigurationEnabled: _typing.Optional[bool] = None


class IpConfigSpec(pyVmomi.vmodl.DynamicData):
   class IpAddressSpec(pyVmomi.vmodl.DynamicData):
      ipAddress: str
      prefixLength: int
      operation: str

   ipAddress: list[IpAddressSpec] = []
   dhcp: _typing.Optional[DhcpConfigSpec] = None
   autoConfigurationEnabled: _typing.Optional[bool] = None


class IpRouteConfigInfo(pyVmomi.vmodl.DynamicData):
   class Gateway(pyVmomi.vmodl.DynamicData):
      ipAddress: _typing.Optional[str] = None
      device: _typing.Optional[str] = None

   class IpRoute(pyVmomi.vmodl.DynamicData):
      network: str
      prefixLength: int
      gateway: Gateway

   ipRoute: list[IpRoute] = []


class IpRouteConfigSpec(pyVmomi.vmodl.DynamicData):
   class GatewaySpec(pyVmomi.vmodl.DynamicData):
      ipAddress: _typing.Optional[str] = None
      device: _typing.Optional[str] = None

   class IpRouteSpec(pyVmomi.vmodl.DynamicData):
      network: str
      prefixLength: int
      gateway: GatewaySpec
      operation: str

   ipRoute: list[IpRouteSpec] = []


class IpStackInfo(pyVmomi.vmodl.DynamicData):
   class EntryType(pyVmomi.VmomiSupport.Enum):
      other: _typing.ClassVar['EntryType'] = 'other'
      invalid: _typing.ClassVar['EntryType'] = 'invalid'
      dynamic: _typing.ClassVar['EntryType'] = 'dynamic'
      manual: _typing.ClassVar['EntryType'] = 'manual'

   class Preference(pyVmomi.VmomiSupport.Enum):
      reserved: _typing.ClassVar['Preference'] = 'reserved'
      low: _typing.ClassVar['Preference'] = 'low'
      medium: _typing.ClassVar['Preference'] = 'medium'
      high: _typing.ClassVar['Preference'] = 'high'

   class NetToMedia(pyVmomi.vmodl.DynamicData):
      ipAddress: str
      physicalAddress: str
      device: str
      type: str

   class DefaultRouter(pyVmomi.vmodl.DynamicData):
      ipAddress: str
      device: str
      lifetime: _datetime.datetime
      preference: str

   neighbor: list[NetToMedia] = []
   defaultRouter: list[DefaultRouter] = []


class NetBIOSConfigInfo(pyVmomi.vmodl.DynamicData):
   class Mode(pyVmomi.VmomiSupport.Enum):
      unknown: _typing.ClassVar['Mode'] = 'unknown'
      enabled: _typing.ClassVar['Mode'] = 'enabled'
      disabled: _typing.ClassVar['Mode'] = 'disabled'
      enabledViaDHCP: _typing.ClassVar['Mode'] = 'enabledViaDHCP'

   mode: str


class WinNetBIOSConfigInfo(NetBIOSConfigInfo):
   primaryWINS: str
   secondaryWINS: _typing.Optional[str] = None
