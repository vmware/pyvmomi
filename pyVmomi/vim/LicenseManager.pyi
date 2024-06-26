# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import HostSystem
from pyVmomi.vim import KeyValue
from pyVmomi.vim import LicenseAssignmentManager

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import KeyAnyValue

class LicenseManager(ManagedObject):
   class LicenseState(Enum):
      initializing: ClassVar['LicenseState'] = 'initializing'
      normal: ClassVar['LicenseState'] = 'normal'
      marginal: ClassVar['LicenseState'] = 'marginal'
      fault: ClassVar['LicenseState'] = 'fault'

   class LicenseKey(Enum):
      esxFull: ClassVar['LicenseKey'] = 'esxFull'
      esxVmtn: ClassVar['LicenseKey'] = 'esxVmtn'
      esxExpress: ClassVar['LicenseKey'] = 'esxExpress'
      san: ClassVar['LicenseKey'] = 'san'
      iscsi: ClassVar['LicenseKey'] = 'iscsi'
      nas: ClassVar['LicenseKey'] = 'nas'
      vsmp: ClassVar['LicenseKey'] = 'vsmp'
      backup: ClassVar['LicenseKey'] = 'backup'
      vc: ClassVar['LicenseKey'] = 'vc'
      vcExpress: ClassVar['LicenseKey'] = 'vcExpress'
      esxHost: ClassVar['LicenseKey'] = 'esxHost'
      gsxHost: ClassVar['LicenseKey'] = 'gsxHost'
      serverHost: ClassVar['LicenseKey'] = 'serverHost'
      drsPower: ClassVar['LicenseKey'] = 'drsPower'
      vmotion: ClassVar['LicenseKey'] = 'vmotion'
      drs: ClassVar['LicenseKey'] = 'drs'
      das: ClassVar['LicenseKey'] = 'das'

   class LicenseSource(DynamicData):
      pass

   class LicenseServer(LicenseSource):
      licenseServer: str

   class LocalLicense(LicenseSource):
      licenseKeys: str

   class EvaluationLicense(LicenseSource):
      remainingHours: Optional[long] = None

   class FeatureInfo(DynamicData):
      class CostUnit(Enum):
         host: ClassVar['CostUnit'] = 'host'
         cpuCore: ClassVar['CostUnit'] = 'cpuCore'
         cpuPackage: ClassVar['CostUnit'] = 'cpuPackage'
         server: ClassVar['CostUnit'] = 'server'
         vm: ClassVar['CostUnit'] = 'vm'

      class State(Enum):
         enabled: ClassVar['State'] = 'enabled'
         disabled: ClassVar['State'] = 'disabled'
         optional: ClassVar['State'] = 'optional'

      class SourceRestriction(Enum):
         unrestricted: ClassVar['SourceRestriction'] = 'unrestricted'
         served: ClassVar['SourceRestriction'] = 'served'
         file: ClassVar['SourceRestriction'] = 'file'

      key: str
      featureName: str
      featureDescription: Optional[str] = None
      state: Optional[State] = None
      costUnit: str
      sourceRestriction: Optional[str] = None
      dependentKey: list[str] = []
      edition: Optional[bool] = None
      expiresOn: Optional[datetime] = None

   class ReservationInfo(DynamicData):
      class State(Enum):
         notUsed: ClassVar['State'] = 'notUsed'
         noLicense: ClassVar['State'] = 'noLicense'
         unlicensedUse: ClassVar['State'] = 'unlicensedUse'
         licensed: ClassVar['State'] = 'licensed'

      key: str
      state: State
      required: int

   class AvailabilityInfo(DynamicData):
      feature: FeatureInfo
      total: int
      available: int

   class DiagnosticInfo(DynamicData):
      sourceLastChanged: datetime
      sourceLost: str
      sourceLatency: float
      licenseRequests: str
      licenseRequestFailures: str
      licenseFeatureUnknowns: str
      opState: LicenseState
      lastStatusUpdate: datetime
      opFailureMessage: str

   class LicenseUsageInfo(DynamicData):
      source: LicenseSource
      sourceAvailable: bool
      reservationInfo: list[ReservationInfo] = []
      featureInfo: list[FeatureInfo] = []

   class EvaluationInfo(DynamicData):
      properties: list[KeyAnyValue] = []

   class LicensableResourceInfo(DynamicData):
      class ResourceKey(Enum):
         numCpuPackages: ClassVar['ResourceKey'] = 'numCpuPackages'
         numCpuCores: ClassVar['ResourceKey'] = 'numCpuCores'
         memorySize: ClassVar['ResourceKey'] = 'memorySize'
         memoryForVms: ClassVar['ResourceKey'] = 'memoryForVms'
         numVmsStarted: ClassVar['ResourceKey'] = 'numVmsStarted'
         numVmsStarting: ClassVar['ResourceKey'] = 'numVmsStarting'
         vsanCapacity: ClassVar['ResourceKey'] = 'vsanCapacity'

      resource: list[KeyAnyValue] = []

   class LicenseInfo(DynamicData):
      licenseKey: str
      editionKey: str
      name: str
      total: int
      used: Optional[int] = None
      costUnit: str
      properties: list[KeyAnyValue] = []
      labels: list[KeyValue] = []

   @property
   def source(self) -> LicenseSource: ...
   @property
   def sourceAvailable(self) -> bool: ...
   @property
   def diagnostics(self) -> Optional[DiagnosticInfo]: ...
   @property
   def featureInfo(self) -> list[FeatureInfo]: ...
   @property
   def licensedEdition(self) -> str: ...
   @property
   def licenses(self) -> list[LicenseInfo]: ...
   @property
   def licenseAssignmentManager(self) -> Optional[LicenseAssignmentManager]: ...
   @property
   def evaluation(self) -> EvaluationInfo: ...

   def QuerySupportedFeatures(self, host: Optional[HostSystem]) -> list[FeatureInfo]: ...
   def QuerySourceAvailability(self, host: Optional[HostSystem]) -> list[AvailabilityInfo]: ...
   def QueryUsage(self, host: Optional[HostSystem]) -> LicenseUsageInfo: ...
   def SetEdition(self, host: Optional[HostSystem], featureKey: Optional[str]) -> NoReturn: ...
   def CheckFeature(self, host: Optional[HostSystem], featureKey: str) -> bool: ...
   def Enable(self, host: Optional[HostSystem], featureKey: str) -> bool: ...
   def Disable(self, host: Optional[HostSystem], featureKey: str) -> bool: ...
   def ConfigureSource(self, host: Optional[HostSystem], licenseSource: LicenseSource) -> NoReturn: ...
   def UpdateLicense(self, licenseKey: str, labels: list[KeyValue]) -> LicenseInfo: ...
   def AddLicense(self, licenseKey: str, labels: list[KeyValue]) -> LicenseInfo: ...
   def RemoveLicense(self, licenseKey: str) -> NoReturn: ...
   def DecodeLicense(self, licenseKey: str) -> LicenseInfo: ...
   def UpdateLabel(self, licenseKey: str, labelKey: str, labelValue: str) -> NoReturn: ...
   def RemoveLabel(self, licenseKey: str, labelKey: str) -> NoReturn: ...
