# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import BoolPolicy
from pyVmomi.vim import HostSystem
from pyVmomi.vim import InheritablePolicy
from pyVmomi.vim import LongPolicy
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import NumericRange
from pyVmomi.vim import StringPolicy

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.dvs import KeyedOpaqueBlob
from pyVmomi.vim.dvs import PortConnectee
from pyVmomi.vim.dvs import PortStatistics
from pyVmomi.vim.dvs import TrafficRuleset

class DistributedVirtualPort(DynamicData):
   class ConfigSpec(DynamicData):
      operation: str
      key: Optional[str] = None
      name: Optional[str] = None
      scope: list[ManagedEntity] = []
      description: Optional[str] = None
      setting: Optional[Setting] = None
      configVersion: Optional[str] = None

   class ConfigInfo(DynamicData):
      name: Optional[str] = None
      scope: list[ManagedEntity] = []
      description: Optional[str] = None
      setting: Optional[Setting] = None
      configVersion: str

   class TrafficShapingPolicy(InheritablePolicy):
      enabled: Optional[BoolPolicy] = None
      averageBandwidth: Optional[LongPolicy] = None
      peakBandwidth: Optional[LongPolicy] = None
      burstSize: Optional[LongPolicy] = None

   class HostLocalPortInfo(DynamicData):
      switchUuid: str
      portKey: str
      setting: Setting
      vnic: str

   class VendorSpecificConfig(InheritablePolicy):
      keyValue: list[KeyedOpaqueBlob] = []

   class FilterParameter(DynamicData):
      parameters: list[str] = []

   class FilterOnFailure(Enum):
      failOpen: ClassVar['FilterOnFailure'] = 'failOpen'
      failClosed: ClassVar['FilterOnFailure'] = 'failClosed'

   class FilterConfig(InheritablePolicy):
      key: Optional[str] = None
      agentName: Optional[str] = None
      slotNumber: Optional[str] = None
      parameters: Optional[FilterParameter] = None
      onFailure: Optional[str] = None

   class TrafficFilterConfig(FilterConfig):
      trafficRuleset: Optional[TrafficRuleset] = None

   class FilterConfigSpec(FilterConfig):
      operation: str

   class TrafficFilterConfigSpec(TrafficFilterConfig):
      operation: str

   class FilterPolicy(InheritablePolicy):
      filterConfig: list[FilterConfig] = []

   class Setting(DynamicData):
      blocked: Optional[BoolPolicy] = None
      vmDirectPathGen2Allowed: Optional[BoolPolicy] = None
      inShapingPolicy: Optional[TrafficShapingPolicy] = None
      outShapingPolicy: Optional[TrafficShapingPolicy] = None
      vendorSpecificConfig: Optional[VendorSpecificConfig] = None
      networkResourcePoolKey: Optional[StringPolicy] = None
      filterPolicy: Optional[FilterPolicy] = None

   class RuntimeInfo(DynamicData):
      class VmDirectPathGen2InactiveReasonNetwork(Enum):
         portNptIncompatibleDvs: ClassVar['VmDirectPathGen2InactiveReasonNetwork'] = 'portNptIncompatibleDvs'
         portNptNoCompatibleNics: ClassVar['VmDirectPathGen2InactiveReasonNetwork'] = 'portNptNoCompatibleNics'
         portNptNoVirtualFunctionsAvailable: ClassVar['VmDirectPathGen2InactiveReasonNetwork'] = 'portNptNoVirtualFunctionsAvailable'
         portNptDisabledForPort: ClassVar['VmDirectPathGen2InactiveReasonNetwork'] = 'portNptDisabledForPort'

      class VmDirectPathGen2InactiveReasonOther(Enum):
         portNptIncompatibleHost: ClassVar['VmDirectPathGen2InactiveReasonOther'] = 'portNptIncompatibleHost'
         portNptIncompatibleConnectee: ClassVar['VmDirectPathGen2InactiveReasonOther'] = 'portNptIncompatibleConnectee'

      linkUp: bool
      blocked: bool
      vlanIds: list[NumericRange] = []
      trunkingMode: Optional[bool] = None
      mtu: Optional[int] = None
      linkPeer: Optional[str] = None
      macAddress: Optional[str] = None
      statusDetail: Optional[str] = None
      vmDirectPathGen2Active: Optional[bool] = None
      vmDirectPathGen2InactiveReasonNetwork: list[str] = []
      vmDirectPathGen2InactiveReasonOther: list[str] = []
      vmDirectPathGen2InactiveReasonExtended: Optional[str] = None

   class State(DynamicData):
      runtimeInfo: Optional[RuntimeInfo] = None
      stats: PortStatistics
      vendorSpecificState: list[KeyedOpaqueBlob] = []

   key: str
   config: ConfigInfo
   dvsUuid: str
   portgroupKey: Optional[str] = None
   proxyHost: Optional[HostSystem] = None
   connectee: Optional[PortConnectee] = None
   conflict: bool
   conflictPortKey: Optional[str] = None
   state: Optional[State] = None
   connectionCookie: Optional[int] = None
   lastStatusChange: datetime
   hostLocalPort: Optional[bool] = None
   externalId: Optional[str] = None
   segmentPortId: Optional[str] = None
