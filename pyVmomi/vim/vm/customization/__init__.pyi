from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from pyVmomi.VmomiSupport import byte


class AdapterMapping(vmodl.DynamicData):
    @property
    def macAddress(self) -> str: ...
    @property
    def adapter(self) -> IPSettings: ...


class AutoIpV6Generator(IpV6Generator): ...


class CloudinitPrep(IdentitySettings):
    @property
    def metadata(self) -> str: ...
    @property
    def userdata(self) -> str: ...


class CustomIpGenerator(IpGenerator):
    @property
    def argument(self) -> str: ...


class CustomIpV6Generator(IpV6Generator):
    @property
    def argument(self) -> str: ...


class CustomNameGenerator(NameGenerator):
    @property
    def argument(self) -> str: ...


class DhcpIpGenerator(IpGenerator): ...


class DhcpIpV6Generator(IpV6Generator): ...


class FixedIp(IpGenerator):
    @property
    def ipAddress(self) -> str: ...


class FixedIpV6(IpV6Generator):
    @property
    def ipAddress(self) -> str: ...
    @property
    def subnetMask(self) -> int: ...


class FixedName(NameGenerator):
    @property
    def name(self) -> str: ...


class GlobalIPSettings(vmodl.DynamicData):
    @property
    def dnsSuffixList(self) -> List[str]: ...
    @property
    def dnsServerList(self) -> List[str]: ...


class GuiRunOnce(vmodl.DynamicData):
    @property
    def commandList(self) -> List[str]: ...


class GuiUnattended(vmodl.DynamicData):
    @property
    def password(self) -> Password: ...
    @property
    def timeZone(self) -> int: ...
    @property
    def autoLogon(self) -> bool: ...
    @property
    def autoLogonCount(self) -> int: ...


class IPSettings(vmodl.DynamicData):
    @property
    def ip(self) -> IpGenerator: ...
    @property
    def subnetMask(self) -> str: ...
    @property
    def gateway(self) -> List[str]: ...
    @property
    def ipV6Spec(self) -> IPSettings.IpV6AddressSpec: ...
    @property
    def dnsServerList(self) -> List[str]: ...
    @property
    def dnsDomain(self) -> str: ...
    @property
    def primaryWINS(self) -> str: ...
    @property
    def secondaryWINS(self) -> str: ...
    @property
    def netBIOS(self) -> IPSettings.NetBIOSMode: ...


    class IpV6AddressSpec(vmodl.DynamicData):
        @property
        def ip(self) -> List[IpV6Generator]: ...
        @property
        def gateway(self) -> List[str]: ...


    class NetBIOSMode(Enum):
        enableNetBIOSViaDhcp = "enableNetBIOSViaDhcp"
        enableNetBIOS = "enableNetBIOS"
        disableNetBIOS = "disableNetBIOS"


class Identification(vmodl.DynamicData):
    @property
    def joinWorkgroup(self) -> str: ...
    @property
    def joinDomain(self) -> str: ...
    @property
    def domainAdmin(self) -> str: ...
    @property
    def domainAdminPassword(self) -> Password: ...


class IdentitySettings(vmodl.DynamicData): ...


class IpGenerator(vmodl.DynamicData): ...


class IpV6Generator(vmodl.DynamicData): ...


class LicenseFilePrintData(vmodl.DynamicData):
    @property
    def autoMode(self) -> LicenseFilePrintData.AutoMode: ...
    @property
    def autoUsers(self) -> int: ...


    class AutoMode(Enum):
        perServer = "perServer"
        perSeat = "perSeat"


class LinuxOptions(Options): ...


class LinuxPrep(IdentitySettings):
    @property
    def hostName(self) -> NameGenerator: ...
    @property
    def domain(self) -> str: ...
    @property
    def timeZone(self) -> str: ...
    @property
    def hwClockUTC(self) -> bool: ...
    @property
    def scriptText(self) -> str: ...


class NameGenerator(vmodl.DynamicData): ...


class Options(vmodl.DynamicData): ...


class Password(vmodl.DynamicData):
    @property
    def value(self) -> str: ...
    @property
    def plainText(self) -> bool: ...


class PrefixNameGenerator(NameGenerator):
    @property
    def base(self) -> str: ...


class Specification(vmodl.DynamicData):
    @property
    def options(self) -> Options: ...
    @property
    def identity(self) -> IdentitySettings: ...
    @property
    def globalIPSettings(self) -> GlobalIPSettings: ...
    @property
    def nicSettingMap(self) -> List[AdapterMapping]: ...
    @property
    def encryptionKey(self) -> List[byte]: ...


class StatelessIpV6Generator(IpV6Generator): ...


class Sysprep(IdentitySettings):
    @property
    def guiUnattended(self) -> GuiUnattended: ...
    @property
    def userData(self) -> UserData: ...
    @property
    def guiRunOnce(self) -> GuiRunOnce: ...
    @property
    def identification(self) -> Identification: ...
    @property
    def licenseFilePrintData(self) -> LicenseFilePrintData: ...


class SysprepText(IdentitySettings):
    @property
    def value(self) -> str: ...


class UnknownIpGenerator(IpGenerator): ...


class UnknownIpV6Generator(IpV6Generator): ...


class UnknownNameGenerator(NameGenerator): ...


class UserData(vmodl.DynamicData):
    @property
    def fullName(self) -> str: ...
    @property
    def orgName(self) -> str: ...
    @property
    def computerName(self) -> NameGenerator: ...
    @property
    def productId(self) -> str: ...


class VirtualMachineNameGenerator(NameGenerator): ...


class WinOptions(Options):
    @property
    def changeSID(self) -> bool: ...
    @property
    def deleteAccounts(self) -> bool: ...
    @property
    def reboot(self) -> WinOptions.SysprepRebootOption: ...


    class SysprepRebootOption(Enum):
        reboot = "reboot"
        noreboot = "noreboot"
        shutdown = "shutdown"