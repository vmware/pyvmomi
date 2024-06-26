# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Datastore
from pyVmomi.vim import KeyValue

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.encryption import CryptoKeyId

from pyVmomi.vim.vslm import ID
from pyVmomi.vim.vslm import VClockInfo

class BaseConfigInfo(DynamicData):
   class BackingInfo(DynamicData):
      datastore: Datastore

   class FileBackingInfo(BackingInfo):
      filePath: str
      backingObjectId: Optional[str] = None
      parent: Optional[FileBackingInfo] = None
      deltaSizeInMB: Optional[long] = None
      keyId: Optional[CryptoKeyId] = None

   class DiskFileBackingInfo(FileBackingInfo):
      class ProvisioningType(Enum):
         thin: ClassVar['ProvisioningType'] = 'thin'
         eagerZeroedThick: ClassVar['ProvisioningType'] = 'eagerZeroedThick'
         lazyZeroedThick: ClassVar['ProvisioningType'] = 'lazyZeroedThick'

      provisioningType: str

   class RawDiskMappingBackingInfo(FileBackingInfo):
      lunUuid: str
      compatibilityMode: str

   id: ID
   name: str
   createTime: datetime
   keepAfterDeleteVm: Optional[bool] = None
   relocationDisabled: Optional[bool] = None
   nativeSnapshotSupported: Optional[bool] = None
   changedBlockTrackingEnabled: Optional[bool] = None
   backing: BackingInfo
   metadata: list[KeyValue] = []
   vclock: Optional[VClockInfo] = None
   iofilter: list[str] = []
