# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl.DynamicData import DynamicData

class DecommissionMode(DynamicData):
   class ObjectAction(Enum):
      noAction: ClassVar['ObjectAction'] = 'noAction'
      ensureObjectAccessibility: ClassVar['ObjectAction'] = 'ensureObjectAccessibility'
      evacuateAllData: ClassVar['ObjectAction'] = 'evacuateAllData'

   objectAction: str
