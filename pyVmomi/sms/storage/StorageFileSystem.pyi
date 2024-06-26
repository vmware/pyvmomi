# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.sms.storage import BackingConfig
from pyVmomi.sms.storage import FileSystemInfo

class StorageFileSystem(DynamicData):
   class FileSystemInterfaceVersion(Enum):
      NFSV3_0: ClassVar['FileSystemInterfaceVersion'] = 'NFSV3_0'

   uuid: str
   info: list[FileSystemInfo] = []
   nativeSnapshotSupported: bool
   thinProvisioningStatus: str
   type: str
   version: str
   backingConfig: Optional[BackingConfig] = None
