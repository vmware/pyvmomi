# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import FileSystemVolume
from pyVmomi.vim.host import MountInfo

class FileSystemMountInfo(DynamicData):
   class VStorageSupportStatus(Enum):
      vStorageSupported: ClassVar['VStorageSupportStatus'] = 'vStorageSupported'
      vStorageUnsupported: ClassVar['VStorageSupportStatus'] = 'vStorageUnsupported'
      vStorageUnknown: ClassVar['VStorageSupportStatus'] = 'vStorageUnknown'

   mountInfo: MountInfo
   volume: FileSystemVolume
   vStorageSupport: Optional[str] = None
