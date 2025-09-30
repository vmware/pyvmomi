# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ClusterComputeResource import ClusterComputeResource

from pyVmomi.vim.EVCMode import EVCMode

from pyVmomi.vim.ExtensibleManagedObject import ExtensibleManagedObject

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.Task import Task

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.host.ConnectSpec import ConnectSpec

from pyVmomi.vim.host.CpuIdInfo import CpuIdInfo

from pyVmomi.vim.host.FeatureCapability import FeatureCapability

from pyVmomi.vim.host.FeatureMask import FeatureMask

from pyVmomi.vim.vm.FeatureRequirement import FeatureRequirement

class EVCManager(ExtensibleManagedObject):
   class EVCState(DynamicData):
      supportedEVCMode: list[EVCMode] = []
      currentEVCModeKey: Optional[str] = None
      guaranteedCPUFeatures: list[CpuIdInfo] = []
      featureCapability: list[FeatureCapability] = []
      featureMask: list[FeatureMask] = []
      featureRequirement: list[FeatureRequirement] = []

   class CheckResult(DynamicData):
      evcModeKey: str
      error: MethodFault
      host: list[HostSystem] = []

   @property
   def managedCluster(self) -> ClusterComputeResource: ...
   @property
   def evcState(self) -> EVCState: ...

   def ConfigureEvc(self, evcModeKey: str, evcGraphicsModeKey: Optional[str]) -> Task: ...
   def DisableEvc(self) -> Task: ...
   def CheckConfigureEvc(self, evcModeKey: str, evcGraphicsModeKey: Optional[str]) -> Task: ...
   def CheckAddHostEvc(self, cnxSpec: ConnectSpec) -> Task: ...
