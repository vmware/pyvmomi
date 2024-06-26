# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class IpStackInfo(DynamicData):
   class EntryType(Enum):
      other: ClassVar['EntryType'] = 'other'
      invalid: ClassVar['EntryType'] = 'invalid'
      dynamic: ClassVar['EntryType'] = 'dynamic'
      manual: ClassVar['EntryType'] = 'manual'

   class Preference(Enum):
      reserved: ClassVar['Preference'] = 'reserved'
      low: ClassVar['Preference'] = 'low'
      medium: ClassVar['Preference'] = 'medium'
      high: ClassVar['Preference'] = 'high'

   class NetToMedia(DynamicData):
      ipAddress: str
      physicalAddress: str
      device: str
      type: str

   class DefaultRouter(DynamicData):
      ipAddress: str
      device: str
      lifetime: datetime
      preference: str

   neighbor: list[NetToMedia] = []
   defaultRouter: list[DefaultRouter] = []
