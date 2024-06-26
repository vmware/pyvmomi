# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.scheduler import MonthlyTaskScheduler

class MonthlyByWeekdayTaskScheduler(MonthlyTaskScheduler):
   class DayOfWeek(Enum):
      sunday: ClassVar['DayOfWeek'] = 'sunday'
      monday: ClassVar['DayOfWeek'] = 'monday'
      tuesday: ClassVar['DayOfWeek'] = 'tuesday'
      wednesday: ClassVar['DayOfWeek'] = 'wednesday'
      thursday: ClassVar['DayOfWeek'] = 'thursday'
      friday: ClassVar['DayOfWeek'] = 'friday'
      saturday: ClassVar['DayOfWeek'] = 'saturday'

   class WeekOfMonth(Enum):
      first: ClassVar['WeekOfMonth'] = 'first'
      second: ClassVar['WeekOfMonth'] = 'second'
      third: ClassVar['WeekOfMonth'] = 'third'
      fourth: ClassVar['WeekOfMonth'] = 'fourth'
      last: ClassVar['WeekOfMonth'] = 'last'

   offset: WeekOfMonth
   weekday: DayOfWeek
