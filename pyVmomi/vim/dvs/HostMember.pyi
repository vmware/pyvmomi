# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.dvs import KeyedOpaqueBlob
from pyVmomi.vim.dvs import ProductSpec

class HostMember(DynamicData):
   class HostComponentState(Enum):
      up: ClassVar['HostComponentState'] = 'up'
      pending: ClassVar['HostComponentState'] = 'pending'
      outOfSync: ClassVar['HostComponentState'] = 'outOfSync'
      warning: ClassVar['HostComponentState'] = 'warning'
      disconnected: ClassVar['HostComponentState'] = 'disconnected'
      down: ClassVar['HostComponentState'] = 'down'

   class ConfigSpec(DynamicData):
      operation: str
      host: HostSystem
      backing: Optional[Backing] = None
      maxProxySwitchPorts: Optional[int] = None
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []

   class PnicSpec(DynamicData):
      pnicDevice: str
      uplinkPortKey: Optional[str] = None
      uplinkPortgroupKey: Optional[str] = None
      connectionCookie: Optional[int] = None

   class Backing(DynamicData):
      pass

   class PnicBacking(Backing):
      pnicSpec: list[PnicSpec] = []

   class RuntimeState(DynamicData):
      currentMaxProxySwitchPorts: int

   class TransportZoneType(Enum):
      vlan: ClassVar['TransportZoneType'] = 'vlan'
      overlay: ClassVar['TransportZoneType'] = 'overlay'

   class TransportZoneInfo(DynamicData):
      uuid: str
      type: str

   class ConfigInfo(DynamicData):
      host: Optional[HostSystem] = None
      maxProxySwitchPorts: int
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []
      backing: Backing
      nsxSwitch: Optional[bool] = None
      ensEnabled: Optional[bool] = None
      ensInterruptEnabled: Optional[bool] = None
      transportZones: list[TransportZoneInfo] = []
      nsxtUsedUplinkNames: list[str] = []
      networkOffloadingEnabled: Optional[bool] = None

   class HostUplinkState(DynamicData):
      class State(Enum):
         active: ClassVar['State'] = 'active'
         standby: ClassVar['State'] = 'standby'

      uplinkName: str
      state: str

   class RuntimeInfo(DynamicData):
      host: HostSystem
      status: Optional[str] = None
      statusDetail: Optional[str] = None
      nsxtStatus: Optional[str] = None
      nsxtStatusDetail: Optional[str] = None
      healthCheckResult: list[HealthCheckResult] = []
      hostUplinkState: list[HostUplinkState] = []

   class HealthCheckResult(DynamicData):
      summary: Optional[str] = None

   class UplinkHealthCheckResult(HealthCheckResult):
      uplinkPortKey: str

   runtimeState: Optional[RuntimeState] = None
   config: ConfigInfo
   productInfo: Optional[ProductSpec] = None
   uplinkPortKey: list[str] = []
   status: str
   statusDetail: Optional[str] = None
