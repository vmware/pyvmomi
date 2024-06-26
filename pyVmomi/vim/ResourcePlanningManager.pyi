# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import HistoricalInterval

from pyVmomi.vmodl import DynamicData

class ResourcePlanningManager(ManagedObject):
   class DatabaseSizeParam(DynamicData):
      inventoryDesc: InventoryDescription
      perfStatsDesc: Optional[PerfStatsDescription] = None

   class InventoryDescription(DynamicData):
      numHosts: int
      numVirtualMachines: int
      numResourcePools: Optional[int] = None
      numClusters: Optional[int] = None
      numCpuDev: Optional[int] = None
      numNetDev: Optional[int] = None
      numDiskDev: Optional[int] = None
      numvCpuDev: Optional[int] = None
      numvNetDev: Optional[int] = None
      numvDiskDev: Optional[int] = None

   class PerfStatsDescription(DynamicData):
      intervals: list[HistoricalInterval] = []

   class DatabaseSizeEstimate(DynamicData):
      size: long

   def EstimateDatabaseSize(self, dbSizeParam: DatabaseSizeParam) -> DatabaseSizeEstimate: ...
