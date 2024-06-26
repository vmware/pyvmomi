# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import ElementDescription

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import Fru

class HardwareStatusInfo(DynamicData):
   class Status(Enum):
      Unknown: ClassVar['Status'] = 'Unknown'
      Green: ClassVar['Status'] = 'Green'
      Yellow: ClassVar['Status'] = 'Yellow'
      Red: ClassVar['Status'] = 'Red'

   class HardwareElementInfo(DynamicData):
      name: str
      status: ElementDescription

   class StorageStatusInfo(HardwareElementInfo):
      class OperationalInfo(DynamicData):
         property: str
         value: str

      operationalInfo: list[OperationalInfo] = []

   class DpuStatusInfo(HardwareElementInfo):
      class OperationalInfo(DynamicData):
         sensorId: str
         healthState: Optional[ElementDescription] = None
         reading: str
         units: Optional[str] = None
         timeStamp: Optional[datetime] = None

      dpuId: str
      fru: Optional[Fru] = None
      sensors: list[OperationalInfo] = []

   memoryStatusInfo: list[HardwareElementInfo] = []
   cpuStatusInfo: list[HardwareElementInfo] = []
   storageStatusInfo: list[StorageStatusInfo] = []
   dpuStatusInfo: list[DpuStatusInfo] = []
