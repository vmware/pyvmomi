# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import DistributedVirtualSwitch
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Network
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.dvs import DistributedVirtualPort
from pyVmomi.vim.dvs import EntityBackup
from pyVmomi.vim.dvs import KeyedOpaqueBlob

class DistributedVirtualPortgroup(Network):
   class PortgroupType(Enum):
      earlyBinding: ClassVar['PortgroupType'] = 'earlyBinding'
      lateBinding: ClassVar['PortgroupType'] = 'lateBinding'
      ephemeral: ClassVar['PortgroupType'] = 'ephemeral'

   class BackingType(Enum):
      standard: ClassVar['BackingType'] = 'standard'
      nsx: ClassVar['BackingType'] = 'nsx'

   class PortgroupPolicy(DynamicData):
      blockOverrideAllowed: bool
      shapingOverrideAllowed: bool
      vendorConfigOverrideAllowed: bool
      livePortMovingAllowed: bool
      portConfigResetAtDisconnect: bool
      networkResourcePoolOverrideAllowed: Optional[bool] = None
      trafficFilterOverrideAllowed: Optional[bool] = None

   class MetaTagName(Enum):
      dvsName: ClassVar['MetaTagName'] = 'dvsName'
      portgroupName: ClassVar['MetaTagName'] = 'portgroupName'
      portIndex: ClassVar['MetaTagName'] = 'portIndex'

   class ConfigSpec(DynamicData):
      configVersion: Optional[str] = None
      name: Optional[str] = None
      numPorts: Optional[int] = None
      portNameFormat: Optional[str] = None
      defaultPortConfig: Optional[DistributedVirtualPort.Setting] = None
      description: Optional[str] = None
      type: Optional[str] = None
      backingType: Optional[str] = None
      scope: list[ManagedEntity] = []
      policy: Optional[PortgroupPolicy] = None
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []
      autoExpand: Optional[bool] = None
      vmVnicNetworkResourcePoolKey: Optional[str] = None
      transportZoneUuid: Optional[str] = None
      transportZoneName: Optional[str] = None
      logicalSwitchUuid: Optional[str] = None
      segmentId: Optional[str] = None

   class ConfigInfo(DynamicData):
      key: str
      name: str
      numPorts: int
      distributedVirtualSwitch: Optional[DistributedVirtualSwitch] = None
      defaultPortConfig: Optional[DistributedVirtualPort.Setting] = None
      description: Optional[str] = None
      type: str
      backingType: Optional[str] = None
      policy: PortgroupPolicy
      portNameFormat: Optional[str] = None
      scope: list[ManagedEntity] = []
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []
      configVersion: Optional[str] = None
      autoExpand: Optional[bool] = None
      vmVnicNetworkResourcePoolKey: Optional[str] = None
      uplink: Optional[bool] = None
      transportZoneUuid: Optional[str] = None
      transportZoneName: Optional[str] = None
      logicalSwitchUuid: Optional[str] = None
      segmentId: Optional[str] = None

   class Problem(DynamicData):
      logicalSwitchUuid: str
      fault: MethodFault

   class NsxPortgroupOperationResult(DynamicData):
      portgroups: list[DistributedVirtualPortgroup] = []
      problems: list[Problem] = []

   @property
   def key(self) -> str: ...
   @property
   def config(self) -> ConfigInfo: ...
   @property
   def portKeys(self) -> list[str]: ...

   def Reconfigure(self, spec: ConfigSpec) -> Task: ...
   def Rollback(self, entityBackup: Optional[EntityBackup.Config]) -> Task: ...
