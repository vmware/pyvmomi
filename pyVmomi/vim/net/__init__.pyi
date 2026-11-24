# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl



class DhcpConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   Dynamic Host Configuration Protocol reporting for IP version 4 and version 6.
   
   Attributes:
       ipv6: IPv6 DHCP client settings.
       ipv4: IPv4 DHCP client settings.
   """
   class DhcpOptions(pyVmomi.vmodl.DynamicData):
      """
      Provides for reporting of DHCP client.
      
      This data object may be used
      at a per interface or per system scope.
      
      Attributes:
          enable: Report state of dhcp client services.
          config: Platform specific settings for DHCP Client.
              
              The key part is a unique number, the value part
              is the platform specific configuration command.
              For example on Linux, BSD systems using the file dhclient.conf
              output would be reported at system scope:
              key='1', value='timeout 60;'
              key='2', value='reboot 10;'
              output reported at per interface scope:
              key='1', value='prepend domain-name-servers 192.0.2.1;'
              key='2', value='require subnet-mask, domain-name-servers;'
      """
      enable: bool
      config: list[pyVmomi.vim.KeyValue] = []

   ipv6: _typing.Optional[DhcpConfigInfo.DhcpOptions] = None
   ipv4: _typing.Optional[DhcpConfigInfo.DhcpOptions] = None


class DhcpConfigSpec(pyVmomi.vmodl.DynamicData):
   """
   Dynamic Host Configuration Protocol Configuration for IP version 4 and version 6.
   
   Attributes:
       ipv6: Configure IPv6 DHCP client settings.
       ipv4: Configure IPv4 DHCP client settings.
   """
   class DhcpOptionsSpec(pyVmomi.vmodl.DynamicData):
      """
      Provides for configuration of IPv6
      
      Attributes:
          enable: Enable or disable dhcp for IPv4.
          config: Platform specific settings for DHCP Client.
              
              The key part is a unique number, the value part
              is the platform specific configuration command.
              See `pyVmomi.vim.net.DhcpConfigInfo` for value formatting.
          operation: Requires one of the values from `pyVmomi.vim.host.ConfigChange.Operation`.
      """
      enable: _typing.Optional[bool] = None
      config: list[pyVmomi.vim.KeyValue] = []
      operation: str

   ipv6: _typing.Optional[DhcpConfigSpec.DhcpOptionsSpec] = None
   ipv4: _typing.Optional[DhcpConfigSpec.DhcpOptionsSpec] = None


class DnsConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   Domain Name Server (DNS) Configuration Specification -
   a data object for reporting the configuration of RFC 1034 client side DNS settings.
   
   Attributes:
       dhcp: Indicates whether or not dynamic host control
           protocol (DHCP) is used to configure DNS configuration.
       hostName: The host name portion of DNS name.
           
           For example, \"esx01\" part of
           esx01.example.com.
       domainName: The domain name portion of the DNS name.
           
           \"example.com\" part of
           esx01.example.com.
       ipAddress: The IP addresses of the DNS servers in order of use.
           
           IPv4 addresses are specified using
           dotted decimal notation. For example, \"192.0.2.1\".
           IPv6 addresses are 128-bit addresses represented as
           eight fields of up to four hexadecimal digits.
           A colon separates each field (:). For example,
           2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the
           symbol '::' to represent multiple 16-bit groups of
           contiguous 0's only once in an address as described in RFC 2373.
       searchDomain: The domain in which to search for hosts, placed in order of preference.
   """
   dhcp: bool
   hostName: str
   domainName: str
   ipAddress: list[str] = []
   searchDomain: list[str] = []


