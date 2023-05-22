from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime


class DhcpConfigInfo(vmodl.DynamicData):
    @property
    def ipv6(self) -> DhcpConfigInfo.DhcpOptions: ...
    @ipv6.setter
    def ipv6(self, value: DhcpConfigInfo.DhcpOptions):
        self._ipv6 = value
    @property
    def ipv4(self) -> DhcpConfigInfo.DhcpOptions: ...
    @ipv4.setter
    def ipv4(self, value: DhcpConfigInfo.DhcpOptions):
        self._ipv4 = value


    class DhcpOptions(vmodl.DynamicData):
        @property
        def enable(self) -> bool: ...
        @enable.setter
        def enable(self, value: bool):
            self._enable = value
        @property
        def config(self) -> List[vim.KeyValue]: ...
        @config.setter
        def config(self, value: List[vim.KeyValue]):
            self._config = value


class DhcpConfigSpec(vmodl.DynamicData):
    @property
    def ipv6(self) -> DhcpConfigSpec.DhcpOptionsSpec: ...
    @ipv6.setter
    def ipv6(self, value: DhcpConfigSpec.DhcpOptionsSpec):
        self._ipv6 = value
    @property
    def ipv4(self) -> DhcpConfigSpec.DhcpOptionsSpec: ...
    @ipv4.setter
    def ipv4(self, value: DhcpConfigSpec.DhcpOptionsSpec):
        self._ipv4 = value


    class DhcpOptionsSpec(vmodl.DynamicData):
        @property
        def enable(self) -> bool: ...
        @enable.setter
        def enable(self, value: bool):
            self._enable = value
        @property
        def config(self) -> List[vim.KeyValue]: ...
        @config.setter
        def config(self, value: List[vim.KeyValue]):
            self._config = value
        @property
        def operation(self) -> str: ...
        @operation.setter
        def operation(self, value: str):
            self._operation = value


class DnsConfigInfo(vmodl.DynamicData):
    @property
    def dhcp(self) -> bool: ...
    @dhcp.setter
    def dhcp(self, value: bool):
        self._dhcp = value
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def domainName(self) -> str: ...
    @domainName.setter
    def domainName(self, value: str):
        self._domainName = value
    @property
    def ipAddress(self) -> List[str]: ...
    @ipAddress.setter
    def ipAddress(self, value: List[str]):
        self._ipAddress = value
    @property
    def searchDomain(self) -> List[str]: ...
    @searchDomain.setter
    def searchDomain(self, value: List[str]):
        self._searchDomain = value


class DnsConfigSpec(vmodl.DynamicData):
    @property
    def dhcp(self) -> bool: ...
    @dhcp.setter
    def dhcp(self, value: bool):
        self._dhcp = value
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def domainName(self) -> str: ...
    @domainName.setter
    def domainName(self, value: str):
        self._domainName = value
    @property
    def ipAddress(self) -> List[str]: ...
    @ipAddress.setter
    def ipAddress(self, value: List[str]):
        self._ipAddress = value
    @property
    def searchDomain(self) -> List[str]: ...
    @searchDomain.setter
    def searchDomain(self, value: List[str]):
        self._searchDomain = value


class IpConfigInfo(vmodl.DynamicData):
    @property
    def ipAddress(self) -> List[IpConfigInfo.IpAddress]: ...
    @ipAddress.setter
    def ipAddress(self, value: List[IpConfigInfo.IpAddress]):
        self._ipAddress = value
    @property
    def dhcp(self) -> DhcpConfigInfo: ...
    @dhcp.setter
    def dhcp(self, value: DhcpConfigInfo):
        self._dhcp = value
    @property
    def autoConfigurationEnabled(self) -> bool: ...
    @autoConfigurationEnabled.setter
    def autoConfigurationEnabled(self, value: bool):
        self._autoConfigurationEnabled = value


    class IpAddress(vmodl.DynamicData):
        @property
        def ipAddress(self) -> str: ...
        @ipAddress.setter
        def ipAddress(self, value: str):
            self._ipAddress = value
        @property
        def prefixLength(self) -> int: ...
        @prefixLength.setter
        def prefixLength(self, value: int):
            self._prefixLength = value
        @property
        def origin(self) -> str: ...
        @origin.setter
        def origin(self, value: str):
            self._origin = value
        @property
        def state(self) -> str: ...
        @state.setter
        def state(self, value: str):
            self._state = value
        @property
        def lifetime(self) -> datetime: ...
        @lifetime.setter
        def lifetime(self, value: datetime):
            self._lifetime = value


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
    @ipAddress.setter
    def ipAddress(self, value: List[IpConfigSpec.IpAddressSpec]):
        self._ipAddress = value
    @property
    def dhcp(self) -> DhcpConfigSpec: ...
    @dhcp.setter
    def dhcp(self, value: DhcpConfigSpec):
        self._dhcp = value
    @property
    def autoConfigurationEnabled(self) -> bool: ...
    @autoConfigurationEnabled.setter
    def autoConfigurationEnabled(self, value: bool):
        self._autoConfigurationEnabled = value


    class IpAddressSpec(vmodl.DynamicData):
        @property
        def ipAddress(self) -> str: ...
        @ipAddress.setter
        def ipAddress(self, value: str):
            self._ipAddress = value
        @property
        def prefixLength(self) -> int: ...
        @prefixLength.setter
        def prefixLength(self, value: int):
            self._prefixLength = value
        @property
        def operation(self) -> str: ...
        @operation.setter
        def operation(self, value: str):
            self._operation = value


