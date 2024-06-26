# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class StorageContainer(DynamicData):
   class VvolContainerTypeEnum(Enum):
      NFS: ClassVar['VvolContainerTypeEnum'] = 'NFS'
      NFS4x: ClassVar['VvolContainerTypeEnum'] = 'NFS4x'
      SCSI: ClassVar['VvolContainerTypeEnum'] = 'SCSI'
      NVMe: ClassVar['VvolContainerTypeEnum'] = 'NVMe'

   uuid: str
   name: str
   maxVvolSizeInMB: long
   providerId: list[str] = []
   arrayId: list[str] = []
   vvolContainerType: Optional[str] = None
   stretched: Optional[bool] = None
