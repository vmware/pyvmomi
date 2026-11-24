# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vmodl
import pyVmomi.vim.option



class AdapterMapping(pyVmomi.vmodl.DynamicData):
   """
   Data object type to associate a virtual network adapter with its IP settings.
   
   Attributes:
       macAddress: The MAC address of a network adapter being customized.
           
           The client cannot change
           this value because the guest operating system has no control over the MAC
           address of a virtual network adapter.
           
           This property is optional. If it is not included, the customization process maps
           the settings from the list of AdapterMappings.IPSettings in the
           Specification.nicSettingMap to the virtual machine's network adapters, in PCI
           slot order. The first virtual network adapter on the PCI bus is assigned
           nicSettingMap[0].IPSettings, the second adapter is assigned
           nicSettingMap[1].IPSettings, and so on.
           
           In vSphere 7.0 series, the MAC addresses must be specified in the
           ascending order of pciSlotNumber, otherwise a MAC address mismatch error
           will be reported. For further details, see the
           https://kb.vmware.com/s/article/87648
       adapter: The IP settings for the associated virtual network adapter.
   """
   macAddress: _typing.Optional[str] = None
   adapter: IPSettings


class IpV6Generator(pyVmomi.vmodl.DynamicData):
   """Base type for the various IpV6 specification possibilities"""
   pass

class AutoIpV6Generator(IpV6Generator):
   """Use automatic address configuration to generate linklocal ipv6 addresses"""
   pass


class IdentitySettings(pyVmomi.vmodl.DynamicData):
   """Base type for sysprep, sysprepText, or linuxPrep object type."""
   pass


class CloudinitPrep(IdentitySettings):
   """
   Guest customization settings to customize a Linux guest operating
   system with raw cloud-init data.
   
   Attributes:
       metadata: Metadata includes the network, instance id and hostname that cloud-init
           processes to configure the VM.
           
           It is in json or yaml format.
           The max size of the metadata is 524288 bytes.
           See detail information about Instance Metadata.
       userdata: Userdata is the user custom content that cloud-init processes to
           configure the VM.
           
           The max size of the userdata is 524288 bytes.
           See detail information about User-Data formats.
   
   Since: vSphere API Release 7.0.3.0
   """
   metadata: str
   userdata: _typing.Optional[str] = None


class IpGenerator(pyVmomi.vmodl.DynamicData):
   """Base type for the various IP specification possibilities."""
   pass


class CustomIpGenerator(IpGenerator):
   """
   Use a command-line program configured with the VirtualCenter server.
   
   Attributes:
       argument: An optional argument that is passed to the utility for this IP address.
           
           The
           meaning of this field is user-defined, in the script.
   """
   argument: _typing.Optional[str] = None


class CustomIpV6Generator(IpV6Generator):
   """
   Use a command-line program configured with the VirtualCenter server.
   
   Attributes:
       argument: An optional argument that is passed to the utility for this ipv6 address.
           
           The
           meaning of this field is user-defined, in the script.
   """
   argument: _typing.Optional[str] = None


class NameGenerator(pyVmomi.vmodl.DynamicData):
   """
   A base object type for a virtual machine name that can be either fixed or
   auto-generated.
   """
   pass


class CustomNameGenerator(NameGenerator):
   """
   Specifies that the VirtualCenter server will launch an external application to
   generate the (hostname/IP).
   
   The command line for this application must be specified
   in the server configuration file (vpxd.cfg) in the vpxd/name-ip-generator key.
   
   Attributes:
       argument: An optional argument that is passed to the utility for this IP address.
           
           The
           meaning of this field is user-defined in the script.
   """
   argument: _typing.Optional[str] = None

class DhcpIpGenerator(IpGenerator):
   """Use a DHCP server to configure the virtual network adapter."""
   pass

class DhcpIpV6Generator(IpV6Generator):
   """Use a DHCP server to configure ipv6 address"""
   pass

class DisableIpV4(IpGenerator):
   """
   Disable IPv4 configuration on the virtual network adapter.
   
   Since: vSphere API Release 9.1.0.0
   """
   pass

class FixedIp(IpGenerator):
   """Use a static IP Address for the virtual network adapter."""
   ipAddress: str

