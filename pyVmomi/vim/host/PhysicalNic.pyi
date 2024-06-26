# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import KeyAnyValue

from pyVmomi.vim.host import FcoeConfig
from pyVmomi.vim.host import IpConfig
from pyVmomi.vim.host import RdmaDevice

class PhysicalNic(DynamicData):
   class Specification(DynamicData):
      ip: Optional[IpConfig] = None
      linkSpeed: Optional[LinkSpeedDuplex] = None
      enableEnhancedNetworkingStack: Optional[bool] = None
      ensInterruptEnabled: Optional[bool] = None

   class Config(DynamicData):
      device: str
      spec: Specification

   class LinkSpeedDuplex(DynamicData):
      speedMb: int
      duplex: bool

   class NetworkHint(DynamicData):
      class HintElement(DynamicData):
         vlanId: Optional[int] = None

      class IpNetwork(NetworkHint.HintElement):
         ipSubnet: str

      class NamedNetwork(NetworkHint.HintElement):
         network: str

      device: str
      subnet: list[IpNetwork] = []
      network: list[NamedNetwork] = []
      connectedSwitchPort: Optional[CdpInfo] = None
      lldpInfo: Optional[LldpInfo] = None

   class CdpDeviceCapability(DynamicData):
      router: bool
      transparentBridge: bool
      sourceRouteBridge: bool
      networkSwitch: bool
      host: bool
      igmpEnabled: bool
      repeater: bool

   class CdpInfo(DynamicData):
      cdpVersion: Optional[int] = None
      timeout: Optional[int] = None
      ttl: Optional[int] = None
      samples: Optional[int] = None
      devId: Optional[str] = None
      address: Optional[str] = None
      portId: Optional[str] = None
      deviceCapability: Optional[CdpDeviceCapability] = None
      softwareVersion: Optional[str] = None
      hardwarePlatform: Optional[str] = None
      ipPrefix: Optional[str] = None
      ipPrefixLen: Optional[int] = None
      vlan: Optional[int] = None
      fullDuplex: Optional[bool] = None
      mtu: Optional[int] = None
      systemName: Optional[str] = None
      systemOID: Optional[str] = None
      mgmtAddr: Optional[str] = None
      location: Optional[str] = None

   class LldpInfo(DynamicData):
      chassisId: str
      portId: str
      timeToLive: int
      parameter: list[KeyAnyValue] = []

   class VmDirectPathGen2SupportedMode(Enum):
      upt: ClassVar['VmDirectPathGen2SupportedMode'] = 'upt'

   class ResourcePoolSchedulerDisallowedReason(Enum):
      userOptOut: ClassVar['ResourcePoolSchedulerDisallowedReason'] = 'userOptOut'
      hardwareUnsupported: ClassVar['ResourcePoolSchedulerDisallowedReason'] = 'hardwareUnsupported'

   key: Optional[str] = None
   device: str
   pci: str
   driver: Optional[str] = None
   driverVersion: Optional[str] = None
   firmwareVersion: Optional[str] = None
   linkSpeed: Optional[LinkSpeedDuplex] = None
   validLinkSpecification: list[LinkSpeedDuplex] = []
   spec: Specification
   wakeOnLanSupported: bool
   mac: str
   fcoeConfiguration: Optional[FcoeConfig] = None
   vmDirectPathGen2Supported: Optional[bool] = None
   vmDirectPathGen2SupportedMode: Optional[str] = None
   resourcePoolSchedulerAllowed: Optional[bool] = None
   resourcePoolSchedulerDisallowedReason: list[str] = []
   autoNegotiateSupported: Optional[bool] = None
   enhancedNetworkingStackSupported: Optional[bool] = None
   ensInterruptSupported: Optional[bool] = None
   rdmaDevice: Optional[RdmaDevice] = None
   dpuId: Optional[str] = None
