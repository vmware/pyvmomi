# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vim.vm import TargetInfo
from pyVmomi.vim.vm import VMotionStunTimeInfo

class VgpuProfileInfo(TargetInfo):
   class ProfileSharing(Enum):
      timeSliced: ClassVar['ProfileSharing'] = 'timeSliced'
      mig: ClassVar['ProfileSharing'] = 'mig'

   class ProfileClass(Enum):
      compute: ClassVar['ProfileClass'] = 'compute'
      quadro: ClassVar['ProfileClass'] = 'quadro'

   profileName: str
   deviceVendorId: long
   fbSizeInGib: long
   profileSharing: str
   profileClass: str
   stunTimeEstimates: list[VMotionStunTimeInfo] = []