class FixedIpV6(IpV6Generator):
   """Use a static ipv6 address for the virtual network adapter"""
   ipAddress: str
   subnetMask: int

class FixedName(NameGenerator):
   """
   A fixed name.
   
   Attributes:
       name: The virtual machine name specified by the client.
   """
   name: str


class GlobalIPSettings(pyVmomi.vmodl.DynamicData):
   """
   A collection of global IP settings for a virtual network adapter.
   
   In Linux, DNS
   server settings are global. The settings can either be statically set or supplied
   by a DHCP server.
   
   Attributes:
       dnsSuffixList: List of name resolution suffixes for the virtual network adapter.
           
           This list
           applies to both Windows and Linux guest customization. For Linux, this setting
           is global, whereas in Windows, this setting is listed on a per-adapter basis,
           even though the setting is global in Windows.
       dnsServerList: List of DNS servers, for a virtual network adapter with a static IP address.
           
           If
           this list is empty, then the guest operating system is expected to use a DHCP
           server to get its DNS server settings. These settings configure the virtual
           machine to use the specified DNS servers. These DNS server settings are listed
           in order of preference.
   """
   dnsSuffixList: list[str] = []
   dnsServerList: list[str] = []


class GuiRunOnce(pyVmomi.vmodl.DynamicData):
   """
   The commands listed in the GuiRunOnce data object type are executed when a user
   logs on the first time after customization completes.
   
   The logon may be driven by
   the `pyVmomi.vim.vm.customization.GuiUnattended.autoLogon` setting.
   
   The GuiRunOnce data object type maps to the GuiRunOnce key in the
   `sysprep.xml` answer file. These values are transferred into the
   `sysprep.xml` file that VirtualCenter stores on the target virtual disk. For
   more detailed information, see Performing Unattended Installations.
   
   Attributes:
       commandList: A list of commands to run at first user logon, after guest customization.
   """
   commandList: list[str] = []


class GuiUnattended(pyVmomi.vmodl.DynamicData):
   """
   The GuiUnattended type maps to the GuiUnattended key in the `sysprep.xml`
   answer file.
   
   These values are plugged directly into the `sysprep.xml` file
   that VirtualCenter stores on the target virtual disk. For more detailed
   information, see Performing Unattended Installations.
   
   Attributes:
       password: The new administrator password for the machine.
           
           To specify that the password
           should be set to blank (that is, no password), set the password value to NULL.
           Because of encryption, \"\" is NOT a valid value.
           
           If password is set to blank and `pyVmomi.vim.vm.customization.GuiUnattended.autoLogon` is set, the
           guest customization will fail.
           
           If the XML file is generated by the VirtualCenter Customization Wizard, then the
           password is encrypted. Otherwise, the client should set the plainText attribute
           to true, so that the customization process does not attempt to decrypt the
           string.
       timeZone: The time zone index for the virtual machine.
           
           Numbers correspond to time zones
           listed at Microsoft Time Zone Index Values.
       autoLogon: Flag to determine whether or not the machine automatically logs on as
           Administrator.
           
           See also the password property.
           
           If the AutoLogon flag is set, `pyVmomi.vim.vm.customization.GuiUnattended.password` must not be
           blank or the guest customization will fail.
       autoLogonCount: If the AutoLogon flag is set, then the AutoLogonCount property specifies the
           number of times the machine should automatically log on as Administrator.
           
           Generally it should be 1, but if your setup requires a number of reboots, you
           may want to increase it. This number may be determined by the list of commands
           executed by the `pyVmomi.vim.vm.customization.GuiRunOnce` command.
   """
   password: _typing.Optional[Password] = None
   timeZone: int
   autoLogon: bool
   autoLogonCount: int


