# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from pyVmomi.vim import ManagedEntity

from pyVmomi.vim.alarm import Alarm
from pyVmomi.vim.alarm import AlarmSpec

class AlarmInfo(AlarmSpec):
   key: str
   alarm: Alarm
   entity: ManagedEntity
   lastModifiedTime: datetime
   lastModifiedUser: str
   creationEventId: int
