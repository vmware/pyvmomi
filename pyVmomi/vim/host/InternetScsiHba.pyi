# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import HostBusAdapter

from pyVmomi.vim.option import OptionDef
from pyVmomi.vim.option import OptionValue

class InternetScsiHba(HostBusAdapter):
   class ParamValue(OptionValue):
      isInherited: Optional[bool] = None

   class DiscoveryCapabilities(DynamicData):
      iSnsDiscoverySettable: bool
      slpDiscoverySettable: bool
      staticTargetDiscoverySettable: bool
      sendTargetsDiscoverySettable: bool

   class DiscoveryProperties(DynamicData):
      class ISnsDiscoveryMethod(Enum):
         isnsStatic: ClassVar['ISnsDiscoveryMethod'] = 'isnsStatic'
         isnsDhcp: ClassVar['ISnsDiscoveryMethod'] = 'isnsDhcp'
         isnsSlp: ClassVar['ISnsDiscoveryMethod'] = 'isnsSlp'

      class SlpDiscoveryMethod(Enum):
         slpDhcp: ClassVar['SlpDiscoveryMethod'] = 'slpDhcp'
         slpAutoUnicast: ClassVar['SlpDiscoveryMethod'] = 'slpAutoUnicast'
         slpAutoMulticast: ClassVar['SlpDiscoveryMethod'] = 'slpAutoMulticast'
         slpManual: ClassVar['SlpDiscoveryMethod'] = 'slpManual'

      iSnsDiscoveryEnabled: bool
      iSnsDiscoveryMethod: Optional[str] = None
      iSnsHost: Optional[str] = None
      slpDiscoveryEnabled: bool
      slpDiscoveryMethod: Optional[str] = None
      slpHost: Optional[str] = None
      staticTargetDiscoveryEnabled: bool
      sendTargetsDiscoveryEnabled: bool

   class ChapAuthenticationType(Enum):
      chapProhibited: ClassVar['ChapAuthenticationType'] = 'chapProhibited'
      chapDiscouraged: ClassVar['ChapAuthenticationType'] = 'chapDiscouraged'
      chapPreferred: ClassVar['ChapAuthenticationType'] = 'chapPreferred'
      chapRequired: ClassVar['ChapAuthenticationType'] = 'chapRequired'

   class AuthenticationCapabilities(DynamicData):
      chapAuthSettable: bool
      krb5AuthSettable: bool
      srpAuthSettable: bool
      spkmAuthSettable: bool
      mutualChapSettable: Optional[bool] = None
      targetChapSettable: Optional[bool] = None
      targetMutualChapSettable: Optional[bool] = None

   class AuthenticationProperties(DynamicData):
      chapAuthEnabled: bool
      chapName: Optional[str] = None
      chapSecret: Optional[str] = None
      chapAuthenticationType: Optional[str] = None
      chapInherited: Optional[bool] = None
      mutualChapName: Optional[str] = None
      mutualChapSecret: Optional[str] = None
      mutualChapAuthenticationType: Optional[str] = None
      mutualChapInherited: Optional[bool] = None

   class DigestType(Enum):
      digestProhibited: ClassVar['DigestType'] = 'digestProhibited'
      digestDiscouraged: ClassVar['DigestType'] = 'digestDiscouraged'
      digestPreferred: ClassVar['DigestType'] = 'digestPreferred'
      digestRequired: ClassVar['DigestType'] = 'digestRequired'

   class DigestCapabilities(DynamicData):
      headerDigestSettable: Optional[bool] = None
      dataDigestSettable: Optional[bool] = None
      targetHeaderDigestSettable: Optional[bool] = None
      targetDataDigestSettable: Optional[bool] = None

   class DigestProperties(DynamicData):
      headerDigestType: Optional[str] = None
      headerDigestInherited: Optional[bool] = None
      dataDigestType: Optional[str] = None
      dataDigestInherited: Optional[bool] = None

   class IPCapabilities(DynamicData):
      addressSettable: bool
      ipConfigurationMethodSettable: bool
      subnetMaskSettable: bool
      defaultGatewaySettable: bool
      primaryDnsServerAddressSettable: bool
      alternateDnsServerAddressSettable: bool
      ipv6Supported: Optional[bool] = None
      arpRedirectSettable: Optional[bool] = None
      mtuSettable: Optional[bool] = None
      hostNameAsTargetAddress: Optional[bool] = None
      nameAliasSettable: Optional[bool] = None
      ipv4EnableSettable: Optional[bool] = None
      ipv6EnableSettable: Optional[bool] = None
      ipv6PrefixLengthSettable: Optional[bool] = None
      ipv6PrefixLength: Optional[int] = None
      ipv6DhcpConfigurationSettable: Optional[bool] = None
      ipv6LinkLocalAutoConfigurationSettable: Optional[bool] = None
      ipv6RouterAdvertisementConfigurationSettable: Optional[bool] = None
      ipv6DefaultGatewaySettable: Optional[bool] = None
      ipv6MaxStaticAddressesSupported: Optional[int] = None

   class IscsiIpv6Address(DynamicData):
      class AddressConfigurationType(Enum):
         DHCP: ClassVar['AddressConfigurationType'] = 'DHCP'
         AutoConfigured: ClassVar['AddressConfigurationType'] = 'AutoConfigured'
         Static: ClassVar['AddressConfigurationType'] = 'Static'
         Other: ClassVar['AddressConfigurationType'] = 'Other'

      class IPv6AddressOperation(Enum):
         add: ClassVar['IPv6AddressOperation'] = 'add'
         remove: ClassVar['IPv6AddressOperation'] = 'remove'

      address: str
      prefixLength: int
      origin: str
      operation: Optional[str] = None

   class IPv6Properties(DynamicData):
      iscsiIpv6Address: list[IscsiIpv6Address] = []
      ipv6DhcpConfigurationEnabled: Optional[bool] = None
      ipv6LinkLocalAutoConfigurationEnabled: Optional[bool] = None
      ipv6RouterAdvertisementConfigurationEnabled: Optional[bool] = None
      ipv6DefaultGateway: Optional[str] = None

   class IPProperties(DynamicData):
      mac: Optional[str] = None
      address: Optional[str] = None
      dhcpConfigurationEnabled: bool
      subnetMask: Optional[str] = None
      defaultGateway: Optional[str] = None
      primaryDnsServerAddress: Optional[str] = None
      alternateDnsServerAddress: Optional[str] = None
      ipv6Address: Optional[str] = None
      ipv6SubnetMask: Optional[str] = None
      ipv6DefaultGateway: Optional[str] = None
      arpRedirectEnabled: Optional[bool] = None
      mtu: Optional[int] = None
      jumboFramesEnabled: Optional[bool] = None
      ipv4Enabled: Optional[bool] = None
      ipv6Enabled: Optional[bool] = None
      ipv6properties: Optional[IPv6Properties] = None

   class SendTarget(DynamicData):
      address: str
      port: Optional[int] = None
      authenticationProperties: Optional[AuthenticationProperties] = None
      digestProperties: Optional[DigestProperties] = None
      supportedAdvancedOptions: list[OptionDef] = []
      advancedOptions: list[ParamValue] = []
      parent: Optional[str] = None

   class StaticTarget(DynamicData):
      class TargetDiscoveryMethod(Enum):
         staticMethod: ClassVar['TargetDiscoveryMethod'] = 'staticMethod'
         sendTargetMethod: ClassVar['TargetDiscoveryMethod'] = 'sendTargetMethod'
         slpMethod: ClassVar['TargetDiscoveryMethod'] = 'slpMethod'
         isnsMethod: ClassVar['TargetDiscoveryMethod'] = 'isnsMethod'
         unknownMethod: ClassVar['TargetDiscoveryMethod'] = 'unknownMethod'

      address: str
      port: Optional[int] = None
      iScsiName: str
      discoveryMethod: Optional[str] = None
      authenticationProperties: Optional[AuthenticationProperties] = None
      digestProperties: Optional[DigestProperties] = None
      supportedAdvancedOptions: list[OptionDef] = []
      advancedOptions: list[ParamValue] = []
      parent: Optional[str] = None

   class TargetSet(DynamicData):
      staticTargets: list[StaticTarget] = []
      sendTargets: list[SendTarget] = []

   class NetworkBindingSupportType(Enum):
      notsupported: ClassVar['NetworkBindingSupportType'] = 'notsupported'
      optional: ClassVar['NetworkBindingSupportType'] = 'optional'
      required: ClassVar['NetworkBindingSupportType'] = 'required'

   isSoftwareBased: bool
   canBeDisabled: Optional[bool] = None
   networkBindingSupport: Optional[NetworkBindingSupportType] = None
   discoveryCapabilities: DiscoveryCapabilities
   discoveryProperties: DiscoveryProperties
   authenticationCapabilities: AuthenticationCapabilities
   authenticationProperties: AuthenticationProperties
   digestCapabilities: Optional[DigestCapabilities] = None
   digestProperties: Optional[DigestProperties] = None
   ipCapabilities: IPCapabilities
   ipProperties: IPProperties
   supportedAdvancedOptions: list[OptionDef] = []
   advancedOptions: list[ParamValue] = []
   iScsiName: str
   iScsiAlias: Optional[str] = None
   configuredSendTarget: list[SendTarget] = []
   configuredStaticTarget: list[StaticTarget] = []
   maxSpeedMb: Optional[int] = None
   currentSpeedMb: Optional[int] = None
