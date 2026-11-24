# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vmodl
import pyVmomi.vim.option



class AdapterMapping(pyVmomi.vmodl.DynamicData):
   macAddress: _typing.Optional[str] = None
   adapter: IPSettings

class AutoIpV6Generator(IpV6Generator):
   pass


class CloudinitPrep(IdentitySettings):
   metadata: str
   userdata: _typing.Optional[str] = None


class CustomIpGenerator(IpGenerator):
   argument: _typing.Optional[str] = None


class CustomIpV6Generator(IpV6Generator):
   argument: _typing.Optional[str] = None


class CustomNameGenerator(NameGenerator):
   argument: _typing.Optional[str] = None

class DhcpIpGenerator(IpGenerator):
   pass

class DhcpIpV6Generator(IpV6Generator):
   pass

class DisableIpV4(IpGenerator):
   pass

class FixedIp(IpGenerator):
   ipAddress: str

class FixedIpV6(IpV6Generator):
   ipAddress: str
   subnetMask: int

class FixedName(NameGenerator):
   name: str


class GlobalIPSettings(pyVmomi.vmodl.DynamicData):
   dnsSuffixList: list[str] = []
   dnsServerList: list[str] = []


class GuiRunOnce(pyVmomi.vmodl.DynamicData):
   commandList: list[str] = []


class GuiUnattended(pyVmomi.vmodl.DynamicData):
   password: _typing.Optional[Password] = None
   timeZone: int
   autoLogon: bool
   autoLogonCount: int


class IPSettings(pyVmomi.vmodl.DynamicData):
   class IpV6AddressSpec(pyVmomi.vmodl.DynamicData):
      ip: list[IpV6Generator] = []
      gateway: list[str] = []

   class NetBIOSMode(pyVmomi.VmomiSupport.Enum):
      enableNetBIOSViaDhcp: _typing.ClassVar['NetBIOSMode'] = 'enableNetBIOSViaDhcp'
      enableNetBIOS: _typing.ClassVar['NetBIOSMode'] = 'enableNetBIOS'
      disableNetBIOS: _typing.ClassVar['NetBIOSMode'] = 'disableNetBIOS'

   ip: IpGenerator
   subnetMask: _typing.Optional[str] = None
   gateway: list[str] = []
   ipV6Spec: _typing.Optional[IpV6AddressSpec] = None
   dnsServerList: list[str] = []
   dnsDomain: _typing.Optional[str] = None
   primaryWINS: _typing.Optional[str] = None
   secondaryWINS: _typing.Optional[str] = None
   netBIOS: _typing.Optional[NetBIOSMode] = None


class Identification(pyVmomi.vmodl.DynamicData):
   joinWorkgroup: _typing.Optional[str] = None
   joinDomain: _typing.Optional[str] = None
   domainAdmin: _typing.Optional[str] = None
   domainAdminPassword: _typing.Optional[Password] = None
   domainOU: _typing.Optional[str] = None


class IdentitySettings(pyVmomi.vmodl.DynamicData):
   pass


class IpGenerator(pyVmomi.vmodl.DynamicData):
   pass


class IpV6Generator(pyVmomi.vmodl.DynamicData):
   pass


class LicenseFilePrintData(pyVmomi.vmodl.DynamicData):
   class AutoMode(pyVmomi.VmomiSupport.Enum):
      perServer: _typing.ClassVar['AutoMode'] = 'perServer'
      perSeat: _typing.ClassVar['AutoMode'] = 'perSeat'

   autoMode: AutoMode
   autoUsers: _typing.Optional[int] = None

class LinuxFlexPrep(IdentitySettings):
   pass

class LinuxOptions(Options):
   pass


class LinuxPrep(IdentitySettings):
   hostName: NameGenerator
   domain: str
   timeZone: _typing.Optional[str] = None
   hwClockUTC: _typing.Optional[bool] = None
   scriptText: _typing.Optional[str] = None
   compatibleCustomizationMethod: _typing.Optional[str] = None
   resetPassword: _typing.Optional[bool] = None
   password: _typing.Optional[Password] = None
   extraConfig: list[pyVmomi.vim.option.OptionValue] = []


class NameGenerator(pyVmomi.vmodl.DynamicData):
   pass


class Options(pyVmomi.vmodl.DynamicData):
   pass


class Password(pyVmomi.vmodl.DynamicData):
   value: str
   plainText: bool

class PrefixNameGenerator(NameGenerator):
   base: str


class Specification(pyVmomi.vmodl.DynamicData):
   options: _typing.Optional[Options] = None
   identity: IdentitySettings
   globalIPSettings: GlobalIPSettings
   nicSettingMap: list[AdapterMapping] = []
   encryptionKey: list[pyVmomi.VmomiSupport.byte] = []

class StatelessIpV6Generator(IpV6Generator):
   pass


class Sysprep(IdentitySettings):
   guiUnattended: GuiUnattended
   userData: UserData
   guiRunOnce: _typing.Optional[GuiRunOnce] = None
   identification: Identification
   licenseFilePrintData: _typing.Optional[LicenseFilePrintData] = None
   scriptText: _typing.Optional[str] = None
   resetPassword: _typing.Optional[bool] = None
   extraConfig: list[pyVmomi.vim.option.OptionValue] = []

class SysprepText(IdentitySettings):
   value: str

class UnknownIpGenerator(IpGenerator):
   pass

class UnknownIpV6Generator(IpV6Generator):
   pass

class UnknownNameGenerator(NameGenerator):
   pass


class UserData(pyVmomi.vmodl.DynamicData):
   fullName: str
   orgName: str
   computerName: NameGenerator
   productId: str

class VirtualMachineNameGenerator(NameGenerator):
   pass


class WinOptions(Options):
   class SysprepRebootOption(pyVmomi.VmomiSupport.Enum):
      reboot: _typing.ClassVar['SysprepRebootOption'] = 'reboot'
      noreboot: _typing.ClassVar['SysprepRebootOption'] = 'noreboot'
      shutdown: _typing.ClassVar['SysprepRebootOption'] = 'shutdown'

   changeSID: bool
   deleteAccounts: bool
   reboot: _typing.Optional[SysprepRebootOption] = None

class WindowsFlexPrep(IdentitySettings):
   pass
