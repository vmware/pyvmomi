# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import HostSystem
from pyVmomi.vim import KeyValue
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import StorageResourceManager
from pyVmomi.vim import Task
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import DatastoreBrowser
from pyVmomi.vim.host import MountInfo

from pyVmomi.vim.storageDrs import StoragePlacementResult

class Datastore(ManagedEntity):
   class Accessible(Enum):
      # Reserved python keyword: commenting out.
      # True: ClassVar['Accessible'] = 'True'
      # Reserved python keyword: commenting out.
      # False: ClassVar['Accessible'] = 'False'
      pass

   class Summary(DynamicData):
      class MaintenanceModeState(Enum):
         normal: ClassVar['MaintenanceModeState'] = 'normal'
         enteringMaintenance: ClassVar['MaintenanceModeState'] = 'enteringMaintenance'
         inMaintenance: ClassVar['MaintenanceModeState'] = 'inMaintenance'

      datastore: Optional[Datastore] = None
      name: str
      url: str
      capacity: long
      freeSpace: long
      uncommitted: Optional[long] = None
      accessible: bool
      multipleHostAccess: Optional[bool] = None
      type: str
      maintenanceMode: Optional[str] = None

   class Info(DynamicData):
      name: str
      url: str
      freeSpace: long
      maxFileSize: long
      maxVirtualDiskCapacity: Optional[long] = None
      maxMemoryFileSize: long
      timestamp: Optional[datetime] = None
      containerId: Optional[str] = None
      aliasOf: Optional[str] = None

   class Capability(DynamicData):
      directoryHierarchySupported: bool
      rawDiskMappingsSupported: bool
      perFileThinProvisioningSupported: bool
      storageIORMSupported: bool
      nativeSnapshotSupported: bool
      topLevelDirectoryCreateSupported: Optional[bool] = None
      seSparseSupported: Optional[bool] = None
      vmfsSparseSupported: Optional[bool] = None
      vsanSparseSupported: Optional[bool] = None
      upitSupported: Optional[bool] = None
      vmdkExpandSupported: Optional[bool] = None
      clusteredVmdkSupported: Optional[bool] = None

   class HostMount(DynamicData):
      key: HostSystem
      mountInfo: MountInfo

   class MountPathDatastorePair(DynamicData):
      oldMountPath: str
      datastore: Datastore

   class VVolContainerFailoverPair(DynamicData):
      srcContainer: Optional[str] = None
      tgtContainer: str
      vvolMapping: list[KeyValue] = []

   @property
   def info(self) -> Info: ...
   @property
   def summary(self) -> Summary: ...
   @property
   def host(self) -> list[HostMount]: ...
   @property
   def vm(self) -> list[VirtualMachine]: ...
   @property
   def browser(self) -> DatastoreBrowser: ...
   @property
   def capability(self) -> Capability: ...
   @property
   def iormConfiguration(self) -> Optional[StorageResourceManager.IORMConfigInfo]: ...

   def Refresh(self) -> NoReturn: ...
   def RefreshStorageInfo(self) -> NoReturn: ...
   def UpdateVirtualMachineFiles(self, mountPathDatastoreMapping: list[MountPathDatastorePair]) -> Task: ...
   def RenameDatastore(self, newName: str) -> NoReturn: ...
   def DestroyDatastore(self) -> NoReturn: ...
   def EnterMaintenanceMode(self) -> StoragePlacementResult: ...
   def ExitMaintenanceMode(self) -> Task: ...
   def IsClusteredVmdkEnabled(self) -> bool: ...
   def UpdateVVolVirtualMachineFiles(self, failoverPair: list[VVolContainerFailoverPair]) -> Task: ...
