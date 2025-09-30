# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.KeyValue import KeyValue

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.StorageResourceManager import StorageResourceManager

from pyVmomi.vim.Task import Task

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.DatastoreBrowser import DatastoreBrowser

from pyVmomi.vim.host.MountInfo import MountInfo

from pyVmomi.vim.storageDrs.StoragePlacementResult import StoragePlacementResult

class Datastore(ManagedEntity):
   class Accessible(Enum):
      # Reserved python keyword: commenting out.
      # True: ClassVar['Accessible'] = 'True'
      # Reserved python keyword: commenting out.
      # False: ClassVar['Accessible'] = 'False'
      pass

   class SectorFormat(Enum):
      native_512: ClassVar['SectorFormat'] = 'native_512'
      emulated_512: ClassVar['SectorFormat'] = 'emulated_512'
      native_4k: ClassVar['SectorFormat'] = 'native_4k'

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
      supportedVDiskFormats: list[str] = []
      logicalSectorSize: Optional[int] = None
      physicalSectorSize: Optional[int] = None

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

   def Refresh(self) -> None: ...
   def RefreshStorageInfo(self) -> None: ...
   def UpdateVirtualMachineFiles(self, mountPathDatastoreMapping: list[MountPathDatastorePair]) -> Task: ...
   def RenameDatastore(self, newName: str) -> None: ...
   def DestroyDatastore(self) -> None: ...
   def EnterMaintenanceMode(self) -> StoragePlacementResult: ...
   def ExitMaintenanceMode(self) -> Task: ...
   def IsClusteredVmdkEnabled(self) -> bool: ...
   def UpdateVVolVirtualMachineFiles(self, failoverPair: list[VVolContainerFailoverPair]) -> Task: ...
