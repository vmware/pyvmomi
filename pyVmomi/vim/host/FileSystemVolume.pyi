# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class FileSystemVolume(DynamicData):
   class FileSystemType(Enum):
      VMFS: ClassVar['FileSystemType'] = 'VMFS'
      NFS: ClassVar['FileSystemType'] = 'NFS'
      NFS41: ClassVar['FileSystemType'] = 'NFS41'
      CIFS: ClassVar['FileSystemType'] = 'CIFS'
      vsan: ClassVar['FileSystemType'] = 'vsan'
      VFFS: ClassVar['FileSystemType'] = 'VFFS'
      VVOL: ClassVar['FileSystemType'] = 'VVOL'
      PMEM: ClassVar['FileSystemType'] = 'PMEM'
      vsanD: ClassVar['FileSystemType'] = 'vsanD'
      OTHER: ClassVar['FileSystemType'] = 'OTHER'

   type: str
   name: str
   capacity: long
