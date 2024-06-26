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

from pyVmomi.vim import ElementDescription
from pyVmomi.vim import HistoricalInterval
from pyVmomi.vim import PerformanceDescription

from pyVmomi.vmodl import DynamicData

class PerformanceManager(ManagedObject):
   class Format(Enum):
      normal: ClassVar['Format'] = 'normal'
      csv: ClassVar['Format'] = 'csv'

   class ProviderSummary(DynamicData):
      entity: ManagedObject
      currentSupported: bool
      summarySupported: bool
      refreshRate: Optional[int] = None

   class CounterInfo(DynamicData):
      class RollupType(Enum):
         average: ClassVar['RollupType'] = 'average'
         maximum: ClassVar['RollupType'] = 'maximum'
         minimum: ClassVar['RollupType'] = 'minimum'
         latest: ClassVar['RollupType'] = 'latest'
         summation: ClassVar['RollupType'] = 'summation'
         none: ClassVar['RollupType'] = 'none'

      class StatsType(Enum):
         absolute: ClassVar['StatsType'] = 'absolute'
         delta: ClassVar['StatsType'] = 'delta'
         rate: ClassVar['StatsType'] = 'rate'

      class Unit(Enum):
         percent: ClassVar['Unit'] = 'percent'
         kiloBytes: ClassVar['Unit'] = 'kiloBytes'
         megaBytes: ClassVar['Unit'] = 'megaBytes'
         gigaBytes: ClassVar['Unit'] = 'gigaBytes'
         megaHertz: ClassVar['Unit'] = 'megaHertz'
         number: ClassVar['Unit'] = 'number'
         microsecond: ClassVar['Unit'] = 'microsecond'
         millisecond: ClassVar['Unit'] = 'millisecond'
         second: ClassVar['Unit'] = 'second'
         kiloBytesPerSecond: ClassVar['Unit'] = 'kiloBytesPerSecond'
         megaBytesPerSecond: ClassVar['Unit'] = 'megaBytesPerSecond'
         watt: ClassVar['Unit'] = 'watt'
         joule: ClassVar['Unit'] = 'joule'
         teraBytes: ClassVar['Unit'] = 'teraBytes'
         celsius: ClassVar['Unit'] = 'celsius'
         nanosecond: ClassVar['Unit'] = 'nanosecond'

      key: int
      nameInfo: ElementDescription
      groupInfo: ElementDescription
      unitInfo: ElementDescription
      rollupType: RollupType
      statsType: StatsType
      level: Optional[int] = None
      perDeviceLevel: Optional[int] = None
      associatedCounterId: list[int] = []

   class MetricId(DynamicData):
      counterId: int
      instance: str

   class QuerySpec(DynamicData):
      entity: ManagedObject
      startTime: Optional[datetime] = None
      endTime: Optional[datetime] = None
      maxSample: Optional[int] = None
      metricId: list[MetricId] = []
      intervalId: Optional[int] = None
      format: Optional[str] = None

   class SampleInfo(DynamicData):
      timestamp: datetime
      interval: int

   class MetricSeries(DynamicData):
      id: MetricId

   class IntSeries(MetricSeries):
      value: list[long] = []

   class MetricSeriesCSV(MetricSeries):
      value: Optional[str] = None

   class EntityMetricBase(DynamicData):
      entity: ManagedObject

   class EntityMetric(EntityMetricBase):
      sampleInfo: list[SampleInfo] = []
      value: list[MetricSeries] = []

   class EntityMetricCSV(EntityMetricBase):
      sampleInfoCSV: str
      value: list[MetricSeriesCSV] = []

   class CompositeEntityMetric(DynamicData):
      entity: Optional[EntityMetricBase] = None
      childEntity: list[EntityMetricBase] = []

   class CounterLevelMapping(DynamicData):
      counterId: int
      aggregateLevel: Optional[int] = None
      perDeviceLevel: Optional[int] = None

   @property
   def description(self) -> PerformanceDescription: ...
   @property
   def historicalInterval(self) -> list[HistoricalInterval]: ...
   @property
   def perfCounter(self) -> list[CounterInfo]: ...

   def QueryProviderSummary(self, entity: ManagedObject) -> ProviderSummary: ...
   def QueryAvailableMetric(self, entity: ManagedObject, beginTime: Optional[datetime], endTime: Optional[datetime], intervalId: Optional[int]) -> list[MetricId]: ...
   def QueryCounter(self, counterId: list[int]) -> list[CounterInfo]: ...
   def QueryCounterByLevel(self, level: int) -> list[CounterInfo]: ...
   def QueryStats(self, querySpec: list[QuerySpec]) -> list[EntityMetricBase]: ...
   def QueryCompositeStats(self, querySpec: QuerySpec) -> CompositeEntityMetric: ...
   def CreateHistoricalInterval(self, intervalId: HistoricalInterval) -> NoReturn: ...
   def RemoveHistoricalInterval(self, samplePeriod: int) -> NoReturn: ...
   def UpdateHistoricalInterval(self, interval: HistoricalInterval) -> NoReturn: ...
   def UpdateCounterLevelMapping(self, counterLevelMap: list[CounterLevelMapping]) -> NoReturn: ...
   def ResetCounterLevelMapping(self, counters: list[int]) -> NoReturn: ...
