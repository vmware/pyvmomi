# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.alarm.Alarm import Alarm

from pyVmomi.vim.alarm.AlarmSpec import AlarmSpec

class AlarmInfo(AlarmSpec):
   key: str
   alarm: Alarm
   entity: ManagedEntity
   lastModifiedTime: datetime
   lastModifiedUser: str
   creationEventId: int
