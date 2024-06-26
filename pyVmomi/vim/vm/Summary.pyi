# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import CustomFieldsManager
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.ext import ManagedByInfo

from pyVmomi.vim.vApp import ProductInfo

from pyVmomi.vim.vm import FaultToleranceConfigInfo
from pyVmomi.vim.vm import GuestInfo
from pyVmomi.vim.vm import RuntimeInfo

class Summary(DynamicData):
   class ConfigSummary(DynamicData):
      name: str
      template: bool
      vmPathName: str
      memorySizeMB: Optional[int] = None
      cpuReservation: Optional[int] = None
      memoryReservation: Optional[int] = None
      numCpu: Optional[int] = None
      numEthernetCards: Optional[int] = None
      numVirtualDisks: Optional[int] = None
      uuid: Optional[str] = None
      instanceUuid: Optional[str] = None
      guestId: Optional[str] = None
      guestFullName: Optional[str] = None
      annotation: Optional[str] = None
      product: Optional[ProductInfo] = None
      installBootRequired: Optional[bool] = None
      ftInfo: Optional[FaultToleranceConfigInfo] = None
      managedBy: Optional[ManagedByInfo] = None
      tpmPresent: Optional[bool] = None
      numVmiopBackings: Optional[int] = None
      hwVersion: Optional[str] = None

   class QuickStats(DynamicData):
      class MemoryTierStats(DynamicData):
         memoryTierType: str
         readBandwidth: long

      overallCpuUsage: Optional[int] = None
      overallCpuDemand: Optional[int] = None
      overallCpuReadiness: Optional[int] = None
      guestMemoryUsage: Optional[int] = None
      hostMemoryUsage: Optional[int] = None
      guestHeartbeatStatus: ManagedEntity.Status
      distributedCpuEntitlement: Optional[int] = None
      distributedMemoryEntitlement: Optional[int] = None
      staticCpuEntitlement: Optional[int] = None
      staticMemoryEntitlement: Optional[int] = None
      grantedMemory: Optional[int] = None
      privateMemory: Optional[int] = None
      sharedMemory: Optional[int] = None
      swappedMemory: Optional[int] = None
      balloonedMemory: Optional[int] = None
      consumedOverheadMemory: Optional[int] = None
      ftLogBandwidth: Optional[int] = None
      ftSecondaryLatency: Optional[int] = None
      ftLatencyStatus: Optional[ManagedEntity.Status] = None
      compressedMemory: Optional[long] = None
      uptimeSeconds: Optional[int] = None
      ssdSwappedMemory: Optional[long] = None
      activeMemory: Optional[int] = None
      memoryTierStats: list[MemoryTierStats] = []

   class GuestSummary(DynamicData):
      guestId: Optional[str] = None
      guestFullName: Optional[str] = None
      toolsStatus: Optional[GuestInfo.ToolsStatus] = None
      toolsVersionStatus: Optional[str] = None
      toolsVersionStatus2: Optional[str] = None
      toolsRunningStatus: Optional[str] = None
      hostName: Optional[str] = None
      ipAddress: Optional[str] = None
      hwVersion: Optional[str] = None

   class StorageSummary(DynamicData):
      committed: long
      uncommitted: long
      unshared: long
      timestamp: datetime

   vm: Optional[VirtualMachine] = None
   runtime: RuntimeInfo
   guest: Optional[GuestSummary] = None
   config: ConfigSummary
   storage: Optional[StorageSummary] = None
   quickStats: QuickStats
   overallStatus: ManagedEntity.Status
   customValue: list[CustomFieldsManager.Value] = []
