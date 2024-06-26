# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class GraphicsConfig(DynamicData):
   class GraphicsType(Enum):
      shared: ClassVar['GraphicsType'] = 'shared'
      sharedDirect: ClassVar['GraphicsType'] = 'sharedDirect'

   class SharedPassthruAssignmentPolicy(Enum):
      performance: ClassVar['SharedPassthruAssignmentPolicy'] = 'performance'
      consolidation: ClassVar['SharedPassthruAssignmentPolicy'] = 'consolidation'

   class VgpuMode(Enum):
      sameSize: ClassVar['VgpuMode'] = 'sameSize'
      mixedSize: ClassVar['VgpuMode'] = 'mixedSize'

   class DeviceType(DynamicData):
      deviceId: str
      graphicsType: str
      vgpuMode: Optional[str] = None

   hostDefaultGraphicsType: str
   sharedPassthruAssignmentPolicy: str
   deviceType: list[DeviceType] = []
