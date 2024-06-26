# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import ManagedEntity

from pyVmomi.vmodl import DynamicData

class AlarmFilterSpec(DynamicData):
   class AlarmTypeByEntity(Enum):
      entityTypeAll: ClassVar['AlarmTypeByEntity'] = 'entityTypeAll'
      entityTypeHost: ClassVar['AlarmTypeByEntity'] = 'entityTypeHost'
      entityTypeVm: ClassVar['AlarmTypeByEntity'] = 'entityTypeVm'

   class AlarmTypeByTrigger(Enum):
      triggerTypeAll: ClassVar['AlarmTypeByTrigger'] = 'triggerTypeAll'
      triggerTypeEvent: ClassVar['AlarmTypeByTrigger'] = 'triggerTypeEvent'
      triggerTypeMetric: ClassVar['AlarmTypeByTrigger'] = 'triggerTypeMetric'

   status: list[ManagedEntity.Status] = []
   typeEntity: Optional[str] = None
   typeTrigger: Optional[str] = None
