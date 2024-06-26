# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Datastore
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.encryption import CryptoKeyId

class DatastoreBrowser(ManagedObject):
   class FileInfo(DynamicData):
      class Details(DynamicData):
         fileType: bool
         fileSize: bool
         modification: bool
         fileOwner: bool

      path: str
      friendlyName: Optional[str] = None
      fileSize: Optional[long] = None
      modification: Optional[datetime] = None
      owner: Optional[str] = None

   class Query(DynamicData):
      pass

   class VmConfigQuery(Query):
      class Filter(DynamicData):
         matchConfigVersion: list[int] = []
         encrypted: Optional[bool] = None

      class Details(DynamicData):
         configVersion: bool
         encryption: Optional[bool] = None

      filter: Optional[Filter] = None
      details: Optional[Details] = None

   class TemplateVmConfigQuery(VmConfigQuery):
      pass

   class VmDiskQuery(Query):
      class Filter(DynamicData):
         diskType: list[type] = []
         matchHardwareVersion: list[int] = []
         controllerType: list[type] = []
         thin: Optional[bool] = None
         encrypted: Optional[bool] = None

      class Details(DynamicData):
         diskType: bool
         capacityKb: bool
         hardwareVersion: bool
         controllerType: Optional[bool] = None
         diskExtents: Optional[bool] = None
         thin: Optional[bool] = None
         encryption: Optional[bool] = None

      filter: Optional[Filter] = None
      details: Optional[Details] = None

   class FolderQuery(Query):
      pass

   class VmSnapshotQuery(Query):
      pass

   class IsoImageQuery(Query):
      pass

   class FloppyImageQuery(Query):
      pass

   class VmNvramQuery(Query):
      pass

   class VmLogQuery(Query):
      pass

   class VmConfigInfo(FileInfo):
      class VmConfigEncryptionInfo(DynamicData):
         keyId: Optional[CryptoKeyId] = None

      configVersion: Optional[int] = None
      encryption: Optional[VmConfigEncryptionInfo] = None

   class TemplateVmConfigInfo(VmConfigInfo):
      pass

   class VmDiskInfo(FileInfo):
      class VmDiskEncryptionInfo(DynamicData):
         keyId: Optional[CryptoKeyId] = None

      diskType: Optional[type] = None
      capacityKb: Optional[long] = None
      hardwareVersion: Optional[int] = None
      controllerType: Optional[type] = None
      diskExtents: list[str] = []
      thin: Optional[bool] = None
      encryption: Optional[VmDiskEncryptionInfo] = None

   class FolderInfo(FileInfo):
      pass

   class VmSnapshotInfo(FileInfo):
      pass

   class IsoImageInfo(FileInfo):
      pass

   class FloppyImageInfo(FileInfo):
      pass

   class VmNvramInfo(FileInfo):
      pass

   class VmLogInfo(FileInfo):
      pass

   class SearchSpec(DynamicData):
      query: list[Query] = []
      details: Optional[FileInfo.Details] = None
      searchCaseInsensitive: Optional[bool] = None
      matchPattern: list[str] = []
      sortFoldersFirst: Optional[bool] = None

   class SearchResults(DynamicData):
      datastore: Optional[Datastore] = None
      folderPath: Optional[str] = None
      file: list[FileInfo] = []

   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def supportedType(self) -> list[Query]: ...

   def Search(self, datastorePath: str, searchSpec: Optional[SearchSpec]) -> Task: ...
   def SearchSubFolders(self, datastorePath: str, searchSpec: Optional[SearchSpec]) -> Task: ...
   def DeleteFile(self, datastorePath: str) -> NoReturn: ...
