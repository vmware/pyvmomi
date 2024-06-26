# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class HealthUpdateInfo(DynamicData):
   class ComponentType(Enum):
      Memory: ClassVar['ComponentType'] = 'Memory'
      Power: ClassVar['ComponentType'] = 'Power'
      Fan: ClassVar['ComponentType'] = 'Fan'
      Network: ClassVar['ComponentType'] = 'Network'
      Storage: ClassVar['ComponentType'] = 'Storage'

   id: str
   componentType: str
   description: str
