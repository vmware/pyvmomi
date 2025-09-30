# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim.ClusterComputeResource import ClusterComputeResource

from pyVmomi.vim.ComputeResource import ComputeResource

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.Task import Task

from pyVmomi.vim.cluster.VsanDiagnosticsThreshold import VsanDiagnosticsThreshold

from pyVmomi.vim.cluster.VsanNetworkDiagnostics import VsanNetworkDiagnostics

from pyVmomi.vim.vm.ProfileSpec import ProfileSpec

from pyVmomi.vim.vsan.IODiagnosticsInstance import IODiagnosticsInstance

from pyVmomi.vim.vsan.IODiagnosticsInstanceQuerySpec import IODiagnosticsInstanceQuerySpec

from pyVmomi.vim.vsan.IODiagnosticsTarget import IODiagnosticsTarget

from pyVmomi.vim.vsan.IODiagnosticsTargetStats import IODiagnosticsTargetStats

from pyVmomi.vim.vsan.VsanIOTripAnalyzerConfig import VsanIOTripAnalyzerConfig

from pyVmomi.vim.vsan.VsanIOTripAnalyzerRecurrence import VsanIOTripAnalyzerRecurrence

class VsanDiagnosticsSystem(ManagedObject):
   def QueryNetworkDiagnostics(self, cluster: ComputeResource, host: Optional[HostSystem]) -> list[VsanNetworkDiagnostics]: ...
   def GetThresholds(self, cluster: ComputeResource, entityType: Optional[str], metric: Optional[str]) -> list[VsanDiagnosticsThreshold]: ...
   def SetThresholds(self, cluster: ComputeResource, thresholds: list[VsanDiagnosticsThreshold]) -> None: ...
   def StartIODiagnosticsTask(self, targets: list[IODiagnosticsTarget], cluster: Optional[ClusterComputeResource], duration: Optional[long]) -> Task: ...
   def QueryIODiagnosticsInstances(self, querySpec: IODiagnosticsInstanceQuerySpec, cluster: Optional[ClusterComputeResource]) -> list[IODiagnosticsInstance]: ...
   def QueryIODiagnosticsStats(self, instanceName: str, cluster: Optional[ClusterComputeResource]) -> list[IODiagnosticsTargetStats]: ...
   def CreateIOTripAnalyzerRecurrences(self, cluster: ComputeResource, recurrences: list[VsanIOTripAnalyzerRecurrence]) -> list[VsanIOTripAnalyzerRecurrence]: ...
   def GetIOTripAnalyzerSchedulerConfig(self, cluster: ComputeResource) -> Optional[VsanIOTripAnalyzerConfig]: ...
   def EditIOTripAnalyzerRecurrences(self, cluster: ComputeResource, recurrences: list[VsanIOTripAnalyzerRecurrence]) -> list[VsanIOTripAnalyzerRecurrence]: ...
   def RemoveIOTripAnalyzerRecurrences(self, cluster: ComputeResource, names: list[str]) -> None: ...
   def SetTraceObjectPolicy(self, cluster: Optional[ComputeResource], traceObjectUuid: str, profile: Optional[ProfileSpec]) -> bool: ...