class IPSettings(pyVmomi.vmodl.DynamicData):
   """
   IP settings for a virtual network adapter.
   
   Attributes:
       ip: Specification to obtain a unique IP address for this virtual network adapter.
       subnetMask: Subnet mask for this virtual network adapter.
       gateway: For a virtual network adapter with a static IP address, this data object type
           contains a list of gateways, in order of preference.
       ipV6Spec: This contains the IpGenerator, subnet mask and gateway info for all
           the ipv6 addresses associated with the virtual network adapter.
       dnsServerList: A list of server IP addresses to use for DNS lookup in a Windows guest operating
           system.
           
           In Windows, these settings are adapter-specific, whereas in Linux, they
           are global. As a result, the Linux guest customization process ignores this
           setting and looks for its DNS servers in the globalIPSettings object.
           
           Specify these servers in order of preference. If this list is not empty, and if
           a DHCP IpGenerator is used, then these settings override the DHCP settings.
       dnsDomain: A DNS domain suffix such as vmware.com.
       primaryWINS: The IP address of the primary WINS server.
           
           This property is ignored for Linux
           guest operating systems.
       secondaryWINS: The IP address of the secondary WINS server.
           
           This property is ignored for Linux
           guest operating systems.
       netBIOS: NetBIOS setting for Windows.
   """
   class IpV6AddressSpec(pyVmomi.vmodl.DynamicData):
      """
      IPv6 settings
      
      Attributes:
          ip: ipv6 address generators
          gateway: gateways
      """
      ip: list[IpV6Generator] = []
      gateway: list[str] = []

   class NetBIOSMode(pyVmomi.VmomiSupport.Enum):
      """
      NetBIOS setting for Windows.
      
      Attributes:
          enableNetBIOSViaDhcp: DHCP server decides whether or not to use NetBIOS.
          enableNetBIOS: Always use NetBIOS.
          disableNetBIOS: Never use NetBIOS.
      """
      enableNetBIOSViaDhcp: _typing.ClassVar['IPSettings.NetBIOSMode'] = 'enableNetBIOSViaDhcp'
      enableNetBIOS: _typing.ClassVar['IPSettings.NetBIOSMode'] = 'enableNetBIOS'
      disableNetBIOS: _typing.ClassVar['IPSettings.NetBIOSMode'] = 'disableNetBIOS'

   ip: IpGenerator
   subnetMask: _typing.Optional[str] = None
   gateway: list[str] = []
   ipV6Spec: _typing.Optional[IPSettings.IpV6AddressSpec] = None
   dnsServerList: list[str] = []
   dnsDomain: _typing.Optional[str] = None
   primaryWINS: _typing.Optional[str] = None
   secondaryWINS: _typing.Optional[str] = None
   netBIOS: _typing.Optional[IPSettings.NetBIOSMode] = None


class Identification(pyVmomi.vmodl.DynamicData):
   """
   The Identification data object type provides information needed to join a workgroup
   or domain.
   
   The Identification data object type maps to the Identification key in the
   `sysprep.xml` answer file. These values are transferred into the
   `sysprep.xml` file that VirtualCenter stores on the target virtual disk. For
   more detailed information, see Performing Unattended Installations.
   
   Attributes:
       joinWorkgroup: The workgroup that the virtual machine should join.
           
           If this value is supplied,
           then the domain name and authentication fields must be empty.
       joinDomain: The domain that the virtual machine should join.
           
           If this value is supplied, then
           domainAdmin and domainAdminPassword must also be supplied, and the workgroup
           name must be empty.
       domainAdmin: This is the domain user account used for authentication if the virtual machine
           is joining a domain.
           
           The user does not need to be a domain administrator, but
           the account must have the privileges required to add computers to the domain.
       domainAdminPassword: This is the password for the domain user account used for authentication if the
           virtual machine is joining a domain.
       domainOU: This is the MachineObjectOU which specifies the full LDAP path name of
           the OU to which the computer belongs.
           
           For example, OU=MyOu,DC=MyDom,DC=MyCompany,DC=com
           Refer to: https://docs.microsoft.com/en-us/windows-hardware/customize/
           desktop/unattend/microsoft-windows-unattendedjoin-
           identification-machineobjectou
           
           Since: vSphere API Release 8.0.2.0
   """
   joinWorkgroup: _typing.Optional[str] = None
   joinDomain: _typing.Optional[str] = None
   domainAdmin: _typing.Optional[str] = None
   domainAdminPassword: _typing.Optional[Password] = None
   domainOU: _typing.Optional[str] = None


