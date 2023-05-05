from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime


class DhcpConfigInfo(vmodl.DynamicData):
    @property
    def ipv6(self) -> DhcpConfigInfo.DhcpOptions: ...
    @property
    def ipv4(self) -> DhcpConfigInfo.DhcpOptions: ...


    class DhcpOptions(vmodl.DynamicData):
        @property
        def enable(self) -> bool: ...
        @property
        def config(self) -> List[vim.KeyValue]: ...


class DhcpConfigSpec(vmodl.DynamicData):
    @property
    def ipv6(self) -> DhcpConfigSpec.DhcpOptionsSpec: ...
    @property
    def ipv4(self) -> DhcpConfigSpec.DhcpOptionsSpec: ...


    class DhcpOptionsSpec(vmodl.DynamicData):
        @property
        def enable(self) -> bool: ...
        @property
        def config(self) -> List[vim.KeyValue]: ...
        @property
        def operation(self) -> str: ...


class DnsConfigInfo(vmodl.DynamicData):
    @property
    def dhcp(self) -> bool: ...
    @property
    def hostName(self) -> str: ...
    @property
    def domainName(self) -> str: ...
    @property
    def ipAddress(self) -> List[str]: ...
    @property
    def searchDomain(self) -> List[str]: ...


class DnsConfigSpec(vmodl.DynamicData):
    @property
    def dhcp(self) -> bool: ...
    @property
    def hostName(self) -> str: ...
    @property
    def domainName(self) -> str: ...
    @property
    def ipAddress(self) -> List[str]: ...
    @property
    def searchDomain(self) -> List[str]: ...


class IpConfigInfo(vmodl.DynamicData):
    @property
    def ipAddress(self) -> List[IpConfigInfo.IpAddress]: ...
    @property
    def dhcp(self) -> DhcpConfigInfo: ...
    @property
    def autoConfigurationEnabled(self) -> bool: ...


    class IpAddress(vmodl.DynamicData):
        @property
        def ipAddress(self) -> str: ...
        @property
        def prefixLength(self) -> int: ...
        @property
        def origin(self) -> str: ...
        @property
        def state(self) -> str: ...
        @property
        def lifetime(self) -> datetime: ...


    class IpAddressOrigin(Enum):
        other = "other"
        manual = "manual"
        dhcp = "dhcp"
        linklayer = "linklayer"
        random = "random"


    class IpAddressStatus(Enum):
        preferred = "preferred"
        deprecated = "deprecated"
        invalid = "invalid"
        inaccessible = "inaccessible"
        unknown = "unknown"
        tentative = "tentative"
        duplicate = "duplicate"


class IpConfigSpec(vmodl.DynamicData):
    @property
    def ipAddress(self) -> List[IpConfigSpec.IpAddressSpec]: ...
    @property
    def dhcp(self) -> DhcpConfigSpec: ...
    @property
    def autoConfigurationEnabled(self) -> bool: ...


    class IpAddressSpec(vmodl.DynamicData):
        @property
        def ipAddress(self) -> str: ...
        @property
        def prefixLength(self) -> int: ...
        @property
        def operation(self) -> str: ...


class IpRouteConfigInfo(vmodl.DynamicData):
    @property
    def ipRoute(self) -> List[IpRouteConfigInfo.IpRoute]: ...


    class Gateway(vmodl.DynamicData):
        @property
        def ipAddress(self) -> str: ...
        @property
        def device(self) -> str: ...


    class IpRoute(vmodl.DynamicData):
        @property
        def network(self) -> str: ...
        @property
        def prefixLength(self) -> int: ...
        @property
        def gateway(self) -> IpRouteConfigInfo.Gateway: ...


class IpRouteConfigSpec(vmodl.DynamicData):
    @property
    def ipRoute(self) -> List[IpRouteConfigSpec.IpRouteSpec]: ...


    class GatewaySpec(vmodl.DynamicData):
        @property
        def ipAddress(self) -> str: ...
        @property
        def device(self) -> str: ...


    class IpRouteSpec(vmodl.DynamicData):
        @property
        def network(self) -> str: ...
        @property
        def prefixLength(self) -> int: ...
        @property
        def gateway(self) -> IpRouteConfigSpec.GatewaySpec: ...
        @property
        def operation(self) -> str: ...


class IpStackInfo(vmodl.DynamicData):
    @property
    def neighbor(self) -> List[IpStackInfo.NetToMedia]: ...
    @property
    def defaultRouter(self) -> List[IpStackInfo.DefaultRouter]: ...


    class DefaultRouter(vmodl.DynamicData):
        @property
        def ipAddress(self) -> str: ...
        @property
        def device(self) -> str: ...
        @property
        def lifetime(self) -> datetime: ...
        @property
        def preference(self) -> str: ...


    class NetToMedia(vmodl.DynamicData):
        @property
        def ipAddress(self) -> str: ...
        @property
        def physicalAddress(self) -> str: ...
        @property
        def device(self) -> str: ...
        @property
        def type(self) -> str: ...


    class EntryType(Enum):
        other = "other"
        invalid = "invalid"
        dynamic = "dynamic"
        manual = "manual"


    class Preference(Enum):
        reserved = "reserved"
        low = "low"
        medium = "medium"
        high = "high"


class NetBIOSConfigInfo(vmodl.DynamicData):
    @property
    def mode(self) -> str: ...


    class Mode(Enum):
        unknown = "unknown"
        enabled = "enabled"
        disabled = "disabled"
        enabledViaDHCP = "enabledviadhcp"


class WinNetBIOSConfigInfo(NetBIOSConfigInfo):
    @property
    def primaryWINS(self) -> str: ...
    @property
    def secondaryWINS(self) -> str: ...