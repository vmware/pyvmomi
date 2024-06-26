# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class BIOSInfo(DynamicData):
   class FirmwareType(Enum):
      BIOS: ClassVar['FirmwareType'] = 'BIOS'
      UEFI: ClassVar['FirmwareType'] = 'UEFI'

   biosVersion: Optional[str] = None
   releaseDate: Optional[datetime] = None
   vendor: Optional[str] = None
   majorRelease: Optional[int] = None
   minorRelease: Optional[int] = None
   firmwareMajorRelease: Optional[int] = None
   firmwareMinorRelease: Optional[int] = None
   firmwareType: Optional[str] = None
