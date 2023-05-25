from typing import List, Literal
from enum import Enum
from pyVmomi import vim, vmodl
from pyVmomi.VmomiSupport import byte


class AdapterMapping(vmodl.DynamicData):
    @property
    def macAddress(self) -> str: ...
    @macAddress.setter
    def macAddress(self, value: str):
        self._macAddress = value
    @property
    def adapter(self) -> IPSettings: ...
    @adapter.setter
    def adapter(self, value: IPSettings):
        self._adapter = value


class AutoIpV6Generator(IpV6Generator): ...


class CloudinitPrep(IdentitySettings):
    @property
    def metadata(self) -> str: ...
    @metadata.setter
    def metadata(self, value: str):
        self._metadata = value
    @property
    def userdata(self) -> str: ...
    @userdata.setter
    def userdata(self, value: str):
        self._userdata = value


class CustomIpGenerator(IpGenerator):
    @property
    def argument(self) -> str: ...
    @argument.setter
    def argument(self, value: str):
        self._argument = value


class CustomIpV6Generator(IpV6Generator):
    @property
    def argument(self) -> str: ...
    @argument.setter
    def argument(self, value: str):
        self._argument = value


class CustomNameGenerator(NameGenerator):
    @property
    def argument(self) -> str: ...
    @argument.setter
    def argument(self, value: str):
        self._argument = value


class DhcpIpGenerator(IpGenerator): ...


class DhcpIpV6Generator(IpV6Generator): ...


class FixedIp(IpGenerator):
    @property
    def ipAddress(self) -> str: ...
    @ipAddress.setter
    def ipAddress(self, value: str):
        self._ipAddress = value


class FixedIpV6(IpV6Generator):
    @property
    def ipAddress(self) -> str: ...
    @ipAddress.setter
    def ipAddress(self, value: str):
        self._ipAddress = value
    @property
    def subnetMask(self) -> int: ...
    @subnetMask.setter
    def subnetMask(self, value: int):
        self._subnetMask = value


class FixedName(NameGenerator):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class GlobalIPSettings(vmodl.DynamicData):
    @property
    def dnsSuffixList(self) -> List[str]: ...
    @dnsSuffixList.setter
    def dnsSuffixList(self, value: List[str]):
        self._dnsSuffixList = value
    @property
    def dnsServerList(self) -> List[str]: ...
    @dnsServerList.setter
    def dnsServerList(self, value: List[str]):
        self._dnsServerList = value


class GuiRunOnce(vmodl.DynamicData):
    @property
    def commandList(self) -> List[str]: ...
    @commandList.setter
    def commandList(self, value: List[str]):
        self._commandList = value


class GuiUnattended(vmodl.DynamicData):
    @property
    def password(self) -> Password: ...
    @password.setter
    def password(self, value: Password):
        self._password = value
    @property
    def timeZone(self) -> int: ...
    @timeZone.setter
    def timeZone(self, value: int):
        self._timeZone = value
    @property
    def autoLogon(self) -> bool: ...
    @autoLogon.setter
    def autoLogon(self, value: bool):
        self._autoLogon = value
    @property
    def autoLogonCount(self) -> int: ...
    @autoLogonCount.setter
    def autoLogonCount(self, value: int):
        self._autoLogonCount = value


class IPSettings(vmodl.DynamicData):
    @property
    def ip(self) -> IpGenerator: ...
    @ip.setter
    def ip(self, value: IpGenerator):
        self._ip = value
    @property
    def subnetMask(self) -> str: ...
    @subnetMask.setter
    def subnetMask(self, value: str):
        self._subnetMask = value
    @property
    def gateway(self) -> List[str]: ...
    @gateway.setter
    def gateway(self, value: List[str]):
        self._gateway = value
    @property
    def ipV6Spec(self) -> IPSettings.IpV6AddressSpec: ...
    @ipV6Spec.setter
    def ipV6Spec(self, value: IPSettings.IpV6AddressSpec):
        self._ipV6Spec = value
    @property
    def dnsServerList(self) -> List[str]: ...
    @dnsServerList.setter
    def dnsServerList(self, value: List[str]):
        self._dnsServerList = value
    @property
    def dnsDomain(self) -> str: ...
    @dnsDomain.setter
    def dnsDomain(self, value: str):
        self._dnsDomain = value
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
    @property
    def netBIOS(self) -> IPSettings.NetBIOSMode | Literal['enableNetBIOSViaDhcp', 'enableNetBIOS', 'disableNetBIOS']: ...
    @netBIOS.setter
    def netBIOS(self, value: IPSettings.NetBIOSMode | Literal['enableNetBIOSViaDhcp', 'enableNetBIOS', 'disableNetBIOS']):
        self._netBIOS = value


    class IpV6AddressSpec(vmodl.DynamicData):
        @property
        def ip(self) -> List[IpV6Generator]: ...
        @ip.setter
        def ip(self, value: List[IpV6Generator]):
            self._ip = value
        @property
        def gateway(self) -> List[str]: ...
        @gateway.setter
        def gateway(self, value: List[str]):
            self._gateway = value


    class NetBIOSMode(Enum):
        enableNetBIOSViaDhcp = "enableNetBIOSViaDhcp"
        enableNetBIOS = "enableNetBIOS"
        disableNetBIOS = "disableNetBIOS"


class Identification(vmodl.DynamicData):
    @property
    def joinWorkgroup(self) -> str: ...
    @joinWorkgroup.setter
    def joinWorkgroup(self, value: str):
        self._joinWorkgroup = value
    @property
    def joinDomain(self) -> str: ...
    @joinDomain.setter
    def joinDomain(self, value: str):
        self._joinDomain = value
    @property
    def domainAdmin(self) -> str: ...
    @domainAdmin.setter
    def domainAdmin(self, value: str):
        self._domainAdmin = value
    @property
    def domainAdminPassword(self) -> Password: ...
    @domainAdminPassword.setter
    def domainAdminPassword(self, value: Password):
        self._domainAdminPassword = value


