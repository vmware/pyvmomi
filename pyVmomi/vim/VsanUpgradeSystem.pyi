# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ClusterComputeResource
from pyVmomi.vim import HostSystem
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan.host import DiskMapping

class VsanUpgradeSystem(ManagedObject):
   class PreflightCheckIssue(DynamicData):
      msg: str

   class HostsDisconnectedIssue(PreflightCheckIssue):
      hosts: list[HostSystem] = []

   class MissingHostsInClusterIssue(PreflightCheckIssue):
      hosts: list[HostSystem] = []

   class RogueHostsInClusterIssue(PreflightCheckIssue):
      uuids: list[str] = []

   class WrongEsxVersionIssue(PreflightCheckIssue):
      hosts: list[HostSystem] = []

   class AutoClaimEnabledOnHostsIssue(PreflightCheckIssue):
      hosts: list[HostSystem] = []

   class APIBrokenIssue(PreflightCheckIssue):
      hosts: list[HostSystem] = []

   class V2ObjectsPresentDuringDowngradeIssue(PreflightCheckIssue):
      uuids: list[str] = []

   class NotEnoughFreeCapacityIssue(PreflightCheckIssue):
      reducedRedundancyUpgradePossible: bool

   class NetworkPartitionInfo(DynamicData):
      hosts: list[HostSystem] = []

   class NetworkPartitionIssue(PreflightCheckIssue):
      partitions: list[NetworkPartitionInfo] = []

   class PreflightCheckResult(DynamicData):
      issues: list[PreflightCheckIssue] = []
      diskMappingToRestore: Optional[DiskMapping] = None

   class UpgradeHistoryItem(DynamicData):
      timestamp: datetime
      host: Optional[HostSystem] = None
      message: str
      task: Optional[Task] = None

   class UpgradeHistoryDiskGroupOpType(Enum):
      add: ClassVar['UpgradeHistoryDiskGroupOpType'] = 'add'
      remove: ClassVar['UpgradeHistoryDiskGroupOpType'] = 'remove'

   class UpgradeHistoryDiskGroupOp(UpgradeHistoryItem):
      operation: str
      diskMapping: DiskMapping

   class UpgradeHistoryPreflightFail(UpgradeHistoryItem):
      preflightResult: PreflightCheckResult

   class UpgradeStatus(DynamicData):
      inProgress: bool
      history: list[UpgradeHistoryItem] = []
      aborted: Optional[bool] = None
      completed: Optional[bool] = None
      progress: Optional[int] = None

   def PerformUpgradePreflightCheck(self, cluster: ClusterComputeResource, downgradeFormat: Optional[bool]) -> PreflightCheckResult: ...
   def QueryUpgradeStatus(self, cluster: ClusterComputeResource) -> UpgradeStatus: ...
   def PerformUpgrade(self, cluster: ClusterComputeResource, performObjectUpgrade: Optional[bool], downgradeFormat: Optional[bool], allowReducedRedundancy: Optional[bool], excludeHosts: list[HostSystem]) -> Task: ...
