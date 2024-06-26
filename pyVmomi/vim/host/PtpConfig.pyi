# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import IpConfig

class PtpConfig(DynamicData):
   class DeviceType(Enum):
      none: ClassVar['DeviceType'] = 'none'
      virtualNic: ClassVar['DeviceType'] = 'virtualNic'
      pciPassthruNic: ClassVar['DeviceType'] = 'pciPassthruNic'

   class PtpPort(DynamicData):
      index: int
      deviceType: Optional[str] = None
      device: Optional[str] = None
      ipConfig: Optional[IpConfig] = None

   domain: Optional[int] = None
   port: list[PtpPort] = []