class DnsConfigSpec(pyVmomi.vmodl.DynamicData):
   """
   Domain Name Server (DNS) Configuration Specification -
   a data object for configuring the RFC 1034 client side DNS settings.
   
   TBD: remove this section, only for discussing what goes into this object.
   Place properties here that are specific to the RFC/common to all systems.
   Properties that are platform specific should go into a separate config spec.
   http://technet.microsoft.com/en-us/library/cc778792.aspx
   http://en.wikipedia.org/wiki/Microsoft_DNS
   
   Attributes:
       dhcp: The flag to indicate whether or not dynamic host control
           protocol (DHCP) will be used to set DNS configuration automatically.
           
           See vim.net.DhcpConfigSpec
       hostName: The host name portion of DNS name.
           
           For example,
           \"esx01\" part of esx01.example.com. The rules for forming a hostname
           are specified in RFC 1034.
       domainName: The domain name portion of the DNS name.
           
           This would be the
           \"example.com\" part of esx01.example.com. The rules for forming
           a domain name are defined in RFC 1034.
       ipAddress: Unicast IP address(s) of one or more DNS servers in order of use.
           
           IPv4 addresses are specified using
           dotted decimal notation. For example, \"192.0.2.1\".
           IPv6 addresses are 128-bit addresses represented as
           eight fields of up to four hexadecimal digits.
           A colon separates each field (:). For example,
           2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the
           symbol '::' to represent multiple 16-bit groups of
           contiguous 0's only once in an address as described in RFC 2373.
       searchDomain: The domain in which to search for hosts in order of preference.
   """
   dhcp: _typing.Optional[bool] = None
   hostName: _typing.Optional[str] = None
   domainName: _typing.Optional[str] = None
   ipAddress: list[str] = []
   searchDomain: list[str] = []


class IpConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   Protocol version independent address reporting data object for network
   interfaces.
   
   Attributes:
       ipAddress: Zero, one or more manual (static) assigned IP addresses to be configured
           on a given interface.
       dhcp: Client side DHCP for a given interface.
       autoConfigurationEnabled: Enable or disable ICMPv6 router solicitation requests from a given interface
           to acquire an IPv6 address and default gateway route from zero, one or more
           routers on the connected network.
           
           If not set then ICMPv6 is not available on this system,
           See vim.host.Network.Capabilities
   """
   class IpAddressOrigin(pyVmomi.VmomiSupport.Enum):
      """
      This specifies how an IP address was obtained for a given interface.
      
      See RFC 4293 IpAddressOriginTC.
      
      Attributes:
          other: Any other type of address configuration other than the below
              mentioned ones will fall under this category.
              
              For e.g., automatic
              address configuration for the link local address falls under
              this type.
          manual: The address is configured manually.
              
              The term 'static' is a synonym.
          dhcp: The address is configured through dhcp.
          linklayer: The address is obtained through stateless autoconfiguration (autoconf).
              
              See RFC 4862, IPv6 Stateless Address Autoconfiguration.
          random: The address is chosen by the system at random
              e.g., an IPv4 address within 169.254/16, or an RFC 3041 privacy address.
      """
      other: _typing.ClassVar['IpConfigInfo.IpAddressOrigin'] = 'other'
      manual: _typing.ClassVar['IpConfigInfo.IpAddressOrigin'] = 'manual'
      dhcp: _typing.ClassVar['IpConfigInfo.IpAddressOrigin'] = 'dhcp'
      linklayer: _typing.ClassVar['IpConfigInfo.IpAddressOrigin'] = 'linklayer'
      random: _typing.ClassVar['IpConfigInfo.IpAddressOrigin'] = 'random'

   class IpAddressStatus(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          preferred: Indicates that this is a valid address.
          deprecated: Indicates that this is a valid but deprecated address
              that should no longer be used as a source address.
          invalid: Indicates that this isn't a valid.
          inaccessible: Indicates that the address is not accessible because
              interface is not operational.
          unknown: Indicates that the status cannot be determined.
          tentative: Indicates that the uniqueness of the
              address on the link is presently being verified.
          duplicate: Indicates the address has been determined to be non-unique
              on the link, this address will not be reachable.
      """
      preferred: _typing.ClassVar['IpConfigInfo.IpAddressStatus'] = 'preferred'
      deprecated: _typing.ClassVar['IpConfigInfo.IpAddressStatus'] = 'deprecated'
      invalid: _typing.ClassVar['IpConfigInfo.IpAddressStatus'] = 'invalid'
      inaccessible: _typing.ClassVar['IpConfigInfo.IpAddressStatus'] = 'inaccessible'
      unknown: _typing.ClassVar['IpConfigInfo.IpAddressStatus'] = 'unknown'
      tentative: _typing.ClassVar['IpConfigInfo.IpAddressStatus'] = 'tentative'
      duplicate: _typing.ClassVar['IpConfigInfo.IpAddressStatus'] = 'duplicate'

   class IpAddress(pyVmomi.vmodl.DynamicData):
      """
      Information about a specific IP Address.
      
      Attributes:
          ipAddress: IPv4 address is specified using dotted decimal notation.
              
              For example, \"192.0.2.1\".
              IPv6 addresses are 128-bit addresses represented as eight fields
              of up to four hexadecimal digits.
              A colon separates each field (:). For example,
              2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the
              symbol '::' to represent multiple 16-bit groups of
              contiguous 0's only once in an address as described in RFC 2373.
          prefixLength: Denotes the length of a generic Internet network address
              prefix.
              
              The prefix length for IPv4 the value range is 0-32.
              For IPv6 prefixLength is a decimal value range 0-128.
              A value of n corresponds to an IP address mask
              that has n contiguous 1-bits from the most significant
              bit (MSB), with all other bits set to 0.
              A value of zero is valid only if the calling context defines
              it.
          origin: How this address was configured.
              
              This can be
              one of the values from the enum IpAddressOrigin
              See `pyVmomi.vim.net.IpConfigInfo.IpAddressOrigin` for values.
          state: The state of this ipAddress.
              
              Can be one of `pyVmomi.vim.net.IpConfigInfo.IpAddressStatus`.
          lifetime: The time when will this address expire.
              
              During this time
              `pyVmomi.vim.net.IpConfigInfo.IpAddressStatus` may change states but is still visible
              from the network.
      """
      ipAddress: str
      prefixLength: int
      origin: _typing.Optional[str] = None
      state: _typing.Optional[str] = None
      lifetime: _typing.Optional[_datetime.datetime] = None

   ipAddress: list[IpConfigInfo.IpAddress] = []
   dhcp: _typing.Optional[DhcpConfigInfo] = None
   autoConfigurationEnabled: _typing.Optional[bool] = None