class LicenseFilePrintData(pyVmomi.vmodl.DynamicData):
   """
   The LicenseFilePrintData type maps directly to the LicenseFilePrintData key in the
   `sysprep.xml` answer file.
   
   These values are transferred into the
   `sysprep.xml` file that VirtualCenter stores on the target virtual disk. For
   more detailed information, see Performing Unattended Installations.
   LicenseFilePrintData provides licensing information for Windows server operating
   systems.
   
   Attributes:
       autoMode: Server licensing mode
       autoUsers: This key is valid only if AutoMode = PerServer.
           
           The integer value indicates the
           number of client licenses purchased for the VirtualCenter server being
           installed.
   """
   class AutoMode(pyVmomi.VmomiSupport.Enum):
      """
      Enumeration of AutoMode values.
      
      Attributes:
          perServer: Indicates that client access licenses have been purchased for the server,
              allowing a certain number of concurrent connections to the VirtualCenter
              server.
          perSeat: Indicates that a client access license has been purchased for each computer
              that accesses the VirtualCenter server.
      """
      perServer: _typing.ClassVar['LicenseFilePrintData.AutoMode'] = 'perServer'
      perSeat: _typing.ClassVar['LicenseFilePrintData.AutoMode'] = 'perSeat'

   autoMode: LicenseFilePrintData.AutoMode
   autoUsers: _typing.Optional[int] = None

class LinuxFlexPrep(IdentitySettings):
   """
   Flexible guest customization settings for Linux operating system.
   
   Flexible guest customization is designed for scenarios where only the
   network configuration of an operating system requires modification.
   
   Since: vSphere API Release 9.1.0.0
   """
   pass


class Options(pyVmomi.vmodl.DynamicData):
   """Base object type for optional operations supported by the customization process."""
   pass

class LinuxOptions(Options):
   """
   Base object type for optional operations supported by the customization process for
   Linux.
   """
   pass


class LinuxPrep(IdentitySettings):
   """
   This is the Linux counterpart to the Windows Sysprep object.
   
   LinuxPrep contains
   machine-wide settings that identify a Linux machine in the same way that the
   Sysprep type identifies a Windows machine.
   
   Attributes:
       hostName: The network host name of the (Linux) virtual machine.
       domain: The fully qualified domain name.
       timeZone: The case-sensitive timezone, such as Europe/Sofia.
           
           Valid timeZone values are based on the tz (timezone)
           database used by Linux and other Unix systems.
           The values are strings (xsd:string) in the form \"Area/Location,\" in which
           Area is a continent or ocean name, and Location is the city, island, or
           other regional designation.
           
           See the List of supported time zones for different vSphere versions in Linux/Unix systems.
       hwClockUTC: Specifies whether the hardware clock is in UTC or local time.
           - True when the hardware clock is in UTC.
           - False when the hardware clock is in local time.
       scriptText: The script to run before and after GOS customization.
       compatibleCustomizationMethod: The compatible customization method is an identifier of a customization
           strategy which is implementable in a group of Linux operating systems.
           
           This value does not need to be set if your operating system is officially
           supported by VMware guest operating system customization. When using a
           Linux operating system which hasn't been officially supported and it is
           designed to be 100% bug-for-bug compatible with an officially supported
           Linux operating system, it can be customized by an existing customization
           method.
           
           Please set the compatible customization method to a supported string value
           e.g. \"GOSC_METHOD_1\".  
           See Supported compatible customization method list.
           
           Since: vSphere API Release 8.0.3.0
       resetPassword: Require root accounts to change their password on first login after
           customization.
           
           Since: vSphere API Release 9.1.0.0
       password: Password set for root accounts.
           
           The password value must be a non-empty string. If this field is not set,
           the root password will remain unchanged.
           
           Set the plainText flag to indicate whether the value is plain text or encrypted.
           
           Since: vSphere API Release 9.1.0.0
       extraConfig: Additional key/value pairs to support third party customization.
           
           Since: vSphere API Release 9.1.0.0
   """
   hostName: NameGenerator
   domain: str
   timeZone: _typing.Optional[str] = None
   hwClockUTC: _typing.Optional[bool] = None
   scriptText: _typing.Optional[str] = None
   compatibleCustomizationMethod: _typing.Optional[str] = None
   resetPassword: _typing.Optional[bool] = None
   password: _typing.Optional[Password] = None
   extraConfig: list[pyVmomi.vim.option.OptionValue] = []


