# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.Task import Task

from pyVmomi.vim.cns.QueryFilter import QueryFilter

from pyVmomi.vim.cns.QueryResult import QueryResult

from pyVmomi.vim.cns.QuerySelection import QuerySelection

from pyVmomi.vim.cns.SnapshotCreateSpec import SnapshotCreateSpec

from pyVmomi.vim.cns.SnapshotDeleteSpec import SnapshotDeleteSpec

from pyVmomi.vim.cns.VolumeACLConfigureSpec import VolumeACLConfigureSpec

from pyVmomi.vim.cns.VolumeAttachDetachSpec import VolumeAttachDetachSpec

from pyVmomi.vim.cns.VolumeCreateSpec import VolumeCreateSpec

from pyVmomi.vim.cns.VolumeExtendSpec import VolumeExtendSpec

from pyVmomi.vim.cns.VolumeId import VolumeId

from pyVmomi.vim.cns.VolumeMetadataUpdateSpec import VolumeMetadataUpdateSpec

from pyVmomi.vim.cns.VolumePolicyReconfigSpec import VolumePolicyReconfigSpec

from pyVmomi.vim.cns.VolumeRelocateSpec import VolumeRelocateSpec

class VolumeManager(ManagedObject):
   def Create(self, createSpecs: list[VolumeCreateSpec]) -> Task: ...
   def UpdateVolumeMetadata(self, updateSpecs: list[VolumeMetadataUpdateSpec]) -> Task: ...
   def Delete(self, volumeIds: list[VolumeId], deleteDisk: bool) -> Task: ...
   def Attach(self, attachSpecs: list[VolumeAttachDetachSpec]) -> Task: ...
   def Detach(self, detachSpecs: list[VolumeAttachDetachSpec]) -> Task: ...
   def QueryAsync(self, filter: QueryFilter, selection: Optional[QuerySelection]) -> Task: ...
   def Query(self, filter: QueryFilter, selection: Optional[QuerySelection]) -> QueryResult: ...
   def ConfigureVolumeACLs(self, ACLConfigSpecs: list[VolumeACLConfigureSpec]) -> Task: ...
   def Extend(self, extendSpecs: list[VolumeExtendSpec]) -> Task: ...
   def CreateSnapshots(self, snapshotSpecs: list[SnapshotCreateSpec]) -> Task: ...
   def DeleteSnapshots(self, snapshotDeleteSpecs: list[SnapshotDeleteSpec]) -> Task: ...
   def Relocate(self, relocateSpecs: list[VolumeRelocateSpec]) -> Task: ...
   def ReconfigPolicy(self, volumePolicyReconfigSpecs: list[VolumePolicyReconfigSpec]) -> Task: ...