class IpRouteConfigInfo(vmodl.DynamicData):
    @property
    def ipRoute(self) -> List[IpRouteConfigInfo.IpRoute]: ...
    @ipRoute.setter
    def ipRoute(self, value: List[IpRouteConfigInfo.IpRoute]):
        self._ipRoute = value


    class Gateway(vmodl.DynamicData):
        @property
        def ipAddress(self) -> str: ...
        @ipAddress.setter
        def ipAddress(self, value: str):
            self._ipAddress = value
        @property
        def device(self) -> str: ...
        @device.setter
        def device(self, value: str):
            self._device = value


    class IpRoute(vmodl.DynamicData):
        @property
        def network(self) -> str: ...
        @network.setter
        def network(self, value: str):
            self._network = value
        @property
        def prefixLength(self) -> int: ...
        @prefixLength.setter
        def prefixLength(self, value: int):
            self._prefixLength = value
        @property
        def gateway(self) -> IpRouteConfigInfo.Gateway: ...
        @gateway.setter
        def gateway(self, value: IpRouteConfigInfo.Gateway):
            self._gateway = value


class IpRouteConfigSpec(vmodl.DynamicData):
    @property
    def ipRoute(self) -> List[IpRouteConfigSpec.IpRouteSpec]: ...
    @ipRoute.setter
    def ipRoute(self, value: List[IpRouteConfigSpec.IpRouteSpec]):
        self._ipRoute = value


    class GatewaySpec(vmodl.DynamicData):
        @property
        def ipAddress(self) -> str: ...
        @ipAddress.setter
        def ipAddress(self, value: str):
            self._ipAddress = value
        @property
        def device(self) -> str: ...
        @device.setter
        def device(self, value: str):
            self._device = value


    class IpRouteSpec(vmodl.DynamicData):
        @property
        def network(self) -> str: ...
        @network.setter
        def network(self, value: str):
            self._network = value
        @property
        def prefixLength(self) -> int: ...
        @prefixLength.setter
        def prefixLength(self, value: int):
            self._prefixLength = value
        @property
        def gateway(self) -> IpRouteConfigSpec.GatewaySpec: ...
        @gateway.setter
        def gateway(self, value: IpRouteConfigSpec.GatewaySpec):
            self._gateway = value
        @property
        def operation(self) -> str: ...
        @operation.setter
        def operation(self, value: str):
            self._operation = value


class IpStackInfo(vmodl.DynamicData):
    @property
    def neighbor(self) -> List[IpStackInfo.NetToMedia]: ...
    @neighbor.setter
    def neighbor(self, value: List[IpStackInfo.NetToMedia]):
        self._neighbor = value
    @property
    def defaultRouter(self) -> List[IpStackInfo.DefaultRouter]: ...
    @defaultRouter.setter
    def defaultRouter(self, value: List[IpStackInfo.DefaultRouter]):
        self._defaultRouter = value


    class DefaultRouter(vmodl.DynamicData):
        @property
        def ipAddress(self) -> str: ...
        @ipAddress.setter
        def ipAddress(self, value: str):
            self._ipAddress = value
        @property
        def device(self) -> str: ...
        @device.setter
        def device(self, value: str):
            self._device = value
        @property
        def lifetime(self) -> datetime: ...
        @lifetime.setter
        def lifetime(self, value: datetime):
            self._lifetime = value
        @property
        def preference(self) -> str: ...
        @preference.setter
        def preference(self, value: str):
            self._preference = value


    class NetToMedia(vmodl.DynamicData):
        @property
        def ipAddress(self) -> str: ...
        @ipAddress.setter
        def ipAddress(self, value: str):
            self._ipAddress = value
        @property
        def physicalAddress(self) -> str: ...
        @physicalAddress.setter
        def physicalAddress(self, value: str):
            self._physicalAddress = value
        @property
        def device(self) -> str: ...
        @device.setter
        def device(self, value: str):
            self._device = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value


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
    @mode.setter
    def mode(self, value: str):
        self._mode = value


    class Mode(Enum):
        unknown = "unknown"
        enabled = "enabled"
        disabled = "disabled"
        enabledViaDHCP = "enabledViaDHCP"


class WinNetBIOSConfigInfo(NetBIOSConfigInfo):
    @property
    def primaryWINS(self) -> str: ...
    @primaryWINS.setter
    def primaryWINS(self, value: str):
        self._primaryWINS = value
    @property
    def secondaryWINS(self) -> str: ...
    @secondaryWINS.setter
    def secondaryWINS(self, value: str):
        self._secondaryWINS = value