class IdentitySettings(vmodl.DynamicData): ...


class IpGenerator(vmodl.DynamicData): ...


class IpV6Generator(vmodl.DynamicData): ...


class LicenseFilePrintData(vmodl.DynamicData):
    @property
    def autoMode(self) -> LicenseFilePrintData.AutoMode | Literal['perServer', 'perSeat']: ...
    @autoMode.setter
    def autoMode(self, value: LicenseFilePrintData.AutoMode | Literal['perServer', 'perSeat']):
        self._autoMode = value
    @property
    def autoUsers(self) -> int: ...
    @autoUsers.setter
    def autoUsers(self, value: int):
        self._autoUsers = value


    class AutoMode(Enum):
        perServer = "perServer"
        perSeat = "perSeat"


class LinuxOptions(Options): ...


class LinuxPrep(IdentitySettings):
    @property
    def hostName(self) -> NameGenerator: ...
    @hostName.setter
    def hostName(self, value: NameGenerator):
        self._hostName = value
    @property
    def domain(self) -> str: ...
    @domain.setter
    def domain(self, value: str):
        self._domain = value
    @property
    def timeZone(self) -> str: ...
    @timeZone.setter
    def timeZone(self, value: str):
        self._timeZone = value
    @property
    def hwClockUTC(self) -> bool: ...
    @hwClockUTC.setter
    def hwClockUTC(self, value: bool):
        self._hwClockUTC = value
    @property
    def scriptText(self) -> str: ...
    @scriptText.setter
    def scriptText(self, value: str):
        self._scriptText = value


class NameGenerator(vmodl.DynamicData): ...


class Options(vmodl.DynamicData): ...


class Password(vmodl.DynamicData):
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str):
        self._value = value
    @property
    def plainText(self) -> bool: ...
    @plainText.setter
    def plainText(self, value: bool):
        self._plainText = value


class PrefixNameGenerator(NameGenerator):
    @property
    def base(self) -> str: ...
    @base.setter
    def base(self, value: str):
        self._base = value


class Specification(vmodl.DynamicData):
    @property
    def options(self) -> Options: ...
    @options.setter
    def options(self, value: Options):
        self._options = value
    @property
    def identity(self) -> IdentitySettings: ...
    @identity.setter
    def identity(self, value: IdentitySettings):
        self._identity = value
    @property
    def globalIPSettings(self) -> GlobalIPSettings: ...
    @globalIPSettings.setter
    def globalIPSettings(self, value: GlobalIPSettings):
        self._globalIPSettings = value
    @property
    def nicSettingMap(self) -> List[AdapterMapping]: ...
    @nicSettingMap.setter
    def nicSettingMap(self, value: List[AdapterMapping]):
        self._nicSettingMap = value
    @property
    def encryptionKey(self) -> List[byte]: ...
    @encryptionKey.setter
    def encryptionKey(self, value: List[byte]):
        self._encryptionKey = value


class StatelessIpV6Generator(IpV6Generator): ...


class Sysprep(IdentitySettings):
    @property
    def guiUnattended(self) -> GuiUnattended: ...
    @guiUnattended.setter
    def guiUnattended(self, value: GuiUnattended):
        self._guiUnattended = value
    @property
    def userData(self) -> UserData: ...
    @userData.setter
    def userData(self, value: UserData):
        self._userData = value
    @property
    def guiRunOnce(self) -> GuiRunOnce: ...
    @guiRunOnce.setter
    def guiRunOnce(self, value: GuiRunOnce):
        self._guiRunOnce = value
    @property
    def identification(self) -> Identification: ...
    @identification.setter
    def identification(self, value: Identification):
        self._identification = value
    @property
    def licenseFilePrintData(self) -> LicenseFilePrintData: ...
    @licenseFilePrintData.setter
    def licenseFilePrintData(self, value: LicenseFilePrintData):
        self._licenseFilePrintData = value


class SysprepText(IdentitySettings):
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str):
        self._value = value


class UnknownIpGenerator(IpGenerator): ...


class UnknownIpV6Generator(IpV6Generator): ...


class UnknownNameGenerator(NameGenerator): ...


class UserData(vmodl.DynamicData):
    @property
    def fullName(self) -> str: ...
    @fullName.setter
    def fullName(self, value: str):
        self._fullName = value
    @property
    def orgName(self) -> str: ...
    @orgName.setter
    def orgName(self, value: str):
        self._orgName = value
    @property
    def computerName(self) -> NameGenerator: ...
    @computerName.setter
    def computerName(self, value: NameGenerator):
        self._computerName = value
    @property
    def productId(self) -> str: ...
    @productId.setter
    def productId(self, value: str):
        self._productId = value


class VirtualMachineNameGenerator(NameGenerator): ...


class WinOptions(Options):
    @property
    def changeSID(self) -> bool: ...
    @changeSID.setter
    def changeSID(self, value: bool):
        self._changeSID = value
    @property
    def deleteAccounts(self) -> bool: ...
    @deleteAccounts.setter
    def deleteAccounts(self, value: bool):
        self._deleteAccounts = value
    @property
    def reboot(self) -> WinOptions.SysprepRebootOption | Literal['reboot', 'noreboot', 'shutdown']: ...
    @reboot.setter
    def reboot(self, value: WinOptions.SysprepRebootOption | Literal['reboot', 'noreboot', 'shutdown']):
        self._reboot = value


    class SysprepRebootOption(Enum):
        reboot = "reboot"
        noreboot = "noreboot"
        shutdown = "shutdown"