class IpConfigSpec(pyVmomi.vmodl.DynamicData):
   """
   Internet Protocol Address Configuration for version 4 and version 6.
   
   Attributes:
       ipAddress: A set of manual (static) IP addresses to be configured on a given interface.
       dhcp: Configure client side DHCP for a given interface.
       autoConfigurationEnabled: Enable or disable ICMPv6 router solictitation requests from a given interface
           to acquire an IPv6 address and default gateway route from zero, one or more
           routers on the connected network.
   """
   class IpAddressSpec(pyVmomi.vmodl.DynamicData):
      """
      Provides for configuration of IP Addresses.
      
      Attributes:
          ipAddress: IPv4 address is specified using
              dotted decimal notation.
              
              For example, \"192.0.2.1\".
              IPv6 addresses are 128-bit addresses specified as
              eight fields of up to four hexadecimal digits.
              A colon separates each field (:). For example,
              2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the
              symbol '::' to represent multiple 16-bit groups of
              contiguous 0's only once in an address as described in RFC 2373.
          prefixLength: Denotes the length of a generic Internet network address
              prefix.
              
              The prefix length for IPv4 the value range is 0-32.
              For IPv6 prefixLength is a decimal value range 0-128.
              A value of n corresponds to an IP address mask
              that has n contiguous 1-bits from the most significant
              bit (MSB), with all other bits set to 0.
              A value of zero is valid only if the calling context defines
              it.
          operation: Requires one of: \"add\" and \"remove\" or \"change\"
              See `pyVmomi.vim.host.ConfigChange.Operation`.
      """
      ipAddress: str
      prefixLength: int
      operation: str

   ipAddress: list[IpConfigSpec.IpAddressSpec] = []
   dhcp: _typing.Optional[DhcpConfigSpec] = None
   autoConfigurationEnabled: _typing.Optional[bool] = None


class IpRouteConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   This data object reports the IP Route Table.
   
   Attributes:
       ipRoute: IP routing table for all address families.
   """
   class Gateway(pyVmomi.vmodl.DynamicData):
      """Next hop Gateway for a given route."""
      ipAddress: _typing.Optional[str] = None
      device: _typing.Optional[str] = None

   class IpRoute(pyVmomi.vmodl.DynamicData):
      """
      IpRoute report an individual host, network or default destination network
      reachable through a given gateway.
      
      Attributes:
          network: IP Address of the destination IP network.
              
              IPv6 addresses are 128-bit addresses represented
              as eight fields of up to four hexadecimal digits. A colon separates each
              field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can
              also consist of symbol '::' to represent multiple 16-bit groups of
              contiguous 0's only once in an address as described in RFC 2373.
          prefixLength: The prefix length.
              
              For IPv4 the value range is 0-31.
              For IPv6 prefixLength is a decimal value range 0-127. The property
              represents the number of contiguous, higher-order bits of the address that make
              up the network portion of the IP address.
          gateway: Where to send the packets for this route.
      """
      network: str
      prefixLength: int
      gateway: IpRouteConfigInfo.Gateway

   ipRoute: list[IpRouteConfigInfo.IpRoute] = []


class IpRouteConfigSpec(pyVmomi.vmodl.DynamicData):
   """
   Address family independent IP Route Table Configuration data object.
   
   Attributes:
       ipRoute: The set of updates to apply to the routing table.
   """
   class GatewaySpec(pyVmomi.vmodl.DynamicData):
      """
      IpRoute report an individual host, network or default destination network
      reachable through a given gateway.
      """
      ipAddress: _typing.Optional[str] = None
      device: _typing.Optional[str] = None

   class IpRouteSpec(pyVmomi.vmodl.DynamicData):
      """
      Specify an individual host, network or default destination network
      reachable through a given gateway.
      
      Attributes:
          network: IP Address of the destination IP network.
              
              IPv6 addresses are 128-bit addresses represented
              as eight fields of up to four hexadecimal digits. A colon separates each
              field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can
              also consist of symbol '::' to represent multiple 16-bit groups of
              contiguous 0's only once in an address as described in RFC 2373.
              To Specify a default network use the value: 0 with prefixLength 0.
          prefixLength: The prefix length.
              
              For IPv4 the value range is 0-31.
              For IPv6 prefixLength is a decimal value range 0-127. The property
              represents the number of contiguous, higher-order bits of the address that make
              up the network portion of the IP address.
          gateway: Where to send the packets for this route.
          operation: Requires one of the values from `pyVmomi.vim.host.ConfigChange.Operation`.
      """
      network: str
      prefixLength: int
      gateway: IpRouteConfigSpec.GatewaySpec
      operation: str

   ipRoute: list[IpRouteConfigSpec.IpRouteSpec] = []


class IpStackInfo(pyVmomi.vmodl.DynamicData):
   """
   Protocol version independent reporting data object for IP stack.
   
   Attributes:
       neighbor: Zero, one or more entries of neighbors discovered using ARP or NDP.
           
           This information is used to help diagnose connectivity or performance
           issues. This property maps to RFC 4293 ipNetToPhysicalTable.
       defaultRouter: Zero one or more entries of discovered IP routers that are directly
           reachable from an interface on this system.
           
           This property maps to RFC 4293 ipDefaultRouterTable.
   """
   class EntryType(pyVmomi.VmomiSupport.Enum):
      """
      IP Stack keeps state on entries in IpNetToMedia table to perform
      physical address lookups for IP addresses.
      
      Here are the standard
      states per @see RFC 4293 ipNetToMediaType.
      
      Attributes:
          other: This implementation is reporting something other than
              what states are listed below.
          invalid: The IP Stack has marked this entry as not useable.
          dynamic: This entry has been learned using ARP or NDP.
          manual: This entry was set manually.
      """
      other: _typing.ClassVar['IpStackInfo.EntryType'] = 'other'
      invalid: _typing.ClassVar['IpStackInfo.EntryType'] = 'invalid'
      dynamic: _typing.ClassVar['IpStackInfo.EntryType'] = 'dynamic'
      manual: _typing.ClassVar['IpStackInfo.EntryType'] = 'manual'

   class Preference(pyVmomi.VmomiSupport.Enum):
      """
      The set of values used to determine ordering of default routers.
      
      See RFC 4293 ipDefaultRouterPreference.
      """
      reserved: _typing.ClassVar['IpStackInfo.Preference'] = 'reserved'
      low: _typing.ClassVar['IpStackInfo.Preference'] = 'low'
      medium: _typing.ClassVar['IpStackInfo.Preference'] = 'medium'
      high: _typing.ClassVar['IpStackInfo.Preference'] = 'high'

   class NetToMedia(pyVmomi.vmodl.DynamicData):
      """
      Information from an IP stack about known mappings between an IP address
      and the underlying physical address it maps to as learned by:
      IPv4: Address Resolution Protocol (ARP) RFC 826
      IPv6: Neighbor Discovery Protocol (NDP) RFC 4861
      
      Attributes:
          ipAddress: A Unicast IP address of another system directly reachable w/o routing.
              
              IPv4 address is specified using dotted decimal notation.
              For example, \"192.0.2.1\".
              IPv6 addresses are 128-bit addresses represented as eight fields
              of up to four hexadecimal digits.
              A colon separates each field (:). For example,
              2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the
              symbol '::' to represent multiple 16-bit groups of
              contiguous 0's only once in an address as described in RFC 2373.
          physicalAddress: The media-dependent of the address or empty string if not yet learned.
              
              For Ethernet interfaces this is a MAC address reported in the format:
              XX:XX:XX:XX:XX:XX where XX are hexadecimal numbers.
          device: The value will be the name of the interface as reported by the
              operating system.
          type: The type/state of this entry as reported by the IP stack.
              
              See `pyVmomi.vim.net.IpStackInfo.EntryType` for values.
      """
      ipAddress: str
      physicalAddress: str
      device: str
      type: str

   class DefaultRouter(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          ipAddress: Unicast IP address of a next-hop router.
          device: This value will contain the name of the interface as reported by the
              operating system.
          lifetime: When this entry will no longer valid.
              
              For IPv6 this value
              see For IPv6 RFC 2462 sections 4.2 and 6.3.4.
          preference: Value of this entry compared to others that this IP stack uses
              when making selection to route traffic on the default
              route when there are multiple default routers.
              
              Value must be one of
              `pyVmomi.vim.net.IpStackInfo.Preference`
      """
      ipAddress: str
      device: str
      lifetime: _datetime.datetime
      preference: str

   neighbor: list[IpStackInfo.NetToMedia] = []
   defaultRouter: list[IpStackInfo.DefaultRouter] = []


class NetBIOSConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   This data object type describes the NetBIOS configuration of
   an operating system.
   
   Attributes:
       mode: NetBIOS configuration mode.
           
           The supported values are described by
           `pyVmomi.vim.net.NetBIOSConfigInfo.Mode`.
   """
   class Mode(pyVmomi.VmomiSupport.Enum):
      """
      NetBIOS configuration mode.
      
      Attributes:
          unknown: Mode of NetBIOS is unknown.
          enabled: NetBIOS is enabled.
          disabled: NetBIOS is disabled.
          enabledViaDHCP: DHCP server decides whether or not to use NetBIOS.
      """
      unknown: _typing.ClassVar['NetBIOSConfigInfo.Mode'] = 'unknown'
      enabled: _typing.ClassVar['NetBIOSConfigInfo.Mode'] = 'enabled'
      disabled: _typing.ClassVar['NetBIOSConfigInfo.Mode'] = 'disabled'
      enabledViaDHCP: _typing.ClassVar['NetBIOSConfigInfo.Mode'] = 'enabledViaDHCP'

   mode: str


class WinNetBIOSConfigInfo(NetBIOSConfigInfo):
   """
   This data object type describes the Windows-specific
   NetBIOS configuration.
   
   Attributes:
       primaryWINS: The IP address of the primary WINS server.
       secondaryWINS: The IP address of the secondary WINS server.
   """
   primaryWINS: str
   secondaryWINS: _typing.Optional[str] = None
