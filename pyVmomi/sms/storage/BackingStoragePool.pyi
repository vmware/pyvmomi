# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class BackingStoragePool(DynamicData):
   class BackingStoragePoolType(Enum):
      thinProvisioningPool: ClassVar['BackingStoragePoolType'] = 'thinProvisioningPool'
      deduplicationPool: ClassVar['BackingStoragePoolType'] = 'deduplicationPool'
      thinAndDeduplicationCombinedPool: ClassVar['BackingStoragePoolType'] = 'thinAndDeduplicationCombinedPool'

   uuid: str
   type: str
   capacityInMB: long
   usedSpaceInMB: long
