# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import ElementDescription

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import Fru

class NumericSensorInfo(DynamicData):
   class HealthState(Enum):
      unknown: ClassVar['HealthState'] = 'unknown'
      green: ClassVar['HealthState'] = 'green'
      yellow: ClassVar['HealthState'] = 'yellow'
      red: ClassVar['HealthState'] = 'red'

   class SensorType(Enum):
      fan: ClassVar['SensorType'] = 'fan'
      power: ClassVar['SensorType'] = 'power'
      temperature: ClassVar['SensorType'] = 'temperature'
      voltage: ClassVar['SensorType'] = 'voltage'
      other: ClassVar['SensorType'] = 'other'
      processor: ClassVar['SensorType'] = 'processor'
      memory: ClassVar['SensorType'] = 'memory'
      storage: ClassVar['SensorType'] = 'storage'
      systemBoard: ClassVar['SensorType'] = 'systemBoard'
      battery: ClassVar['SensorType'] = 'battery'
      bios: ClassVar['SensorType'] = 'bios'
      cable: ClassVar['SensorType'] = 'cable'
      watchdog: ClassVar['SensorType'] = 'watchdog'

   name: str
   healthState: Optional[ElementDescription] = None
   currentReading: long
   unitModifier: int
   baseUnits: str
   rateUnits: Optional[str] = None
   sensorType: str
   id: Optional[str] = None
   sensorNumber: Optional[long] = None
   timeStamp: Optional[str] = None
   fru: Optional[Fru] = None
