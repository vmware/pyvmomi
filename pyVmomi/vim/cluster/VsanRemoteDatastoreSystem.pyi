# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ClusterComputeResource
from pyVmomi.vim import Datastore
from pyVmomi.vim import Task

from pyVmomi.vim.vsan import DatastoreSourcePrecheckResult
from pyVmomi.vim.vsan import HciMeshDatastoreSource
from pyVmomi.vim.vsan import MountPrecheckResult
from pyVmomi.vim.vsan import RemoteVcInfo
from pyVmomi.vim.vsan import VcRemoteVsanServerClusterInfo
from pyVmomi.vim.vsan import XVCDatastoreInfo
from pyVmomi.vim.vsan import XvcQueryResultSet
from pyVmomi.vim.vsan import XvcQuerySpec

class VsanRemoteDatastoreSystem(ManagedObject):
   def MountPrecheck(self, cluster: ClusterComputeResource, datastore: Datastore, serverClusterInfo: Optional[VcRemoteVsanServerClusterInfo]) -> MountPrecheckResult: ...
   def RemoteVcMountPrecheck(self, cluster: ClusterComputeResource, xvcDatastore: XVCDatastoreInfo) -> MountPrecheckResult: ...
   def QueryDatastoreSource(self, vcHosts: list[str]) -> list[HciMeshDatastoreSource]: ...
   def PrecheckDatastoreSource(self, datastoreSource: HciMeshDatastoreSource, operation: Optional[str]) -> DatastoreSourcePrecheckResult: ...
   def CreateDatastoreSource(self, datastoreSource: HciMeshDatastoreSource) -> Task: ...
   def UpdateDatastoreSource(self, datastoreSource: HciMeshDatastoreSource) -> Task: ...
   def DestroyDatastoreSource(self, datastoreSource: HciMeshDatastoreSource) -> Task: ...
   def QueryHciMeshDatastores(self, querySpecs: list[XvcQuerySpec], extraVcInfos: list[RemoteVcInfo]) -> list[XvcQueryResultSet]: ...
