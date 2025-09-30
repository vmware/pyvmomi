# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.Task import Task

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.host.NasVolume import NasVolume

from pyVmomi.vim.host.ScsiDisk import ScsiDisk

from pyVmomi.vim.host.UnresolvedVmfsResignatureSpec import UnresolvedVmfsResignatureSpec

from pyVmomi.vim.host.UnresolvedVmfsVolume import UnresolvedVmfsVolume

from pyVmomi.vim.host.VmfsDatastoreCreateSpec import VmfsDatastoreCreateSpec

from pyVmomi.vim.host.VmfsDatastoreExpandSpec import VmfsDatastoreExpandSpec

from pyVmomi.vim.host.VmfsDatastoreExtendSpec import VmfsDatastoreExtendSpec

from pyVmomi.vim.host.VmfsDatastoreOption import VmfsDatastoreOption

class DatastoreSystem(ManagedObject):
   class Capabilities(DynamicData):
      nfsMountCreationRequired: bool
      nfsMountCreationSupported: bool
      localDatastoreSupported: bool
      vmfsExtentExpansionSupported: bool

   class VvolDatastoreSpec(DynamicData):
      name: str
      scId: str

   class DatastoreResult(DynamicData):
      key: Datastore
      fault: Optional[MethodFault] = None

   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def capabilities(self) -> Capabilities: ...

   def UpdateLocalSwapDatastore(self, datastore: Optional[Datastore]) -> None: ...
   def QueryAvailableDisksForVmfs(self, datastore: Optional[Datastore]) -> list[ScsiDisk]: ...
   def QueryVmfsDatastoreCreateOptions(self, devicePath: str, vmfsMajorVersion: Optional[int]) -> list[VmfsDatastoreOption]: ...
   def CreateVmfsDatastore(self, spec: VmfsDatastoreCreateSpec) -> Datastore: ...
   def QueryVmfsDatastoreExtendOptions(self, datastore: Datastore, devicePath: str, suppressExpandCandidates: Optional[bool]) -> list[VmfsDatastoreOption]: ...
   def QueryVmfsDatastoreExpandOptions(self, datastore: Datastore) -> list[VmfsDatastoreOption]: ...
   def ExtendVmfsDatastore(self, datastore: Datastore, spec: VmfsDatastoreExtendSpec) -> Datastore: ...
   def EnableClusteredVmdkSupport(self, datastore: Datastore) -> None: ...
   def DisableClusteredVmdkSupport(self, datastore: Datastore) -> None: ...
   def ExpandVmfsDatastore(self, datastore: Datastore, spec: VmfsDatastoreExpandSpec) -> Datastore: ...
   def CreateNasDatastore(self, spec: NasVolume.Specification) -> Datastore: ...
   def CreateLocalDatastore(self, name: str, path: str) -> Datastore: ...
   def CreateVvolDatastore(self, spec: VvolDatastoreSpec) -> Datastore: ...
   def RemoveDatastore(self, datastore: Datastore) -> None: ...
   def SetMaxQueueDepth(self, datastore: Datastore, maxQdepth: long) -> None: ...
   def QueryMaxQueueDepth(self, datastore: Datastore) -> long: ...
   def RemoveDatastoreEx(self, datastore: list[Datastore]) -> Task: ...
   def ConfigureDatastorePrincipal(self, userName: str, password: Optional[str]) -> None: ...
   def QueryUnresolvedVmfsVolumes(self) -> list[UnresolvedVmfsVolume]: ...
   def ResignatureUnresolvedVmfsVolume(self, resolutionSpec: UnresolvedVmfsResignatureSpec) -> Task: ...
