# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.alarm.Alarm import Alarm

class AlarmState(DynamicData):
   key: str
   entity: ManagedEntity
   alarm: Alarm
   overallStatus: ManagedEntity.Status
   time: datetime
   acknowledged: Optional[bool] = None
   acknowledgedByUser: Optional[str] = None
   acknowledgedTime: Optional[datetime] = None
   eventKey: Optional[int] = None
   disabled: Optional[bool] = None
