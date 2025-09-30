# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl.DynamicData import DynamicData

class ConfigChange(DynamicData):
   class Mode(Enum):
      modify: ClassVar['Mode'] = 'modify'
      replace: ClassVar['Mode'] = 'replace'

   class Operation(Enum):
      add: ClassVar['Operation'] = 'add'
      remove: ClassVar['Operation'] = 'remove'
      edit: ClassVar['Operation'] = 'edit'
      ignore: ClassVar['Operation'] = 'ignore'

   class Owner(Enum):
      NSX: ClassVar['Owner'] = 'NSX'
      VSAN: ClassVar['Owner'] = 'VSAN'
