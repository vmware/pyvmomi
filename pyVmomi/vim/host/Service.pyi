# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class Service(DynamicData):
   class Policy(Enum):
      on: ClassVar['Policy'] = 'on'
      automatic: ClassVar['Policy'] = 'automatic'
      off: ClassVar['Policy'] = 'off'

   class SourcePackage(DynamicData):
      sourcePackageName: str
      description: str

   key: str
   label: str
   required: bool
   uninstallable: bool
   running: bool
   ruleset: list[str] = []
   policy: str
   sourcePackage: Optional[SourcePackage] = None
