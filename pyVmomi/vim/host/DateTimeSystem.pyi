# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.DateTimeConfig import DateTimeConfig

from pyVmomi.vim.host.DateTimeInfo import DateTimeInfo

class DateTimeSystem(ManagedObject):
   class TimeZone(DynamicData):
      key: str
      name: str
      description: str
      gmtOffset: int

   class ServiceTestResult(DynamicData):
      workingNormally: bool
      report: list[str] = []

   @property
   def dateTimeInfo(self) -> DateTimeInfo: ...

   def UpdateConfig(self, config: DateTimeConfig) -> None: ...
   def QueryAvailableTimeZones(self) -> list[TimeZone]: ...
   def QueryDateTime(self) -> datetime: ...
   def UpdateDateTime(self, dateTime: datetime) -> None: ...
   def Refresh(self) -> None: ...
   def TestTimeService(self) -> Optional[ServiceTestResult]: ...
