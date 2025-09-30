# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.ClusterComputeResource import ClusterComputeResource

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.Task import Task

from pyVmomi.vim.vsan.DatastoreSourcePrecheckResult import DatastoreSourcePrecheckResult

from pyVmomi.vim.vsan.HciMeshDatastoreSource import HciMeshDatastoreSource

from pyVmomi.vim.vsan.MountPrecheckResult import MountPrecheckResult

from pyVmomi.vim.vsan.RemoteVcInfo import RemoteVcInfo

from pyVmomi.vim.vsan.VcRemoteVsanServerClusterInfo import VcRemoteVsanServerClusterInfo

from pyVmomi.vim.vsan.XVCDatastoreInfo import XVCDatastoreInfo

from pyVmomi.vim.vsan.XvcQueryResultSet import XvcQueryResultSet

from pyVmomi.vim.vsan.XvcQuerySpec import XvcQuerySpec

class VsanRemoteDatastoreSystem(ManagedObject):
   def MountPrecheck(self, cluster: ClusterComputeResource, datastore: Datastore, serverClusterInfo: Optional[VcRemoteVsanServerClusterInfo]) -> MountPrecheckResult: ...
   def RemoteVcMountPrecheck(self, cluster: ClusterComputeResource, xvcDatastore: XVCDatastoreInfo) -> MountPrecheckResult: ...
   def QueryDatastoreSource(self, vcHosts: list[str]) -> list[HciMeshDatastoreSource]: ...
   def PrecheckDatastoreSource(self, datastoreSource: HciMeshDatastoreSource, operation: Optional[str]) -> DatastoreSourcePrecheckResult: ...
   def CreateDatastoreSource(self, datastoreSource: HciMeshDatastoreSource) -> Task: ...
   def UpdateDatastoreSource(self, datastoreSource: HciMeshDatastoreSource) -> Task: ...
   def DestroyDatastoreSource(self, datastoreSource: HciMeshDatastoreSource) -> Task: ...
   def QueryHciMeshDatastores(self, querySpecs: list[XvcQuerySpec], extraVcInfos: list[RemoteVcInfo]) -> list[XvcQueryResultSet]: ...
