# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import KeyValue
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

class HttpNfcLease(ManagedObject):
   class State(Enum):
      initializing: ClassVar['State'] = 'initializing'
      ready: ClassVar['State'] = 'ready'
      done: ClassVar['State'] = 'done'
      error: ClassVar['State'] = 'error'

   class Mode(Enum):
      pushOrGet: ClassVar['Mode'] = 'pushOrGet'
      pull: ClassVar['Mode'] = 'pull'

   class DatastoreLeaseInfo(DynamicData):
      datastoreKey: str
      hosts: list[HostInfo] = []

   class HostInfo(DynamicData):
      url: str
      sslThumbprint: str

   class Info(DynamicData):
      lease: HttpNfcLease
      entity: ManagedEntity
      deviceUrl: list[DeviceUrl] = []
      totalDiskCapacityInKB: long
      leaseTimeout: int
      hostMap: list[DatastoreLeaseInfo] = []

   class DeviceUrl(DynamicData):
      key: str
      importKey: str
      url: str
      sslThumbprint: str
      disk: Optional[bool] = None
      targetId: Optional[str] = None
      datastoreKey: Optional[str] = None
      fileSize: Optional[long] = None

   class ManifestEntry(DynamicData):
      class ChecksumType(Enum):
         sha1: ClassVar['ChecksumType'] = 'sha1'
         sha256: ClassVar['ChecksumType'] = 'sha256'

      key: str
      sha1: str
      checksum: Optional[str] = None
      checksumType: Optional[str] = None
      size: long
      disk: bool
      capacity: Optional[long] = None
      populatedSize: Optional[long] = None

   class SourceFile(DynamicData):
      targetDeviceId: str
      url: str
      memberName: Optional[str] = None
      create: bool
      sslThumbprint: Optional[str] = None
      httpHeaders: list[KeyValue] = []
      size: Optional[long] = None

   class Capabilities(DynamicData):
      pullModeSupported: bool
      corsSupported: bool

   class ProbeResult(DynamicData):
      serverAccessible: bool

   @property
   def initializeProgress(self) -> int: ...
   @property
   def transferProgress(self) -> int: ...
   @property
   def mode(self) -> str: ...
   @property
   def capabilities(self) -> Capabilities: ...
   @property
   def info(self) -> Optional[Info]: ...
   @property
   def state(self) -> State: ...
   @property
   def error(self) -> Optional[MethodFault]: ...

   def GetManifest(self) -> list[ManifestEntry]: ...
   def SetManifestChecksumType(self, deviceUrlsToChecksumTypes: list[KeyValue]) -> NoReturn: ...
   def Complete(self) -> NoReturn: ...
   def Abort(self, fault: Optional[MethodFault]) -> NoReturn: ...
   def Progress(self, percent: int) -> NoReturn: ...
   def PullFromUrls(self, files: list[SourceFile]) -> Task: ...
   def ProbeUrls(self, files: list[SourceFile], timeout: Optional[int]) -> list[ProbeResult]: ...
