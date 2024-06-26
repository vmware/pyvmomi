# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import Description
from pyVmomi.vim import HostSystem
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData

class DiagnosticManager(ManagedObject):
   class LogDescriptor(DynamicData):
      class Creator(Enum):
         vpxd: ClassVar['Creator'] = 'vpxd'
         vpxa: ClassVar['Creator'] = 'vpxa'
         hostd: ClassVar['Creator'] = 'hostd'
         serverd: ClassVar['Creator'] = 'serverd'
         install: ClassVar['Creator'] = 'install'
         vpxClient: ClassVar['Creator'] = 'vpxClient'
         recordLog: ClassVar['Creator'] = 'recordLog'

      class Format(Enum):
         plain: ClassVar['Format'] = 'plain'

      key: str
      fileName: str
      creator: str
      format: str
      mimeType: str
      info: Description

   class LogHeader(DynamicData):
      lineStart: int
      lineEnd: int
      lineText: list[str] = []

   class BundleInfo(DynamicData):
      system: Optional[HostSystem] = None
      url: str

   class AuditRecordResult(DynamicData):
      records: list[str] = []
      nextToken: str

   def QueryDescriptions(self, host: Optional[HostSystem]) -> list[LogDescriptor]: ...
   def Browse(self, host: Optional[HostSystem], key: str, start: Optional[int], lines: Optional[int]) -> LogHeader: ...
   def GenerateLogBundles(self, includeDefault: bool, host: list[HostSystem]) -> Task: ...
   def FetchAuditRecords(self, token: Optional[str]) -> AuditRecordResult: ...
   def EmitSyslogMark(self, message: str) -> NoReturn: ...
