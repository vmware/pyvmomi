# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import ClusterComputeResource
from pyVmomi.vim import ComputeResource
from pyVmomi.vim import HostSystem
from pyVmomi.vim import Task

from pyVmomi.vim.cluster import VsanDiagnosticsThreshold
from pyVmomi.vim.cluster import VsanNetworkDiagnostics

from pyVmomi.vim.vm import ProfileSpec

from pyVmomi.vim.vsan import IODiagnosticsInstance
from pyVmomi.vim.vsan import IODiagnosticsInstanceQuerySpec
from pyVmomi.vim.vsan import IODiagnosticsTarget
from pyVmomi.vim.vsan import IODiagnosticsTargetStats
from pyVmomi.vim.vsan import VsanIOTripAnalyzerConfig
from pyVmomi.vim.vsan import VsanIOTripAnalyzerRecurrence

class VsanDiagnosticsSystem(ManagedObject):
   def QueryNetworkDiagnostics(self, cluster: ComputeResource, host: Optional[HostSystem]) -> list[VsanNetworkDiagnostics]: ...
   def GetThresholds(self, cluster: ComputeResource, entityType: Optional[str], metric: Optional[str]) -> list[VsanDiagnosticsThreshold]: ...
   def SetThresholds(self, cluster: ComputeResource, thresholds: list[VsanDiagnosticsThreshold]) -> NoReturn: ...
   def StartIODiagnosticsTask(self, targets: list[IODiagnosticsTarget], cluster: Optional[ClusterComputeResource], duration: Optional[long]) -> Task: ...
   def QueryIODiagnosticsInstances(self, querySpec: IODiagnosticsInstanceQuerySpec, cluster: Optional[ClusterComputeResource]) -> list[IODiagnosticsInstance]: ...
   def QueryIODiagnosticsStats(self, instanceName: str, cluster: Optional[ClusterComputeResource]) -> list[IODiagnosticsTargetStats]: ...
   def CreateIOTripAnalyzerRecurrences(self, cluster: ComputeResource, recurrences: list[VsanIOTripAnalyzerRecurrence]) -> list[VsanIOTripAnalyzerRecurrence]: ...
   def GetIOTripAnalyzerSchedulerConfig(self, cluster: ComputeResource) -> Optional[VsanIOTripAnalyzerConfig]: ...
   def EditIOTripAnalyzerRecurrences(self, cluster: ComputeResource, recurrences: list[VsanIOTripAnalyzerRecurrence]) -> list[VsanIOTripAnalyzerRecurrence]: ...
   def RemoveIOTripAnalyzerRecurrences(self, cluster: ComputeResource, names: list[str]) -> NoReturn: ...
   def SetTraceObjectPolicy(self, cluster: Optional[ComputeResource], traceObjectUuid: str, profile: Optional[ProfileSpec]) -> bool: ...