class Password(pyVmomi.vmodl.DynamicData):
   """
   Contains a password string and a flag that specifies whether the string is in plain
   text or encrypted.
   
   Attributes:
       value: The password string.
           
           It is encrypted if the associated plainText flag is false.
       plainText: Flag to specify whether or not the password is in plain text, rather than
           encrypted.
   """
   value: str
   plainText: bool

class PrefixNameGenerator(NameGenerator):
   """
   Specifies that a unique name should be generated by concatenating the base string
   with a number.
   
   Virtual machine names are unique across the set of hosts and virtual machines known
   to the VirtualCenter instance. VirtualCenter tracks the network names of virtual
   machines as well as hosts. VMware Tools runs in a guest operating system and
   reports information to VirtualCenter, including the network name of the guest.
   
   Attributes:
       base: Base prefix, to which a unique number is appended.
   """
   base: str


class Specification(pyVmomi.vmodl.DynamicData):
   """
   The Specification data object type contains information required to customize a
   virtual machine when deploying it or migrating it to a new host.
   
   Attributes:
       options: Optional operations (either LinuxOptions or WinOptions).
       identity: Network identity and settings, similar to Microsoft's Sysprep tool.
           
           This is a
           Sysprep, LinuxPrep, WindowsFlexPrep, LinuxFlexPrep, CloudinitPrep or
           SysprepText object.
       globalIPSettings: Global IP settings constitute the IP settings that are not specific to a
           particular virtual network adapter.
       nicSettingMap: IP settings that are specific to a particular virtual network adapter.
           
           The
           AdapterMapping object maps a network adapter's MAC address to its Adapter
           settings object. May be empty if there are no network adapters, else should
           match number of network adapters in the VM.
       encryptionKey: Byte array containing the public key used to encrypt any passwords stored in the
           specification.
           
           Both the client and the server can use this to determine if
           stored passwords can be decrypted by the server or if the passwords need to be
           re-entered and re-encrypted before the specification can be used.
   """
   options: _typing.Optional[Options] = None
   identity: IdentitySettings
   globalIPSettings: GlobalIPSettings
   nicSettingMap: list[AdapterMapping] = []
   encryptionKey: list[pyVmomi.VmomiSupport.byte] = []

class StatelessIpV6Generator(IpV6Generator):
   """Use stateless autoconfiguration to configure to ipv6 address"""
   pass


class Sysprep(IdentitySettings):
   """
   An object representation of a Windows `sysprep.xml` answer file.
   
   The sysprep
   type encloses all the individual keys listed in a `sysprep.xml` file. For
   more detailed information, see Performing Unattended Installations.
   
   Attributes:
       guiUnattended: An object representation of the sysprep GuiUnattended key.
       userData: An object representation of the sysprep UserData key.
       guiRunOnce: An object representation of the sysprep GuiRunOnce key.
       identification: An object representation of the sysprep Identification key.
       licenseFilePrintData: An object representation of the sysprep LicenseFilePrintData key.
           
           Required only
           for Windows 2000 Server and Windows Server 2003.
       scriptText: The script to run before and after GOS customization.
           
           The script must be a batch file for Windows virtual machines.
           For additional information, refer to Setting the customization script for virtual machines in vSphere.
           
           Since: vSphere API Release 9.1.0.0
       resetPassword: Require local Administrators group accounts to change their password
           at the first logon after customization.
           
           Since: vSphere API Release 9.1.0.0
       extraConfig: Additional key/value pairs to support third party customization.
           
           Since: vSphere API Release 9.1.0.0
   """
   guiUnattended: GuiUnattended
   userData: UserData
   guiRunOnce: _typing.Optional[GuiRunOnce] = None
   identification: Identification
   licenseFilePrintData: _typing.Optional[LicenseFilePrintData] = None
   scriptText: _typing.Optional[str] = None
   resetPassword: _typing.Optional[bool] = None
   extraConfig: list[pyVmomi.vim.option.OptionValue] = []

