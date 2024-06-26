# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import ClusterComputeResource
from pyVmomi.vim import EVCMode
from pyVmomi.vim import ExtensibleManagedObject
from pyVmomi.vim import HostSystem
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.host import ConnectSpec
from pyVmomi.vim.host import CpuIdInfo
from pyVmomi.vim.host import FeatureCapability
from pyVmomi.vim.host import FeatureMask

from pyVmomi.vim.vm import FeatureRequirement

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
