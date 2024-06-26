# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import double
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Datastore
from pyVmomi.vim import HostSystem
from pyVmomi.vim import SharesInfo
from pyVmomi.vim import SharesOption
from pyVmomi.vim import StoragePod
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.cluster import ActionHistory
from pyVmomi.vim.cluster import DrsFaults
from pyVmomi.vim.cluster import Recommendation

from pyVmomi.vim.option import BoolOption
from pyVmomi.vim.option import IntOption
from pyVmomi.vim.option import LongOption

from pyVmomi.vim.storageDrs import ConfigInfo
from pyVmomi.vim.storageDrs import ConfigSpec
from pyVmomi.vim.storageDrs import StoragePlacementResult
from pyVmomi.vim.storageDrs import StoragePlacementSpec

class StorageResourceManager(ManagedObject):
   class IOAllocationInfo(DynamicData):
      limit: Optional[long] = None
      shares: Optional[SharesInfo] = None
      reservation: Optional[int] = None

   class IOAllocationOption(DynamicData):
      limitOption: LongOption
      sharesOption: SharesOption

   class CongestionThresholdMode(Enum):
      automatic: ClassVar['CongestionThresholdMode'] = 'automatic'
      manual: ClassVar['CongestionThresholdMode'] = 'manual'

   class IORMConfigInfo(DynamicData):
      enabled: bool
      congestionThresholdMode: str
      congestionThreshold: int
      percentOfPeakThroughput: Optional[int] = None
      statsCollectionEnabled: bool
      reservationEnabled: bool
      statsAggregationDisabled: Optional[bool] = None
      reservableIopsThreshold: Optional[int] = None

   class IORMConfigSpec(DynamicData):
      enabled: Optional[bool] = None
      congestionThresholdMode: Optional[str] = None
      congestionThreshold: Optional[int] = None
      percentOfPeakThroughput: Optional[int] = None
      statsCollectionEnabled: Optional[bool] = None
      reservationEnabled: Optional[bool] = None
      statsAggregationDisabled: Optional[bool] = None
      reservableIopsThreshold: Optional[int] = None

   class IORMConfigOption(DynamicData):
      enabledOption: BoolOption
      congestionThresholdOption: IntOption
      statsCollectionEnabledOption: BoolOption
      reservationEnabledOption: BoolOption

   class StoragePerformanceSummary(DynamicData):
      interval: int
      percentile: list[int] = []
      datastoreReadLatency: list[double] = []
      datastoreWriteLatency: list[double] = []
      datastoreVmLatency: list[double] = []
      datastoreReadIops: list[double] = []
      datastoreWriteIops: list[double] = []
      siocActivityDuration: int

   class PodStorageDrsEntry(DynamicData):
      storageDrsConfig: ConfigInfo
      recommendation: list[Recommendation] = []
      drsFault: list[DrsFaults] = []
      actionHistory: list[ActionHistory] = []

   class StorageProfileStatistics(DynamicData):
      profileId: str
      totalSpaceMB: long
      usedSpaceMB: long

   def ConfigureDatastoreIORM(self, datastore: Datastore, spec: IORMConfigSpec) -> Task: ...
   def QueryIORMConfigOption(self, host: HostSystem) -> IORMConfigOption: ...
   def QueryDatastorePerformanceSummary(self, datastore: Datastore) -> list[StoragePerformanceSummary]: ...
   def ApplyRecommendationToPod(self, pod: StoragePod, key: str) -> Task: ...
   def ApplyRecommendation(self, key: list[str]) -> Task: ...
   def CancelRecommendation(self, key: list[str]) -> NoReturn: ...
   def RefreshRecommendation(self, pod: StoragePod) -> NoReturn: ...
   def RefreshRecommendationsForPod(self, pod: StoragePod) -> Task: ...
   def ConfigureStorageDrsForPod(self, pod: StoragePod, spec: ConfigSpec, modify: bool) -> Task: ...
   def ValidateStoragePodConfig(self, pod: StoragePod, spec: ConfigSpec) -> Optional[MethodFault]: ...
   def RecommendDatastores(self, storageSpec: StoragePlacementSpec) -> StoragePlacementResult: ...