class SysprepText(IdentitySettings):
   """
   An alternate way to specify the `sysprep.xml` answer file.
   
   This string is
   written to the `sysprep.xml` answer file on the target virtual disk.
   
   Attributes:
       value: Text for the `sysprep.xml` answer file.
           
           For additional details, see Using custom sysprep.xml for vCenter Guest Customization and
           Specifying network settings in custom sysprep.xml.
   """
   value: str

class UnknownIpGenerator(IpGenerator):
   """
   The IP address is left unspecified.
   
   The user must be prompted to supply an IP
   address.
   """
   pass

class UnknownIpV6Generator(IpV6Generator):
   """
   The ipv6 address is left unspecified.
   
   The user must be prompted to supply an ipv6
   address.
   """
   pass

class UnknownNameGenerator(NameGenerator):
   """
   Indicates that the name is not specified in advance.
   
   The client should prompt the
   user for the value to complete the specification.
   """
   pass


class UserData(pyVmomi.vmodl.DynamicData):
   """
   Personal data pertaining to the owner of the virtual machine.
   
   The UserData data object type maps to the UserData key in the `sysprep.xml`
   answer file. These values are transferred directly into the `sysprep.xml`
   file that VirtualCenter stores on the target virtual disk. For more detailed
   information, see Performing Unattended Installations.
   
   Attributes:
       fullName: User's full name.
       orgName: User's organization.
       computerName: The computer name of the (Windows) virtual machine.
           
           Computer name may contain
           letters (A-Z), numbers(0-9) and hyphens (-) but no spaces or periods (.).
           The name may not consists entirely of digits.
           Computer name is restricted to 15 characters in length. If the computer
           name is longer than 15 characters, it will be truncated to 15 characters.
       productId: Microsoft Sysprep requires that a valid serial number be included in the answer
           file when mini-setup runs.
           
           This serial number is ignored if the original guest
           operating system was installed using a volume-licensed CD.
   """
   fullName: str
   orgName: str
   computerName: NameGenerator
   productId: str

class VirtualMachineNameGenerator(NameGenerator):
   """
   Specifies that VirtualCenter should generate a virtual machine name from a base
   prefix comprising the virtual machine entity name.
   
   A number is appended, if
   necessary, to make it unique.
   
   Virtual machine names are unique across the set of hosts and virtual machines known
   to the VirtualCenter instance. VMware Tools reports the names of existing virtual
   machines.
   """
   pass


class WinOptions(Options):
   """
   Optional operations supported by the customization process for Windows.
   
   Attributes:
       changeSID: The customization process should modify the machine's security identifier (SID).
           
           For Vista OS and greater, SID will always be modified and a value of false will
           generate an error.
       deleteAccounts: If deleteAccounts is true, then all user accounts are removed from the system as
           part of the customization.
           
           Mini-setup creates a new Administrator account with a
           blank password.
       reboot: A value of type SysprepRebootOption specifying the action that should be
           taken after running sysprep.
           
           Defaults to \"reboot\".
   """
   class SysprepRebootOption(pyVmomi.VmomiSupport.Enum):
      """
      A enum constant specifying what should be done to the guest vm after running
      sysprep.
      
      Attributes:
          reboot: Reboot the machine after running sysprep.
              
              This will cause values
              specified in the sysprep.xml to be applied immediately.
          noreboot: Take no action.
              
              Leave the guest os running after running sysprep. This
              option can be used to look at values for debugging purposes after
              running sysprep.
          shutdown: Shutdown the machine after running sysprep.
              
              This puts the vm in a
              sealed state.
      """
      reboot: _typing.ClassVar['WinOptions.SysprepRebootOption'] = 'reboot'
      noreboot: _typing.ClassVar['WinOptions.SysprepRebootOption'] = 'noreboot'
      shutdown: _typing.ClassVar['WinOptions.SysprepRebootOption'] = 'shutdown'

   changeSID: bool
   deleteAccounts: bool
   reboot: _typing.Optional[WinOptions.SysprepRebootOption] = None

class WindowsFlexPrep(IdentitySettings):
   """
   Flexible guest customization settings for Windows operating system.
   
   Flexible guest customization is designed for scenarios where only the
   network configuration of an operating system requires modification.
   
   Since: vSphere API Release 9.1.0.0
   """
   pass
