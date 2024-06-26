# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import ClusterComputeResource
from pyVmomi.vim import HostSystem
from pyVmomi.vim import Task
from pyVmomi.vim import VirtualMachine

from pyVmomi.vim.cluster import VsanIoInsightInstance
from pyVmomi.vim.cluster import VsanIoInsightInstanceQuerySpec

from pyVmomi.vim.host import VsanHostIoInsightInfo

class VsanIoInsightManager(ManagedObject):
   def StartIoInsight(self, cluster: Optional[ClusterComputeResource], runName: Optional[str], durationSec: Optional[long], targetHosts: list[HostSystem], targetVMs: list[VirtualMachine]) -> Task: ...
   def StopIoInsight(self, cluster: Optional[ClusterComputeResource], runName: Optional[str], hostsIoInsightInfos: list[VsanHostIoInsightInfo]) -> Task: ...
   def QueryIoInsightInstances(self, querySpec: VsanIoInsightInstanceQuerySpec, cluster: Optional[ClusterComputeResource]) -> list[VsanIoInsightInstance]: ...
   def DeleteIoInsightInstance(self, runName: str, cluster: Optional[ClusterComputeResource]) -> NoReturn: ...
   def RenameIoInsightInstance(self, oldRunName: str, newRunName: str, cluster: Optional[ClusterComputeResource]) -> NoReturn: ...
