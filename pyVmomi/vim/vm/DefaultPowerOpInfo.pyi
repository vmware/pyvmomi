# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class DefaultPowerOpInfo(DynamicData):
   class PowerOpType(Enum):
      soft: ClassVar['PowerOpType'] = 'soft'
      hard: ClassVar['PowerOpType'] = 'hard'
      preset: ClassVar['PowerOpType'] = 'preset'

   class StandbyActionType(Enum):
      checkpoint: ClassVar['StandbyActionType'] = 'checkpoint'
      powerOnSuspend: ClassVar['StandbyActionType'] = 'powerOnSuspend'

   powerOffType: Optional[str] = None
   suspendType: Optional[str] = None
   resetType: Optional[str] = None
   defaultPowerOffType: Optional[str] = None
   defaultSuspendType: Optional[str] = None
   defaultResetType: Optional[str] = None
   standbyAction: Optional[str] = None
