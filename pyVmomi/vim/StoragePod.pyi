# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Folder
from pyVmomi.vim import StorageResourceManager

from pyVmomi.vmodl import DynamicData

class StoragePod(Folder):
   class Summary(DynamicData):
      name: str
      capacity: long
      freeSpace: long

   @property
   def summary(self) -> Optional[Summary]: ...
   @property
   def podStorageDrsEntry(self) -> Optional[StorageResourceManager.PodStorageDrsEntry]: ...
