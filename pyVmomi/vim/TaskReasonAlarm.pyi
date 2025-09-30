# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.TaskReason import TaskReason

from pyVmomi.vim.alarm.Alarm import Alarm

class TaskReasonAlarm(TaskReason):
   alarmName: str
   alarm: Alarm
   entityName: str
   entity: ManagedEntity
